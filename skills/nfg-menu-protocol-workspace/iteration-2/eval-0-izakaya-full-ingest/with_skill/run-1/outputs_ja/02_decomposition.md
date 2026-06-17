# 02 · 分解 — 鳥平（Torihei）

各料理について: 構成要素 → 材料（複合材料は展開）、20種リストからの調理法、全項目に
出典タグ。ここで正規資産を適用: 日本酒は `product_master` に一致。食事系の料理は
`food_culture_kb` に一致なし。`ingredient_glossary` を要する用語なし（いずれも平易な
英語名を持つ一般的な品）。

---

## 料理1 — 牛すじ煮込み（Beef tendon stew）
- 英語名: Beef tendon stew  [INFERRED·high]（一般的な料理。用語集項目ではないが標準的な平易英語名）
- 構成要素・材料:
  - beef tendon（牛すじ）  [MENU·high]（牛すじ＝beef tendon、名称に明記）
  - konnyaku（こんにゃく）  [INFERRED·med]  ← この料理に非常によく入るが明記なし → gap
  - daikon（大根）  [INFERRED·low]  ← 地域差あり。よく入る → gap
  - dashi（複合 → kombu [INFERRED·med]、katsuobushi/かつお [INFERRED·med]）  [INFERRED·med]
  - 味付けのベース: miso または 醤油 または みりん/酒  [UNKNOWN]  ← 大豆/小麦を左右 → gap
  - negi（ねぎ）の薬味  [INFERRED·low]
- 調理法: 煮る/煮込む（煮込み＝stewed）  [MENU·high → INFERRED·high]
- 適用した正規一致: なし（食事系）。名称は標準英語であり用語集由来ではない
- メモ: 複合材料 `dashi` を展開し、隠れた魚アレルゲンを可視化。味付けベースが未確定で、
  安全に関わる主要な不明点（大豆 ± 小麦）。

## 料理2 — 鶏の唐揚げ（Chicken karaage / 日本式フライドチキン）
- 英語名: Chicken karaage (Japanese fried chicken)  [INFERRED·high]（日本由来の語で広く知られる。ローマ字＋注釈が適切）
- 構成要素・材料:
  - chicken（鶏、通常もも肉）  [MENU·high]（鶏＝chicken）
  - 漬けダレ: 醤油  [INFERRED·med]  ← 一般的。→ 大豆＋小麦 → gap
  - 漬けダレの香味: 生姜・にんにく  [INFERRED·low]
  - 衣の澱粉: 片栗粉 または 小麦粉 または ブレンド  [UNKNOWN]  ← 小麦を左右 → gap
  - 揚げ油: 植物油 か ごま油入りブレンドか  [UNKNOWN]  ← ごまを左右 → gap
- 調理法: 油で揚げる（唐揚げ）  [MENU·high → INFERRED·high]
- 適用した正規一致: なし。（用語集の教訓に注意: 片栗粉＝「Potato starch」であり
  cornstarch ではない —— 衣が確定した際に正しく訳すため記録）
- メモ: 独立した安全上の不明点が2つ —— 衣（小麦）と油（ごま）。どちらも断定不可。両方 → gap。

## 料理3 — だし巻き卵（Dashimaki tamago / 巻き卵）
- 英語名: Dashimaki tamago (rolled Japanese omelette)  [INFERRED·high]
- 構成要素・材料:
  - egg（卵）  [MENU·high]（卵＝egg、名称に明記）
  - dashi（複合 → kombu [INFERRED·med]、katsuobushi/かつお [INFERRED·med]）  [MENU·med]（だし＝dashi、名称に明記）
  - 調味: 醤油 and/or みりん、砂糖、塩  [INFERRED·low]  ← 大豆/小麦 → gap
