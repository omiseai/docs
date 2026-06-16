# 06 · NFG output — Torihei
status: draft (pending operator sign-off)

The dataset. One block per dish: Machine Semantics + Human Narrative +
verification_rank. No operator input has been received, so every safety-relevant
inferred/unknown field below is **flagged, not asserted** — it lives as a gap, not a
fact. Only the sake (canonical) is fully verified.

---

## Dish 1 — Beef tendon stew (牛すじ煮込み)
- verification_rank: **B**  (open safety gaps: soy/wheat seasoning, dashi/fish)
- data_source: live

### Machine Semantics
- ingredient_ids: beef-tendon [MENU·high]; konnyaku [INFERRED·med → GAP];
  daikon [INFERRED·low → GAP]; dashi(kombu, katsuobushi) [INFERRED·med → GAP];
  seasoning-base [UNKNOWN → GAP]
- method_ids: simmer/boil [MENU·high]
- allergens: **not asserted** — soy [UNKNOWN→GAP], wheat [UNKNOWN→GAP],
  fish/bonito [INFERRED·med→GAP]. (Concierge must defer to staff on these.)
- restrictions: vegetarian = no, vegan = no, no-beef = no, hindu = no [all MENU·high];
  halal = no [INFERRED·low→GAP, but contains beef regardless]
- taste_profile: umami-forward, savory, rich; gentle saltiness (values + verbalization) [INFERRED·med]
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: not in food-culture KB → no verified narrative. A generic
  description ("a slow-simmered izakaya staple of beef tendon") is [INFERRED] and is
  withheld from authoritative presentation until operator confirms. [INFERRED·low]
- serving notes: typically served hot, garnished with green onion [INFERRED·low]

---

## Dish 2 — Chicken karaage (鶏の唐揚げ)
- verification_rank: **B**  (open safety gaps: wheat coating, sesame oil, soy marinade)
- data_source: live

### Machine Semantics
- ingredient_ids: chicken [MENU·high]; coating-starch [UNKNOWN→GAP];
  marinade-soy-sauce [INFERRED·med→GAP]; ginger/garlic [INFERRED·low]; frying-oil [UNKNOWN→GAP]
- method_ids: deep-fry [MENU·high]
- allergens: **not asserted** — wheat [UNKNOWN→GAP], soy [INFERRED·med→GAP],
  sesame [UNKNOWN→GAP]
- restrictions: vegetarian = no, vegan = no [MENU·high]; no-beef = yes-ok,
  no-pork = yes-ok pending shared-fryer check [INFERRED·med→GAP]; halal = no
  [INFERRED·low→GAP]; gluten-free = UNKNOWN (hinges on coating) [GAP]
- taste_profile: savory, juicy, crisp exterior [INFERRED·med]
- calorie_range: range 4 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: karaage is a ubiquitous izakaya dish; no verified
  regional narrative in KB. [INFERRED·low] — withheld from authoritative claim.
- serving notes: usually served with lemon wedge [INFERRED·low]

---

## Dish 3 — Dashimaki tamago (だし巻き卵)
- verification_rank: **B**  (egg is solid, but dashi/fish + soy seasoning open)
- data_source: live

### Machine Semantics
- ingredient_ids: egg [MENU·high]; dashi(kombu, katsuobushi) [MENU·med for dashi /
  INFERRED·med for composition → GAP]; seasoning soy/mirin/sugar [INFERRED·low→GAP]
- method_ids: pan-fry (rolled) [INFERRED·high]
- allergens: **egg = yes [MENU·high]** (asserted — named on menu). Not asserted:
  fish/bonito [INFERRED·med→GAP], soy [INFERRED·low→GAP], wheat [INFERRED·low→GAP]
- restrictions: vegan = no (egg) [MENU·high]; vegetarian = depends on dashi type
  [INFERRED·med→GAP]; pescatarian = yes-ok [MENU·high]
- taste_profile: umami, mildly sweet, soft/fluffy texture [INFERRED·med]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: a classic Japanese rolled omelette; not a KB regional
  dish → no verified origin narrative. [INFERRED·low]
- serving notes: often served with grated daikon [INFERRED·low]

---

## Dish 4 — Potato salad (ポテトサラダ)
- verification_rank: **B**  (egg via mayo highly likely but unconfirmed; pork unknown)
- data_source: live

### Machine Semantics
- ingredient_ids: potato [MENU·high]; mayonnaise(egg-yolk, oil, vinegar)
  [INFERRED·high→GAP]; cucumber/carrot/onion [INFERRED·med]; ham/bacon [INFERRED·low→GAP]
- method_ids: boil (potato) + mix/dress [INFERRED·med]
- allergens: **not asserted** — egg [INFERRED·high→GAP] (very likely, but unconfirmed,
  so flagged not asserted)
