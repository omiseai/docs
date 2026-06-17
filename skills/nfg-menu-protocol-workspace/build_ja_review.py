#!/usr/bin/env python3
# Builds a self-contained Japanese-language review page for a colleague to judge
# the with-skill eval outputs. Renders the stage markdown files, shows each
# evaluation criterion in Japanese, and lets the reviewer record a judgment + notes
# and export them as JSON.
import json, os, glob, html

import sys
ITER = os.path.join(os.path.dirname(__file__), sys.argv[1] if len(sys.argv) > 1 else "iteration-1")
OUT = os.path.join(ITER, "review_ja.html")

EVALS = [
    {
        "key": "eval-0-izakaya-full-ingest",
        "title": "テスト1 — 居酒屋メニューの取り込み（鳥平・大阪）",
        "prompt": "大阪の居酒屋「鳥平」を新規導入します。オーナーから届いたメニュー（牛すじ煮込み／鶏の唐揚げ／だし巻き卵／ポテトサラダ／本日の刺身盛り合わせ／黒龍 純米吟醸）を NFG データに取り込み、コンシェルジュがアレルギーを含むお客様の質問に答えられるようにしてください。",
        "note": "※ この実行ではオーナーは不在の想定です。確認できない項目は推測のまま事実にせず、確認事項として残す挙動を見ています。",
    },
    {
        "key": "eval-1-allergy-trap-verify",
        "title": "テスト2 — アレルゲン検証（ランチ4品）",
        "prompt": "ランチメニュー（ロースかつ定食／エビフライ／杏仁豆腐／コーヒーゼリー）について、コンシェルジュを稼働させる前にアレルゲンを検証してください。アレルギーのあるお客様がこの回答を頼りにします。",
        "note": "※ オーナー不在の想定。「杏仁豆腐＝豆腐＝大豆」やゼラチン＝肉、といった誤りの罠を避けられているかが見どころです。",
    },
    {
        "key": "eval-2-gap-finding-soba",
        "title": "テスト3 — 確認事項の洗い出し（そば店）",
        "prompt": "そば店のメニュー（ざるそば／天ぷらそば／カレーうどん／そばがき）について、コンシェルジュが安全にお客様へ答えられるようにする前に、オーナーへ何を確認すべきかを洗い出してください。",
        "note": "※ オーナー不在の想定。確認事項（gap register）の質と、安全性を最優先にした並びが見どころです。",
    },
]

# Japanese translations of the auto-grading assertion texts (keyed by English text).
JA = {
    "Separates observed facts from inferences using explicit provenance tags":
        "観察した事実と推測を、出典タグ（[MENU]/[OPERATOR]/[CANONICAL]/[INFERRED]/[UNKNOWN]）で明確に区別している",
    "Produces a gap register / operator questions ranked safety-first":
        "オーナーへの確認事項を、安全性を最優先に並べてまとめている",
    "Routes uncertain allergen status to gaps rather than asserting it as fact":
        "不確かなアレルゲン情報を事実として断定せず、確認事項に回している",
    "Assigns a per-record verification grade (S/A/B/C or confidence)":
        "料理ごとに信頼度（S/A/B/C）を付けている",
    "Expands composite ingredients (dashi, roux, batter, mayo) so hidden allergens surface":
        "複合材料（だし・ルウ・衣・マヨネーズ等）を分解し、隠れたアレルゲンを表に出している",
    "Produces a Stage 07 operator sign-off sheet that foregrounds inferred items for confirmation":
        "オーナー確認シート（07）を作成し、推測項目を確認用に前面に出している",
    "Handles the sake (黒龍) via canonical matching and avoids the 龍-substring brand error":
        "日本酒（黒龍）を正式名称で照合し、「龍」の部分一致による銘柄取り違えを避けている",
    "Flags the daily-rotating sashimi (本日の) as not having a fixed allergen profile":
        "「本日の刺身」は日替わりのため、固定のアレルゲン情報を持たないものとして注意喚起している",
    "Keeps gelatin as its own token, not a meat allergen (dessert mis-tag pitfall)":
        "ゼラチンを肉類アレルゲンにせず独立項目として扱っている（デザート誤タグの落とし穴）",
    "Does not auto-derive soy from 豆腐 in 杏仁豆腐 (naming trap)":
        "杏仁豆腐の「豆腐」から大豆を自動的に導いていない（名称の罠）",
    "Identifies the soba buckwheat/wheat ratio as a top safety gap":
        "そば粉／小麦の配合比を、最重要の確認事項として特定している",
    "Flags curry-udon roux as a hidden-allergen composite (wheat/dairy)":
        "カレーうどんのルウを、隠れアレルゲン（小麦・乳）を含む複合材料として注意している",
}

