# 02 · Decomposition — Soba shop (`soba-shop-onboarding`)

For each dish: components → ingredients (composites expanded), cooking methods,
every field provenance-tagged. Canonical assets applied where a real match exists.

**Canonical-asset lookup result for this menu:** none of the four dishes match an
entry in the seed `product_master.json` (beverages only), `ingredient_glossary.json`
(none of タイ/カニ面/バイ貝/へしこ/片栗粉/能登牛/若狭牛 appear here), or
`food_culture_kb.json` (へしこ, 柿の葉寿司 only — no soba dishes). So **no
`[CANONICAL]` tag is honestly available** for any dish here. All non-menu facts are
`[INFERRED]` or `[UNKNOWN]`; safety-relevant ones become gaps. (Candidate KB drafts
proposed at end — explicitly NOT canonical.)

---

## Dish 1 — ざるそば  (Zaru soba — chilled buckwheat noodles with dipping sauce [INFERRED·high])
- English name: Zaru soba (chilled buckwheat noodles) [INFERRED·high] — Japan-unique,
  Romaji+gloss per glossary Policy B; no glossary entry so tagged INFERRED not CANONICAL
- Components & ingredients:
  - **soba noodles** [MENU·high] → composite, expand:
    - buckwheat flour (そば粉) [INFERRED·high]  ← the defining ingredient
    - **wheat flour (つなぎ)** [INFERRED·med] ← MOST soba is 二八 (80/20 buckwheat/wheat); some shops are 十割 (100% buckwheat, no wheat). **Ratio UNKNOWN per this shop** → GAP (wheat allergen)
  - **つゆ / そばつゆ (dipping sauce)** [INFERRED·high] → composite, expand:
    - soy sauce (醤油 → soy + wheat) [INFERRED·high] → GAP confirm
    - dashi (composite → kombu + katsuobushi/bonito → fish) [INFERRED·med] → GAP
    - mirin / sugar [INFERRED·low]
  - garnish: nori (seaweed) [INFERRED·med], spring onion (negi) [INFERRED·med],
    wasabi [INFERRED·low] — typical but unconfirmed
- Cooking methods: boil (noodles), then chill/rinse [INFERRED·high]
- Canonical matches applied: none
- Notes: buckwheat is intrinsic; the live safety unknown is whether wheat is present
  in the noodle (二八 vs 十割) AND in the tsuyu's soy sauce.

---

## Dish 2 — 天ぷらそば  (Tempura soba — hot soba in broth topped with tempura [INFERRED·high])
- English name: Tempura soba [INFERRED·high]
- Components & ingredients:
  - **soba noodles** [MENU·high] → buckwheat flour [INFERRED·high] + wheat flour (つなぎ?) [INFERRED·med] → GAP (same 二八/十割 question)
  - **hot かけつゆ broth** [INFERRED·high] → composite:
    - soy sauce (→ soy + wheat) [INFERRED·high] → GAP
    - dashi (kombu + katsuobushi → fish) [INFERRED·med] → GAP
    - mirin/sugar [INFERRED·low]
  - **tempura** [MENU·high] → composite, expand:
    - batter: wheat flour (→ wheat) [INFERRED·high] → GAP confirm
    - batter: **egg** (→ egg) [INFERRED·med] ← many tempura batters contain egg; some don't → GAP
    - the fried item itself [UNKNOWN] ← shrimp (海老天, → crustacean/shrimp) is the
      default for 天ぷらそば but could be vegetable (kakiage, kabocha…) → GAP (shrimp/crustacean allergen)
    - **frying oil** [UNKNOWN] ← pure vegetable vs blend containing sesame → GAP (sesame allergen)
- Cooking methods: boil (noodles), deep-fry (tempura), simmer/heat (broth) [INFERRED·high]
- Canonical matches applied: none
- Notes: highest-allergen-density dish. Shrimp, egg, wheat, sesame all plausible and
  all unconfirmed.

---

## Dish 3 — カレーうどん  (Curry udon — wheat udon in curry broth [INFERRED·high])
- English name: Curry udon [INFERRED·high]
- Components & ingredients:
  - **udon noodles** [MENU·high] → wheat flour (→ wheat) [INFERRED·high] → GAP confirm
    (udon is wheat by definition; this is high-confidence but still owner-confirm)
  - **curry roux / curry broth** [INFERRED·high] → composite, expand (allergens hide here):
    - wheat flour (roux base → wheat) [INFERRED·high] → GAP
    - fat/oil [INFERRED·med]
    - curry spices [INFERRED·med]
    - dashi base (kombu + katsuobushi → fish) [INFERRED·med] → GAP (curry-udon broth is usually dashi-based, unlike Western curry)
    - soy sauce / soy in seasoning (→ soy + wheat) [INFERRED·med] → GAP
    - **dairy** (some roux contain milk powder → milk) [INFERRED·low] → GAP
    - **possible meat: pork or beef or chicken** [UNKNOWN] ← affects no-pork/no-beef/halal restrictions and (chicken/pork/beef) allergen tokens → GAP
  - toppings: spring onion, possibly aburaage (fried tofu → soy) [INFERRED·low]
- Cooking methods: boil (noodles), simmer (curry broth) [INFERRED·high]
- Canonical matches applied: none
- Notes: commercial curry roux is a classic hidden-allergen composite (wheat + dairy
  + sometimes beef/pork extract). Meat identity drives religious restrictions.

---

## Dish 4 — そばがき  (Sobagaki — buckwheat dumpling/porridge [INFERRED·high])
- English name: Sobagaki (buckwheat dumpling) [INFERRED·high] — Japan-unique, Romaji+gloss
- Components & ingredients:
  - **buckwheat flour (そば粉)** [INFERRED·high] → buckwheat allergen — the whole dish
  - hot water [INFERRED·high]
  - typically **NO wheat** (sobagaki is usually just buckwheat + water) [INFERRED·med]
    → but confirm no wheat tsunagi → GAP (could be wheat-free, important for the
    rare wheat-allergic-but-buckwheat-tolerant diner — and confirms whether it is a
    safer option than the noodles)
  - served with: dipping つゆ (→ soy/wheat/fish, same as Dish 1) or wasabi-soy [INFERRED·med] → GAP
- Cooking methods: mix/knead with hot water; sometimes boil [INFERRED·med]
- Canonical matches applied: none
- Notes: simplest dish; buckwheat-dominant. Main unknown is the accompanying sauce.

---

## Candidate canonical proposals (DRAFT — NOT read back as [CANONICAL] this run)
Appended to `assets/canonical/candidates/food_culture_kb.candidates.jsonl`:
- そばがき (Sobagaki) — buckwheat dumpling, candidate KB narrative for human verification
- ざるそば (Zaru soba) — candidate KB narrative for human verification
These are queued for human verification against the MAFF source before any promotion.
