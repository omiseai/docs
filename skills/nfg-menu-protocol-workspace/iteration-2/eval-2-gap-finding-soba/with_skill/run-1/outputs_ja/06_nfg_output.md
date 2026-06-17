# 06 · NFG 出力 — そば店（`soba-shop-onboarding`）
status: **draft（オーナー承認待ち）**

料理ごとに1ブロック: 機械的意味＋人間向けナラティブ＋verification_rank。
オーナー回答はまだ存在しないため、安全に関わる推測/不明の項目はすべて NAMED GAP として
扱い、決して事実として断定しない。4品すべてオーナー確認前。

---

## 料理1 — ざるそば（Zaru soba）
- verification_rank: **C**（安全項目が未確認。そばはほぼ確実だが未確認。小麦/大豆/魚が OPEN）
- data_source: live

### 機械的意味
- ingredient_ids: buckwheat-flour [INFERRED·high → GAP 確認], wheat-flour(つなぎ?) [INFERRED·med → GAP],
  tsuyu{soy-sauce [INFERRED·high → GAP], dashi(kombu, katsuobushi) [INFERRED·med → GAP], mirin/sugar [INFERRED·low]},
  nori/negi/wasabi（薬味）[INFERRED·med]
- method_ids: boil, chill/rinse [INFERRED·high]
- allergens: そば = おそらくあり [INFERRED·high] —— flag、断定せず;
  小麦 / 大豆 / 魚 = **OPEN GAP** —— 断定しない（04 の #2, #8 参照）
- restrictions: グルテンフリー = 不可 [INFERRED·med → GAP]; ベジタリアン/ヴィーガン = OPEN GAP（魚だし）
- taste_profile: クリーン、そばの香ばしさ、savory-うま味のつけ汁（「香ばしく、さわやか、うま味のつけ汁」）[INFERRED]
- calorie_range: 5段階中 2 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: [INFERRED —— 食文化KB 一致なし] 一般的: 竹ざるに盛った冷たいそばを
  つけ汁で。権威的提示はしない。
- 提供メモ: 麺をつゆにつけて食べる。薬味はお好みで [INFERRED]

---

## 料理2 — 天ぷらそば（Tempura soba）
- verification_rank: **C**（アレルゲン密度最高。えび/卵/ごま/小麦/魚/大豆 すべて OPEN）
- data_source: live

### 機械的意味
- ingredient_ids: buckwheat-flour [INFERRED·high → GAP], wheat-flour(麺のつなぎ?) [INFERRED·med → GAP],
  kake-tsuyu{soy-sauce [INFERRED·high → GAP], dashi(kombu, katsuobushi) [INFERRED·med → GAP]},
  tempura{衣: wheat-flour [INFERRED·high → GAP], egg? [INFERRED·med → GAP]; 具材: shrimp-or-vegetable [UNKNOWN → GAP]; frying-oil [UNKNOWN → GAP]}
- method_ids: boil, deep-fry, simmer/heat [INFERRED·high]
- allergens: そば = おそらくあり [INFERRED·high] flag; 小麦 / 卵 / **えび（甲殻類）** / ごま / 大豆 / 魚 = **OPEN GAP** —— 断定しない（04 の #2〜#5, #8）
- restrictions: グルテンフリー = 不可 [INFERRED·high → GAP 確認]; ベジタリアン/ヴィーガン/ペスカタリアン = OPEN GAP; ハラル = OPEN GAP
- taste_profile: 温かい savory なつゆ、カリッとした天ぷら（「温かいうま味のつゆに揚げのカリッと」）[INFERRED]
- calorie_range: 5段階中 3 [INFERRED·low]

### 人間向けナラティブ
- 物語: [INFERRED —— KB 一致なし] 一般的: だしつゆの温かいそばに天ぷらをのせたもの。権威的でない。
- 提供メモ: 天ぷらがカリッとしているうちに早めに食べる [INFERRED]

---

## 料理3 — カレーうどん（Curry udon）
- verification_rank: **C**（肉の種類不明 → 宗教制限が OPEN。乳/小麦/大豆/魚が OPEN）
- data_source: live

