# 06 · NFG 出力 — 鳥平（Torihei）
status: draft（オーナー承認待ち）

データセット。料理ごとに1ブロック: 機械的意味（Machine Semantics）＋人間向けナラティブ
＋ verification_rank。オーナー入力は未受領のため、安全に関わる推測/不明の項目はすべて
**事実として断定せず**、gap として残す。完全検証済みは日本酒（正規）のみ。

---

## 料理1 — 牛すじ煮込み（Beef tendon stew）
- verification_rank: **B**（OPEN の安全 gap: 大豆/小麦の味付け、だし/魚）
- data_source: live

### 機械的意味
- ingredient_ids: beef-tendon [MENU·high]; konnyaku [INFERRED·med → GAP];
  daikon [INFERRED·low → GAP]; dashi(kombu, katsuobushi) [INFERRED·med → GAP];
  seasoning-base [UNKNOWN → GAP]
- method_ids: simmer/boil [MENU·high]
- allergens: **断定しない** — 大豆 [UNKNOWN→GAP]、小麦 [UNKNOWN→GAP]、
  魚/かつお [INFERRED·med→GAP]。（コンシェルジュはこれらをスタッフに委ねる。）
- restrictions: ベジタリアン = 不可、ヴィーガン = 不可、no-beef = 不可、ヒンドゥー = 不可
  [すべて MENU·high]; ハラル = 不可 [INFERRED·low→GAP、ただし牛肉を含むため不可]
- taste_profile: うま味が前面、savory、こく; 穏やかな塩味（値＋言語化）[INFERRED·med]
- calorie_range: 5段階中 3 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 食文化KB になし → 検証済みナラティブなし。一般的な説明（「牛すじを
  じっくり煮込んだ居酒屋の定番」）は [INFERRED] であり、オーナー確認まで権威的提示を控える。
  [INFERRED·low]
- 提供メモ: 通常は温かい状態でねぎを添えて提供 [INFERRED·low]

---

## 料理2 — 鶏の唐揚げ（Chicken karaage）
- verification_rank: **B**（OPEN の安全 gap: 小麦の衣、ごま油、大豆の漬けダレ）
- data_source: live

### 機械的意味
- ingredient_ids: chicken [MENU·high]; coating-starch [UNKNOWN→GAP];
  marinade-soy-sauce [INFERRED·med→GAP]; ginger/garlic [INFERRED·low]; frying-oil [UNKNOWN→GAP]
- method_ids: deep-fry [MENU·high]
- allergens: **断定しない** — 小麦 [UNKNOWN→GAP]、大豆 [INFERRED·med→GAP]、
  ごま [UNKNOWN→GAP]
- restrictions: ベジタリアン = 不可、ヴィーガン = 不可 [MENU·high]; no-beef = 可、
  no-pork = 共用フライヤー確認待ちで可 [INFERRED·med→GAP]; ハラル = 不可
  [INFERRED·low→GAP]; グルテンフリー = 不明（衣次第）[GAP]
- taste_profile: savory、ジューシー、表面はカリッと [INFERRED·med]
- calorie_range: 5段階中 4 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 唐揚げは居酒屋でごく一般的。KB に検証済みの地域ナラティブなし。
  [INFERRED·low] —— 権威的主張は控える。
- 提供メモ: 通常はレモンを添えて提供 [INFERRED·low]

---

## 料理3 — だし巻き卵（Dashimaki tamago）
- verification_rank: **B**（卵は確実だが、だし/魚＋大豆調味が OPEN）
- data_source: live

### 機械的意味
- ingredient_ids: egg [MENU·high]; dashi(kombu, katsuobushi) [だしは MENU·med /
  組成は INFERRED·med → GAP]; 調味 soy/mirin/sugar [INFERRED·low→GAP]
- method_ids: pan-fry（巻き）[INFERRED·high]
- allergens: **卵 = あり [MENU·high]**（断定 —— メニューに記載）。断定しない:
  魚/かつお [INFERRED·med→GAP]、大豆 [INFERRED·low→GAP]、小麦 [INFERRED·low→GAP]
- restrictions: ヴィーガン = 不可（卵）[MENU·high]; ベジタリアン = だしの種類次第
  [INFERRED·med→GAP]; ペスカタリアン = 可 [MENU·high]
- taste_profile: うま味、ほのかな甘み、やわらかい食感 [INFERRED·med]
- calorie_range: 5段階中 2 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 日本の定番の巻き卵。KB の地域料理ではない → 検証済みの由来
  ナラティブなし。[INFERRED·low]
- 提供メモ: しばしば大根おろしを添えて提供 [INFERRED·low]

---

## 料理4 — ポテトサラダ（Potato salad）
- verification_rank: **B**（マヨ経由の卵は可能性高いが未確認。豚は不明）
- data_source: live

### 機械的意味
- ingredient_ids: potato [MENU·high]; mayonnaise(卵黄, 油, 酢)
  [INFERRED·high→GAP]; きゅうり/にんじん/玉ねぎ [INFERRED·med]; ham/bacon [INFERRED·low→GAP]
- method_ids: 茹で（じゃがいも）＋和え [INFERRED·med]
- allergens: **断定しない** — 卵 [INFERRED·high→GAP]（可能性高いが未確認のため、
  断定せず flag）
