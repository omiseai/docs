# 06 · NFG output — Torihei (鳥平), Osaka izakaya

The verified dataset in NFG shape. One block per dish: Machine Semantics + Human
Narrative + verification_rank. No operator answers were available, so no `[INFERRED]`
or `[UNKNOWN]` safety field has been promoted to fact — every such field is named as
an open gap and the rank reflects it. Honest incompleteness over fake completeness.

Rank legend: **S** all safety fields [OPERATOR]/[CANONICAL]; **A** core confirmed,
only minor narrative gaps; **B** open safety gaps or significant [INFERRED] fields;
**C** largely [INFERRED], pre-operator draft.

---

## Dish 1 — Beef tendon stew (牛すじ煮込み)
- verification_rank: **C**  (seasoning base + dashi both unconfirmed; soy/wheat/fish/halal all open)
- data_source: live

### Machine Semantics
- ingredient_ids: beef-tendon [MENU·high]; konnyaku [INFERRED·med → GAP];
  dashi(kombu, katsuobushi) [INFERRED·med → GAP]; seasoning-base [UNKNOWN → GAP];
  negi [INFERRED·low]
- method_ids: simmer [MENU·high]
- allergens: **none asserted.** Open: soy [UNKNOWN], wheat [UNKNOWN], fish [INFERRED] — all in gap register, not stated as fact.
- restrictions: vegetarian = no, vegan = no, no-beef = fails [all MENU·high]; halal = no [INFERRED → GAP]
- taste_profile: umami-forward, savory, rich; gelatinous/tender texture → "deeply savory, melt-in-mouth tendon" [INFERRED·med]
- calorie_range: range 3 of 5 (moderate) [INFERRED·low]

### Human Narrative
- story / cultural context: Not in food-culture KB. Generic note only: a classic
  Kansai izakaya simmered dish; beef tendon braised until gelatinous. [INFERRED — flagged, not authoritative]
- serving notes: typically topped with green onion; pairs with sake/beer [INFERRED·low]

---

## Dish 2 — Japanese fried chicken / karaage (鶏の唐揚げ)
- verification_rank: **C**  (coating, oil, marinade all unconfirmed → wheat/sesame/soy open)
- data_source: live

### Machine Semantics
- ingredient_ids: chicken [MENU·high]; marinade-soy-sauce [INFERRED·med → GAP];
  garlic/ginger/sake [INFERRED·low]; coating-starch-or-flour [UNKNOWN → GAP];
  frying-oil [UNKNOWN → GAP]
- method_ids: deep-fry [MENU·high]
- allergens: **none asserted.** Open: soy [INFERRED], wheat [UNKNOWN], sesame [UNKNOWN] — gap register.
- restrictions: vegetarian = no, vegan = no [MENU·high]; no-pork = likely ok [INFERRED·med]; halal = no [INFERRED → GAP]; gluten-free = undetermined [UNKNOWN → GAP]
- taste_profile: savory, umami, crispy exterior / juicy → "crisp-fried, savory and juicy" [INFERRED·med]
- calorie_range: range 4 of 5 (higher; deep-fried) [INFERRED·low]

### Human Narrative
- story / cultural context: Not in food-culture KB. Generic: karaage is a staple
  izakaya fried-chicken dish. [INFERRED — flagged]
- serving notes: usually served with lemon and/or mayonnaise [INFERRED·low]

---

## Dish 3 — Rolled dashi omelette / dashimaki tamago (だし巻き卵)
- verification_rank: **B**  (egg confirmed [MENU]; but dashi fish + soy seasoning open, so a safety gap remains)
- data_source: live

### Machine Semantics
- ingredient_ids: egg [MENU·high]; dashi(kombu, katsuobushi) [MENU named / composition INFERRED·med → GAP]; seasoning-soy/mirin [INFERRED·med → GAP]; cooking-oil [INFERRED·low]
- method_ids: pan-fry (rolled / 焼く) [MENU·high]
- allergens: **egg = yes [MENU·high] ✅ ASSERTED.** Open: fish [INFERRED], soy [INFERRED], wheat [INFERRED·low] — gap register.
- restrictions: vegan = no (egg) [MENU·high]; dairy-free = yes [INFERRED·high]; vegetarian = undetermined (dashi fish) [INFERRED → GAP]; pescatarian = likely [INFERRED·med]
- taste_profile: umami, mildly sweet/savory, soft fluffy texture → "delicate, dashi-rich, lightly sweet" [INFERRED·med]
- calorie_range: range 2 of 5 (lower) [INFERRED·low]

### Human Narrative
- story / cultural context: Not in food-culture KB. Generic: a rolled Japanese
  omelette seasoned with dashi. [INFERRED — flagged]
- serving notes: served warm, often with grated daikon [INFERRED·low]

---

## Dish 4 — Potato salad (ポテトサラダ)
- verification_rank: **C**  (egg via mayo only inferred; possible pork; vegetarian/halal/no-pork all open)
- data_source: live

### Machine Semantics
- ingredient_ids: potato [MENU·high]; mayonnaise(egg-yolk, oil, vinegar) [INFERRED·high → GAP]; cucumber/carrot/onion [INFERRED·med]; ham-or-bacon [INFERRED·low → GAP]; pepper/salt [INFERRED·low]
- method_ids: boil (potato) + raw (veg) [INFERRED·med]
- allergens: **none asserted.** Open: egg [INFERRED·high], mustard [UNKNOWN, EU] — gap register.
- restrictions: vegan = no (mayo egg) [INFERRED·high → GAP]; vegetarian = undetermined (possible ham) [INFERRED → GAP]; no-pork = undetermined [UNKNOWN → GAP]; halal = undetermined [UNKNOWN → GAP]
- taste_profile: creamy, savory, mild → "creamy and mild, gently savory" [INFERRED·med]
- calorie_range: range 3 of 5 (moderate; mayo) [INFERRED·low]