STAGE_LABEL = {
    "01_source_capture.md": "01 ソース取り込み（原文ママ）",
    "02_decomposition.md": "02 分解（材料・調理法）",
    "03_allergens_restrictions.md": "03 アレルゲン・制限の導出",
    "04_gap_register.md": "04 確認事項リスト",
    "05_operator_dialogue.md": "05 オーナーとのやりとり",
    "06_nfg_output.md": "06 NFG 出力（データセット）",
    "07_operator_review.md": "07 オーナー確認シート",
}

def read_outputs(key):
    base = os.path.join(ITER, key, "with_skill", "run-1", "outputs")
    ja = os.path.join(ITER, key, "with_skill", "run-1", "outputs_ja")
    files = []
    for p in sorted(glob.glob(os.path.join(base, "*.md"))):
        name = os.path.basename(p)
        ja_path = os.path.join(ja, name)  # prefer a Japanese-translated copy if present
        use = ja_path if os.path.exists(ja_path) else p
        files.append((name, open(use, encoding="utf-8").read()))
    return files

def read_grading(key):
    gp = os.path.join(ITER, key, "with_skill", "run-1", "grading.json")
    if os.path.exists(gp):
        return json.load(open(gp, encoding="utf-8"))
    return {"expectations": []}

cards = []
for ev in EVALS:
    outs = read_outputs(ev["key"])
    grading = read_grading(ev["key"])
    crit_rows = []
    for i, e in enumerate(grading.get("expectations", [])):
        ja = JA.get(e["text"], e["text"])
        auto = "自動判定: 合格" if e["passed"] else "自動判定: 要確認"
        auto_cls = "ok" if e["passed"] else "warn"
        cid = f'{ev["key"]}__c{i}'
        crit_rows.append(f'''
        <div class="crit">
          <div class="crit-head">
            <span class="crit-text">{html.escape(ja)}</span>
            <span class="badge {auto_cls}">{auto}</span>
          </div>
          <div class="judge" data-cid="{cid}">
            <label><input type="radio" name="{cid}" value="適切"> 適切</label>
            <label><input type="radio" name="{cid}" value="要改善"> 要改善</label>
            <label><input type="radio" name="{cid}" value="不適切"> 不適切</label>
            <input type="text" class="crit-note" data-cid="{cid}" placeholder="コメント（任意）">
          </div>
        </div>''')
    stage_blocks = []
    for name, content in outs:
        label = STAGE_LABEL.get(name, name)
        stage_blocks.append(f'''
        <details class="stage">
          <summary>{html.escape(label)}</summary>
          <div class="md" data-md="{html.escape(json.dumps(content))}"></div>
        </details>''')
    cards.append(f'''
    <section class="card" id="{ev['key']}">
      <h2>{html.escape(ev["title"])}</h2>
      <div class="prompt"><strong>お題:</strong> {html.escape(ev["prompt"])}</div>
      <div class="hint">{html.escape(ev["note"])}</div>

      <h3>スキルが作った成果物</h3>
      {''.join(stage_blocks)}

      <h3>評価ポイント（各項目をご判断ください）</h3>
      {''.join(crit_rows)}

      <h3>総合コメント</h3>
      <textarea class="overall" data-cid="{ev['key']}__overall"
        placeholder="この料理データは、アレルギーのお客様に安心して出せる水準ですか？ 気になる点・誤り・追加で確認すべきことなど自由にご記入ください。"></textarea>
    </section>''')

