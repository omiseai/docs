"""質問エンジンの学習ループ（店の傾向 → 質問の質・量に反映する配管）。

設計の核 = 店主の1タップを最大限に重くする:
- 厨房共通質問1タップ → 該当全品に波及 + 冗長な単品質問が消える
- 「商品によって違う(varies)」1タップ → 品ごとの同じ選択肢の質問に即分解
- 過去の回答は次の質問生成の文脈になり、同じことを二度と聞かない

役割:
1. KITCHEN_AXIS_KEYWORDS + _axis_scope — 厨房軸の定義。波及スコープは
   kitchen_profile.CASCADE_RULES の applies_to から導出する(二重管理しない)。
2. purge_axis_clarifications — 厨房回答で冗長になった単品質問を一掃。
   axis タグ付き質問は構造一致(誤爆なし)、旧質問はキーワードでフォールバック。
3. expand_varies_to_item_questions — varies回答を品ごとの質問に即分解(radio軸)。
4. apply_axis_item_rules — axis付き単品質問の回答をCASCADE_RULESで正確に1品へ反映。
5. lint_clarifications — 生成質問の品質リント(生成スクリプト/enrichの両経路から呼ぶ正本)。
6. build_store_facts_context — 過去回答を生成プロンプト用テキストに変換。

タレ・ソース(sauce_base)・調理油(cooking_oil)は品ごとに中身が違うので
軸キーワードに意図的に載せない(全体回答で単品特有の質問を消さない)。
"""
import json

from sqlalchemy.orm import Session

# 厨房質問ID → 単品質問文の軸キーワード(axis無し旧質問のフォールバック判定用)。
# 「厨房の回答だけで単品の答えが確定する」軸だけを載せる(保守的に)。
KITCHEN_AXIS_KEYWORDS = {
    "tempura_batter": ["衣"],
    "karaage_marinade": ["衣", "下味"],
    "frying_oil": ["揚げ油"],
    "dashi_base": ["だし", "出汁"],
    "gyoza_wrapper": ["皮"],
    "pasta_type": ["パスタ", "麺"],
    "curry_base": ["ルー", "ベース"],
    "bread_base": ["生地"],
    "gelatin_source": ["ゼラチン", "寒天", "固め"],
    "dressing": ["ドレッシング"],
}

# 回答がこれらの値なら波及しない(=単品質問を消さない)。
# 「商品によって違う」と答えた店では単品質問こそが正解の経路。
NON_PROPAGATING_VALUES = {"varies", "unknown", "none_above", ""}

# リント: 選択肢に出てはいけないメタ回答(UI側の共通ボタンと重複)。
# 「その他」もUI側に「その他(入力する)」ボタンがあるため選択肢に入れない
# (裸の「その他」タップ=内容ゼロの回答で質問が消費される事故を防ぐ)
META_OPTIONS = {"合っています", "違います", "わかりません", "分かりません", "該当なし", "不明", "正しい", "間違い"}


def _axis_scope(question_id: str):
    """波及スコープをCASCADE_RULESのapplies_toから導出(kitchen_profileが正本)。"""
    from app.admin_api.kitchen_profile import CASCADE_RULES
    for rule in (CASCADE_RULES.get(question_id) or {}).values():
        scope = rule.get("applies_to")
        if scope:
            return scope
    return None


def _answered_kitchen_values(restaurant_id: int, db: Session) -> dict:
    """店主が回答済みの厨房質問 {question_id: [値,...]}。supplement は除く。"""
    from app.store_knowledge.models import StoreKnowledge
    entries = db.query(StoreKnowledge).filter(
        StoreKnowledge.restaurant_id == restaurant_id,
        StoreKnowledge.category == "kitchen_profile",
    ).all()
    out = {}
    for e in entries:
        if e.key.endswith("_supplement"):
            continue
        try:
            parsed = json.loads(e.value)
            values = parsed if isinstance(parsed, list) else [parsed]
        except (json.JSONDecodeError, TypeError):
            values = [e.value]
        out[e.key] = [str(v) for v in values]
    return out


