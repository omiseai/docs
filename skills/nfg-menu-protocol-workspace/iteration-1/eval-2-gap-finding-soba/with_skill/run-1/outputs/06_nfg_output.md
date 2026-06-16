# 06 · NFG output — Soba shop

The verified dataset. One block per dish: Machine Semantics + Human Narrative +
verification_rank. **Operator unavailable this run**, so no safety field is
operator-confirmed; safety-relevant `[INFERRED]`/`[UNKNOWN]` claims are flagged, not
asserted as fact. All four dishes are pre-operator-review drafts → **rank C**.

The concierge should **not** answer diner allergen/restriction questions about these
dishes as fact until the Stage 04 gaps are closed by the operator. Buckwheat is the
one safe affirmative claim (this is a soba shop and buckwheat is definitional in
Dishes 1, 2, 4) — everything else (wheat, soy, egg, crustacean, sesame, peanut,
dairy, fish, and all restrictions) is unresolved.

---

## Dish 1 — Zaru soba (ざるそば)
- verification_rank: **C** (open safety gaps: noodle wheat ratio, つゆ soy/wheat, dashi fish)
- data_source: live

### Machine Semantics
- ingredient_ids: soba-noodles(buckwheat + wheat, ratio [UNKNOWN] → GAP) [MENU·high],
  tsuyu(dashi + soy-sauce + mirin) [INFERRED·med], dashi(kombu, katsuobushi) [INFERRED·med],
  nori [INFERRED·med → GAP], wasabi/negi [INFERRED·med]
- method_ids: boil, chill/rinse [INFERRED·high]
- allergens: **buckwheat = yes [MENU·high]** (JP man). wheat = likely but UNRESOLVED
  [UNKNOWN/INFERRED] → GAP; soy = likely [INFERRED] → GAP; fish(bonito) = likely
  [INFERRED] → GAP. None asserted except buckwheat.
- restrictions: vegetarian/vegan = likely no (dashi fish) [INFERRED] → GAP;
  gluten-free = no [INFERRED/UNKNOWN] → GAP. Not asserted.
- taste_profile: umami-forward, savory; cool/refreshing; firm noodle texture
  ("clean buckwheat aroma, light savory dipping sauce") [INFERRED·med]
- calorie_range: range 2 of 5 (lower-moderate) [INFERRED·low]

### Human Narrative
- story / cultural context: Chilled buckwheat noodles served on a bamboo tray (ざる)
  with a dipping sauce — a classic Japanese soba presentation. [INFERRED — NOT in
  verified food-culture KB; do not present house/region claims as established fact.]
- serving notes: served cold; dip noodles into the つゆ before eating. [INFERRED·med]

---

## Dish 2 — Tempura soba (天ぷらそば)
- verification_rank: **C** (open safety gaps: noodle ratio, tempura item, batter egg,
  frying oil, broth soy/wheat, dashi fish — highest-risk dish on the menu)
- data_source: live

### Machine Semantics
- ingredient_ids: soba-noodles(buckwheat + wheat, ratio [UNKNOWN] → GAP) [MENU·high],
  broth(dashi + soy-sauce + mirin) [INFERRED·med], tempura(batter[wheat + egg?] +
  item[shrimp?]) [UNKNOWN → GAP], frying-oil[UNKNOWN → GAP]
- method_ids: boil, simmer, deep-fry [INFERRED·high]
- allergens: **buckwheat = yes [MENU·high]** (JP man). wheat = likely [UNKNOWN/INFERRED]
  → GAP; egg = UNRESOLVED [UNKNOWN] → GAP; crustacean(shrimp) = UNRESOLVED [UNKNOWN]
  → GAP; sesame/peanut(oil) = UNRESOLVED [UNKNOWN] → GAP; soy = likely [INFERRED] →
  GAP; fish(bonito) = likely [INFERRED] → GAP. Only buckwheat asserted.
- restrictions: vegetarian/vegan = likely no [INFERRED/UNKNOWN] → GAP; gluten-free =
  no [INFERRED/UNKNOWN] → GAP; halal = UNRESOLVED [UNKNOWN] → GAP. Not asserted.
