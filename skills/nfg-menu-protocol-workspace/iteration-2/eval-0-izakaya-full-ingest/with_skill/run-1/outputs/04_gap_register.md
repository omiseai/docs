# 04 · Gap register — Torihei

Questions for the operator, ranked safety-first. Status: OPEN / ANSWERED.
This file is itself the async artifact the operator can answer later.

## A. Safety-critical (allergen / restriction)

1. **[OPEN]** Dish 1 牛すじ煮込み — seasoning base: a) miso (→ soy), b) soy sauce
   (→ soy + wheat), c) salt/sake/mirin only (→ neither), d) other?
   *Determines soy and wheat allergen status.*
2. **[OPEN]** Dishes 1 & 3 (煮込み, だし巻き卵) — dashi type: a) katsuo (bonito)
   dashi (→ fish), b) kombu-only dashi (→ no fish), c) blended/other?
   *Determines fish allergen, and vegetarian status for だし巻き卵.*
3. **[OPEN]** Dish 2 鶏の唐揚げ — coating: a) potato starch / 片栗粉 (→ gluten-free,
   no wheat), b) wheat flour (→ wheat), c) blend? *Determines wheat / gluten-free.*
4. **[OPEN]** Dish 2 鶏の唐揚げ — frying oil: a) pure vegetable oil, b) blend
   containing sesame oil, c) other? *Determines sesame allergen.*
5. **[OPEN]** Dish 2 鶏の唐揚げ — marinade: does it contain soy sauce?
   a) yes (→ soy + wheat), b) no, c) other? *Determines soy/wheat.*
6. **[OPEN]** Dish 4 ポテトサラダ — does it contain mayonnaise / egg?
   a) yes (→ egg), b) egg-free dressing? *Determines egg allergen.*
7. **[OPEN]** Dish 4 ポテトサラダ — does it contain ham or bacon?
   a) yes (→ pork), b) no? *Determines no-pork / halal / vegetarian.*
8. **[OPEN]** Dish 5 本日の刺身盛り合わせ — because contents change daily, what is the
   process for telling diners today's species and any shellfish/squid/roe present?
   a) staff confirm verbally, b) a daily list could feed the concierge, c) other?
   *Determines whether the concierge can answer species-level allergy questions at all
   (fish/crab/shrimp/squid/abalone/salmon-roe).*
9. **[OPEN]** Cross-dish — is the fryer used for 唐揚げ shared with any pork/wheat items
   (cross-contact)? *Affects no-pork and trace-wheat answers for fried dishes.*
10. **[OPEN]** Halal/no-pork posture of the kitchen overall (cooking alcohol/mirin,
    shared utensils)? *Affects halal status across dishes 1, 2, 5.*

## B. Ingredient identity
11. **[OPEN]** Dish 1 — is konnyaku actually used? Any daikon? *(non-safety, but
    improves accuracy)*
12. **[OPEN]** Dish 2 — chicken cut (thigh vs breast)? *(narrative only)*
13. **[OPEN]** Dish 4 — typical vegetables (cucumber/carrot/onion)? *(narrative)*

## C. Narrative / cultural
14. **[OPEN]** None of dishes 1–5 matched the food-culture KB, so any cultural/origin
    narrative would be `[INFERRED]`. Confirm whether the owner wants a verified
    regional-origin story added (and the correct region) before we present one — we
    will not generate an authoritative history unverified.

## Verified — no gap
- Dish 6 黒龍 純米吟醸 — fully matched to product_master (Kokuryu Junmai Ginjo, Fukui,
  15.5% ABV, no allergens). No questions.