- 調理法: 焼く/巻く（fry カテゴリの方法）  [INFERRED·high]
- 適用した正規一致: なし
- メモ: 卵は `[MENU·high]`（名称記載）。だしは名称に明記（だし）のため確実に含むが、
  だしの*組成*（ゆえに魚）は推測 → gap。かつお不使用の昆布だしの店もあり、仮定しない。

## 料理4 — ポテトサラダ（Potato salad）
- 英語名: Potato salad  [INFERRED·high]（平易な英語名が存在）
- 構成要素・材料:
  - potato（じゃがいも）  [MENU·high]（ポテト＝potato）
  - mayonnaise（複合 → 卵黄 [INFERRED·high]、酢、植物油）  [INFERRED·high]  ← 卵 → gap（ただし可能性高）
  - きゅうり、にんじん、玉ねぎ  [INFERRED·med]
  - ハム または ベーコン  [INFERRED·low]  ← あれば → 豚 → no-pork/halal 制限に影響 → gap
- 調理法: 茹でる（じゃがいも）後に和える（生で組み立て）  [INFERRED·med]
- 適用した正規一致: なし
- メモ: マヨネーズが「卵を隠す複合材料」（複合材料内アレルゲンの典型）。卵は可能性が高いが
  依然として推測 → gap。ハム/ベーコンの有無は制限に関わる不明点 → gap。

## 料理5 — 本日の刺身盛り合わせ（Today's assorted sashimi）
- 英語名: Today's assorted sashimi  [INFERRED·high]
- 構成要素・材料:
  - 盛り合わせの生魚 —— 具体的な魚種は日替わり  [UNKNOWN]  ← どの魚？ → gap（貝/イカの可能性も）
  - 付け合わせ: 大根（つま）、しそ、わさび  [INFERRED·med]
  - 醤油を添えて提供  [INFERRED·med]  ← 大豆＋小麦 → gap
- 調理法: 生  [INFERRED·high]
- 適用した正規一致: なし。用語集の教訓を記録: 後で特定の魚が確定したら丁寧に訳す
  （タイ → Sea bream、ローマ字化しない。バイ貝 → Whelk）。
- メモ: 内容は本質的に日替わり。魚アレルゲンは「種類としては確実」（刺身だから）だが、
  *具体的な魚種* や 甲殻類/頭足類/魚卵（例: かに、えび、いか、いくら）は不明 → 複数の gap。
  この料理は、オーナー/日替わりの入力なしには魚種レベルのアレルギー質問に安全に
  答えられない。

## 料理6 — 黒龍 純米吟醸（グラス）（Kokuryu Junmai Ginjo、グラス売り）
- 英語名: **Kokuryu Junmai Ginjo**  [CANONICAL·high]
- 正規一致: `product_master.json` → `pm_kokuryu_junmai_ginjo`
  - 製品の完全な同一性が一致: name_ja「黒龍 純米吟醸」== メニュー「黒龍 純米吟醸」。
    完全な同一性で一致させ、銘柄の部分一致ではない（龍 ⊂ 黒龍 の罠を回避）。
  - maker: 黒龍酒造 / Kokuryu Sake Brewing Co.  [CANONICAL·high]
  - category: sake / junmai_ginjo  [CANONICAL·high]
  - region: Fukui  [CANONICAL·high]
  - abv: 15.5%  [CANONICAL·high]
  - allergens: []（なし）  [CANONICAL·high]
  - restrictions: contains-alcohol; no-alcohol:fail  [CANONICAL·high]
  - verified_against: 蔵元公式スペック; 正規 verification_rank: S
- 構成要素・材料: 米、米麹、水（純米＝醸造アルコール無添加）  [CANONICAL·high（product_master のカテゴリ経由）]
- 調理法: 該当なし（醸造飲料）。提供＝注ぐ（グラス売り、グラス）  [MENU·high]
- メモ: 正規の上書きを適用 —— 検証済みスペックが ABV・アレルゲン・産地に関する
  モデルの推測に優先する。本実行で唯一の完全検証済みレコード。
