"""
Phase 1: 厨房プロファイル — v5.1（キッチン共有リソースのみ）
メニュー構成に応じた隠れ材料の確認。全てタップ式、CASCADE_RULESで即波及。

v5.0 変更点:
- sauce_base, curry_base, bread_base 追加
- cooking_oil に ghee, coconut_oil 追加
- gelatin_source を checkbox + varies 化
- dressing に varies 追加
- nuts → peanut / tree_nuts に分割（dessert_base, dressing）
- _ALLERGEN_KEY_MAP に walnut, cashew_nut, almond, gelatin, beef 追加
- karaage_marinade potato_starch の誤った remove_allergens 削除
- DASHI_CATEGORIES から ramen 削除（ramen_broth で個別対応）
- ramen_broth miso ラベル修正
- 質問順序を再整理
"""
import json
from sqlalchemy.orm import Session
from app.menus.models import Menu
from app.allergens.models import Allergen
from app.allergens.fixed_allergens import normalize_allergen_name
from app.restrictions.models import Restriction
from app.store_knowledge.models import StoreKnowledge

# --- キーワード定義 ---
TEMPURA_KEYWORDS = ["天ぷら", "天婦羅", "てんぷら"]
KARAAGE_KEYWORDS = ["唐揚げ", "から揚げ", "竜田揚げ", "ザンギ"]
FRIED_KEYWORDS = TEMPURA_KEYWORDS + KARAAGE_KEYWORDS + ["フライ", "カツ", "春巻き", "コロッケ", "揚げ"]

DRINK_CATEGORIES = {
    "drink", "beer", "sake", "sour", "highball",
    "whisky", "wine", "shochu", "fruit_wine", "soft_drink",
}

DASHI_CATEGORIES = {"soup", "nabe", "steamed", "rice", "soba"}

SALAD_KEYWORDS = ["サラダ", "マリネ", "カルパッチョ"]
PASTA_KEYWORDS = [
    "パスタ", "スパゲッティ", "ペンネ", "リゾット",
    "カルボナーラ", "ミートソース", "ボロネーゼ", "ペペロンチーノ",
    "ナポリタン", "ラザニア", "ニョッキ",
]
RAMEN_KEYWORDS = ["ラーメン", "らーめん", "拉麺", "つけ麺", "まぜそば"]
GYOZA_KEYWORDS = ["餃子", "ギョーザ", "ぎょうざ"]
CURRY_KEYWORDS = ["カレー", "カリー"]
GELATIN_KEYWORDS = ["パンナコッタ", "プリン", "ゼリー", "ムース", "ババロア"]
BREAD_KEYWORDS = ["パン", "ナン", "フォカッチャ", "ピザ", "ピッツァ", "トースト", "バゲット"]

