# Allergen Verification — Lunch Menu

**Purpose:** Pre-launch allergen verification before enabling the AI menu concierge. A diner with allergies will rely on these answers, so each item is treated conservatively: where an ingredient is *typical but not guaranteed* for a dish, it is flagged as **NEEDS OWNER CONFIRMATION** rather than assumed safe.

**Reference framework:** Japan's allergen labeling system — 8 mandatory items (*tokutei genryō*) + 20 recommended items (*tokutei genryō ni junzuru mono*). Mandatory items carry the highest risk and are called out explicitly.

- Mandatory (8): egg (卵), milk (乳), wheat (小麦), buckwheat (そば), peanut (落花生), shrimp/prawn (えび), crab (かに), walnut (くるみ).
- Recommended (20): almond, abalone, squid, salmon roe, orange, cashew, kiwi, beef, gelatin, sesame, salmon, mackerel, soybean, chicken, banana, pork, matsutake, peach, yam, apple.

> **CAUTION:** This is an ingredient-knowledge verification based on standard recipes for each dish. It is **not** a substitute for the restaurant owner confirming the actual recipe, brand-specific products, and shared-fryer / cross-contact practices in *this* kitchen. Several items below cannot be finalized without that confirmation. See the open questions at the end.

---

## 1. ロースかつ定食 — Pork Loin Tonkatsu Set ¥1,000

A breaded, deep-fried pork loin cutlet served as a set meal (typically with rice, miso soup, shredded cabbage, pickles, and tonkatsu sauce).

| Allergen | Status | Reason |
|---|---|---|
| Pork (豚肉) | **CONTAINS** | Main ingredient (loin = ロース). |
| Wheat (小麦) | **CONTAINS** | Panko breading + flour dredge; tonkatsu sauce is wheat-based. |
| Egg (卵) | **CONTAINS** | Standard breading uses egg wash (flour → egg → panko). |
| Soybean (大豆) | **LIKELY** | Miso soup (miso = soy), tonkatsu sauce, frying oil may be soy/blended. |
| Milk (乳) | **POSSIBLE** | Some panko / batters contain milk; tonkatsu sauce usually does not. Needs confirmation. |
| Sesame (ごま) | **POSSIBLE** | Tonkatsu sauce and toppings sometimes include sesame. Confirm. |
| Shrimp / Crab (えび・かに) | **CROSS-CONTACT RISK** | If fried in the **same oil** as the エビフライ (item 2), pork katsu carries shrimp cross-contact. This is critical — see open questions. |

**Set-meal note:** Miso soup almost always contains **soybean**, and dashi may contain **fish (mackerel/bonito)**. Pickles and dressings vary. The full set, not just the cutlet, must be itemized.

---

## 2. エビフライ — Fried Shrimp (Ebi Fry) ¥1,200

Breaded, deep-fried shrimp/prawn.

| Allergen | Status | Reason |
|---|---|---|
| Shrimp / Prawn (えび) | **CONTAINS** | Main ingredient. **Mandatory allergen — highest risk.** |
| Wheat (小麦) | **CONTAINS** | Flour + panko breading. |
| Egg (卵) | **CONTAINS** | Egg wash in breading. |
| Crab (かに) | **POSSIBLE / CROSS-CONTACT** | Shrimp and crab are frequently processed/handled together; shared supplier or oil raises crab cross-contact risk. Confirm. |
| Soybean (大豆) | **POSSIBLE** | Frying oil, accompanying sauce (often tartar = egg/milk, or tonkatsu sauce = soy/wheat). |
| Milk (乳) | **POSSIBLE** | If served with **tartar sauce** (mayonnaise + sometimes dairy) — confirm the accompanying sauce. |

---

## 3. 杏仁豆腐 — Annin Tofu (Almond Tofu) ¥350

**⚠️ NAMING TRAP — read carefully.** Despite "豆腐 (tofu)" in the name, this dessert is **not soybean tofu**. It is a chilled, milk-based jelly/pudding set with agar or gelatin, flavored to taste of almond.

| Allergen | Status | Reason |
|---|---|---|
| Milk (乳) | **CONTAINS (typical)** | Standard annin tofu is made with milk and/or cream/evaporated milk. **High-risk for a dairy-allergic diner.** Confirm recipe. |
| Almond / Apricot kernel (アーモンド / 杏仁) | **CONTAINS / TREE-NUT RISK** | Traditional 杏仁 = apricot kernel; modern versions use **almond essence or actual almond**. Almond is a recommended-label allergen and a tree nut. **A tree-nut-allergic diner is at risk.** Confirm whether real almond/apricot kernel or synthetic flavoring is used. |
| Gelatin (ゼラチン) | **POSSIBLE** | If set with gelatin (vs. agar/kanten). Relevant for gelatin allergy and for halal/vegetarian, not a top-8 but a recommended-label item. |
| Soybean (大豆) | **DO NOT ASSUME** | The name says "tofu" but this typically contains **no soy**. The AI must **not** tell a soy-allergic diner to avoid it on the assumption it is tofu, nor reassure a diner it is "just tofu." Confirm actual ingredients. |