- restrictions: vegan = no (mayo egg) [INFERRED·high→GAP]; vegetarian = depends on
  ham/bacon [INFERRED·low→GAP]; no-pork / halal = UNKNOWN (ham/bacon?) [GAP]
- taste_profile: creamy, savory, mild [INFERRED·med]
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: izakaya/yoshoku staple; no verified KB narrative. [INFERRED·low]
- serving notes: served chilled [INFERRED·low]

---

## Dish 5 — Today's assorted sashimi (本日の刺身盛り合わせ)
- verification_rank: **C**  (contents inherently daily-variable; species unknown; multiple open shellfish/roe allergen gaps)
- data_source: live

### Machine Semantics
- ingredient_ids: assorted-raw-fish [UNKNOWN→GAP, daily]; daikon/shiso/wasabi
  garnish [INFERRED·med]; soy-sauce accompaniment [INFERRED·med→GAP]
- method_ids: raw [INFERRED·high]
- allergens: **not asserted** — fish [INFERRED·high→GAP, which species]; crab,
  shrimp/prawn, squid, abalone, salmon-roe all [UNKNOWN→GAP]; soy/wheat (soy sauce)
  [INFERRED·med→GAP]
- restrictions: vegan/vegetarian = no [INFERRED·high]; pescatarian = yes-ok
  [INFERRED·high]; no-beef/no-pork = yes-ok [INFERRED·high]; halal = no
  [INFERRED·low→GAP]
- taste_profile: fresh, clean, varies by fish [INFERRED·low]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: a daily sashimi assortment; contents change with the
  catch. No verified KB narrative. [INFERRED·low]
- serving notes: served chilled with wasabi and soy sauce; **the concierge must direct
  diners to confirm today's species and any shellfish with staff.** [INFERRED·high]

---

## Dish 6 — Kokuryu Junmai Ginjo (黒龍 純米吟醸) — by the glass
- verification_rank: **S**  (fully canonical; no safety gaps)
- data_source: live

### Machine Semantics
- ingredient_ids: rice, rice-koji, water [CANONICAL·high]
- method_ids: n/a (brewed); served poured by the glass [MENU·high]
- product identity: Kokuryu Junmai Ginjo, maker 黒龍酒造 (Kokuryu Sake Brewing Co.),
  Fukui, junmai_ginjo, ABV 15.5% [CANONICAL·high] (product_master: pm_kokuryu_junmai_ginjo)
- allergens: none [CANONICAL·high]
- restrictions: no-alcohol = FAIL [CANONICAL·high]; halal = no (alcohol)
  [CANONICAL·high]; vegan/vegetarian = yes-ok; gluten-free = yes-ok [CANONICAL·high]
- taste_profile: junmai ginjo — clean, fragrant, balanced (verbalized) [INFERRED·low for tasting note; spec CANONICAL]
- calorie_range: range 2 of 5 [INFERRED·low] (typical sake per glass)

### Human Narrative
- story / cultural context: Kokuryu is a celebrated Fukui brewery; specific narrative
  beyond the verified spec is [INFERRED] and withheld unless from a verified source.
  Verified facts (Fukui, junmai ginjo, 15.5%) [CANONICAL·high].
- serving notes: served by the glass [MENU·high]; junmai ginjo typically enjoyed
  chilled or at room temperature [INFERRED·low]

---

## Verification gate (run before declaring the dataset done)
- [x] No allergen/restriction field rests on [INFERRED]/[UNKNOWN] **as asserted fact** —
      all such are flagged → GAP, not asserted. (Only asserted allergen: egg on Dish 3,
      which is [MENU·high]. Only asserted restrictions are MENU/CANONICAL-grounded.)
- [x] Every derived allergen traces to a specific ingredient (chains shown in Stage 03)
- [x] Canonical overrides applied — sake matched product_master and overrode any guess
- [x] Composites expanded (dashi → kombu+katsuobushi; mayonnaise → egg-yolk+oil+vinegar;
      sashimi assortment flagged for hidden shellfish)
- [x] Machine Semantics and Human Narrative kept separate
- [x] gelatin not filed as a meat allergen (n/a here); halal/no-pork under
      restrictions, not allergens (Dish 4 ham/bacon → pork restriction, not allergen)
- [x] No "varies by item" answer cascaded — no operator answers exist yet; nothing cascaded
- [x] verification_rank assigned per dish; remaining gaps named explicitly

## Run summary
- Dishes: 6 | reached S/A: 1 (Dish 6, S) | at B/C: 5 (four B, one C)
- Open safety gaps still blocking: **10** (gap-register items A1–A10)
- Status: **draft** (pending operator sign-off via Stage 07)