html_doc = f'''<!doctype html>
<html lang="ja">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>NFG メニュープロトコル — 評価シート</title>
<script src="https://cdn.jsdelivr.net/npm/marked/marked.min.js"></script>
<style>
  :root {{ --green:#166E3F; --light:#26BD6C; }}
  body {{ font-family: -apple-system, "Hiragino Sans", "Noto Sans JP", sans-serif;
    margin:0; background:#f6f7f6; color:#1c1c1c; line-height:1.7; }}
  header {{ background:var(--green); color:#fff; padding:20px 24px; }}
  header h1 {{ margin:0 0 4px; font-size:20px; }}
  header p {{ margin:0; opacity:.9; font-size:14px; }}
  main {{ max-width:920px; margin:0 auto; padding:24px 16px 80px; }}
  .intro {{ background:#fff; border:1px solid #e3e6e3; border-radius:10px; padding:16px 18px; margin-bottom:22px; }}
  .card {{ background:#fff; border:1px solid #e3e6e3; border-radius:10px; padding:18px 20px; margin-bottom:26px; }}
  .card h2 {{ color:var(--green); margin:0 0 10px; font-size:18px; }}
  .prompt {{ background:#f0f6f2; border-radius:8px; padding:10px 12px; font-size:14px; }}
  .hint {{ color:#5a6b5f; font-size:13px; margin:8px 0 4px; }}
  h3 {{ font-size:15px; border-bottom:2px solid #eef0ee; padding-bottom:6px; margin:22px 0 12px; }}
  details.stage {{ border:1px solid #e3e6e3; border-radius:8px; margin:8px 0; }}
  details.stage summary {{ cursor:pointer; padding:10px 12px; font-weight:600; color:var(--green); }}
  .md {{ padding:0 16px 12px; font-size:14px; overflow-x:auto; }}
  .md table {{ border-collapse:collapse; }}
  .md th, .md td {{ border:1px solid #ddd; padding:4px 8px; font-size:13px; }}
  .md code {{ background:#f3f3f3; padding:1px 4px; border-radius:4px; }}
  .md pre {{ background:#f3f3f3; padding:10px; border-radius:6px; overflow-x:auto; }}
  .crit {{ border:1px solid #eef0ee; border-radius:8px; padding:10px 12px; margin:8px 0; }}
  .crit-head {{ display:flex; justify-content:space-between; gap:10px; align-items:flex-start; }}
  .crit-text {{ font-size:14px; }}
  .badge {{ font-size:11px; padding:2px 8px; border-radius:20px; white-space:nowrap; }}
  .badge.ok {{ background:#e3f5ea; color:#166E3F; }}
  .badge.warn {{ background:#fdecec; color:#b3261e; }}
  .judge {{ margin-top:8px; display:flex; gap:14px; align-items:center; flex-wrap:wrap; }}
  .judge label {{ font-size:13px; }}
  .crit-note {{ flex:1; min-width:180px; padding:5px 8px; border:1px solid #d8dcd8; border-radius:6px; font-size:13px; }}
  textarea.overall {{ width:100%; min-height:90px; padding:10px; border:1px solid #d8dcd8; border-radius:8px; font-size:14px; box-sizing:border-box; }}
  .bar {{ position:fixed; bottom:0; left:0; right:0; background:#fff; border-top:1px solid #e3e6e3; padding:12px 16px; text-align:center; }}
  .bar button {{ background:var(--green); color:#fff; border:none; padding:10px 22px; border-radius:8px; font-size:15px; cursor:pointer; }}
  .bar span {{ color:#5a6b5f; font-size:13px; margin-left:12px; }}
</style>
</head>
<body>
<header>
  <h1>NFG メニュープロトコル — 評価シート</h1>
  <p>各テストで、スキル（OmiseAI の中核プロセスの手動版）が作った成果物をご確認ください。</p>
</header>
<main>
  <div class="intro">
    <p><strong>お願いしたいこと:</strong> このツールは、レストランのメニューを「ハルシネーション（AIの思い込み）を出さない」ことを最優先に、構造化データへ変換するためのものです。特に<strong>アレルギー情報</strong>が、確かな根拠（メニュー記載・オーナー確認・検証済みデータ）に基づいているか、推測が事実として混ざっていないかをご判断ください。</p>
    <p>各「評価ポイント」には参考として自動判定（合格／要確認）を表示していますが、最終的なご判断は専門家であるあなたの目でお願いします。記入後、画面下の「評価を書き出す」でファイルを保存できます。</p>
  </div>
  {''.join(cards)}
</main>
<div class="bar">
  <button onclick="exportReview()">評価を書き出す（JSON）</button>
  <span id="status"></span>
</div>
<script>
  document.querySelectorAll('.md').forEach(function(el){{
    try {{ el.innerHTML = marked.parse(JSON.parse(el.dataset.md)); }}
    catch(e) {{ el.textContent = el.dataset.md; }}
  }});
  function exportReview() {{
    var out = {{ generated: new Date().toISOString(), reviews: {{}} }};
    document.querySelectorAll('input[type=radio]:checked').forEach(function(r){{
      out.reviews[r.name] = out.reviews[r.name] || {{}};
      out.reviews[r.name].judgment = r.value;
    }});
    document.querySelectorAll('.crit-note').forEach(function(t){{
      if(t.value.trim()) {{ out.reviews[t.dataset.cid] = out.reviews[t.dataset.cid] || {{}}; out.reviews[t.dataset.cid].note = t.value.trim(); }}
    }});
    document.querySelectorAll('.overall').forEach(function(t){{
      if(t.value.trim()) {{ out.reviews[t.dataset.cid] = {{ overall: t.value.trim() }}; }}
    }});
    var blob = new Blob([JSON.stringify(out, null, 2)], {{type:'application/json'}});
    var a = document.createElement('a'); a.href = URL.createObjectURL(blob);
    a.download = 'nfg_review_ja_feedback.json'; a.click();
    document.getElementById('status').textContent = '保存しました（ダウンロードフォルダをご確認ください）';
  }}
</script>
</body>
</html>'''

open(OUT, "w", encoding="utf-8").write(html_doc)
print("wrote", OUT, os.path.getsize(OUT), "bytes")
