# 03 · アレルゲン・制限 — 鳥平（Torihei）

段階02 の材料から導出。各アレルゲンは特定の材料まで辿れ、連鎖の中で**もっとも弱い**
出典を継ぐ。状態は JP / US / EU / CA / AU 別（義務 `mand` / 推奨 `rec` / なし `none`）。
連鎖が `[INFERRED]` や `[UNKNOWN]` に依存するアレルゲンは**事実として断定せず** → GAP。

---

## 料理1 — 牛すじ煮込み（Beef tendon stew）
### アレルゲン
| アレルゲン | 由来材料 | 出典 | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| 魚（かつお） | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| 大豆 | 味付けベース（味噌/醤油） | [UNKNOWN] → GAP | rec | mand | mand | mand | mand |
| 小麦 | 醤油ベースの場合 | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
### 制限
| 制限 | 状態 | 由来 | 出典 |
|---|---|---|---|
| ベジタリアン / ヴィーガン | 不可（牛肉を含む） | beef tendon | [MENU·high] |
| ペスカタリアン | 不可（牛肉を含む） | beef tendon | [MENU·high] |
| no-beef | 不可（牛肉を含む） | beef tendon | [MENU·high] |
| ヒンドゥー | 不可（牛肉） | beef tendon | [MENU·high] |
| ハラル | おそらく不可（だし煮込みにアルコール/みりんが一般的。牛肉もハラル屠畜が必要） | 味付け/肉 | [INFERRED·low] → GAP |
### ここで生じた gap
- 味付けベース（味噌 vs 醤油）→ 大豆、醤油なら小麦
- だしの組成 → 魚（かつお）

## 料理2 — 鶏の唐揚げ（Chicken karaage）
### アレルゲン
| アレルゲン | 由来材料 | 出典 | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| 小麦 | 衣（小麦粉？）および/または 漬けダレの醤油 | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
| 大豆 | 漬けダレの醤油 | [INFERRED·med] → GAP | rec | mand | mand | mand | mand |
| ごま | 揚げ油（ごまブレンドの場合） | [UNKNOWN] → GAP | rec | mand | mand | mand | mand |
### 制限
| 制限 | 状態 | 由来 | 出典 |
|---|---|---|---|
| ベジタリアン / ヴィーガン | 不可（鶏） | chicken | [MENU·high] |
| no-beef / no-pork | 可（鶏のみ。共用フライヤーで豚が無い場合） | chicken | [INFERRED·med] → GAP（交差接触） |
| ハラル | おそらく不可（非ハラル鶏＋醤油/アルコール漬けダレ） | 鶏/漬けダレ | [INFERRED·low] → GAP |
| グルテンフリー | 不明（衣が片栗粉なら GF、小麦なら不可） | 衣 | [UNKNOWN] → GAP |
### ここで生じた gap
- 衣: 片栗粉 vs 小麦粉 → 小麦 / グルテンフリー
- 揚げ油: ごまブレンド？ → ごま
- 漬けダレに醤油？ → 大豆、小麦

## 料理3 — だし巻き卵（Dashimaki tamago）
### アレルゲン
| アレルゲン | 由来材料 | 出典 | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| 卵 | egg | [MENU·high] | mand | mand | mand | mand | mand |
| 魚（かつお） | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| 大豆 | 調味の醤油（使用時） | [INFERRED·low] → GAP | rec | mand | mand | mand | mand |
| 小麦 | 調味に醤油を使う場合 | [INFERRED·low] → GAP | mand | mand | mand | mand | mand |
### 制限
| 制限 | 状態 | 由来 | 出典 |
|---|---|---|---|
| ベジタリアン | だしが昆布のみなら可。かつおだしなら不可 | egg + dashi | [INFERRED·med] → GAP |
| ヴィーガン | 不可（卵） | egg | [MENU·high] |
| ペスカタリアン | 可 | egg/dashi | [MENU·high] |
### ここで生じた gap
- だしの組成（かつお vs 昆布のみ）→ 魚アレルゲン＋ベジタリアン可否
- 調味の醤油？ → 大豆、小麦