- restrictions: ヴィーガン = 不可（マヨの卵）[INFERRED·high→GAP]; ベジタリアン =
  ハム/ベーコン次第 [INFERRED·low→GAP]; no-pork / ハラル = 不明（ハム/ベーコン？）[GAP]
- taste_profile: クリーミー、savory、マイルド [INFERRED·med]
- calorie_range: 5段階中 3 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 居酒屋/洋食の定番。検証済み KB ナラティブなし。[INFERRED·low]
- 提供メモ: 冷やして提供 [INFERRED·low]

---

## 料理5 — 本日の刺身盛り合わせ（Today's assorted sashimi）
- verification_rank: **C**（内容が本質的に日替わり。魚種不明。貝/魚卵の OPEN gap が複数）
- data_source: live

### 機械的意味
- ingredient_ids: assorted-raw-fish [UNKNOWN→GAP、日替わり]; 大根/しそ/わさび
  の付け合わせ [INFERRED·med]; soy-sauce の添え [INFERRED·med→GAP]
- method_ids: raw [INFERRED·high]
- allergens: **断定しない** — 魚 [INFERRED·high→GAP、どの魚種]; かに、えび、いか、
  あわび、いくら はすべて [UNKNOWN→GAP]; 大豆/小麦（醤油）[INFERRED·med→GAP]
- restrictions: ヴィーガン/ベジタリアン = 不可 [INFERRED·high]; ペスカタリアン = 可
  [INFERRED·high]; no-beef/no-pork = 可 [INFERRED·high]; ハラル = 不可
  [INFERRED·low→GAP]
- taste_profile: 新鮮、クリーン、魚により変化 [INFERRED·low]
- calorie_range: 5段階中 2 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 日替わりの刺身盛り合わせ。内容は仕入れにより変化。検証済み KB
  ナラティブなし。[INFERRED·low]
- 提供メモ: わさびと醤油を添えて冷やして提供; **コンシェルジュは本日の魚種と貝類の
  有無をスタッフに確認するよう案内しなければならない。** [INFERRED·high]

---

## 料理6 — 黒龍 純米吟醸（Kokuryu Junmai Ginjo）— グラス売り
- verification_rank: **S**（完全に正規。安全 gap なし）
- data_source: live

### 機械的意味
- ingredient_ids: rice, rice-koji, water [CANONICAL·high]
- method_ids: 該当なし（醸造）; グラスで注いで提供 [MENU·high]
- 製品同一性: Kokuryu Junmai Ginjo, maker 黒龍酒造（Kokuryu Sake Brewing Co.）,
  Fukui, junmai_ginjo, ABV 15.5% [CANONICAL·high]（product_master: pm_kokuryu_junmai_ginjo）
- allergens: なし [CANONICAL·high]
- restrictions: no-alcohol = FAIL [CANONICAL·high]; ハラル = 不可（アルコール）
  [CANONICAL·high]; ヴィーガン/ベジタリアン = 可; グルテンフリー = 可 [CANONICAL·high]
- taste_profile: 純米吟醸 —— クリーン、芳香、バランス（言語化）[テイスティングノートは INFERRED·low; スペックは CANONICAL]
- calorie_range: 5段階中 2 [INFERRED·low]（グラス1杯の標準的な日本酒）

### 人間向けナラティブ
- 物語 / 文化的背景: 黒龍は名高い福井の蔵元。検証済みスペックを超える具体的な
  ナラティブは [INFERRED] であり、検証済みソースからでない限り控える。検証済みの事実
  （Fukui、純米吟醸、15.5%）[CANONICAL·high]。
- 提供メモ: グラスで提供 [MENU·high]; 純米吟醸は通常、冷やまたは常温で楽しむ [INFERRED·low]

---

## 検証ゲート（データセット完成を宣言する前に実行）
- [x] アレルゲン/制限の項目が [INFERRED]/[UNKNOWN] に**断定的事実として**依存していない ——
      該当はすべて → GAP として flag、断定なし。（断定したアレルゲンは料理3 の卵のみで
      [MENU·high]。断定した制限は MENU/CANONICAL 由来のみ。）
- [x] 導いた各アレルゲンが特定の材料まで辿れる（連鎖は段階03 に明示）
- [x] 正規の上書きを適用 —— 日本酒が product_master に一致し、推測を上書き
- [x] 複合材料を展開（だし → kombu+katsuobushi; マヨネーズ → 卵黄+油+酢;
      刺身盛り合わせは隠れた貝類について flag）
- [x] 機械的意味と人間向けナラティブを分離
- [x] ゼラチンを肉アレルゲンに分類していない（本件では該当なし）; ハラル/no-pork は
      アレルゲンでなく制限に（料理4 のハム/ベーコン → 豚の制限であってアレルゲンでない）
- [x] 「品による」回答を波及させていない —— オーナー回答がまだ存在せず、波及なし
- [x] 料理ごとに verification_rank を付与; 残る gap を明示

## 実行サマリー
- 料理数: 6 | S/A に到達: 1（料理6, S）| B/C: 5（B が4、C が1）
- まだ妨げている安全 gap: **10**（確認事項リストの A1〜A10）
- 状態: **draft**（段階07 によるオーナー承認待ち）