### 機械的意味
- ingredient_ids: udon{wheat-flour [INFERRED·high → GAP 確認]},
  curry-broth{roux: wheat-flour [INFERRED·high → GAP], fat [INFERRED·med], spices [INFERRED·med],
  dairy? [INFERRED·low → GAP], dashi(kombu, katsuobushi) [INFERRED·med → GAP], soy/soy-sauce [INFERRED·med → GAP],
  meat: none-or-chicken-or-pork-or-beef [UNKNOWN → GAP]}, negi, aburaage? [INFERRED·low]
- method_ids: boil, simmer [INFERRED·high]
- allergens: 小麦 = おそらくあり（うどん）[INFERRED·high] flag; 乳 / 大豆 / 魚 / 鶏 / 豚 / 牛 = **OPEN GAP** —— 断定しない（04 の #6, #7, #8）
- restrictions: **no-pork = OPEN GAP, no-beef = OPEN GAP, ハラル = OPEN GAP**（肉の種類不明）;
  グルテンフリー = 不可 [INFERRED·high → GAP 確認]; ベジタリアン/ヴィーガン/乳不使用 = OPEN GAP
- taste_profile: 温かく、スパイスが効いた、とろみのあるうま味カレー（「こく深く、ほどよくスパイシーなだしカレーつゆ」）[INFERRED]
- calorie_range: 5段階中 3 [INFERRED·low]

### 人間向けナラティブ
- 物語: [INFERRED] 一般的: 小麦うどんに和風カレーをだしカレーつゆで。権威的でない。
- 提供メモ: とろみのあるつゆで跳ねやすい [INFERRED]

---

## 料理4 — そばがき（Sobagaki）
- verification_rank: **C**（そばはほぼ確実。小麦/添えが OPEN）
- data_source: live

### 機械的意味
- ingredient_ids: buckwheat-flour [INFERRED·high → GAP 確認], hot-water [INFERRED·high],
  wheat-tsunagi?（通常なし）[INFERRED·med → GAP], 添え: tsuyu/soy/wasabi [INFERRED·med → GAP]
- method_ids: 湯で練る; （時に茹でる）[INFERRED·med]
- allergens: そば = おそらくあり [INFERRED·high] flag; 小麦 / 大豆 / 魚 = **OPEN GAP**（つなぎ＋添え次第、04 の #9）—— 断定しない
- restrictions: グルテンフリー = 小麦なし＋醤油つけなしなら**可の可能性** [UNKNOWN → GAP]; ベジタリアン/ヴィーガン = OPEN GAP（添え）
- taste_profile: やわらかく、もち様、純粋なそば（「やわらかく、香ばしく、ほどよい弾力」）[INFERRED]
- calorie_range: 5段階中 2 [INFERRED·low]

### 人間向けナラティブ
- 物語: [INFERRED —— KB 一致なし] 一般的: そば粉を湯で練ったもの。そばの古い食べ方。権威的でない。
- 提供メモ: つけ汁またはわさびで食べる [INFERRED]

---

## 検証ゲート（データセット完成を宣言する前に実行）
- [x] アレルゲン/制限の項目が [INFERRED]/[UNKNOWN] に事実として依存していない —— 該当はすべて OPEN GAP として扱い、断定なし
- [x] 導いた各アレルゲンが特定の材料まで辿れる（段階03 の連鎖参照）
- [x] 正規の上書きを適用 —— どの料理にも**正規一致は存在せず**。正規としての捏造なし（候補のみ待機）
- [x] 複合材料を展開（つゆ、天ぷら、カレールウ、そば麺）し、隠れたアレルゲンを可視化
- [x] 機械的意味と人間向けナラティブを分離
- [x] ゼラチンを誤分類していない（該当なし）。ハラル/no-pork/no-beef はアレルゲンでなく制限に
- [x] 「品による」回答を波及させていない（波及させるオーナー回答が存在しない）
- [x] 料理ごとに verification_rank を付与。残る gap を明示
- [ ] **S/A でゲート未通過** —— 全料理に OPEN の安全 gap あり。これは正直な C 評価の
      オーナー確認前ドラフト

## 実行サマリー
- 料理数: 4 | S/A に到達: 0 | B/C: 4（すべて C）
- **まだ妨げている安全 gap: 9**（確認事項リスト セクション A、#1〜#9）
- 状態: **draft** —— オーナー承認待ち（段階07）。解消まで、コンシェルジュは
  すべてのアレルゲン/制限の質問に「スタッフにご確認ください」と答える必要がある。