def propagating_kitchen_axes(restaurant_id: int, db: Session) -> dict:
    """単品質問を不要にできる回答済み軸 {question_id: (scope, keywords)}。"""
    answered = _answered_kitchen_values(restaurant_id, db)
    out = {}
    for qid, keywords in KITCHEN_AXIS_KEYWORDS.items():
        values = answered.get(qid)
        if not values:
            continue
        concrete = [v for v in values if v not in NON_PROPAGATING_VALUES]
        scope = _axis_scope(qid)
        if concrete and scope:
            out[qid] = (scope, keywords)
    return out


def varies_kitchen_axes(restaurant_id: int, db: Session) -> dict:
    """「商品によって違う」と回答済みの軸 {question_id: (scope, keywords)}。
    この軸は単品質問が正解の経路 → 生成を抑制せず、生成された質問にはaxisタグを付ける。"""
    answered = _answered_kitchen_values(restaurant_id, db)
    out = {}
    for qid, keywords in KITCHEN_AXIS_KEYWORDS.items():
        values = answered.get(qid)
        if not values:
            continue
        scope = _axis_scope(qid)
        if scope and all(v in NON_PROPAGATING_VALUES for v in values) and "varies" in values:
            out[qid] = (scope, keywords)
    return out


# ---------------------------------------------------------------------------
# 店舗プロフィール質問 — 客が実際に聞くのにAIが「未登録」と返す項目を店主に聞く。
# 回答は restaurants の記録フィールドに直接入る(fast_navが即答えられるようになる)。
# 会話ログマイニング(mine_chat_gaps.py)で頻出だった軸だけを載せる(聞きすぎない)。
# ---------------------------------------------------------------------------
STORE_PROFILE_QUESTIONS = [
    {
        "id": "seats",
        "field": "seats",
        "question": "お店の座席について教えてください（例: カウンター8席・テーブル20席）",
        "type": "text",
        "options": [],
        "maxlen": 50,  # restaurants.seats String(50)
    },
    {
        "id": "payment_methods",
        "field": "payment_methods",
        "question": "使える支払い方法はどれですか？",
        "type": "checkbox",
        "options": ["現金", "クレジットカード", "電子マネー（iD/QUICPay等）",
                    "QRコード決済（PayPay等）", "交通系IC（Suica等）"],
        "maxlen": 200,
    },
    {
        "id": "parking_slot",
        "field": "parking_slot",
        "question": "駐車場はありますか？",
        "type": "radio",
        "options": ["専用駐車場あり", "近隣のコインパーキング利用", "駐車場なし"],
        "maxlen": 100,
    },
    {
        "id": "access_info",
        "field": "access_info",
        "question": "お店までの行き方を教えてください（例: JR福井駅 東口から徒歩3分）",
        "type": "text",
        "options": [],
        "maxlen": 200,
    },
]


def store_profile_pending(restaurant) -> list[dict]:
    """記録フィールドが空の店舗プロフィール質問だけ返す。
    回答済み判定はフィールド自体(非空=答えた or 元から登録済み)なので状態テーブル不要。"""
    out = []
    for spec in STORE_PROFILE_QUESTIONS:
        val = getattr(restaurant, spec["field"], None)
        if val is None or not str(val).strip():
            out.append(spec)
    return out


def apply_store_profile_answer(restaurant, spec: dict, selected: list | None,
                               text_note: str | None, db: Session) -> str:
    """店舗プロフィール回答を記録フィールドに書き、出典をstore_knowledgeに残す。
    書いた値を返す。文字数はFE側でフィールド上限(max_input)に揃えて入力制限済み、
    ここは防御の最終切り詰めのみ。"""
    from app.admin_api.kitchen_profile import _save_store_knowledge

    value = "、".join(selected or []).strip() or (text_note or "").strip()
    value = value[: spec["maxlen"]]
    setattr(restaurant, spec["field"], value)
    _save_store_knowledge(
        restaurant.id, f"store_profile_{spec['id']}", value, None, db,
        category="store_profile",
    )
    return value


