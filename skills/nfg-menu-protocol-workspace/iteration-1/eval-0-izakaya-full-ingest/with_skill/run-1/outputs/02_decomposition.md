# 02 · Decomposition — Torihei (鳥平), Osaka izakaya

For each dish: components → ingredients (composites expanded), cooking methods from
the 20-method master, every field provenance-tagged. The source gave names + prices
only, so almost all ingredient content here is `[INFERRED]` from culinary norms or
`[UNKNOWN]` — flagged for the operator, never asserted.

Glossary boundary rule (Policy B): plain English when one exists; Romaji + gloss
only for Japan-unique items.

---

## Dish 1 — 牛すじ煮込み (Beef tendon stew [glossary·high])
- English name: Beef tendon stew  [CANONICAL·high] (ingredient_glossary — plain English exists)
- Components & ingredients:
  - beef tendon  [MENU·high]  (dish name names it directly)
  - konnyaku  [INFERRED·med]  ← very common in this dish but not stated → gap
  - dashi (composite → kombu + katsuobushi/bonito)  [INFERRED·med]  ← base stock assumed; composition unconfirmed → gap
  - seasoning base: miso OR soy sauce OR mirin blend  [UNKNOWN]  ← which? determines soy/wheat → gap
  - green onion / negi (garnish)  [INFERRED·low]
- Cooking methods: simmer/boil (煮込み = simmered)  [MENU·high]  (the name states the method)
- Canonical matches applied: glossary for English name. No product_master (food, not beverage).
- Notes: composite `dashi` expanded so hidden fish/kombu allergens are visible. Seasoning base is the key safety-affecting unknown.

## Dish 2 — 鶏の唐揚げ (Japanese fried chicken / karaage [glossary·high])
- English name: Japanese fried chicken (karaage)  [CANONICAL·high] (Japan-unique prep; Romaji + gloss appropriate)
- Components & ingredients:
  - chicken (typically thigh)  [MENU·high]  (鶏 = chicken)
  - marinade: soy sauce  [INFERRED·med]  ← standard karaage marinade → soy/wheat gap
  - marinade: garlic, ginger, sake  [INFERRED·low]
  - coating: potato starch and/or wheat flour  [UNKNOWN]  ← katakuriko vs komeko vs wheat? determines wheat → gap
  - frying oil: type unknown  [UNKNOWN]  ← could be blend containing sesame → sesame gap
- Cooking methods: deep-fry (唐揚げ = deep-fried)  [MENU·high]
- Canonical matches applied: glossary for name.
- Notes: two safety-critical unknowns — coating (wheat) and frying oil (sesame/cross-contamination). Marinade soy is the typical norm but unconfirmed.

## Dish 3 — だし巻き卵 (Rolled dashi omelette / dashimaki tamago [glossary·high])
- English name: Rolled dashi omelette (dashimaki tamago)  [CANONICAL·high] (Japan-unique; Romaji + gloss)
- Components & ingredients:
  - egg  [MENU·high]  (卵 = egg)
  - dashi (composite → kombu + katsuobushi/bonito)  [MENU·high → composition INFERRED·med]  (だし named; species inside it inferred → fish gap)
  - seasoning: soy sauce and/or mirin, salt, sugar  [INFERRED·med]  ← soy/wheat gap
  - cooking oil for the pan  [INFERRED·low]  ← type unknown → minor oil gap
- Cooking methods: pan-fry / rolled (焼く category)  [MENU·high]
- Canonical matches applied: glossary for name.
- Notes: egg is certain ([MENU]). Dashi is named on the dish but its fish content (katsuobushi) is inferred → fish allergen is a gap. Light seasoning soy unconfirmed.

## Dish 4 — ポテトサラダ (Potato salad [glossary·high])
- English name: Potato salad  [CANONICAL·high] (plain English exists)
- Components & ingredients:
  - potato  [MENU·high]
  - mayonnaise (composite → egg yolk + vegetable oil + vinegar)  [INFERRED·high]  ← standard binder; expands to egg → egg gap
  - cucumber, carrot, onion  [INFERRED·med]
  - ham OR bacon  [INFERRED·low]  ← common but not universal; if pork, affects no-pork/halal → gap
  - black pepper, salt  [INFERRED·low]
- Cooking methods: boil (potato), raw (vegetables), mix/dress (no exact method token — closest: boil + raw)  [INFERRED·med]
- Canonical matches applied: glossary for name.
- Notes: mayonnaise composite expanded → egg is the hidden allergen here. Possible pork (ham/bacon) is both an allergen-adjacent and a restriction (no-pork/halal) unknown.

## Dish 5 — 本日の刺身盛り合わせ (Today's assorted sashimi [glossary·high])
- English name: Today's assorted sashimi  [CANONICAL·high] (plain English exists)
- Components & ingredients:
  - assorted raw fish — **specific species UNKNOWN, rotates daily**  [UNKNOWN]  ← cannot enumerate; each species may carry its own allergen (e.g. mackerel/サバ, salmon roe/いくら, abalone/あわび, shrimp/海老 garnish) → gap
  - garnish: daikon (tsuma), shiso, wasabi  [INFERRED·med]
  - served with soy sauce on the side  [INFERRED·med]  ← soy/wheat gap (dip)
- Cooking methods: raw (刺身)  [MENU·high]
- Canonical matches applied: glossary for name.
- Notes: this is a **daily-variable** dish. The fish identity drives the entire allergen picture and is structurally unknowable from a static record — it must be answered per-service by the operator, not inferred. Highest-risk dish in the set.

## Dish 6 — 黒龍 純米吟醸 (グラス) (Kokuryū Junmai Ginjo, by the glass [product_master·high])
- English name: Kokuryū Junmai Ginjō (sake), by the glass  [CANONICAL·high]
- product_master match: matched on **full product identity** 黒龍 純米吟醸 (Kokuryu Sake Brewery, Fukui). NOT matched by 龍 substring — brand-name substring matching is forbidden (龍 ⊂ 黒龍 cross-contamination rule). Junmai Ginjō grade = rice + water + koji + yeast, no added distilled alcohol.
- Components & ingredients:
  - rice (sakamai)  [CANONICAL·high]
  - water  [CANONICAL·high]
  - koji (Aspergillus oryzae)  [CANONICAL·high]
  - yeast  [CANONICAL·high]
  - (no brewer's alcohol — junmai)  [CANONICAL·high]
- Cooking methods: brewed/fermented (no food cooking-method token applies; beverage)  [CANONICAL·high]
- Canonical matches applied: product_master for the full spec.
- Notes: a verified product_master entry, so its spec overrides any inference. Sake allergen note: contains alcohol (restriction: no-alcohol = fails); JP allergen list does not flag rice. Some jurisdictions track sulphites in beverages — but sake is generally not added-sulphite; left as a low-priority confirm, not asserted.
