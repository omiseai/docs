# 05 · Operator dialogue — Lunch Menu

Records both live (in-conversation) and async answers. Each answer becomes
[OPERATOR] provenance for the relevant field.

## Status: PENDING — no operator exchange conducted this run

The restaurant operator was **explicitly unavailable** during this run. Per the run
instruction, no operator answers were invented. The clarification exchange has NOT
happened yet.

- Live exchange: none (operator not available; the standing-in user did not provide
  operator answers).
- Async register: `04_gap_register.md` has been prepared as the artifact to send to the
  operator. As of this run, **0 of 17** questions are answered. **0 of 14** safety-critical
  questions are answered.

### What this means for provenance
- No field anywhere in this dataset has been upgraded to `[OPERATOR]` / VAD.
- Every allergen and restriction that was a GAP in Stage 03 **remains a gap**.
- The only allergen carried into Stage 06 as fact is **crustacean (Dish 2)**, which rests
  on `[MENU]` and never needed the operator.

## Open after this exchange
- ALL questions Q1–Q17 remain **OPEN**.
- Next action: deliver `04_gap_register.md` to the operator; log answers here with date
  and answerer; then re-run Stage 06 to upgrade provenance and recompute verification_rank.

> Reminder for whoever resumes this: never let a "varies by item/by day" answer cascade
> to a specific dish. Record `[OPERATOR]` only when an answer pins down the specific field.
