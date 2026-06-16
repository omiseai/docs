# 05 · Operator dialogue — Soba shop

Records both live (in-conversation) and async answers. Each answer becomes
`[OPERATOR]` provenance for the relevant field.

## Status: PENDING — no operator exchange has occurred

The restaurant operator was **not available** during this run, and no stand-in was
authorized to answer on their behalf. Per protocol, operator answers must not be
invented: when the operator is absent, gaps stay OPEN and provenance stays at
`[INFERRED]`/`[UNKNOWN]`. No field has been upgraded to `[OPERATOR]`.

- Live exchange: not conducted (no operator / stand-in present).
- Async register: `04_gap_register.md` is the artifact to send the operator. All 16
  questions (12 safety-critical) remain OPEN awaiting their reply.

## Open after this exchange
- Q1–Q16: all OPEN.
- Safety-critical Q1–Q12: all OPEN.

## When answers arrive (instructions for the next run)
- Log each answer here with date, channel, and answering person/role.
- Only mark a field `[OPERATOR]` when the answer pins down that **specific** field.
- Do **not** cascade a "varies by item/batch/store" answer to specific dishes — e.g.
  if the noodle ratio "varies by batch," the wheat-allergen gap stays OPEN per dish.
- After logging, regenerate Stage 06 and recompute `verification_rank` per dish.
