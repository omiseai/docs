# Candidates — a human-review queue, NOT canonical data

When a run encounters a fact that *should* be canonical but isn't yet (no matching
entry, or the asset wasn't available), it may append a **draft** here. Candidates
are explicitly unverified. They exist so a human can later check each one against
the real source (brewery spec, glossary policy, MAFF data) and promote the good ones
into the canonical files.

## Rules

- Every candidate carries `"status": "draft-unverified"` and a `"source_run"`.
- A candidate is **never** read back as `[CANONICAL]` — not in the run that created
  it, not by a later run. Only a human promotes a candidate.
- One JSON object per line (JSONL), appended to the matching file:
  - `product_master.candidates.jsonl`
  - `ingredient_glossary.candidates.jsonl`
  - `food_culture_kb.candidates.jsonl`

## Example line (product_master candidate)

```json
{"status":"draft-unverified","source_run":"bonta-nishi-umeda/2026-06-16","name_ja":"〇〇 純米","name_en":"(proposed) Maru-maru Junmai","maker_ja":"〇〇酒造","category":"sake","needs":"verify ABV + subcategory against brewery spec"}
```

## Promotion (human, outside this skill)

1. Verify the candidate against the authoritative source.
2. Fix anything wrong (the AI draft is a starting point, not the answer).
3. Move the corrected entry into the canonical `*.json` file with a real
   `verification_rank`.
4. Delete the promoted line from the `.candidates.jsonl`.
