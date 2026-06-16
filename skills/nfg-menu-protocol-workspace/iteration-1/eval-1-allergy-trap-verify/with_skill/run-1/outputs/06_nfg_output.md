# 06 · NFG output — Lunch Menu

The verified dataset. One block per dish: Machine Semantics + Human Narrative +
verification_rank. Stage 05 produced NO operator answers (operator unavailable), so no
provenance was upgraded to [OPERATOR]; all Stage 03 gaps remain open. Per the iron rule,
no [INFERRED]/[UNKNOWN] safety field is written here as fact — gaps are named, not asserted.

---

## Dish 1 — Pork loin cutlet set (ロースかつ定食)
- verification_rank: **C**  (largely [INFERRED]; multiple open safety gaps: breading,
  sauce, oil, meat species, sides — pre-operator-review draft)
- data_source: live

### Machine Semantics
- ingredient_ids: meat-loin(species unconfirmed) [INFERRED·high → GAP], breading(flour
  [INFERRED·high → GAP], egg [INFERRED·high → GAP], panko→wheat [INFERRED·high → GAP]),
  frying-oil [UNKNOWN → GAP], tonkatsu-sauce(soy-sauce→soy+wheat) [INFERRED·med → GAP],
  set-sides(rice/miso-soup/cabbage/pickles) [UNKNOWN → GAP]
- method_ids: deep-fry [INFERRED·high]
- allergens: **none asserted as fact.** Suspected (all GAPS, NOT facts): wheat, egg, soy
  (+ wheat) from breading/sauce [INFERRED]; sesame/peanut from oil [UNKNOWN]. → see gap register Q1,3,5,6,7
- restrictions: NOT vegetarian/vegan (meat) [INFERRED·high]; gluten-free = no
  [INFERRED·high]; no-pork/halal/kosher = UNDETERMINED until meat species confirmed (GAP Q5)
- taste_profile: savory, umami, crisp-coating texture; verbalized "rich, crisp-fried,
  savory" [INFERRED·med]
- calorie_range: range 4 of 5 (higher — fried + set) [INFERRED·low]

### Human Narrative
- story / cultural context: Tonkatsu is a yōshoku-era breaded fried cutlet. **[INFERRED]
  — NOT verified against food-culture KB this run; do not present as established fact.**
- serving notes: typically with shredded cabbage, rice, miso soup [INFERRED — sides not printed].

---

## Dish 2 — Fried prawn (エビフライ)
- verification_rank: **B**  (one allergen — crustacean — is a confirmed [MENU] fact, but
  open safety gaps remain on breading, oil, and sauce)
- data_source: live

### Machine Semantics
- ingredient_ids: shrimp/prawn→crustacean [MENU·high], breading(flour [INFERRED·high → GAP],
  egg [INFERRED·high → GAP], panko→wheat [INFERRED·high → GAP]), frying-oil [UNKNOWN → GAP],
  sauce(tartar?) [UNKNOWN → GAP]
- method_ids: deep-fry [INFERRED·high]
- allergens: **crustacean = YES [MENU·high] (FACT)** — JP/US/EU/CA/AU all mandatory.
  Suspected (GAPS, NOT facts): wheat, egg from breading [INFERRED]; sesame/peanut from oil
  [UNKNOWN]; egg/milk from tartar sauce [UNKNOWN]. → gap register Q2,4,8
- restrictions: NOT vegetarian/vegan [MENU·high]; pescatarian = yes [MENU·high];
  kosher = no (shellfish) [MENU·high]; gluten-free = no [INFERRED·high]; halal/dairy-free = UNDETERMINED (GAP)
- taste_profile: savory, sweet-shrimp, crisp; verbalized "sweet prawn, crisp coating" [INFERRED·med]
- calorie_range: range 3 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: ebi fry, a yōshoku fried-prawn staple. **[INFERRED — not KB-verified].**
- serving notes: usually with tartar sauce, lemon, or Worcester [INFERRED — sauce unconfirmed].

---

## Dish 3 — Annin dofu (杏仁豆腐)
- verification_rank: **C**  (key safety fields all [UNKNOWN]: dairy, tree-nut, gelling agent,
  soy-confirmation — pre-operator-review draft)
- data_source: live