def suppressed_axes_for_generation(restaurant_id: int, food_menus: list, all_menus: list, db: Session) -> dict:
    """質問生成時に単品質問を作るべきでない軸 {question_id: (scope, keywords)}。
    - 回答済み(具体値) → 既知なので聞かない
    - 未回答だが厨房質問として聞く予定 → 単品で先回りすると重複(チャットで店全体を1回聞く方が軽い)
    - 「商品によって違う(varies)」回答済み → 単品で聞くのが正解なので抑制しない"""
    from app.admin_api.kitchen_profile import get_phase1_questions

    answered = _answered_kitchen_values(restaurant_id, db)
    required = set(get_phase1_questions(food_menus, all_menus=all_menus))
    out = {}
    for qid, keywords in KITCHEN_AXIS_KEYWORDS.items():
        values = answered.get(qid)
        if values and all(v in NON_PROPAGATING_VALUES for v in values):
            continue  # varies等 → 単品質問こそが正解の経路
        scope = _axis_scope(qid)
        if scope and (values or qid in required):
            out[qid] = (scope, keywords)
    return out


def purge_axis_clarifications(restaurant_id: int, question_id: str, db: Session) -> int:
    """厨房質問への回答で冗長になった単品質問(clarification)を一掃する。
    axisタグ付き質問は構造一致のみ(誤爆ゼロ)。タグ無しの旧質問は
    波及スコープ内×軸キーワード部分一致でフォールバック判定。
    消した質問数を返す。波及しない回答(varies等)では呼び出し側で呼ばないこと。"""
    from app.menus.models import Menu
    from app.admin_api.kitchen_profile import (
        _get_target_menus_by_scope, DRINK_CATEGORIES,
    )

    keywords = KITCHEN_AXIS_KEYWORDS.get(question_id)
    scope = _axis_scope(question_id)
    if not keywords or not scope:
        return 0

    # 触るのは質問を持つメニューだけ(全品ロードしない)
    menus = db.query(Menu).filter(
        Menu.restaurant_id == restaurant_id,
        Menu.status == True,  # noqa: E712
        Menu.clarification_needed.isnot(None),
    ).all()
    if question_id != "gelatin_source":
        menus = [m for m in menus if (m.category or "").lower() not in DRINK_CATEGORIES]
    targets = _get_target_menus_by_scope(scope, menus)

    purged = 0
    for menu in targets:
        cl = menu.clarification_needed
        if not isinstance(cl, list) or not cl:
            continue
        remaining = []
        for q in cl:
            if not isinstance(q, dict):
                remaining.append(q)
                continue
            axis = q.get("axis")
            if axis is not None:
                # axisタグ付き: 構造一致のみで判定(文言に依存しない)
                if axis == question_id:
                    purged += 1
                    continue
                remaining.append(q)
                continue
            text = q.get("question") or ""
            if text and any(kw in text for kw in keywords):
                purged += 1
                continue
            remaining.append(q)
        if len(remaining) != len(cl):
            menu.clarification_needed = remaining if remaining else None
    return purged


