# 02 · Decomposition — Lunch Menu

For each dish: components → ingredients (expand composites), cooking methods,
every field provenance-tagged. Canonical assets unavailable on disk this run, so
"glossary"/"KB" names below are documented-knowledge matches and are tagged
[INFERRED] where I am not certain a verified canonical entry exists.

---

## Dish 1 — ロースかつ定食 (Pork loin cutlet set meal)
- English name: Pork loin cutlet set (tonkatsu set)  [INFERRED·high]
  - "ロース" = loin cut; "かつ" (katsu) = breaded deep-fried cutlet; "定食" = set meal.
  - Common plain-English term exists ("pork cutlet") → Policy B: use English, not Romaji.
- Components & ingredients:
  - **pork loin**  [MENU·high]  (ロース = loin; meat type pork is standard for とんかつ
    but the printed name does not actually say "豚/pork" → see note) 
    - NOTE: ロースかつ is overwhelmingly pork by convention, but ロース can also be
      chicken/beef loin. Meat species not printed → treat species as [INFERRED·high], flag.
  - **breading / panko coating** (composite → wheat flour + egg wash + panko breadcrumbs[→wheat])  [INFERRED·high]
    - flour  [INFERRED·high]
    - egg (batter/wash)  [INFERRED·high]
    - panko breadcrumbs → wheat  [INFERRED·high]
  - **frying oil**  [UNKNOWN]  ← type undisclosed (could be vegetable blend, or contain
    sesame / peanut / animal fat) → gap
  - **tonkatsu sauce** (composite, typically → vegetables, fruit, vinegar, sugar, soy sauce[→soy+wheat], spices)  [INFERRED·med]
    - soy sauce → soy + wheat  [INFERRED·med]
    - whether sauce is served / which sauce  [UNKNOWN] → gap
  - Set-meal accompaniments (rice, miso soup, shredded cabbage, pickles)  [UNKNOWN]
    - NOT printed; conventional only. miso soup would add soy + likely dashi(fish). → gap
- Cooking methods: deep-fry (from the 20-method list)  [INFERRED·high]
- Canonical matches applied: none confirmed (assets not on disk). "Tonkatsu" cultural
  narrative would need food-culture KB verification → narrative is [INFERRED], flagged.
- Notes: classic hidden-allergen dish — wheat/egg/soy all enter via breading + sauce,
  none of which is printed. Frying oil and sauce undisclosed.

---

## Dish 2 — エビフライ (Fried prawn / breaded fried shrimp)
- English name: Fried prawn (ebi fry)  [INFERRED·high]  (plain English "fried shrimp/prawn" exists → Policy B)
- Components & ingredients:
  - **shrimp / prawn (エビ)** → crustacean  [MENU·high]
  - **breading / panko coating** (composite → wheat flour + egg wash + panko[→wheat])  [INFERRED·high]
    - flour  [INFERRED·high]
    - egg (batter/wash)  [INFERRED·high]
    - panko breadcrumbs → wheat  [INFERRED·high]
  - **frying oil**  [UNKNOWN]  ← type undisclosed → gap
  - **accompanying sauce** (tartar sauce → egg + dairy? / Worcester sauce / lemon)  [UNKNOWN] → gap
- Cooking methods: deep-fry  [INFERRED·high]
- Canonical matches applied: none.
- Notes: crustacean is the one HIGH-confidence allergen (from the printed name itself).
  Breading wheat/egg are inferred; oil + sauce undisclosed. Tartar sauce, if served,
  is a hidden egg/dairy source.

---

## Dish 3 — 杏仁豆腐 (Annin dofu / almond-kernel jelly)
- English name: Annin dofu (apricot-kernel jelly / "almond tofu")  [INFERRED·high]
  - TRAP 1: "豆腐 (tofu)" in the NAME does NOT mean it contains soybean tofu. 杏仁豆腐 is
    a sweet jelly named for its tofu-like texture. Do NOT auto-derive soy from the word.
  - TRAP 2: "杏仁" = kyōnin = APRICOT KERNEL, not tree-nut almond. Modern recipes very
    commonly substitute almond essence and/or use actual almond → possible tree-nut. This
    is genuinely undetermined per recipe.
- Components & ingredients:
  - **gelling agent** — agar (kanten) OR gelatin OR carrageenan  [UNKNOWN]  ← determines
    gelatin token + vegan status → gap
  - **milk / dairy** (most common recipes use milk or evaporated milk)  [INFERRED·med]
    ← determines milk allergen → gap (could be water/coconut-based instead)
  - **apricot-kernel flavour (杏仁/kyōnin) OR almond essence OR actual almond**  [UNKNOWN]
    ← determines tree-nut (almond) allergen → gap
  - **sugar**  [INFERRED·high]
- Cooking methods: (none/raw-set; "boil" to dissolve gelling agent) → set/chill  [INFERRED·med]
- Canonical matches applied: none confirmed.
- Notes: DESSERT — guard against the dessert-mistagged-with-meat class of error. Do NOT
  attach beef/pork. The only meat-adjacent token possible is GELATIN, which is its own
  token and is NOT a meat allergen (see Stage 03). Soy is NOT implied by the name.

---

## Dish 4 — コーヒーゼリー (Coffee jelly)
- English name: Coffee jelly  [INFERRED·high]  (plain English exists → Policy B)
- Components & ingredients:
  - **brewed coffee**  [MENU·high]  (from name)
  - **gelling agent** — gelatin OR agar (kanten)  [UNKNOWN]  ← TRAP: "ゼリー/jelly" is
    most often gelatin in Japan but agar versions exist → determines gelatin token +
    vegan status → gap
  - **sugar**  [INFERRED·high]
  - **cream / coffee creamer / milk topping**  [UNKNOWN]  ← commonly served with cream
    or a creamer; determines milk allergen → gap
  - **garnish (e.g. condensed milk, syrup)**  [UNKNOWN] → gap
- Cooking methods: set/chill  [INFERRED·med]
- Canonical matches applied: none.
- Notes: DESSERT — gelatin is the key token and is NOT a meat allergen. Dairy enters only
  via an undisclosed cream/creamer topping. Do NOT assert milk as fact.