### Human Narrative
- story / cultural context: Not in food-culture KB. Generic: a Japanese-style potato
  salad, a common izakaya side. [INFERRED — flagged]
- serving notes: served chilled [INFERRED·low]

---

## Dish 5 — Today's assorted sashimi (本日の刺身盛り合わせ)
- verification_rank: **C**  (fish species unknown and daily-variable → entire allergen profile open; highest-risk record)
- data_source: live

### Machine Semantics
- ingredient_ids: assorted-raw-fish [UNKNOWN → GAP, daily]; daikon-tsuma/shiso/wasabi [INFERRED·med]; dipping-soy-sauce [INFERRED·med → GAP]
- method_ids: raw [MENU·high]
- allergens: **none asserted.** Open and daily-variable: fish [UNKNOWN], crustacean/shrimp [UNKNOWN], salmon-roe [UNKNOWN], abalone [UNKNOWN], squid [UNKNOWN], soy+wheat (dip) [INFERRED] — gap register, must be confirmed per service.
- restrictions: vegetarian = no, vegan = no [MENU·high]; pescatarian = likely yes [INFERRED·med]
- taste_profile: fresh, clean, varies by fish → "fresh raw seafood, clean and delicate" [INFERRED·low]
- calorie_range: range 2 of 5 (lower) [INFERRED·low]

### Human Narrative
- story / cultural context: Not in food-culture KB (and inherently variable). Generic:
  a daily selection of fresh sashimi. [INFERRED — flagged]
- serving notes: **concierge must surface the daily species before answering any
  allergy question on this dish.** Recommend an operator daily-input field.

---

## Dish 6 — Kokuryū Junmai Ginjō, by the glass (黒龍 純米吟醸 グラス)
- verification_rank: **A**  (all safety-relevant fields [CANONICAL] from product_master; only the operator's acknowledgement of the canonical match + pour size remains, a narrative/confirmation gap)
- data_source: live

### Machine Semantics
- ingredient_ids: rice [CANONICAL·high]; water [CANONICAL·high]; koji [CANONICAL·high]; yeast [CANONICAL·high] (junmai — no added distilled alcohol) [CANONICAL·high]
- method_ids: brewed/fermented (beverage; no food cooking-method token) [CANONICAL·high]
- allergens: **none [CANONICAL·high] ✅ ASSERTED** (no food allergens from rice/water/koji/yeast). Sulphites = not added (sake) [INFERRED·low, EU-only, minor — flagged not asserted].
- restrictions: no-alcohol = fails [CANONICAL·high] ✅; halal = fails (alcohol) [CANONICAL·high] ✅; vegan = yes, vegetarian = yes, gluten-free = yes [CANONICAL·high]
- taste_profile: junmai ginjō — clean, fruity-floral ginjō aroma, smooth, slightly dry → "fragrant and clean, smooth with a gentle dryness" [CANONICAL·med]
- calorie_range: range 2 of 5 per standard glass pour [INFERRED·low]

### Human Narrative
- story / cultural context: Kokuryu Sake Brewery (黒龍酒造), Fukui Prefecture — a
  highly regarded junmai ginjō. [CANONICAL·high via product_master] (Matched on full
  product identity, NOT by 龍 substring.)
- serving notes: served by the glass, ¥900; good chilled. [pour size = OPEN, ask operator]

---

# Verification gate (run before declaring the dataset done)
- [x] No allergen/restriction field rests on [INFERRED] or [UNKNOWN] **as fact** — all such are in the gap register, not asserted. Asserted fields rest only on [MENU]/[CANONICAL] (Dish 3 egg; Dish 6 alcohol/halal/etc.; protein-based vegetarian=no across dishes).
- [x] Every derived allergen traces to a specific ingredient (shown in Stage 03 chains).
- [x] Canonical overrides applied: product_master for Dish 6 (full-identity match, no substring); ingredient_glossary for all English dish names (Policy B boundary respected).
- [x] Composites expanded so hidden allergens are visible: dashi → kombu+katsuobushi (Dishes 1,3); mayonnaise → egg yolk+oil+vinegar (Dish 4).
- [x] Machine Semantics and Human Narrative kept separate per dish.
- [x] gelatin not filed as a meat allergen; halal / no-pork / no-alcohol kept under restrictions, not allergens.
- [x] No "varies by item/day" answer cascaded — Dish 5 fish kept open per-service; no operator answers existed to cascade anyway.
- [x] verification_rank assigned per dish; remaining gaps named explicitly (Stage 04).
- [ ] **Operator dialogue complete — NOT YET. Pending (Stage 05). This is the single
      reason no dish reached S and five of six sit at B/C. Gate "passes" only in the
      honest-incompleteness sense: the record ships at its true rank with gaps named.**

# Run summary
- Dishes: **6** | reached S/A: **1** (Dish 6, rank A) | at B/C: **5** (Dish 3 = B; Dishes 1, 2, 4, 5 = C)
- Reached **S**: 0 (S impossible without operator confirmation; only Dish 6 is canonical-backed and it sits at A pending operator acknowledgement)
- **Open safety gaps still blocking: 10**   ← the number that matters most
  (Stage 04 Section A items 1–10; Dish 5's species gap is recurring/per-service.)