def expand_varies_to_item_questions(restaurant_id: int, question_id: str, db: Session) -> int:
    """「商品によって違う(varies)」回答の軸を、品ごとの同じ選択肢の単品質問に即分解する。
    店主の体験: varies 1タップ → 該当する品の質問がすぐ並ぶ(生成スクリプトの実行を待たない)。
    radio型の軸のみ(checkbox型は単品UIが単一選択のため、生成スクリプトのLLM質問に任せる)。
    追加した質問数を返す。"""
    from app.menus.models import Menu
    from app.admin_api.kitchen_profile import (
        KITCHEN_QUESTIONS, _get_target_menus_by_scope, DRINK_CATEGORIES,
    )

    q_def = KITCHEN_QUESTIONS.get(question_id)
    scope = _axis_scope(question_id)
    if not q_def or q_def.get("type") != "radio" or not scope:
        return 0
    options = [o["label"] for o in (q_def.get("options") or [])
               if o.get("value") not in NON_PROPAGATING_VALUES]
    if len(options) < 2:
        return 0

    menus = db.query(Menu).filter(
        Menu.restaurant_id == restaurant_id,
        Menu.status == True,  # noqa: E712
    ).all()
    if question_id != "gelatin_source":
        menus = [m for m in menus if (m.category or "").lower() not in DRINK_CATEGORIES]
    targets = _get_target_menus_by_scope(scope, menus)

    added = 0
    for menu in targets:
        cl = menu.clarification_needed if isinstance(menu.clarification_needed, list) else []
        if any(isinstance(q, dict) and q.get("axis") == question_id for q in cl):
            continue  # 既に同軸の単品質問がある
        # 先頭に挿入=次の配信ですぐ出る。質問文はUI側で「メニュー名」が前置されるので
        # 厨房質問の文言をそのまま使う(例:「天ぷらの衣に卵は入っていますか？」)
        menu.clarification_needed = [{
            "field": "ingredients",
            "type": "select",
            "axis": question_id,
            "question": q_def["question"],
            "options": options,
        }] + list(cl)
        added += 1
    return added


def apply_axis_item_rules(menu, question_id: str, selected_labels: list | None, db: Session) -> list:
    """axis付き単品質問への回答をCASCADE_RULESで正確に1品へ反映する。
    キーワード推測(「卵なし」を否定と誤読する等)でなく、選択肢→値コード→ルールの決定論。
    付与したアレルゲン(name_en)のリストを返す(undo用)。"""
    from app.admin_api.kitchen_profile import (
        KITCHEN_QUESTIONS, CASCADE_RULES, _apply_rule_to_menu,
    )
    q_def = KITCHEN_QUESTIONS.get(question_id)
    if not q_def:
        return []
    value_by_label = {o["label"]: o["value"] for o in (q_def.get("options") or [])}
    added_all = []
    for label in selected_labels or []:
        val = value_by_label.get(str(label))
        rule = (CASCADE_RULES.get(question_id) or {}).get(val or "", {})
        if rule:
            added, _removed = _apply_rule_to_menu(menu, rule, db)
            added_all.extend(added)
    return added_all


def lint_clarifications(clarifications: list, axis_keywords: list | None = None) -> tuple[list, list]:
    """生成された質問を機械チェックし (採用リスト, 却下理由リスト) を返す。
    生成スクリプトと nfg_enrichment(新メニューのenrich時生成)の両経路から呼ぶ正本。
    2026-06-10に手動で間引いた不良4パターン(汎用yes/no・メタ選択肢・
    「のみ/も含む」型・選択肢欠落)を自動で落とす。
    axis_keywords: 店主が厨房共通質問で回答済みの軸(衣/だし等)。該当質問は重複なので却下。"""
    kept, rejected = [], []
    for c in clarifications:
        if not isinstance(c, dict):
            rejected.append("dict以外")
            continue
        q = (c.get("question") or "").strip()
        qtype = c.get("type", "select")
        options = c.get("options")

        if not q:
            rejected.append("質問文なし")
            continue
        if "アレルゲン" in q:
            rejected.append(f"質問文に「アレルゲン」: {q}")
            continue
        if axis_keywords and any(kw in q for kw in axis_keywords):
            rejected.append(f"厨房回答済みの軸と重複: {q}")
            continue

        if qtype == "photo":
            if "撮" not in q:
                rejected.append(f"photoなのに撮影依頼でない: {q}")
                continue
            # 醤油・味噌・みりんは大豆/小麦を自動付与できる。撮影依頼は店主負担の無駄
            if any(w in q for w in ("醤油", "味噌", "みりん")):
                rejected.append(f"定番調味料の撮影依頼: {q}")
                continue
            c.pop("options", None)  # photoに選択肢は不要
            kept.append(c)
            continue

        # select系
        if not isinstance(options, list):
            rejected.append(f"選択肢が不足: {q}")
            continue
        # 裸の「その他」はUIの「その他(入力する)」ボタンと重複し、
        # タップすると内容ゼロの回答で質問が消費されるため選択肢から外す
        options = [str(o).strip() for o in options if str(o).strip() and str(o).strip() != "その他"]
        if len(options) < 2:
            rejected.append(f"選択肢が不足: {q}")
            continue
        if set(options) <= {"はい", "いいえ"}:
            rejected.append(f"汎用yes/no: {q}")
            continue
        if any(o in META_OPTIONS for o in options):
            rejected.append(f"メタ選択肢: {q} {options}")
            continue
        if any(o.endswith("のみ") for o in options) and any("含む" in o for o in options):
            rejected.append(f"「のみ/含む」型: {q} {options}")
            continue
        c["options"] = options
        kept.append(c)
    return kept[:2], rejected  # 1品 最大2問