## 料理4 — ポテトサラダ（Potato salad）
### アレルゲン
| アレルゲン | 由来材料 | 出典 | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| 卵 | mayonnaise → 卵黄 | [INFERRED·high] → GAP | mand | mand | mand | mand | mand |
| （豚）— アレルゲンでなく制限を参照 | ハム/ベーコンがあれば | [INFERRED·low] → GAP | — | — | — | — | — |
### 制限
| 制限 | 状態 | 由来 | 出典 |
|---|---|---|---|
| ヴィーガン | 不可（マヨの卵） | mayonnaise | [INFERRED·high] → GAP |
| ベジタリアン | ハム/ベーコンが無ければ可 | ham/bacon? | [INFERRED·low] → GAP |
| no-pork / ハラル | 不明（ハム/ベーコン？） | ham/bacon? | [INFERRED·low] → GAP |
### ここで生じた gap
- マヨネーズの有無（卵）？ → 卵（可能性高いが未確認）
- ハム/ベーコンの有無？ → 豚 / no-pork / ハラル / ベジタリアン
- 注: 豚はアレルゲンではなく**制限**に分類（アレルゲン規則に従う）。

## 料理5 — 本日の刺身盛り合わせ（Today's assorted sashimi）
### アレルゲン
| アレルゲン | 由来材料 | 出典 | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| 魚 | 生魚（種類は確実、魚種は不明） | [INFERRED·high] → GAP（どの魚種） | rec | mand | mand | mand | mand |
| いくら（鮭卵） | 含まれる可能性 | [UNKNOWN] → GAP | rec | none | none | none | none |
| かに | 含まれる可能性 | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
| えび | 含まれる可能性 | [UNKNOWN] → GAP | mand | mand | mand | mand | mand |
| いか/あわび | 含まれる可能性 | [UNKNOWN] → GAP | rec | mand | mand | mand | mand |
| 大豆＋小麦 | 添えの醤油 | [INFERRED·med] → GAP | rec/mand | mand | mand | mand | mand |
### 制限
| 制限 | 状態 | 由来 | 出典 |
|---|---|---|---|
| ヴィーガン / ベジタリアン | 不可（生魚） | fish | [INFERRED·high] |
| ペスカタリアン | 可 | fish | [INFERRED·high] |
| no-beef / no-pork | 可 | 魚のみ | [INFERRED·high] |
| ハラル | 不可（醤油＋非ハラルの魚の取り扱いが一般的。貝の懸念も） | 魚/添え | [INFERRED·low] → GAP |
### ここで生じた gap
- 日替わりの魚種リスト → どの魚か。貝/頭足類/魚卵の有無？（複数アレルゲン）
- この料理は本質的に日替わり —— 魚種レベルのアレルギー回答には、一度きりの確認ではなく
  日々のオーナー入力が必要。

## 料理6 — 黒龍 純米吟醸（Kokuryu Junmai Ginjo）
### アレルゲン
| アレルゲン | 由来材料 | 出典 | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| （なし） | 米、麹、水 | [CANONICAL·high] | none | none | none | none | none |
### 制限
| 制限 | 状態 | 由来 | 出典 |
|---|---|---|---|
| no-alcohol | FAIL（アルコール約15.5%を含む） | sake | [CANONICAL·high] |
| ハラル | 不可（アルコール） | sake | [CANONICAL·high] |
| ヴィーガン / ベジタリアン | 可（純米: 米/麹/水。動物性なし） | sake | [CANONICAL·high] |
| グルテンフリー | 可（米ベース、小麦なし） | sake | [CANONICAL·high] |
### ここで生じた gap
- なし。product_master により完全に検証済み。

---

## 横断的な安全メモ
だしを含む2品（1, 3）は同じ katsuobushi → 魚 の疑問を共有。醤油の疑問は料理 1, 2, 3, 5
で繰り返し現れる。これらは「likely な答えが共通」でも料理ごとの gap である ——
「どこでも同じ X を使う」というオーナーの回答があれば解消するが、それまでは料理ごとに
OPEN のまま（推測を波及させない）。
