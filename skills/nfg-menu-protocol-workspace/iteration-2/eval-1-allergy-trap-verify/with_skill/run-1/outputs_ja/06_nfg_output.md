# 06 · NFG 出力 —（店名未提供 — ランチメニュー）
status: **draft（オーナー承認待ち）**

NFG の形のデータセット。料理ごとに1ブロック: 機械的意味＋人間向けナラティブ＋
verification_rank。**本実行ではオーナー接触なし**のため、安全に関わる項目はすべて
`[INFERRED]`/`[UNKNOWN]` に依存し、**事実として断定せず flag した gap** として扱う。
段階07 の承認まで、どの料理も **C** を超えられない。正規一致もなかったため
`[CANONICAL]` への格上げもなし。

---

## 料理1 — ロースかつ定食（Pork loin cutlet set meal）
- verification_rank: **C**（揚げ物＋定食。全アレルゲン連鎖が未解決）
- data_source: live

### 機械的意味
- ingredient_ids: pork-loin [INFERRED·high → GAP], breading(wheat-flour, egg, panko→wheat) [INFERRED·med → GAP],
  frying-oil(base unknown) [UNKNOWN → GAP], rice [INFERRED·med], miso-soup(miso→soy, dashi→katsuobushi/fish, tofu→soy?) [INFERRED·med → GAP],
  shredded-cabbage [INFERRED·med], tonkatsu-sauce(soy-sauce→soy+wheat) [INFERRED·med → GAP]
- method_ids: deep-fry [INFERRED·high]; boil/simmer [INFERRED·med]
- allergens: **一切断定しない** —— 小麦、卵、大豆、魚、ごま、ピーナッツ はすべて
  flag した GAP（段階03 参照）であり事実ではない。アレルゲンの安全主張を提示しないこと。
- restrictions: no-pork = 不可 [INFERRED·high → GAP], ハラル = 不可 [INFERRED·high → GAP],
  ベジタリアン = 不可 [INFERRED·high → GAP], グルテンフリー = 不可 [INFERRED·med → GAP] —— すべて確認待ち
