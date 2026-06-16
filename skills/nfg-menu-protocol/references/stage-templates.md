# Stage templates — reference

Copy these shapes into each numbered file. They are scaffolds, not straitjackets —
keep the headers and the provenance discipline; adapt the rest to the menu.

Provenance tag on every claim: `[MENU] [OPERATOR] [CANONICAL] [INFERRED] [UNKNOWN]`,
with confidence `·high|med|low`. Example: `wheat [INFERRED·low]`.

---

## 01_source_capture.md

```markdown
# 01 · Source capture — <Restaurant name>

- Run date: <YYYY-MM-DD>
- data_source: live
- Sources received:
  - <e.g. menu-front.jpg — photo, sharp>
  - <e.g. drinks.pdf — text-selectable>

## Items (verbatim, original language)

### <Section name as printed>
| # | Printed name | Printed description | Price | Notes on legibility |
|---|---|---|---|---|
| 1 | 牛すじ煮込み | — | ¥680 | clear |
| 2 | 本日の[illegible] | — | ¥1200 | photo blur, right edge |

(Repeat per section. Transcribe only. No interpretation, no translation here.)
```

---

## 02_decomposition.md

```markdown
# 02 · Decomposition — <Restaurant name>

For each dish: components → ingredients (expand composites), cooking methods,
every field provenance-tagged.

## Dish 1 — 牛すじ煮込み (Beef tendon stew [CANONICAL·high])
- English name: Beef tendon stew  [CANONICAL·high] (ingredient_glossary)
- Components & ingredients:
  - beef tendon  [MENU·high]
  - konnyaku  [INFERRED·med]
  - dashi (composite → kombu, bonito/katsuobushi)  [INFERRED·med]
  - miso OR soy-based seasoning  [UNKNOWN]   ← which base? → gap
- Cooking methods: boil/simmer  [INFERRED·high]
- Canonical matches applied: none for beverage; glossary used for name
- Notes: composite `dashi` expanded; base seasoning undetermined
```

---

## 03_allergens_restrictions.md

```markdown
# 03 · Allergens & restrictions — <Restaurant name>

Derived from Stage 02 ingredients. Each allergen traces to an ingredient and
inherits the weakest provenance in its chain.

## Dish 1 — 牛すじ煮込み
### Allergens (derive across JP/US/EU/CA/AU)
| Allergen | From ingredient | Provenance | JP | US | EU | CA | AU |
|---|---|---|---|---|---|---|---|
| fish (bonito) | dashi → katsuobushi | [INFERRED·med] → GAP | rec | none | none | none | none |
| soy | seasoning base | [UNKNOWN] → GAP | — | — | — | — | — |

### Restrictions
| Restriction | Status | From | Provenance |
|---|---|---|---|
| vegetarian | no (contains beef) | beef tendon | [MENU·high] |
| no-beef | no | beef tendon | [MENU·high] |

### Gaps generated here
- Seasoning base (miso vs soy) → affects soy allergen
- Dashi composition → affects fish allergen
```

---

## 04_gap_register.md

```markdown
# 04 · Gap register — <Restaurant name>

Questions for the operator, ranked safety-first. Status: OPEN / ANSWERED.

## A. Safety-critical (allergen / restriction)
1. **[OPEN]** Dish 1 牛すじ煮込み — seasoning base: a) miso (soy), b) soy sauce
   (soy + wheat), c) other? *Determines soy/wheat allergen status.*
2. **[OPEN]** Dish 3 tempura — frying oil: a) pure vegetable, b) blend with sesame,
   c) other? *Determines sesame allergen.*

## B. Ingredient identity
3. **[OPEN]** Dish 1 — is konnyaku actually present, or is that an assumption?

## C. Narrative / cultural
4. **[OPEN]** Dish 5 — regional origin claim not in food-culture KB; confirm or drop.
```

---

## 05_operator_dialogue.md

```markdown
# 05 · Operator dialogue — <Restaurant name>

Records both live (in-conversation) and async answers. Each answer becomes
[OPERATOR] provenance for the relevant field.

## Exchange 1 — <date>, via <live chat / email>, answered by <name/role>
- Q1 (seasoning base): "白味噌ベースです" → miso base, contains soy, no wheat.
  → Dish 1 soy = yes [OPERATOR·high]; wheat = no [OPERATOR·high]
- Q2 (tempura oil): "店によって違う" = varies by store.
  → Does NOT resolve per-dish oil. Gap stays OPEN. Do not cascade.

## Open after this exchange
- Q3, Q4 still OPEN.
```