# --- 質問マスター ---
KITCHEN_QUESTIONS = {
    "signature_menu": {
        "question": "初めてのお客さんに必ず勧める自慢の料理は？（3品まで）",
        "type": "menu_select",
        "parent": None,
        "options": None,
        "max_select": 3,
    },
    "cooking_oil": {
        "question": "ほとんどの料理に使うメインの油は？",
        "type": "radio",
        "parent": None,
        "options": [
            {"value": "salad_oil", "label": "サラダ油"},
            {"value": "sesame_oil", "label": "ごま油"},
            {"value": "butter", "label": "バター"},
            {"value": "lard", "label": "ラード（豚の脂）"},
            {"value": "olive_oil", "label": "オリーブオイル"},
            {"value": "ghee", "label": "ギー（澄ましバター）"},
            {"value": "coconut_oil", "label": "ココナッツオイル"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "cooking_oil_sub": {
        "question": "他にも使う油・脂はありますか？（複数OK・なければスキップ）",
        "type": "checkbox",
        "parent": "cooking_oil",
        "options": [
            {"value": "salad_oil", "label": "サラダ油"},
            {"value": "sesame_oil", "label": "ごま油"},
            {"value": "butter", "label": "バター"},
            {"value": "lard", "label": "ラード（豚の脂）"},
            {"value": "olive_oil", "label": "オリーブオイル"},
            {"value": "ghee", "label": "ギー（澄ましバター）"},
            {"value": "coconut_oil", "label": "ココナッツオイル"},
            {"value": "none_above", "label": "他にはない"},
        ],
    },
    "frying_oil": {
        "question": "揚げ物の油は何を使っていますか？",
        "type": "checkbox",
        "parent": None,
        "options": [
            {"value": "salad_oil", "label": "サラダ油"},
            {"value": "canola", "label": "菜種油"},
            {"value": "sesame_mix", "label": "ごま油"},
            {"value": "lard", "label": "ラード（豚の脂）"},
            {"value": "beef_fat", "label": "牛脂"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "tempura_batter": {
        "question": "天ぷらの衣に卵は入っていますか？",
        "type": "radio",
        "parent": "frying_oil",
        "options": [
            {"value": "yes_egg", "label": "はい（天ぷら粉 or 卵入り）"},
            {"value": "no_egg", "label": "いいえ（小麦粉のみ）"},
            {"value": "rice_flour", "label": "米粉を使っている"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "karaage_marinade": {
        "question": "唐揚げの下味・衣に使っている材料は？（複数OK）",
        "type": "checkbox",
        "parent": "frying_oil",
        "options": [
            {"value": "soy_sauce", "label": "醤油"},
            {"value": "egg", "label": "卵"},
            {"value": "wheat_flour", "label": "小麦粉"},
            {"value": "potato_starch", "label": "片栗粉"},
            {"value": "garlic", "label": "にんにく"},
            {"value": "ginger", "label": "生姜"},
            {"value": "sake", "label": "酒"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "pasta_type": {
        "question": "パスタは生パスタ（卵入り）ですか？乾麺（小麦のみ）ですか？",
        "type": "radio",
        "parent": None,
        "options": [
            {"value": "fresh_egg", "label": "生パスタ（卵入り）"},
            {"value": "dried", "label": "乾麺（小麦のみ）"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "dashi_base": {
        "question": "メインの出汁・スープのベースは？",
        "type": "radio",
        "parent": None,
        "options": [
            {"value": "bonito", "label": "鰹出汁"},
            {"value": "kelp", "label": "昆布出汁"},
            {"value": "bonito_kelp", "label": "合わせ（鰹+昆布）"},
            {"value": "niboshi", "label": "煮干し"},
            {"value": "chicken", "label": "鶏ガラ"},
            {"value": "pork_bone", "label": "豚骨"},
            {"value": "shellfish", "label": "貝・海老・蟹"},
            {"value": "granule", "label": "顆粒だし"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "dashi_sub": {
        "question": "他にも使う出汁はありますか？（複数OK・なければスキップ）",
        "type": "checkbox",
        "parent": "dashi_base",
        "options": [
            {"value": "bonito", "label": "鰹出汁"},
            {"value": "kelp", "label": "昆布出汁"},
            {"value": "bonito_kelp", "label": "合わせ（鰹+昆布）"},
            {"value": "niboshi", "label": "煮干し"},
            {"value": "chicken", "label": "鶏ガラ"},
            {"value": "pork_bone", "label": "豚骨"},
            {"value": "shellfish", "label": "貝・海老・蟹"},
            {"value": "granule", "label": "顆粒だし"},
            {"value": "none_above", "label": "他にはない"},
        ],
    },
    "ramen_broth": {
        "question": "ラーメンのスープに入っているものは？（複数OK）",
        "type": "checkbox",
        "parent": None,
        "options": [
            {"value": "chicken", "label": "鶏ガラ"},
            {"value": "pork_bone", "label": "豚骨"},
            {"value": "niboshi", "label": "煮干し・魚粉"},
            {"value": "shellfish", "label": "海老・貝"},
            {"value": "soy_sauce", "label": "醤油（タレ）"},
            {"value": "miso", "label": "味噌（大豆）"},
            {"value": "backfat", "label": "背脂"},
            {"value": "garlic", "label": "にんにく"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "sauce_base": {
        "question": "焼き物や丼のタレ・ソースに使っている材料は？（複数OK）",
        "type": "checkbox",
        "parent": None,
        "options": [
            {"value": "soy_sauce", "label": "醤油"},
            {"value": "miso", "label": "味噌"},
            {"value": "worcester", "label": "ウスターソース"},
            {"value": "demiglace", "label": "デミグラスソース（小麦入り）"},
            {"value": "tomato", "label": "トマトソース"},
            {"value": "ponzu", "label": "ポン酢"},
            {"value": "mirin", "label": "みりん（アルコール）"},
            {"value": "oyster", "label": "オイスターソース"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "dressing": {
        "question": "サラダのドレッシングは何を使っていますか？",
        "type": "checkbox",
        "parent": None,
        "options": [
            {"value": "wafu_soy", "label": "和風（醤油ベース）"},
            {"value": "sesame", "label": "ごまドレッシング"},
            {"value": "mayo", "label": "マヨネーズ（卵入り）"},
            {"value": "caesar", "label": "シーザー（卵・乳・アンチョビ）"},
            {"value": "olive_oil", "label": "オリーブオイル＆塩"},
            {"value": "french", "label": "フレンチ（酢・油）"},
            {"value": "homemade", "label": "自家製（成分は商品による）"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "curry_base": {
        "question": "カレーのルー・ベースは？",
        "type": "radio",
        "parent": None,
        "options": [
            {"value": "commercial_roux", "label": "市販ルー（小麦・乳入り）"},
            {"value": "homemade_wheat", "label": "自家製（小麦粉あり）"},
            {"value": "homemade_spice", "label": "自家製スパイスカレー（小麦なし）"},
            {"value": "nut_paste", "label": "ナッツペースト入り"},
            {"value": "yogurt", "label": "ヨーグルト入り"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "bread_base": {
        "question": "パン・ナン・ピザ生地に卵や乳製品は入っていますか？",
        "type": "radio",
        "parent": None,
        "options": [
            {"value": "egg_milk", "label": "卵＋乳製品あり"},
            {"value": "egg_only", "label": "卵のみ（乳なし）"},
            {"value": "milk_only", "label": "乳製品のみ（卵なし）"},
            {"value": "wheat_only", "label": "小麦のみ（卵・乳なし）"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "gelatin_source": {
        "question": "プリン・パンナコッタ・ゼリー等を固めるのに何を使っていますか？",
        "type": "checkbox",
        "parent": None,
        "options": [
            {"value": "pork_gelatin", "label": "ゼラチン（豚由来）"},
            {"value": "beef_gelatin", "label": "ゼラチン（牛由来）"},
            {"value": "agar", "label": "寒天（植物性）"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
    "gyoza_wrapper": {
        "question": "餃子の皮に卵は入っていますか？",
        "type": "radio",
        "parent": None,
        "options": [
            {"value": "egg_in", "label": "卵入り"},
            {"value": "wheat_only", "label": "小麦のみ（卵なし）"},
            {"value": "varies", "label": "商品によって違う"},
            {"value": "unknown", "label": "わからない"},
        ],
    },
}

# --- 波及ルール ---
# 制約(restrictions_fail)の原則:
#   肉・魚・魚介 → vegan + vegetarian 両方を立てる
#   卵・乳のみ   → vegan のみ（ovo/lactoベジは可）
#   豚 → halal, no_pork 追加 / 牛 → hindu 追加 / 酒 → no_alcohol
CASCADE_RULES = {
    "signature_menu": {},
    "cooking_oil": {
        "salad_oil":   {},
        "sesame_oil":  {"add_allergens": ["sesame"],  "applies_to": "stir_fry"},
        "butter":      {"add_allergens": ["milk"],    "applies_to": "stir_fry",
                        "restrictions_fail": ["vegan"]},
        "lard":        {"add_allergens": ["pork"],    "applies_to": "stir_fry",
                        "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "olive_oil":   {},
        "ghee":        {"add_allergens": ["milk"],    "applies_to": "stir_fry",
                        "restrictions_fail": ["vegan"]},
        "coconut_oil": {},
        "varies":      {},
        "unknown":     {},
    },
    # サブ油: メインと同じ波及（記録だけにしない）。none_above は無効
    "cooking_oil_sub": {
        "salad_oil":   {},
        "sesame_oil":  {"add_allergens": ["sesame"],  "applies_to": "stir_fry"},
        "butter":      {"add_allergens": ["milk"],    "applies_to": "stir_fry",
                        "restrictions_fail": ["vegan"]},
        "lard":        {"add_allergens": ["pork"],    "applies_to": "stir_fry",
                        "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "olive_oil":   {},
        "ghee":        {"add_allergens": ["milk"],    "applies_to": "stir_fry",
                        "restrictions_fail": ["vegan"]},
        "coconut_oil": {},
        "none_above":  {},
    },
    "frying_oil": {
        "canola":     {"remove_allergens": ["sesame", "soybean"], "applies_to": "fried_all"},
        "salad_oil":  {"applies_to": "fried_all"},
        "sesame_mix": {"add_allergens": ["sesame"],               "applies_to": "fried_all"},
        "lard":       {"add_allergens": ["pork"],                 "applies_to": "fried_all",
                       "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "beef_fat":   {"add_allergens": ["beef"],                 "applies_to": "fried_all",
                       "restrictions_fail": ["hindu", "vegan", "vegetarian"]},
        "varies":     {},
        "unknown":    {},
    },
    "tempura_batter": {
        # 衣は小麦が基本。卵入りでも小麦は付く
        "yes_egg":    {"add_allergens": ["egg", "wheat"], "applies_to": "tempura",
                       "restrictions_fail": ["vegan"]},
        "no_egg":     {"add_allergens": ["wheat"],        "applies_to": "tempura"},
        "rice_flour": {"remove_allergens": ["wheat"],     "applies_to": "tempura"},
        "varies":     {},
        "unknown":    {},
    },
    "karaage_marinade": {
        "soy_sauce":     {"add_allergens": ["soybean"], "applies_to": "karaage"},
        "egg":           {"add_allergens": ["egg"],     "applies_to": "karaage",
                          "restrictions_fail": ["vegan"]},
        "wheat_flour":   {"add_allergens": ["wheat"],   "applies_to": "karaage"},
        "potato_starch": {"applies_to": "karaage"},
        "garlic":        {},
        "ginger":        {},
        "sake":          {},
        "varies":        {},
        "unknown":       {},
    },
    "pasta_type": {
        "fresh_egg":   {"add_allergens": ["egg", "wheat"], "applies_to": "pasta",
                        "restrictions_fail": ["vegan"]},
        "dried":       {"add_allergens": ["wheat"],        "applies_to": "pasta"},
        "varies":      {},
        "unknown":     {},
    },
    "dashi_base": {
        "bonito":      {"add_allergens": ["fish"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "kelp":        {},
        "bonito_kelp": {"add_allergens": ["fish"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "niboshi":     {"add_allergens": ["fish"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "chicken":     {"add_allergens": ["chicken"], "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "pork_bone":   {"add_allergens": ["pork"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "shellfish":   {"add_allergens": ["shrimp", "crab"], "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "granule":     {"applies_to": "dashi_dishes"},  # 種類不明=推測しない（無印）
        "varies":      {},
        "unknown":     {},
    },
    # サブ出汁: メインと同じ波及
    "dashi_sub": {
        "bonito":      {"add_allergens": ["fish"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "kelp":        {},
        "bonito_kelp": {"add_allergens": ["fish"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "niboshi":     {"add_allergens": ["fish"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "chicken":     {"add_allergens": ["chicken"], "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "pork_bone":   {"add_allergens": ["pork"],    "applies_to": "dashi_dishes",
                        "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "shellfish":   {"add_allergens": ["shrimp", "crab"], "applies_to": "dashi_dishes",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "granule":     {"applies_to": "dashi_dishes"},
        "none_above":  {},
    },
    "ramen_broth": {
        "chicken":     {"add_allergens": ["chicken"], "applies_to": "ramen",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "pork_bone":   {"add_allergens": ["pork"],    "applies_to": "ramen",
                        "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "niboshi":     {"add_allergens": ["fish"],    "applies_to": "ramen",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "shellfish":   {"add_allergens": ["shrimp"],  "applies_to": "ramen",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "soy_sauce":   {"add_allergens": ["soybean"], "applies_to": "ramen"},
        "miso":        {"add_allergens": ["soybean"], "applies_to": "ramen"},
        "backfat":     {"add_allergens": ["pork"],    "applies_to": "ramen",
                        "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "garlic":      {},
        "varies":      {},
        "unknown":     {},
    },
    "sauce_base": {
        "soy_sauce":   {"add_allergens": ["soybean"], "applies_to": "grilled_bowl"},
        "miso":        {"add_allergens": ["soybean"], "applies_to": "grilled_bowl"},
        "worcester":   {},
        "demiglace":   {"add_allergens": ["wheat", "milk"], "applies_to": "grilled_bowl"},
        "tomato":      {},
        "ponzu":       {"add_allergens": ["soybean"], "applies_to": "grilled_bowl"},
        "mirin":       {"restrictions_fail": ["no_alcohol"], "applies_to": "grilled_bowl"},
        "oyster":      {"applies_to": "grilled_bowl"},
        "varies":      {},
        "unknown":     {},
    },
    "dressing": {
        "wafu_soy":    {"add_allergens": ["soybean"], "applies_to": "salad"},
        "sesame":      {"add_allergens": ["sesame"],  "applies_to": "salad"},
        "mayo":        {"add_allergens": ["egg"],     "applies_to": "salad",
                        "restrictions_fail": ["vegan"]},
        "caesar":      {"add_allergens": ["egg", "milk", "fish"], "applies_to": "salad",
                        "restrictions_fail": ["vegan", "vegetarian"]},
        "olive_oil":   {},
        "french":      {},
        "homemade":    {},
        "varies":      {},
        "unknown":     {},
    },
    "curry_base": {
        "commercial_roux": {"add_allergens": ["wheat", "milk"], "applies_to": "curry"},
        "homemade_wheat":  {"add_allergens": ["wheat"],         "applies_to": "curry"},
        "homemade_spice":  {},
        "nut_paste":       {"add_allergens": ["peanut"],        "applies_to": "curry"},
        "yogurt":          {"add_allergens": ["milk"],          "applies_to": "curry",
                            "restrictions_fail": ["vegan"]},
        "varies":          {},
        "unknown":         {},
    },
    "bread_base": {
        # パン・ナン・ピザ生地は小麦が基本。卵/乳の有無に関わらず小麦を付ける
        "egg_milk":    {"add_allergens": ["egg", "milk", "wheat"], "applies_to": "bread",
                        "restrictions_fail": ["vegan"]},
        "egg_only":    {"add_allergens": ["egg", "wheat"],         "applies_to": "bread",
                        "restrictions_fail": ["vegan"]},
        "milk_only":   {"add_allergens": ["milk", "wheat"],        "applies_to": "bread",
                        "restrictions_fail": ["vegan"]},
        "wheat_only":  {"add_allergens": ["wheat"],               "applies_to": "bread"},
        "varies":      {},
        "unknown":     {},
    },
    "gelatin_source": {
        "pork_gelatin": {"add_allergens": ["gelatin", "pork"], "applies_to": "gelatin_target",
                         "restrictions_fail": ["halal", "vegan", "vegetarian", "no_pork"]},
        "beef_gelatin": {"add_allergens": ["gelatin", "beef"], "applies_to": "gelatin_target",
                         "restrictions_fail": ["vegan", "vegetarian", "hindu"]},
        "agar":         {"applies_to": "gelatin_target"},
        "varies":       {},
        "unknown":      {},
    },
    "gyoza_wrapper": {
        "egg_in":      {"add_allergens": ["egg", "wheat"], "applies_to": "gyoza",
                        "restrictions_fail": ["vegan"]},
        "wheat_only":  {"add_allergens": ["wheat"],        "applies_to": "gyoza"},
        "varies":      {},
        "unknown":     {},
    },
}

def _get_food_menus(restaurant_id: int, db: Session) -> list:
    menus = db.query(Menu).filter(Menu.restaurant_id == restaurant_id).all()
    return [m for m in menus if (m.category or "").lower() not in DRINK_CATEGORIES]


def _get_all_menus(restaurant_id: int, db: Session) -> list:
    return db.query(Menu).filter(Menu.restaurant_id == restaurant_id).all()


def _menu_name(m: Menu) -> str:
    return m.name_jp or ""


def _has_keyword(name: str, keywords: list) -> bool:
    for kw in keywords:
        if kw not in name:
            continue
        if kw == "カツ":
            idx = name.find(kw)
            while idx >= 0:
                next_char = name[idx + len(kw):idx + len(kw) + 1]
                if next_char != "オ":
                    return True
                idx = name.find(kw, idx + 1)
            continue
        if kw == "揚げ":
            idx = name.find(kw)
            while idx >= 0:
                prev_char = name[idx - 1:idx] if idx > 0 else ""
                if prev_char not in ("唐", "か"):
                    return True
                idx = name.find(kw, idx + 1)
            continue
        return True
    return False


def _has_any_keyword(menus: list, keywords: list) -> bool:
    return any(_has_keyword(_menu_name(m), keywords) for m in menus)


def _get_fried_menus(menus: list) -> list:
    return [m for m in menus
            if _has_keyword(_menu_name(m), FRIED_KEYWORDS)
            or (m.category or "").lower() == "tempura"]


def _get_tempura_menus(menus: list) -> list:
    return [m for m in menus
            if _has_keyword(_menu_name(m), TEMPURA_KEYWORDS)]


def _get_karaage_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), KARAAGE_KEYWORDS)]


# 油を使わない料理（cooking_oil の波及対象から除外）
RAW_NO_OIL_KEYWORDS = [
    "刺身", "お造り", "造り", "刺し", "寿司", "鮨", "寿し", "カルパッチョ",
    "冷奴", "酢の物", "なめろう", "ユッケ", "タルタル", "マリネ", "サラダ", "漬け",
]


def _get_stir_fry_menus(menus: list) -> list:
    out = []
    for m in menus:
        if (m.category or "").lower() not in {"main", "side", "yakitori", "appetizer"}:
            continue
        # 生もの・酢の物等は調理油を使わない → メイン油の波及対象外
        if _has_keyword(_menu_name(m), RAW_NO_OIL_KEYWORDS):
            continue
        out.append(m)
    return out


def _get_dashi_menus(menus: list) -> list:
    return [m for m in menus if (m.category or "").lower() in DASHI_CATEGORIES]


def _get_ramen_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), RAMEN_KEYWORDS)
            or (m.category or "").lower() == "ramen"]


def _get_salad_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), SALAD_KEYWORDS)
            or (m.category or "").lower() == "salad"]


def _get_dessert_menus(menus: list) -> list:
    return [m for m in menus if (m.category or "").lower() == "dessert"]


def _get_gelatin_menus(all_menus: list) -> list:
    """デザート全品 + ゼラチン系ドリンク（パンナコッタ等）"""
    result = []
    for m in all_menus:
        cat = (m.category or "").lower()
        if cat == "dessert":
            result.append(m)
        elif _has_keyword(_menu_name(m), GELATIN_KEYWORDS):
            result.append(m)
    return result


def _get_pasta_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), PASTA_KEYWORDS)
            or (m.category or "").lower() == "pasta"]


def _get_curry_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), CURRY_KEYWORDS)
            or (m.category or "").lower() == "curry"]


def _get_bread_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), BREAD_KEYWORDS)
            or (m.category or "").lower() in {"bread", "pizza"}]


GRILLED_BOWL_CATEGORIES = {"main", "yakitori", "side", "rice", "appetizer"}
SAUCE_KEYWORDS = ["タレ", "ソース", "照り焼き", "丼", "焼き鳥", "つくね"]


def _get_grilled_bowl_menus(menus: list) -> list:
    return [m for m in menus
            if (m.category or "").lower() in GRILLED_BOWL_CATEGORIES
            or _has_keyword(_menu_name(m), SAUCE_KEYWORDS)]


def _get_gyoza_menus(menus: list) -> list:
    return [m for m in menus if _has_keyword(_menu_name(m), GYOZA_KEYWORDS)]


def _get_target_menus_by_scope(scope: str, menus: list) -> list:
    if scope == "fried_all":
        return _get_fried_menus(menus)
    elif scope == "tempura":
        return _get_tempura_menus(menus)
    elif scope == "karaage":
        return _get_karaage_menus(menus)
    elif scope == "stir_fry":
        return _get_stir_fry_menus(menus)
    elif scope == "dashi_dishes":
        return _get_dashi_menus(menus)
    elif scope == "ramen":
        return _get_ramen_menus(menus)
    elif scope == "salad":
        return _get_salad_menus(menus)
    elif scope == "dessert_all":
        return _get_dessert_menus(menus)
    elif scope == "gelatin_target":
        return _get_gelatin_menus(menus)
    elif scope == "pasta":
        return _get_pasta_menus(menus)
    elif scope == "curry":
        return _get_curry_menus(menus)
    elif scope == "bread":
        return _get_bread_menus(menus)
    elif scope == "grilled_bowl":
        return _get_grilled_bowl_menus(menus)
    elif scope == "gyoza":
        return _get_gyoza_menus(menus)
    return menus


# --- 公開関数 ---

def get_phase1_questions(menus: list, all_menus: list = None) -> list:
    """メニュー構成に応じて出すべき質問IDリストを返す（優先度順）"""
    questions = []
    menu_names = [_menu_name(m) for m in menus]
    categories = [(m.category or "").lower() for m in menus]

    # ゼラチン判定用: ドリンク含む全メニュー
    if all_menus is None:
        all_menus = menus
    all_names = [_menu_name(m) for m in all_menus]

    # 1. signature_menu（全店共通）
    questions.append("signature_menu")

    # 2. cooking_oil + sub: main/side/yakitori/appetizer
    if any(c in {"main", "side", "yakitori", "appetizer"} for c in categories):
        questions.append("cooking_oil")
        questions.append("cooking_oil_sub")

    # 3. frying_oil + children
    has_fried = any(_has_keyword(n, FRIED_KEYWORDS) for n in menu_names) \
                or "tempura" in categories
    if has_fried:
        questions.append("frying_oil")
        if any(_has_keyword(n, TEMPURA_KEYWORDS) for n in menu_names) or "tempura" in categories:
            questions.append("tempura_batter")
        if any(_has_keyword(n, KARAAGE_KEYWORDS) for n in menu_names):
            questions.append("karaage_marinade")

    # pasta_type: パスタキーワード（一括仕入れ＝キッチン共有リソース）
    if _has_any_keyword(menus, PASTA_KEYWORDS) or "pasta" in categories:
        questions.append("pasta_type")

    # dashi_base + sub
    if any(c in DASHI_CATEGORIES for c in categories):
        questions.append("dashi_base")
        questions.append("dashi_sub")

    # ramen_broth
    if _has_any_keyword(menus, RAMEN_KEYWORDS) or "ramen" in categories:
        questions.append("ramen_broth")

    # sauce_base: 焼き物・丼・タレ系
    if any(c in GRILLED_BOWL_CATEGORIES for c in categories) \
       or _has_any_keyword(menus, SAUCE_KEYWORDS):
        questions.append("sauce_base")

    # dressing: サラダ系
    if _has_any_keyword(menus, SALAD_KEYWORDS) or "salad" in categories:
        questions.append("dressing")

    # curry_base
    if _has_any_keyword(menus, CURRY_KEYWORDS) or "curry" in categories:
        questions.append("curry_base")

    # bread_base
    if _has_any_keyword(menus, BREAD_KEYWORDS) or any(c in {"bread", "pizza"} for c in categories):
        questions.append("bread_base")

    # gelatin_source: デザート+ゼラチン系ドリンク（パンナコッタ等）
    if any((m.category or "").lower() == "dessert" for m in all_menus) \
       or _has_any_keyword(all_menus, GELATIN_KEYWORDS):
        questions.append("gelatin_source")

    # gyoza_wrapper
    if _has_any_keyword(menus, GYOZA_KEYWORDS):
        questions.append("gyoza_wrapper")

    return questions


def get_phase1_question_detail(question_id: str, menus: list, all_menus: list = None, lang: str = "ja") -> dict | None:
    """UI表示用の質問データを返す。
    lang(ja/en/...)で質問文・選択肢ラベルを差し替える(訳が無ければ JP)。
    店主向けは ja 固定、admin/プラットフォーム閲覧時のみ別言語を渡す。"""
    from app.admin_api.kitchen_profile_i18n import localize_question_text, localize_option_label

    q = KITCHEN_QUESTIONS.get(question_id)
    if not q:
        return None

    scope_map = {
        "frying_oil": "fried_all",
        "tempura_batter": "tempura",
        "karaage_marinade": "karaage",
        "cooking_oil": "stir_fry",
        "pasta_type": "pasta",
        "dashi_base": "dashi_dishes",
        "ramen_broth": "ramen",
        "sauce_base": "grilled_bowl",
        "dressing": "salad",
        "curry_base": "curry",
        "bread_base": "bread",
        "gelatin_source": "gelatin_target",
        "gyoza_wrapper": "gyoza",
    }
    scope = scope_map.get(question_id, "")

    target = _get_target_menus_by_scope(scope, menus) if scope else menus
    affected = len(target)

    detail = {
        "id": question_id,
        "question": localize_question_text(question_id, q["question"], lang),
        "type": q["type"],
        "options": [
            {"value": o["value"], "label": localize_option_label(question_id, o["value"], o["label"], lang)}
            for o in q["options"]
        ] if q["options"] else None,
        "affected_menu_count": affected,
        "is_branch": q["parent"] is not None,
        "parent_id": q["parent"],
        "allow_note": True,  # 全 KITCHEN_QUESTIONS で自由記入欄を有効化（補足を拾うため）
    }

    if q.get("max_select"):
        detail["max_select"] = q["max_select"]

    # menu_selectタイプの場合はメニューリストを添付
    if q["type"] == "menu_select":
        food_menus = [m for m in menus if (m.category or "").lower() not in DRINK_CATEGORIES]
        detail["menu_list"] = [{"uid": m.uid, "name": _menu_name(m)} for m in food_menus]

    return detail


def allergen_has_ingredient_source(allergen_name_lower: str, menu_ingredients) -> bool:
    for ing in menu_ingredients:
        flag = (ing.allergen_flag or "").lower()
        if not flag:
            continue
        # 'fish:0.3' のような確信度付きトークンに対応(":確信度"を除去して比較)
        flags = [f.strip().split(":")[0] for f in flag.split(",")]
        if allergen_name_lower in flags:
            return True
    return False


def safe_remove_allergens(menu: Menu, allergens_to_remove: list, db: Session):
    for allergen_key in allergens_to_remove:
        if allergen_has_ingredient_source(allergen_key, menu.ingredients or []):
            continue
        normalized = normalize_allergen_name(allergen_key)
        if not normalized:
            continue
        to_remove = None
        for a in (menu.allergens or []):
            if a.name_en == normalized:
                to_remove = a
                break
        if to_remove:
            menu.allergens.remove(to_remove)


def apply_kitchen_answer(
    restaurant_id: int,
    question_id: str,
    selected_value,
    per_item_answers: dict | None,
    supplement_text: str | None,
    db: Session,
    actor: dict | None = None,
) -> dict:
    """
    Phase 1回答を適用: CASCADE_RULESで波及 + store_knowledge保存
    actor = {"via": owner_mode|admin_owner|admin_platform, "user_id": int|None}
    誰が回答したかの出所(代行運用の監査用)。store_knowledge に記録する。
    """
    q_def = KITCHEN_QUESTIONS.get(question_id)
    if not q_def:
        raise ValueError(f"Unknown question_id: {question_id}")

    food_menus = _get_food_menus(restaurant_id, db)
    rules = CASCADE_RULES.get(question_id, {})

    # gelatin_source: ドリンク含む全メニューが波及対象
    if question_id == "gelatin_source":
        menu_pool = _get_all_menus(restaurant_id, db)
    else:
        menu_pool = food_menus

    # checkbox（複数値）対応
    values = [selected_value] if isinstance(selected_value, str) else selected_value

    allergens_added = set()
    allergens_removed = set()
    affected_menus = 0

    for val in values:
        if val == "varies" and per_item_answers:
            for menu_uid, item_val in per_item_answers.items():
                item_rule = rules.get(item_val, {})
                menu = next((m for m in menu_pool if m.uid == menu_uid), None)
                if not menu:
                    continue
                added, removed = _apply_rule_to_menu(menu, item_rule, db)
                allergens_added.update(added)
                allergens_removed.update(removed)
                affected_menus += 1
            continue

        # varies without per_item_answers: skip
        if val == "varies":
            continue

        rule = rules.get(val, {})
        scope = rule.get("applies_to")
        if not scope:
            continue

        target_menus = _get_target_menus_by_scope(scope, menu_pool)
        for menu in target_menus:
            added, removed = _apply_rule_to_menu(menu, rule, db)
            allergens_added.update(added)
            allergens_removed.update(removed)
            affected_menus += 1

    # store_knowledge に保存
    store_val = values if len(values) > 1 else values[0] if values else ""
    _save_store_knowledge(restaurant_id, question_id, store_val, supplement_text, db, actor=actor)

    # signature_menuは特別処理
    if question_id == "signature_menu" and values:
        _apply_signature(food_menus, values, db)

    db.flush()
    return {
        "question_id": question_id,
        "affected_menus": affected_menus,
        "allergens_added": list(allergens_added),
        "allergens_removed": list(allergens_removed),
    }


def _apply_signature(food_menus: list, menu_uids: list, db: Session):
    """看板メニューのsignature_scoreを更新"""
    for i, uid in enumerate(menu_uids[:3]):
        menu = next((m for m in food_menus if m.uid == uid), None)
        if menu:
            menu.signature_score = 100 - (i * 10)  # 100, 90, 80


def _apply_rule_to_menu(menu: Menu, rule: dict, db: Session) -> tuple:
    added = set()
    removed = set()

    for allergen_key in rule.get("add_allergens", []):
        normalized = normalize_allergen_name(allergen_key)
        if not normalized:
            continue
        existing_names = {a.name_en for a in (menu.allergens or [])}
        if normalized not in existing_names:
            allergen = db.query(Allergen).filter(Allergen.name_en == normalized).first()
            if allergen:
                menu.allergens.append(allergen)
                added.add(normalized)

    for allergen_key in rule.get("remove_allergens", []):
        if allergen_has_ingredient_source(allergen_key, menu.ingredients or []):
            continue
        normalized = normalize_allergen_name(allergen_key)
        if not normalized:
            continue
        to_remove = None
        for a in (menu.allergens or []):
            if a.name_en == normalized:
                to_remove = a
                break
        if to_remove:
            menu.allergens.remove(to_remove)
            removed.add(normalized)

    for restriction_name in rule.get("restrictions_fail", []):
        restriction = db.query(Restriction).filter(
            Restriction.name_en.ilike(restriction_name)
        ).first()
        if restriction:
            existing_ids = {r.id for r in (menu.restrictions or [])}
            if restriction.id not in existing_ids:
                menu.restrictions.append(restriction)

    # VADマーキング: 店主回答に基づく変更を記録
    fc = dict(menu.field_confidence or {})
    store_verified = fc.get("store_verified", [])
    if not isinstance(store_verified, list):
        store_verified = []
    if "kitchen_profile" not in store_verified:
        store_verified.append("kitchen_profile")
    fc["store_verified"] = store_verified
    menu.field_confidence = fc

    # verification_rank昇格: AI推定(C)→店主確認済み(B)
    if menu.verification_rank in (None, "C"):
        menu.verification_rank = "B"

    return added, removed


def labels_for_values(question_id: str, values: list) -> list[str]:
    """値コード→選択肢ラベル。プロンプト注入・サマリー表示など読み手向け変換の正本。"""
    q_def = KITCHEN_QUESTIONS.get(question_id) or {}
    label_by_value = {o["value"]: o["label"] for o in (q_def.get("options") or [])}
    return [label_by_value.get(str(v), str(v)) for v in values]


def _save_store_knowledge(
    restaurant_id: int, key: str, value, supplement_text: str | None, db: Session,
    category: str = "kitchen_profile", actor: dict | None = None,
):
    # actor = {"via": owner_mode|admin_owner|admin_platform, "user_id": int|None}
    # 誰が回答したかの出所。代行運用の監査用(回答自体はブロックしない)。
    via = (actor or {}).get("via")
    by_user = (actor or {}).get("user_id")

    val_str = json.dumps(value, ensure_ascii=False) if not isinstance(value, str) else value

    existing = db.query(StoreKnowledge).filter(
        StoreKnowledge.restaurant_id == restaurant_id,
        StoreKnowledge.key == key,
    ).first()

    if existing:
        existing.value = val_str
        existing.source = "owner"
        existing.verified = True
        if via:
            existing.answered_via = via
            existing.answered_by_user_id = by_user
    else:
        sk = StoreKnowledge(
            restaurant_id=restaurant_id,
            key=key,
            value=val_str,
            category=category,
            source="owner",
            verified=True,
            answered_via=via,
            answered_by_user_id=by_user,
        )
        db.add(sk)

    if supplement_text and supplement_text.strip():
        supp_key = f"{key}_supplement"
        existing_supp = db.query(StoreKnowledge).filter(
            StoreKnowledge.restaurant_id == restaurant_id,
            StoreKnowledge.key == supp_key,
        ).first()
        if existing_supp:
            existing_supp.value = supplement_text.strip()
            existing_supp.source = "owner"
            existing_supp.verified = True
            if via:
                existing_supp.answered_via = via
                existing_supp.answered_by_user_id = by_user
        else:
            sk_supp = StoreKnowledge(
                restaurant_id=restaurant_id,
                key=supp_key,
                value=supplement_text.strip(),
                category="kitchen_profile",
                source="owner",
                verified=True,
                answered_via=via,
                answered_by_user_id=by_user,
            )
            db.add(sk_supp)


def reapply_kitchen_profile_to_menus(restaurant_id: int, menu_uids: list, db: Session) -> int:
    """既存のkitchen_profile回答を新メニューに再適用（CASCADEルール）
    メニュー追加時に呼び出し、店主回答済みのアレルゲン・制約を自動波及させる。
    """
    sk_entries = db.query(StoreKnowledge).filter(
        StoreKnowledge.restaurant_id == restaurant_id,
        StoreKnowledge.category == "kitchen_profile",
    ).all()
    if not sk_entries:
        return 0

    target_menus = db.query(Menu).filter(Menu.uid.in_(menu_uids)).all()
    if not target_menus:
        return 0

    affected = 0
    for entry in sk_entries:
        question_id = entry.key
        if question_id.endswith("_supplement"):
            continue
        rules = CASCADE_RULES.get(question_id, {})
        if not rules:
            continue

        # Parse stored value (string or JSON array)
        try:
            parsed = json.loads(entry.value)
            values = parsed if isinstance(parsed, list) else [parsed]
        except (json.JSONDecodeError, TypeError):
            values = [entry.value]

        # gelatin_source: ドリンク含む全新メニューが対象
        if question_id == "gelatin_source":
            menu_pool = target_menus
        else:
            menu_pool = [m for m in target_menus
                         if (m.category or "").lower() not in DRINK_CATEGORIES]

        for val in values:
            rule = rules.get(val, {})
            scope = rule.get("applies_to")
            if not scope:
                continue
            for menu in _get_target_menus_by_scope(scope, menu_pool):
                _apply_rule_to_menu(menu, rule, db)
                affected += 1

    if affected > 0:
        db.flush()
    return affected


def detect_unanswered_questions(restaurant_id: int, db: Session) -> list:
    """メニュー構成から必要な質問を算出し、store_knowledgeに回答がない質問IDを返す。
    判定に使うのは name_jp/category だけなので列射影でロードする
    (店主チャットの毎タップで呼ばれる経路。全カラムhydrationだと大型店で重い)。"""
    all_menus = db.query(Menu.name_jp, Menu.category).filter(
        Menu.restaurant_id == restaurant_id,
    ).all()
    food_menus = [m for m in all_menus
                  if (m.category or "").lower() not in DRINK_CATEGORIES]
    required = get_phase1_questions(food_menus, all_menus=all_menus)

    sk_entries = db.query(StoreKnowledge).filter(
        StoreKnowledge.restaurant_id == restaurant_id,
        StoreKnowledge.category == "kitchen_profile",
    ).all()
    answered = {e.key for e in sk_entries if not e.key.endswith("_supplement")}

    return [q for q in required if q not in answered]


def get_varies_menu_list(question_id: str, restaurant_id: int, db: Session) -> list:
    food_menus = _get_food_menus(restaurant_id, db)
    # 「商品によって違う」を選べる全質問の波及スコープ
    scope_map = {
        "cooking_oil": "stir_fry",
        "frying_oil": "fried_all",
        "tempura_batter": "tempura",
        "karaage_marinade": "karaage",
        "pasta_type": "pasta",
        "dashi_base": "dashi_dishes",
        "ramen_broth": "ramen",
        "sauce_base": "grilled_bowl",
        "dressing": "salad",
        "curry_base": "curry",
        "bread_base": "bread",
        "gelatin_source": "gelatin_target",
        "gyoza_wrapper": "gyoza",
    }
    scope = scope_map.get(question_id)
    if not scope:
        return []

    # gelatin_target はドリンク含む全メニュー
    if scope == "gelatin_target":
        all_menus = _get_all_menus(restaurant_id, db)
        target = _get_target_menus_by_scope(scope, all_menus)
    else:
        target = _get_target_menus_by_scope(scope, food_menus)
    return [{"menu_uid": m.uid, "menu_name": _menu_name(m)} for m in target]