- taste_profile: savory / うま味 / 揚げのカリッと（言語化）[INFERRED·low]
- calorie_range: 5段階中 4（高め、揚げ＋ご飯）[INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 食文化KB になし → **空白のまま**（[INFERRED] になるため。捏造の
  由来説明は書かない）。
- 提供メモ: 通常は千切りキャベツ・ご飯・味噌汁とともに提供 [INFERRED·med] —— 未確認。

---

## 料理2 — エビフライ（Breaded fried shrimp）
- verification_rank: **C**
- data_source: live

### 機械的意味
- ingredient_ids: shrimp [INFERRED·high → GAP], breading(wheat-flour, egg, panko→wheat) [INFERRED·med → GAP],
  frying-oil(base unknown) [UNKNOWN → GAP], sauce(tartar→egg? / tonkatsu→soy+wheat?) [UNKNOWN → GAP]
- method_ids: deep-fry [INFERRED·high]
- allergens: **一切断定しない。** 甲殻類（えび）は名称からほぼ確実だが、なお
  オーナー確認のため flag。小麦、卵、ごま、ピーナッツ はすべて GAP。
- restrictions: ベジタリアン = 不可 [INFERRED·high], ペスカタリアン = 可 [INFERRED·med], グルテンフリー = 不可 [INFERRED·med → GAP]
- taste_profile: savory / うま味 / 揚げのカリッと [INFERRED·low]
- calorie_range: 5段階中 3 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 食文化KB になし → 空白のまま。
- 提供メモ: タルタルまたはとんかつソースで提供されることが多い [UNKNOWN] —— 未確認。

---

## 料理3 — 杏仁豆腐（Annin-dofu / almond jelly）
- verification_rank: **C**
- data_source: live
- **名称の罠メモ（レコードに引き継ぐ）: 「豆腐」は食感の語であり大豆ではない。
  大豆は断定しない。デザート誤タグへの注意: このデザートに肉アレルゲンを付けない。**

### 機械的意味
- ingredient_ids: milk/cream [INFERRED·med → GAP], sugar [INFERRED·med],
  setting-agent(agar OR gelatin) [UNKNOWN → GAP], almond-flavor(apricot-kernel OR essence) [UNKNOWN → GAP]
- method_ids: （冷やし固め / なし）[INFERRED·med]
- allergens: **一切断定しない。** 乳（dairy）とアーモンド（木の実）は flag した GAP。
  大豆 = 明示的に不在（名称の罠を却下）。
- restrictions: ベジタリアン / ヴィーガン / ハラル / コーシャ / 乳不使用 はすべて
  **凝固剤＋乳次第** = GAP。
- taste_profile: 甘い / なめらか / 冷たい [INFERRED·low]
- calorie_range: 5段階中 2 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 食文化KB になし → 空白のまま（捏造の由来なし）。
- 提供メモ: 冷たいデザート [INFERRED·med]。

---

## 料理4 — コーヒーゼリー（Coffee jelly）
- verification_rank: **C**
- data_source: live
- **デザート誤タグへの注意: 肉アレルゲンなし。ゼラチン（使用時）は独立トークンであり
  肉アレルゲンではない。**

### 機械的意味
- ingredient_ids: brewed-coffee [INFERRED·high], sugar [INFERRED·med],
  setting-agent(gelatin OR agar) [UNKNOWN → GAP], topping(cream/milk?) [UNKNOWN → GAP]
- method_ids: （冷やし固め / なし）[INFERRED·med]
- allergens: **一切断定しない。** 乳（dairy）は flag した GAP（トッピング次第）。
- restrictions: ベジタリアン / ヴィーガン / ハラル / コーシャ / 乳不使用 はすべて
  凝固剤＋トッピング次第 = GAP。
- taste_profile: ほろ苦い甘さ / なめらか / 冷たい [INFERRED·low]
- calorie_range: 5段階中 2 [INFERRED·low]

### 人間向けナラティブ
- 物語 / 文化的背景: 食文化KB になし → 空白のまま。
- 提供メモ: 冷たいデザート。クリーム/シロップを添えることが多い [UNKNOWN]。

---

## 検証ゲート（データセット完成を宣言する前に実行）
- [x] アレルゲン/制限の項目が [INFERRED]/[UNKNOWN] に事実として依存していない —— 確認済:
      **アレルゲンの断定はゼロ**。すべて確認事項リストに存在。
- [x] （潜在的な）導出アレルゲンが特定の材料まで辿れる（段階03 に連鎖を明示）。
- [x] 一致時に正規の上書きを適用 —— **一致は存在せず**。[CANONICAL] に誤タグなし。
      正規データの捏造なし。
- [x] 複合材料を展開（衣、味噌汁、だし、とんかつソース、凝固剤）。
- [x] 機械的意味と人間向けナラティブを分離。
- [x] ゼラチンを肉アレルゲンに分類していない。ハラル/pork-free はアレルゲンでなく制限に。
- [x] 「品による」回答を波及させていない（回答なし —— オーナー不在）。
- [x] 料理ごとに verification_rank を付与。残る gap を明示。
- [ ] **オーナー承認（段階07）—— 未取得。データセットは DRAFT のまま。**

## 実行サマリー
- 料理数: 4 | S/A に到達: **0** | B/C: **4**（すべて C）
- まだ妨げている安全 gap: **12**（確認事項リスト Q1〜Q12）
- 状態: **draft**（未確定。本実行ではオーナー不在）

> この状態でのコンシェルジュの挙動: この4品すべてについて、アレルギー質問には
> 「申し訳ございません、スタッフにご確認ください / please check with staff」と答え、
> どの料理についても「いずれのアレルゲンも不使用」と述べては**いけない**。
