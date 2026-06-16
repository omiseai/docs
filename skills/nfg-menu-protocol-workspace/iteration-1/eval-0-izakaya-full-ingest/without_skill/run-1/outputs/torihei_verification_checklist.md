# Torihei — Owner Verification Checklist (HITL / VAD)

The structured data is ~90% AI-generated. Per VAD, the owner must confirm the items below before the concierge presents allergen/ingredient answers as authoritative. Answers should be written back with `verification_rank: owner_verified`, which then outranks the AI guesses.

## Per-dish questions to send the owner

**1. 牛すじ煮込み (Beef tendon stew)**
- [ ] Is miso used? (affects soy/wheat allergen + flavor description)
- [ ] What is the dashi base — bonito/katsuo (→ fish allergen) or kombu only?
- [ ] Which soy sauce brand? (wheat-free tamari vs. standard wheat-containing)
- [ ] Does it include konnyaku / daikon / other vegetables?

**2. 鶏の唐揚げ (Karaage)**
- [ ] Coating: potato starch (katakuriko, wheat-free), wheat flour, or a mix?
- [ ] Any egg in the batter/marinade?
- [ ] Is the fryer shared with other items (cross-contact)?
- [ ] Chicken cut (thigh/breast)?

**3. だし巻き卵 (Dashi omelette)**
- [ ] Dashi base — bonito (→ fish) or kombu only? **(decisive for fish allergen + vegetarian status)**
- [ ] Soy sauce / wheat-free?
- [ ] Served with grated daikon or other garnish?

**4. ポテトサラダ (Potato salad)**
- [ ] Does it contain ham? (→ pork allergen + vegetarian status)
- [ ] Confirm mayonnaise (egg). Any dairy?
- [ ] Other mix-ins (corn, cucumber, carrot, onion)?

**5. 本日の刺身盛り合わせ (Today's sashimi) — HIGHEST PRIORITY**
- [ ] Set up a way to capture **today's fish list** (ideally a daily update, or instruct concierge to defer to staff).
- [ ] Typical fish rotation? (helps concierge describe the dish generally)
- [ ] Does it ever include crustaceans (shrimp) or molluscs (squid/octopus)?
- [ ] Shared knives/cutting boards (cross-contact)?

**6. 黒龍 純米吟醸 (グラス) (Kokuryu Junmai Ginjo)**
- [ ] Confirm exact product/grade label (Kokuryu has multiple junmai ginjo products).
- [ ] Provide verified brewery spec (rice variety, polishing ratio, ABV) → add to `product_master.json` so the concierge serves grounded specs and does NOT hallucinate tasting notes.

## General onboarding questions
- [ ] Any house-wide cross-contact policies (shared fryer, shared dashi pot, shared knives)?
- [ ] Are there standard substitutions on request (e.g., kombu dashi for vegetarian diners)?
- [ ] Confirm all prices are pre-tax / current.

## Process note
Until these are confirmed, the concierge should: (a) answer allergen questions with explicit uncertainty, (b) always defer to staff for the daily sashimi platter, and (c) never free-generate sake tasting notes or fixed sashimi contents. Once the owner confirms, re-rank confirmed fields to `owner_verified`.
