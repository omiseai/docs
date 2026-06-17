# 02 · 分解 — そば店（`soba-shop-onboarding`）

各料理について: 構成要素 → 材料（複合材料は展開）、調理法、全項目に出典タグ。実際に
一致がある場合のみ正規資産を適用。

**このメニューの正規照合の結果:** 4品いずれもシードの `product_master.json`（飲料のみ）、
`ingredient_glossary.json`（タイ/カニ面/バイ貝/へしこ/片栗粉/能登牛/若狭牛 はここに現れない）、
`food_culture_kb.json`（へしこ, 柿の葉寿司 のみ —— そば料理なし）に一致しない。よって
どの料理にも**正直に付けられる `[CANONICAL]` タグはない**。メニュー以外の事実はすべて
`[INFERRED]` か `[UNKNOWN]` であり、安全に関わるものは gap になる。（末尾に候補 KB 下書きを
提案 —— 明示的に正規ではない。）

---

## 料理1 — ざるそば（Zaru soba — つけ汁つき冷たいそば [INFERRED·high]）
- 英語名: Zaru soba (chilled buckwheat noodles) [INFERRED·high] —— 日本固有、用語集の
  Policy B に従いローマ字＋注釈。用語集項目がないので CANONICAL でなく INFERRED とタグ付け
- 構成要素・材料:
  - **そば麺** [MENU·high] → 複合、展開:
    - そば粉（buckwheat flour）[INFERRED·high]  ← 定義的な材料
    - **小麦粉（つなぎ）** [INFERRED·med] ← そばの多くは 二八（そば/小麦 80/20）。一部の店は
      十割（100% そば粉、小麦なし）。**この店の配合比は UNKNOWN** → GAP（小麦アレルゲン）
  - **つゆ / そばつゆ（つけ汁）** [INFERRED·high] → 複合、展開:
    - 醤油（→ 大豆 + 小麦）[INFERRED·high] → GAP 確認
    - だし（複合 → kombu + katsuobushi/かつお → 魚）[INFERRED·med] → GAP
    - みりん / 砂糖 [INFERRED·low]
  - 薬味: のり（海藻）[INFERRED·med]、ねぎ [INFERRED·med]、わさび [INFERRED·low] ——
    一般的だが未確認
- 調理法: 茹でる（麺）後に冷やす/すすぐ [INFERRED·high]
- 適用した正規一致: なし
- メモ: そばは本質的に含まれる。生きた安全上の不明点は、麺に小麦が含まれるか
  （二八 vs 十割）と、つゆの醤油に小麦が含まれるか。

---

## 料理2 — 天ぷらそば（Tempura soba — 温かいそばに天ぷらをのせたもの [INFERRED·high]）
- 英語名: Tempura soba [INFERRED·high]
- 構成要素・材料:
  - **そば麺** [MENU·high] → そば粉 [INFERRED·high] + 小麦粉（つなぎ?）[INFERRED·med] → GAP（同じ 二八/十割 の疑問）
  - **温かいかけつゆ** [INFERRED·high] → 複合:
    - 醤油（→ 大豆 + 小麦）[INFERRED·high] → GAP
    - だし（kombu + katsuobushi → 魚）[INFERRED·med] → GAP
    - みりん/砂糖 [INFERRED·low]
  - **天ぷら** [MENU·high] → 複合、展開:
    - 衣: 小麦粉（→ 小麦）[INFERRED·high] → GAP 確認
    - 衣: **卵**（→ 卵）[INFERRED·med] ← 天ぷらの衣に卵を使うことが多いが、使わない店もある → GAP
    - 揚げる具材そのもの [UNKNOWN] ← 天ぷらそばは えび（海老天, → 甲殻類/えび）が
      標準だが、野菜（かき揚げ、かぼちゃ…）の可能性も → GAP（えび/甲殻類アレルゲン）
    - **揚げ油** [UNKNOWN] ← 純植物油 vs ごま油入りブレンド → GAP（ごまアレルゲン）
- 調理法: 茹でる（麺）、揚げる（天ぷら）、煮る/温める（つゆ）[INFERRED·high]
- 適用した正規一致: なし
- メモ: アレルゲン密度が最も高い料理。えび、卵、小麦、ごま すべてあり得て、すべて未確認。

---

## 料理3 — カレーうどん（Curry udon — カレーつゆの小麦うどん [INFERRED·high]）
- 英語名: Curry udon [INFERRED·high]
- 構成要素・材料:
  - **うどん麺** [MENU·high] → 小麦粉（→ 小麦）[INFERRED·high] → GAP 確認
    （うどんは定義上小麦。高信頼だがオーナー確認は必要）
  - **カレールウ / カレーつゆ** [INFERRED·high] → 複合、展開（ここにアレルゲンが隠れる）:
    - 小麦粉（ルウのベース → 小麦）[INFERRED·high] → GAP
    - 油脂 [INFERRED·med]
    - カレースパイス [INFERRED·med]
    - だしベース（kombu + katsuobushi → 魚）[INFERRED·med] → GAP（カレーうどんのつゆは
      西洋カレーと違い通常だしベース）
    - 醤油 / 調味の大豆（→ 大豆 + 小麦）[INFERRED·med] → GAP
    - **乳**（一部のルウは脱脂粉乳を含む → 乳）[INFERRED·low] → GAP
    - **肉の可能性: 豚 or 牛 or 鶏** [UNKNOWN] ← no-pork/no-beef/ハラル の制限と
      （鶏/豚/牛）アレルゲンに影響 → GAP
  - トッピング: ねぎ、油揚げの可能性（→ 大豆）[INFERRED·low]
- 調理法: 茹でる（麺）、煮る（カレーつゆ）[INFERRED·high]
- 適用した正規一致: なし
- メモ: 市販のカレールウは典型的な「隠れアレルゲンの複合材料」（小麦 + 乳 + 時に
  牛/豚エキス）。肉の種類が宗教上の制限を左右する。

---

## 料理4 — そばがき（Sobagaki — そばの団子/粥 [INFERRED·high]）
- 英語名: Sobagaki (buckwheat dumpling) [INFERRED·high] —— 日本固有、ローマ字＋注釈
- 構成要素・材料:
  - **そば粉（buckwheat flour）** [INFERRED·high] → そばアレルゲン —— 料理全体
  - 湯 [INFERRED·high]
  - 通常は**小麦なし**（そばがきは普通そば粉＋湯のみ）[INFERRED·med]
    → ただし小麦つなぎがないことを確認 → GAP（小麦不使用の可能性。小麦アレルギーだが
    そばは大丈夫という稀なお客様に重要 —— 麺より安全な選択肢かどうかも確認できる）
  - 添え: つけつゆ（→ 大豆/小麦/魚、料理1 と同じ）または わさび醤油 [INFERRED·med] → GAP
- 調理法: 湯で練る。時に茹でる [INFERRED·med]
- 適用した正規一致: なし
- メモ: 最もシンプルな料理。そばが主体。主な不明点は添えのソース。

---

## 候補正規提案（下書き —— 本実行では [CANONICAL] として読み戻さない）
`assets/canonical/candidates/food_culture_kb.candidates.jsonl` に追記:
- そばがき（Sobagaki）—— そばの団子、人間検証用の候補 KB ナラティブ
- ざるそば（Zaru soba）—— 人間検証用の候補 KB ナラティブ
これらは昇格前に MAFF ソースで人間が検証するための待ち行列。
