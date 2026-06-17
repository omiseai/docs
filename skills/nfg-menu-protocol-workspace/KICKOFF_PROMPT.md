# Kickoff prompt for the next session

Paste the block below to resume work on the NFG menu-protocol skill.

---

I'm continuing work on the **NFG menu-protocol skill** (OmiseAI's core menu→verified-data
process). A previous session built and eval-tested it; everything is stashed in this repo.

Before doing anything, please read, in order:
1. `skills/nfg-menu-protocol-workspace/HANDOFF.md` — full state, decisions, file map, next steps
2. `skills/nfg-menu-protocol/SKILL.md` — the protocol itself
3. `skills/nfg-menu-protocol/NFG_SUMMARY.md` — the NFG product/data-model spec
4. `skills/nfg-menu-protocol/references/` and `assets/canonical/` — supporting detail

Context in one line: the skill turns a restaurant menu into a verified NFG dataset via a
numbered, provenance-tagged pipeline (stages 01–07) whose hard rule is that no inferred or
unknown allergen claim is ever asserted as fact — it becomes an operator gap question, and
stage 07 is the Japanese operator sign-off where VAD is earned. Two eval iterations passed
(iteration-2: 8/8 with-skill on all 3 tests, with stage 07 + canonical assets).

We're using the **skill-creator** workflow (draft → eval → review → iterate → package).

Apply this feedback from my colleague's review and re-run the evals. It's in `iteration-2/review_ja.html`.

What I want to do this session:
[TELL CLAUDE WHAT YOU WANT — e.g. one of:]
- "Apply this feedback from my colleague's review and re-run the evals." (attach/paste the
  `feedback.json` downloaded from `iteration-2/review_ja.html`, or describe the changes)
- "Make these specific changes to SKILL.md: …"
- "Package the skill as an installable .skill file."
- "Add a new test case for <cuisine/edge case> and run it."

Please confirm you've loaded the context and give me a 3–4 line summary of the current
skill state before we change anything.