---

## 06_nfg_output.md

```markdown
# 06 · NFG output — <Restaurant name>
status: draft (pending operator sign-off)   ← becomes "finalized (operator-signed YYYY-MM-DD)" after Stage 07

The dataset. One block per dish: Machine Semantics + Human Narrative +
verification_rank.

## Dish 1 — Beef tendon stew (牛すじ煮込み)
- verification_rank: **A**  (soy/wheat now operator-confirmed; konnyaku still inferred)
- data_source: live

### Machine Semantics
- ingredient_ids: beef-tendon [MENU], konnyaku [INFERRED·med → GAP], dashi(kombu,
  katsuobushi) [INFERRED·med], white-miso [OPERATOR·high]
- method_ids: simmer [INFERRED·high]
- allergens: soy = yes [OPERATOR·high] (from miso); fish = likely [INFERRED] —
  flagged, not asserted; (JP rec / others none)
- restrictions: vegetarian = no, no-beef = no, halal = no [all MENU·high]
- taste_profile: umami-forward, savory  (values + verbalization)
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: <from food-culture KB if matched [CANONICAL], else
  [INFERRED] and flagged>
- serving notes: <…>

---

## Verification gate (run before declaring the dataset done)
- [ ] No allergen/restriction field rests on [INFERRED] or [UNKNOWN] as fact
      (any that do are in the gap register, not asserted here)
- [ ] Every derived allergen traces to a specific ingredient
- [ ] Canonical overrides (product_master / glossary / food-culture KB) applied
- [ ] Composites expanded so hidden allergens are visible
- [ ] Machine Semantics and Human Narrative kept separate
- [ ] gelatin not filed as meat allergen; halal/pork-free under restrictions not allergens
- [ ] No "varies by item" answer cascaded to specific dishes
- [ ] verification_rank assigned per dish; remaining gaps named explicitly

## Run summary
- Dishes: <n> | reached S/A: <n> | at B/C: <n>
- Open safety gaps still blocking: **<n>**   ← the number that matters most
- Status: draft / finalized (operator-signed <date>)
```

---

## 07_operator_review.md

Write this in the operator's language. For the Japanese restaurants we serve, write
it in Japanese — an owner can only confirm what they can read. The English here is
just to show the structure.

```markdown
# 07 · オーナー確認シート — <店名>
# (Operator review & sign-off)

このシートは、メニュー内容について我々がまとめた理解です。特に「推測（要確認）」
の項目を確認・修正していただくことで、AIコンシェルジュがアレルギー等に正確に
回答できるようになります。

## 料理ごとの内容（やさしい言葉で）
### 1. 牛すじ煮込み
- 主な材料: 牛すじ、こんにゃく、だし …
- 含まれるアレルゲン（現時点の理解）: …
- 食べられない方: 牛肉NG / ハラルNG …

## ⚠️ 我々の推測 — ご確認ください  (every [INFERRED] item, foregrounded)
| # | 料理 | 我々の推測 | ✔ そのとおり / ✖ 違う → 正しくは… |
|---|---|---|---|
| 1 | 牛すじ煮込み | 味付けのベースは醤油（→ 大豆・小麦を含む）と推測 | ☐ ✔   ☐ ✖ → ______ |
| 2 | だし | かつおだし（→ 魚アレルゲン）と推測 | ☐ ✔   ☐ ✖ → ______ |

## ✅ すでに確定している項目（再確認は不要です）
- だし巻き卵 … 卵 [メニュー記載]
- 黒龍 純米吟醸 … アルコール [公式データ照合済み]

## ❓ まだ分からないこと（お答えいただけると助かります）
- (open gap-register items that still block safe allergen answers)

## いまの状態
- 現在の信頼度: B（主要な安全項目が未確認のため）。
  この状態だとコンシェルジュは「スタッフにご確認ください」と案内します。

---
## 確認記録 (filled after the operator responds)
- 日付 / 回答者:
- 確定した項目（→ [OPERATOR] に格上げ）:
- 修正された推測:
- → 06_nfg_output.md を finalized に更新し、verification_rank を再計算
```