- taste_profile: umami, savory-warm, crisp tempura over soft noodle ("hot savory
  broth, crisp fried topping") [INFERRED·med]
- calorie_range: range 3 of 5 (moderate) [INFERRED·low]

### Human Narrative
- story / cultural context: Hot soba in a savory dashi broth topped with tempura — a
  standard soba-shop staple. [INFERRED — NOT in verified food-culture KB; do not
  assert specifics.]
- serving notes: served hot; tempura is added on top and softens in the broth.
  [INFERRED·med]

---

## Dish 3 — Curry udon (カレーうどん)
- verification_rank: **C** (open safety gaps: roux dairy, animal stock/extract, meat
  topping, halal/no-pork/no-beef)
- data_source: live

### Machine Semantics
- ingredient_ids: udon-noodles(wheat) [CANONICAL·high], curry-roux(wheat + fat +
  spices + dairy? + animal-extract?) [INFERRED·med; dairy/extract UNKNOWN → GAP],
  dashi(kombu, katsuobushi) [INFERRED·med], meat-topping[UNKNOWN → GAP], negi [INFERRED·med]
- method_ids: boil, simmer [INFERRED·high]
- allergens: **wheat = yes [CANONICAL·high]** (udon + roux flour; JP man). dairy =
  UNRESOLVED [UNKNOWN] → GAP; soy = likely [INFERRED] → GAP; fish(bonito) = likely
  [INFERRED] → GAP. (beef/pork/chicken not JP allergen items — see restrictions.)
- restrictions: dairy-free = UNRESOLVED [UNKNOWN] → GAP; no-pork/no-beef = UNRESOLVED
  [UNKNOWN] → GAP; halal = UNRESOLVED [UNKNOWN] → GAP; vegetarian/vegan = likely no
  [INFERRED/UNKNOWN] → GAP; gluten-free = no [CANONICAL·high]. Only wheat & gluten-free
  asserted.
- taste_profile: rich umami, mild-to-medium spice, thick/starchy broth ("warming,
  savory, gently spiced") [INFERRED·med]
- calorie_range: range 3 of 5 (moderate) [INFERRED·low]

### Human Narrative
- story / cultural context: Japanese curry served over thick udon noodles in a
  dashi-curry broth — a comfort-food classic. [INFERRED — NOT in verified
  food-culture KB.]
- serving notes: served hot; broth is thick and splash-prone. [INFERRED·med]

---

## Dish 4 — Sobagaki (そばがき)
- verification_rank: **C** (open safety gaps: any wheat blended in, accompaniment →
  soy/wheat/fish, vegetarian status)
- data_source: live

### Machine Semantics
- ingredient_ids: buckwheat-flour [INFERRED·high], hot-water, accompaniment[soy-sauce
  / sugar+kinako / tsuyu — UNKNOWN → GAP]
- method_ids: boil/scald-and-knead [INFERRED·high]
- allergens: **buckwheat = yes [INFERRED·high]** (definitional; JP man — highest
  concentration on menu). wheat = UNRESOLVED [UNKNOWN] → GAP; soy/fish = depend on
  accompaniment [UNKNOWN] → GAP. Only buckwheat asserted.
- restrictions: vegetarian/vegan = depends on accompaniment [UNKNOWN] → GAP;
  gluten-free = UNRESOLVED [UNKNOWN] → GAP. Not asserted.
- taste_profile: mild, earthy buckwheat, soft/mochi-like texture ("pure buckwheat
  flavor, warm and tender") [INFERRED·med]
- calorie_range: range 2 of 5 (lower-moderate) [INFERRED·low]

### Human Narrative
- story / cultural context: A rustic, traditional buckwheat preparation — buckwheat
  flour kneaded with hot water into a soft mass, the oldest form of eating soba before
  noodles. [INFERRED — NOT in verified food-culture KB; the "oldest form" framing is a
  general claim and must be operator/KB-verified before being presented as fact.]
- serving notes: served hot, eaten with a dip or topping. [INFERRED·med]

---

## Verification gate (run before declaring the dataset done)
- [x] No allergen/restriction field rests on [INFERRED] or [UNKNOWN] as fact — all
      such fields are flagged `→ GAP` and routed to Stage 04, not asserted. (Only
      buckwheat — Dishes 1/2/4 — and wheat/gluten-free — Dish 3 — are asserted, each
      from a [MENU]/[CANONICAL] chain.)
- [x] Every derived allergen traces to a specific ingredient (Stage 03 chains).
- [x] Canonical overrides applied where available (dish-name terms; udon ⇒ wheat).
      Note: no beverage on menu, so no product_master match; no dish matched the
      verified food-culture KB, so all narrative is [INFERRED] and flagged.
- [x] Composites expanded (soba noodle blend, つゆ/dashi, tempura batter, curry roux)
      so hidden allergens (wheat, egg, dairy, soy) are visible.
- [x] Machine Semantics and Human Narrative kept separate.
- [x] gelatin not filed as meat allergen (none present); halal/pork-free kept under
      restrictions, not allergens; beef/pork/chicken tracked as restrictions only.
- [x] No "varies by item" answer cascaded (none received — operator absent).
- [x] verification_rank assigned per dish (all C); remaining gaps named explicitly.

**GATE RESULT: Does NOT pass at S/A.** Every dish ships at **C** — pre-operator-review
draft. This is an honest, expected outcome given the operator was unavailable. The
record is usable internally but the concierge must not present allergen/restriction
answers as fact (beyond buckwheat presence) until Stage 04 is answered.

## Run summary
- Dishes: 4 | reached S/A: 0 | at B/C: 4 (all C)
- Open safety gaps still blocking: **12**   ← the number that matters most
