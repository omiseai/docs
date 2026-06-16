# 06 · NFG output — Soba shop (`soba-shop-onboarding`)
status: **draft (pending operator sign-off)**

One block per dish: Machine Semantics + Human Narrative + verification_rank.
No operator answers exist yet, so every safety-relevant inferred/unknown field is
carried as a NAMED GAP — never asserted as fact. All four dishes are pre-operator-review.

---

## Dish 1 — Zaru soba (ざるそば)
- verification_rank: **C** (no safety field confirmed; buckwheat near-certain but unconfirmed; wheat/soy/fish open)
- data_source: live

### Machine Semantics
- ingredient_ids: buckwheat-flour [INFERRED·high → GAP confirm], wheat-flour(つなぎ?) [INFERRED·med → GAP],
  tsuyu{soy-sauce [INFERRED·high → GAP], dashi(kombu, katsuobushi) [INFERRED·med → GAP], mirin/sugar [INFERRED·low]},
  nori/negi/wasabi (garnish) [INFERRED·med]
- method_ids: boil, chill/rinse [INFERRED·high]
- allergens: buckwheat = LIKELY YES [INFERRED·high] — flagged, not asserted;
  wheat / soy / fish = **OPEN GAP** — not asserted (see 04 #2, #8)
- restrictions: gluten-free = no [INFERRED·med → GAP]; vegetarian/vegan = OPEN GAP (fish dashi)
- taste_profile: clean, nutty buckwheat, savory-umami dip ("nutty, refreshing, umami dipping sauce") [INFERRED]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: [INFERRED — no food-culture KB match] Generic: chilled
  buckwheat noodles on a bamboo tray with a dipping sauce. NOT presented as authoritative.
- serving notes: dip noodles into tsuyu; condiments to taste [INFERRED]

---

## Dish 2 — Tempura soba (天ぷらそば)
- verification_rank: **C** (highest allergen density; shrimp/egg/sesame/wheat/fish/soy all open)
- data_source: live

### Machine Semantics
- ingredient_ids: buckwheat-flour [INFERRED·high → GAP], wheat-flour(noodle つなぎ?) [INFERRED·med → GAP],
  kake-tsuyu{soy-sauce [INFERRED·high → GAP], dashi(kombu, katsuobushi) [INFERRED·med → GAP]},
  tempura{batter: wheat-flour [INFERRED·high → GAP], egg? [INFERRED·med → GAP]; item: shrimp-or-vegetable [UNKNOWN → GAP]; frying-oil [UNKNOWN → GAP]}
- method_ids: boil, deep-fry, simmer/heat [INFERRED·high]
- allergens: buckwheat = LIKELY YES [INFERRED·high] flagged; wheat / egg / **shrimp(crustacean)** / sesame / soy / fish = **OPEN GAP** — not asserted (04 #2–#5, #8)
- restrictions: gluten-free = no [INFERRED·high → GAP confirm]; vegetarian/vegan/pescatarian = OPEN GAP; halal = OPEN GAP
- taste_profile: hot savory broth, crisp tempura ("warm umami broth with crisp fried topping") [INFERRED]
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story: [INFERRED — no KB match] Generic: hot soba in dashi broth topped with tempura. Not authoritative.
- serving notes: eat promptly while tempura is crisp [INFERRED]

---

## Dish 3 — Curry udon (カレーうどん)
- verification_rank: **C** (meat identity unknown → religious restrictions open; dairy/wheat/soy/fish open)
- data_source: live

### Machine Semantics
- ingredient_ids: udon{wheat-flour [INFERRED·high → GAP confirm]},
  curry-broth{roux: wheat-flour [INFERRED·high → GAP], fat [INFERRED·med], spices [INFERRED·med],
  dairy? [INFERRED·low → GAP], dashi(kombu, katsuobushi) [INFERRED·med → GAP], soy/soy-sauce [INFERRED·med → GAP],
  meat: none-or-chicken-or-pork-or-beef [UNKNOWN → GAP]}, negi, aburaage? [INFERRED·low]
- method_ids: boil, simmer [INFERRED·high]
- allergens: wheat = LIKELY YES (udon) [INFERRED·high] flagged; milk / soy / fish / chicken / pork / beef = **OPEN GAP** — not asserted (04 #6, #7, #8)
- restrictions: **no-pork = OPEN GAP, no-beef = OPEN GAP, halal = OPEN GAP** (meat identity unknown);
  gluten-free = no [INFERRED·high → GAP confirm]; vegetarian/vegan/dairy-free = OPEN GAP
- taste_profile: warm, spiced, thick umami curry ("rich, mildly spiced dashi-curry broth") [INFERRED]
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story: [INFERRED] Generic: Japanese-style curry over wheat udon in a dashi-curry broth. Not authoritative.
- serving notes: thick broth, can splatter [INFERRED]

---

## Dish 4 — Sobagaki (そばがき)
- verification_rank: **C** (buckwheat near-certain; wheat/accompaniment open)
- data_source: live

### Machine Semantics
- ingredient_ids: buckwheat-flour [INFERRED·high → GAP confirm], hot-water [INFERRED·high],
  wheat-tsunagi? (usually none) [INFERRED·med → GAP], accompaniment: tsuyu/soy/wasabi [INFERRED·med → GAP]
- method_ids: mix/knead with hot water; (sometimes boil) [INFERRED·med]
- allergens: buckwheat = LIKELY YES [INFERRED·high] flagged; wheat / soy / fish = **OPEN GAP** (depends on tsunagi + accompaniment, 04 #9) — not asserted
- restrictions: gluten-free = POSSIBLY YES if no wheat + no soy-sauce dip [UNKNOWN → GAP]; vegetarian/vegan = OPEN GAP (accompaniment)
- taste_profile: soft, mochi-like, pure buckwheat ("soft, nutty, gently chewy") [INFERRED]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story: [INFERRED — no KB match] Generic: buckwheat flour kneaded with hot water; an older way of eating soba. Not authoritative.
- serving notes: eat with dip or wasabi [INFERRED]

---

## Verification gate (run before declaring the dataset done)
- [x] No allergen/restriction field rests on [INFERRED]/[UNKNOWN] as fact — every such field is carried as an OPEN GAP, not asserted
- [x] Every derived allergen traces to a specific ingredient (see Stage 03 chains)
- [x] Canonical overrides applied — **no canonical match existed** for any dish; nothing was fabricated as canonical (candidates queued only)
- [x] Composites expanded (tsuyu, tempura, curry roux, soba noodle) so hidden allergens are visible
- [x] Machine Semantics and Human Narrative kept separate
- [x] gelatin not mis-filed (n/a); halal/no-pork/no-beef kept under restrictions, not allergens
- [x] No "varies by item" answer cascaded (no operator answers exist to cascade)
- [x] verification_rank assigned per dish; remaining gaps named explicitly
- [ ] **GATE NOT PASSED at S/A** — every dish has open safety gaps; this is an honest C-grade pre-operator-review draft

## Run summary
- Dishes: 4 | reached S/A: 0 | at B/C: 4 (all C)
- **Open safety gaps still blocking: 9** (gap register section A, #1–#9)
- Status: **draft** — pending operator sign-off (Stage 07). Concierge must answer
  "スタッフにご確認ください" for all allergen/restriction questions until these close.