**Why this matters:** A literal reading of the name would mislead in *both* directions — it could wrongly flag soy, and could wrongly reassure someone that a "tofu" dessert is dairy/nut-free. The real risks here are **milk and almond/tree-nut**, which the name completely hides.

---

## 4. コーヒーゼリー — Coffee Jelly ¥300

Coffee-flavored jelly dessert, usually served with a pour of cream/milk and/or syrup.

| Allergen | Status | Reason |
|---|---|---|
| Milk (乳) | **LIKELY (as served)** | Coffee jelly is very commonly topped with **cream, condensed milk, or coffee creamer**. The jelly itself is often dairy-free, but the dish *as plated* usually involves dairy. **Confirm whether cream/milk is served on or alongside it**, and whether it can be served without. |
| Gelatin (ゼラチン) | **POSSIBLE** | If set with gelatin rather than agar. |
| Egg (卵) | **POSSIBLE** | Rare, but some recipes/garnishes (e.g., custard, certain creamers) may contain egg. Confirm. |
| Soybean (大豆) | **POSSIBLE** | Non-dairy "creamers" (フレッシュ / コーヒーフレッシュ) can be soy/oil-based. Confirm the creamer product. |
| Caffeine | **NOT an allergen** but worth a diner-facing note | Contains coffee/caffeine — relevant for sensitivity, not allergy labeling. |

---

## Cross-cutting risk: SHARED FRYER

Items 1 (tonkatsu) and 2 (ebi fry) are both deep-fried. If they share a fryer/oil:
- The **pork katsu carries shrimp (えび) cross-contact** — a mandatory-allergen risk a shrimp-allergic diner must be warned about even though the cutlet "contains no shrimp."
- Any other fried item shares this oil too.

**The AI must not tell a shrimp-allergic diner that the tonkatsu is shrimp-free without resolving the fryer question.** This is the single most dangerous gap.

---

## Summary table (mandatory-8 allergens highlighted)

| Dish | Egg | Milk | Wheat | Buckwheat | Peanut | Shrimp | Crab | Walnut | Other notable |
|---|---|---|---|---|---|---|---|---|---|
| ロースかつ定食 | YES | possible | YES | no | no | cross-contact (oil) | cross-contact | no | pork, soy, sesame?, fish (dashi) |
| エビフライ | YES | possible (sauce) | YES | no | no | **YES** | possible | no | soy |
| 杏仁豆腐 | no | **YES (typical)** | no | no | no | no | no | no | **almond/tree-nut**, gelatin?, NOT soy |
| コーヒーゼリー | possible | **likely (as served)** | no | no | no | no | no | no | gelatin?, soy (creamer)? |

---

## Verdict — NOT cleared for AI concierge launch yet

The menu cannot be safely turned on for allergy-reliant diners until the owner confirms the open questions below. Confirmed (high-confidence) facts: ebi fry contains shrimp/wheat/egg; tonkatsu contains pork/wheat/egg. Everything marked "possible/likely/typical" is a recipe-specific unknown that the AI would otherwise have to guess at — and guessing about allergens is unacceptable.

### Open questions the owner MUST confirm before launch

1. **Shared fryer?** Are the tonkatsu and ebi fry cooked in the same oil? (Determines shrimp/crab cross-contact warning on the tonkatsu.)
2. **杏仁豆腐 recipe:** Made with milk/cream? (almost certainly yes) Real almond/apricot kernel or synthetic flavor? Set with gelatin or agar? — confirms milk + tree-nut + gelatin status.
3. **コーヒーゼリー as served:** Is cream/milk/creamer poured on or served alongside? Can it be served without? What creamer product (dairy vs. soy/oil-based)?
4. **Tonkatsu breading & sauce:** Does the panko/batter contain milk? Does the tonkatsu sauce contain sesame? Confirm frying-oil type (soy/blend).
5. **エビフライ accompaniment:** Tartar sauce (egg/milk) or tonkatsu sauce (wheat/soy)? Any crab in the supply chain?
6. **The full 定食 set:** Itemize miso soup (soy + fish dashi), pickles, and any side dressings — these carry allergens beyond the cutlet itself.

Per VAD / HITL principle: none of the "possible/likely" entries should be presented to diners as verified until the owner confirms. Until then, the concierge should answer allergen questions on these items with explicit uncertainty and a "please ask staff" fallback rather than a confident safe/unsafe call.