def build_store_facts_context(restaurant_id: int, db: Session, max_clarifications: int = 30) -> str:
    """店主の過去回答を質問生成プロンプト用の「確認済みの事実」テキストにする。
    厨房回答は値コードを人間の言葉(選択肢ラベル)に変換して渡す。"""
    from app.store_knowledge.models import StoreKnowledge
    from app.admin_api.kitchen_profile import KITCHEN_QUESTIONS, labels_for_values

    lines = []

    # 1) 厨房共通の回答(店全体の事実)
    answered = _answered_kitchen_values(restaurant_id, db)
    for qid, values in answered.items():
        q_def = KITCHEN_QUESTIONS.get(qid)
        if not q_def or qid == "signature_menu":
            continue
        labels = [lb for v, lb in zip(values, labels_for_values(qid, values))
                  if v not in ("", "none_above")]
        if labels:
            lines.append(f"- {q_def['question']} → {('、'.join(labels))}")

    # 2) 単品質問への過去回答(店の傾向。新しい順に上限まで)
    entries = db.query(StoreKnowledge).filter(
        StoreKnowledge.restaurant_id == restaurant_id,
        StoreKnowledge.category == "clarification",
    ).order_by(StoreKnowledge.id.desc()).limit(max_clarifications).all()
    for e in entries:
        try:
            v = json.loads(e.value)
        except (json.JSONDecodeError, TypeError):
            continue
        if not isinstance(v, dict):
            continue
        question = (v.get("question") or "").strip()
        answer = "、".join(v.get("selected") or []) or (v.get("text_note") or "").strip()
        if question and answer:
            lines.append(f"- 「{question}」→ {answer}")

    # 3) 仕入れ語彙(納品書から読み取った商品名)。AIの推測を「この店の現実」に寄せる。
    # 仕入れている=その料理に使っているとは限らないので、事実でなく傾向として渡す
    products = []
    seen = set()
    proc = db.query(StoreKnowledge).filter(
        StoreKnowledge.restaurant_id == restaurant_id,
        StoreKnowledge.category == "procurement",
    ).order_by(StoreKnowledge.id.desc()).limit(10).all()
    for e in proc:
        try:
            for p in (json.loads(e.value) or {}).get("products") or []:
                if p not in seen:
                    seen.add(p)
                    products.append(p)
        except (json.JSONDecodeError, TypeError):
            continue
    if products:
        lines.append(
            "- この店が仕入れている商品(納品書より。質問の選択肢はこのリストに寄せる。"
            "ただし仕入れ=使用とは限らないので断定はしない): " + "、".join(products[:40])
        )

    return "\n".join(lines)