### Machine Semantics
- ingredient_ids: gelling-agent(agar OR gelatin OR carrageenan) [UNKNOWN → GAP],
  dairy/milk [INFERRED·med → GAP], apricot-kernel/almond-flavour [UNKNOWN → GAP], sugar [INFERRED·high]
- method_ids: set/chill [INFERRED·med]
- allergens: **none asserted as fact.** Suspected (GAPS): milk [INFERRED·med];
  tree-nut/almond [UNKNOWN]. **Soy = explicitly NOT derived** — the name "豆腐/tofu" is a
  texture reference, not a soybean ingredient (confirm-no-soy is GAP Q12). → gap register Q9,10,11,12
- restrictions: vegetarian/vegan/halal/kosher/no-pork/no-beef = UNDETERMINED pending
  gelling-agent identity (GAP Q11). If gelatin: gelatin is its own token, NOT a meat allergen.
- taste_profile: sweet, milky, smooth/silky texture; "delicate, lightly sweet, silky" [INFERRED·med]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: Chinese-origin almond-kernel dessert. **[INFERRED — not KB-verified].**
- serving notes: chilled; sometimes with fruit/syrup [INFERRED].

---

## Dish 4 — Coffee jelly (コーヒーゼリー)
- verification_rank: **C**  (gelling agent and dairy topping both [UNKNOWN] — pre-operator-review draft)
- data_source: live

### Machine Semantics
- ingredient_ids: brewed-coffee [MENU·high], gelling-agent(gelatin OR agar) [UNKNOWN → GAP],
  sugar [INFERRED·high], cream/creamer/milk-topping [UNKNOWN → GAP]
- method_ids: set/chill [INFERRED·med]
- allergens: **none asserted as fact.** Suspected (GAP): milk from cream/creamer topping
  [UNKNOWN]. Gelatin (if used) is its own token, NOT a meat allergen. → gap register Q13,14
- restrictions: vegetarian/vegan/halal/kosher = UNDETERMINED pending gelling-agent identity
  (GAP Q13); dairy-free = UNDETERMINED pending topping (GAP Q14); no-alcohol = yes [INFERRED·med]
- taste_profile: bitter-sweet coffee, soft-set texture; "bittersweet coffee, soft jelly" [INFERRED·med]
- calorie_range: range 2 of 5 [INFERRED·low]

### Human Narrative
- story / cultural context: coffee jelly, popular in Japanese cafés. **[INFERRED — not KB-verified].**
- serving notes: chilled, often with cream or syrup [INFERRED — topping unconfirmed].

---

## Verification gate (run before declaring the dataset done)
- [x] No allergen/restriction field rests on [INFERRED] or [UNKNOWN] as fact — all such
      claims are routed to the gap register; only crustacean (Dish 2, [MENU]) is asserted.
- [x] Every derived allergen traces to a specific ingredient.
- [~] Canonical overrides applied — N/A this run: canonical asset files
      (product_master.json, ingredient_glossary.json, food-culture KB) were not present on
      disk, so no [CANONICAL] tag was claimed; uncertain names/narrative left [INFERRED].
- [x] Composites expanded (breading → flour/egg/panko→wheat; tonkatsu sauce → soy sauce→soy+wheat).
- [x] Machine Semantics and Human Narrative kept separate.
- [x] gelatin not filed as meat allergen; halal/pork-free kept under restrictions, not allergens.
- [x] No "varies by item" answer cascaded — moot (no operator answers received).
- [x] verification_rank assigned per dish; remaining gaps named explicitly.
- [!] **Operator exchange PENDING** (operator unavailable). Dataset ships at B/C with gaps
      named. It must NOT be used to answer diner allergy questions beyond the single
      confirmed crustacean fact until the gap register is answered.

### GO / NO-GO for turning on the concierge
**NO-GO for allergy answering.** With 14 open safety-critical gaps and only one confirmed
allergen (crustacean), the concierge cannot safely answer allergy questions about wheat,
egg, soy, milk, sesame, peanut, or tree-nut for these dishes, nor halal/vegan/gluten-free
status. The concierge may state crustacean-presence for エビフライ. Resolve the gap register
with the operator, then re-run Stage 06.

## Run summary
- Dishes: 4 | reached S/A: 0 | at B/C: 4 (1 at B, 3 at C)
- Open safety gaps still blocking: **14**   ← the number that matters most
- Confirmed allergen facts: 1 (crustacean / エビフライ, [MENU])
