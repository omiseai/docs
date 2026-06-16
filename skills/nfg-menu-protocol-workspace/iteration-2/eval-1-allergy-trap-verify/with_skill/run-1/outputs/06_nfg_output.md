# 06 · NFG output — (Unnamed store — lunch menu)
status: **draft (pending operator sign-off)**

The dataset, in the NFG shape. One block per dish: Machine Semantics + Human
Narrative + verification_rank. **No operator contact this run**, so every
safety-relevant field rests on `[INFERRED]`/`[UNKNOWN]` and is therefore carried as a
**flagged gap, not asserted as fact**. No dish can rank above **C** until Stage 07
sign-off. No canonical entry matched, so there are no `[CANONICAL]` upgrades.

---

## Dish 1 — Pork loin cutlet set meal (ロースかつ定食)
- verification_rank: **C**  (deep-fried + set-meal; every allergen chain unresolved)
- data_source: live

### Machine Semantics
- ingredient_ids: pork-loin [INFERRED·high → GAP], breading(wheat-flour, egg, panko→wheat) [INFERRED·med → GAP],
  frying-oil(base unknown) [UNKNOWN → GAP], rice [INFERRED·med], miso-soup(miso→soy, dashi→katsuobushi/fish, tofu→soy?) [INFERRED·med → GAP],
  shredded-cabbage [INFERRED·med], tonkatsu-sauce(soy-sauce→soy+wheat) [INFERRED·med → GAP]
- method_ids: deep-fry [INFERRED·high]; boil/simmer [INFERRED·med]
- allergens: **NONE ASSERTED** — wheat, egg, soy, fish, sesame, peanut are all
  flagged GAPs (see Stage 03), not facts. Do not present any allergen safety claim.
- restrictions: no-pork = fails [INFERRED·high → GAP], halal = fails [INFERRED·high → GAP],
  vegetarian = no [INFERRED·high → GAP], gluten-free = fails [INFERRED·med → GAP] — all pending confirmation
- taste_profile: savory / umami / crisp-fried (verbalized) [INFERRED·low]
- calorie_range: range 4 of 5 (high, fried + rice) [INFERRED·low]

### Human Narrative
- story / cultural context: not in food-culture KB → **left blank** (would be
  [INFERRED]; not writing an invented origin story).
- serving notes: typically served with shredded cabbage, rice, miso soup [INFERRED·med] — unconfirmed.

---

## Dish 2 — Breaded fried shrimp (エビフライ)
- verification_rank: **C**
- data_source: live

### Machine Semantics
- ingredient_ids: shrimp [INFERRED·high → GAP], breading(wheat-flour, egg, panko→wheat) [INFERRED·med → GAP],
  frying-oil(base unknown) [UNKNOWN → GAP], sauce(tartar→egg? / tonkatsu→soy+wheat?) [UNKNOWN → GAP]
- method_ids: deep-fry [INFERRED·high]
- allergens: **NONE ASSERTED.** Crustacean (shrimp) is near-certain from the name but
  still flagged for operator confirmation; wheat, egg, sesame, peanut all GAPs.
- restrictions: vegetarian = no [INFERRED·high], pescatarian = ok [INFERRED·med], gluten-free = fails [INFERRED·med → GAP]
- taste_profile: savory / umami / crisp-fried [INFERRED·low]
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: not in food-culture KB → left blank.
- serving notes: commonly served with tartar or tonkatsu sauce [UNKNOWN] — unconfirmed.

---

## Dish 3 — Annin-dofu / almond jelly (杏仁豆腐)
- verification_rank: **C**
- data_source: live
- **Naming-trap note (carried into the record): "豆腐" is a texture word, NOT soy.
  Soy is NOT asserted. Dessert-mistagging guard: no meat allergens on this dessert.**

### Machine Semantics
- ingredient_ids: milk/cream [INFERRED·med → GAP], sugar [INFERRED·med],
  setting-agent(agar OR gelatin) [UNKNOWN → GAP], almond-flavor(apricot-kernel OR essence) [UNKNOWN → GAP]
- method_ids: (chilled-set / none) [INFERRED·med]
- allergens: **NONE ASSERTED.** milk (dairy) and almond (tree nut) are flagged GAPs.
  Soy = explicitly NOT present (name trap rejected).
- restrictions: vegetarian / vegan / halal / kosher / dairy-free all **depend on
  setting agent + dairy** = GAPs.
- taste_profile: sweet / smooth / cool [INFERRED·low]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: not in food-culture KB → left blank (no invented history).
- serving notes: chilled dessert [INFERRED·med].

---

## Dish 4 — Coffee jelly (コーヒーゼリー)
- verification_rank: **C**
- data_source: live
- **Dessert-mistagging guard: no meat allergens. Gelatin (if used) is its own token,
  not a meat allergen.**

### Machine Semantics
- ingredient_ids: brewed-coffee [INFERRED·high], sugar [INFERRED·med],
  setting-agent(gelatin OR agar) [UNKNOWN → GAP], topping(cream/milk?) [UNKNOWN → GAP]
- method_ids: (chilled-set / none) [INFERRED·med]
- allergens: **NONE ASSERTED.** milk (dairy) is a flagged GAP (topping-dependent).
- restrictions: vegetarian / vegan / halal / kosher / dairy-free all depend on
  setting agent + topping = GAPs.
- taste_profile: bitter-sweet / smooth / cool [INFERRED·low]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: not in food-culture KB → left blank.
- serving notes: chilled dessert, often with cream/syrup [UNKNOWN].

---

## Verification gate (run before declaring the dataset done)
- [x] No allergen/restriction field rests on [INFERRED]/[UNKNOWN] as fact — confirmed:
      **zero allergens asserted**; all live in the gap register.
- [x] Every (potential) derived allergen traces to a specific ingredient (Stage 03 chains shown).
- [x] Canonical overrides applied where matched — **no matches existed**; nothing
      mis-tagged as [CANONICAL]; no fabricated canonical data.
- [x] Composites expanded (breading, miso soup, dashi, tonkatsu sauce, setting agents).
- [x] Machine Semantics and Human Narrative kept separate.
- [x] gelatin NOT filed as a meat allergen; halal/pork-free under restrictions, not allergens.
- [x] No "varies by item" answer cascaded (none were given — operator unavailable).
- [x] verification_rank assigned per dish; remaining gaps named explicitly.
- [ ] **Operator sign-off (Stage 07) — NOT yet obtained. Dataset stays a DRAFT.**

## Run summary
- Dishes: 4 | reached S/A: **0** | at B/C: **4** (all C)
- Open safety gaps still blocking: **12** (gap-register Q1–Q12)
- Status: **draft** (not finalized; operator unavailable this run)

> Concierge behaviour at this state: for every one of these four dishes the concierge
> must answer allergy questions with "申し訳ございません、スタッフにご確認ください /
> please check with staff" and must **not** state any dish as free of any allergen.
