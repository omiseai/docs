# 02 · Decomposition — Torihei

For each dish: components → ingredients (composites expanded), cooking methods from
the 20-method list, every field provenance-tagged. Canonical assets applied here:
the sake matched `product_master`; no food dish matched `food_culture_kb`; no menu
term required `ingredient_glossary` (all are common items with plain English names).

---

## Dish 1 — 牛すじ煮込み (Beef tendon stew)
- English name: Beef tendon stew  [INFERRED·high] (common dish; not a glossary entry, but a standard plain-English name)
- Components & ingredients:
  - beef tendon  [MENU·high]  (牛すじ = beef tendon, stated in name)
  - konnyaku  [INFERRED·med]  ← very common in this dish but not stated → gap
  - daikon  [INFERRED·low]  ← regional variant; often present → gap
  - dashi (composite → kombu [INFERRED·med], katsuobushi/bonito [INFERRED·med])  [INFERRED·med]
  - seasoning base: miso OR soy sauce OR mirin/sake  [UNKNOWN]  ← determines soy/wheat → gap
  - negi / green onion garnish  [INFERRED·low]
- Cooking methods: boil/simmer (煮込み = stewed)  [MENU·high → INFERRED·high]
- Canonical matches applied: none (food); name is standard English, not glossary-derived
- Notes: composite `dashi` expanded so hidden fish allergen is visible; seasoning
  base undetermined and is the key safety-relevant unknown (soy ± wheat).

## Dish 2 — 鶏の唐揚げ (Chicken karaage / Japanese fried chicken)
- English name: Chicken karaage (Japanese fried chicken)  [INFERRED·high] (Japan-origin term, widely known; Romaji + gloss appropriate)
- Components & ingredients:
  - chicken (thigh, typically)  [MENU·high]  (鶏 = chicken)
  - marinade: soy sauce  [INFERRED·med]  ← typical; → soy + wheat → gap
  - marinade aromatics: ginger, garlic  [INFERRED·low]
  - coating starch: potato starch (片栗粉) OR wheat flour OR a blend  [UNKNOWN]  ← determines wheat → gap
  - frying oil: vegetable oil vs blend containing sesame  [UNKNOWN]  ← determines sesame → gap
- Cooking methods: deep-fry (唐揚げ)  [MENU·high → INFERRED·high]
- Canonical matches applied: none. (Note glossary lesson: 片栗粉 = "Potato starch",
  NOT cornstarch — recorded so a confirmed coating is translated correctly.)
- Notes: two independent safety unknowns — coating (wheat) and oil (sesame). Neither
  may be asserted; both → gaps.

## Dish 3 — だし巻き卵 (Dashimaki tamago / rolled omelette)
- English name: Dashimaki tamago (rolled Japanese omelette)  [INFERRED·high]
- Components & ingredients:
  - egg  [MENU·high]  (卵 = egg, stated in name)
  - dashi (composite → kombu [INFERRED·med], katsuobushi/bonito [INFERRED·med])  [MENU·med]  (だし = dashi, stated in name)
  - seasoning: soy sauce and/or mirin, sugar, salt  [INFERRED·low]  ← soy/wheat → gap
- Cooking methods: pan-fry / rolled (a fry-category method)  [INFERRED·high]
- Canonical matches applied: none
- Notes: egg is `[MENU·high]` (named). Dashi is named (だし) so the dish definitely
  contains dashi, but the dashi *composition* (hence fish) is inferred → gap. Some
  shops use katsuo-free kombu dashi; cannot assume.

## Dish 4 — ポテトサラダ (Potato salad)
- English name: Potato salad  [INFERRED·high] (plain English name exists)
- Components & ingredients:
  - potato  [MENU·high]  (ポテト = potato)
  - mayonnaise (composite → egg yolk [INFERRED·high], vinegar, vegetable oil)  [INFERRED·high]  ← egg → gap (but high-likelihood)
  - cucumber, carrot, onion  [INFERRED·med]
  - ham OR bacon  [INFERRED·low]  ← if present → pork → affects no-pork/halal restriction → gap
- Cooking methods: boil (potato), then mix/dress (raw assembly)  [INFERRED·med]
- Canonical matches applied: none
- Notes: mayonnaise is the hidden-egg composite (classic allergen-in-composite case);
  egg is high-likelihood but still inferred → gap. Possible ham/bacon is a
  restriction-affecting unknown → gap.

## Dish 5 — 本日の刺身盛り合わせ (Today's assorted sashimi)
- English name: Today's assorted sashimi  [INFERRED·high]
- Components & ingredients:
  - assorted raw fish — specific species vary daily  [UNKNOWN]  ← which fish? → gap (also shellfish/squid possible)
  - garnish: daikon (tsuma), shiso, wasabi  [INFERRED·med]
  - served with soy sauce on the side  [INFERRED·med]  ← soy + wheat → gap
- Cooking methods: raw  [INFERRED·high]
- Canonical matches applied: none. Glossary lesson noted: if specific fish are later
  confirmed, translate carefully (タイ → Sea bream, not romanized; バイ貝 → Whelk).
- Notes: contents are inherently daily-variable. Fish allergen is certain-in-kind
  (it is sashimi) but the *specific species* and any shellfish/cephalopod/roe
  (e.g. crab, shrimp, squid, ikura) are unknown → multiple gaps. This dish cannot
  safely answer species-level allergy questions without an operator/daily input.

## Dish 6 — 黒龍 純米吟醸 (グラス) (Kokuryu Junmai Ginjo, by the glass)
- English name: **Kokuryu Junmai Ginjo**  [CANONICAL·high]
- CANONICAL MATCH: `product_master.json` → `pm_kokuryu_junmai_ginjo`
  - Full product identity agrees: name_ja "黒龍 純米吟醸" == menu "黒龍 純米吟醸". Matched
    on full identity, NOT brand substring (avoided the 龍 ⊂ 黒龍 trap).
  - maker: 黒龍酒造 / Kokuryu Sake Brewing Co.  [CANONICAL·high]
  - category: sake / junmai_ginjo  [CANONICAL·high]
  - region: Fukui  [CANONICAL·high]
  - abv: 15.5%  [CANONICAL·high]
  - allergens: [] (none)  [CANONICAL·high]
  - restrictions: contains-alcohol; no-alcohol:fail  [CANONICAL·high]
  - verified_against: brewery official spec; canonical verification_rank: S
- Components & ingredients: rice, rice koji, water (junmai = no added alcohol)  [CANONICAL·high via product_master category]
- Cooking methods: n/a (brewed beverage); serving = poured (by the glass, グラス)  [MENU·high]
- Notes: canonical override applied — the verified spec supersedes any model guess
  about ABV, allergens, or region. This is the run's one fully-verified record.
