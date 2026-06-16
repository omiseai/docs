#!/usr/bin/env python3
import json, re, os, glob, sys

ITER = os.path.join(os.path.dirname(__file__), sys.argv[1] if len(sys.argv) > 1 else "iteration-1")

EVALS = {
    "eval-0-izakaya-full-ingest": "izakaya-full-ingest",
    "eval-1-allergy-trap-verify": "allergy-trap-verify",
    "eval-2-gap-finding-soba": "gap-finding-soba",
}

TAGS = ["[MENU]", "[OPERATOR]", "[CANONICAL]", "[INFERRED]", "[UNKNOWN]"]

def load_text(outdir):
    texts = {}
    for p in sorted(glob.glob(os.path.join(outdir, "*.md"))):
        with open(p, encoding="utf-8") as f:
            texts[os.path.basename(p)] = f.read()
    return texts

def snippet(text, pat, flags=re.I):
    m = re.search(pat, text, flags)
    if not m:
        return None
    s = max(0, m.start() - 40)
    e = min(len(text), m.end() + 40)
    return "…" + text[s:e].replace("\n", " ") + "…"

def grade_run(outdir, eval_key):
    texts = load_text(outdir)
    allcat = "\n".join(texts.values())
    files = set(texts.keys())
    exp = []

    # A1: explicit provenance tags separating observed from inferred
    tags_found = [t for t in TAGS if t in allcat]
    exp.append({
        "text": "Separates observed facts from inferences using explicit provenance tags",
        "passed": len(tags_found) >= 3,
        "evidence": f"tags present: {tags_found}" if tags_found else "no provenance tags found",
    })

    # A2: safety-ranked gap register / operator questions
    has_gap = bool(re.search(r"gap register|owner.{0,3}question|questions? for the operator|safety[- ]critical|must (?:confirm|ask)", allcat, re.I))
    safety_first = bool(re.search(r"safety[- ]?(critical|first)|highest risk|## ?A\.|critical allergen", allcat, re.I))
    exp.append({
        "text": "Produces a gap register / operator questions ranked safety-first",
        "passed": has_gap and safety_first,
        "evidence": (snippet(allcat, r"safety[- ]?(critical|first)|highest risk|critical allergen") or
                     ("has questions but no explicit safety ranking" if has_gap else "no gap/questions content")),
    })

    # A3: no allergen asserted as fact from inferred/unknown basis (routes uncertainty to gaps)
    routes = bool(re.search(r"(gap|not asserted|leave[ds]? open|pending|do not (?:assert|state)|flagged, not asserted|→ ?GAP)", allcat, re.I))
    # negative signal: declaring a dish allergen-free as a VERIFIED fact.
    # The real failure is an allergen-free claim carrying a high-trust provenance
    # with no hedge — i.e. presented as fact. Gap-question options ("b) wheat-free
    # coating"), restriction-derivation prose ("→ milk allergen + dairy-free"), and
    # anything tagged [INFERRED]/[UNKNOWN] are NOT failures.
    FREE = re.compile(r"(peanut|sesame|wheat|soy|egg|dairy|milk)[- ]free", re.I)
    CONFIRM = re.compile(r"\[OPERATOR|\[CANONICAL|\[MENU|confirmed|verified|✔", re.I)
    HEDGE = re.compile(r"gap|question|\?|\[INFERRED|\[UNKNOWN|→|[abc]\)|determines|likely|assume|if |whether", re.I)
    bad = any(FREE.search(ln) and CONFIRM.search(ln) and not HEDGE.search(ln)
              for ln in allcat.splitlines())
    exp.append({
        "text": "Routes uncertain allergen status to gaps rather than asserting it as fact",
        "passed": routes and not bad,
        "evidence": (snippet(allcat, r"→ ?GAP|flagged, not asserted|not asserted|leave[ds]? open") or
                     ("uncertainty-routing language present" if routes else "no uncertainty-routing language")) +
                    (" | WARNING: unconfirmed allergen-free claim found" if bad else ""),
    })

    # A4: per-record confidence / verification grade
    has_rank = bool(re.search(r"verification[_ ]?rank|rank[:\s]*[SABC]\b|\b[SABC] ?[-–] |grade", allcat, re.I))
    exp.append({
        "text": "Assigns a per-record verification grade (S/A/B/C or confidence)",
        "passed": has_rank,
        "evidence": snippet(allcat, r"verification[_ ]?rank|rank[:\s]*[SABC]\b") or "no verification grade found",
    })

    # A5: composite ingredient expansion
    comp = bool(re.search(r"composite|dashi.{0,6}(→|->|:).{0,3}(kombu|katsuobushi|bonito)|roux.{0,30}(flour|wheat|dairy)|batter.{0,20}(egg|wheat)|mayonnaise.{0,6}(→|->).{0,4}egg|expand", allcat, re.I))
    exp.append({
        "text": "Expands composite ingredients (dashi, roux, batter, mayo) so hidden allergens surface",
        "passed": comp,
        "evidence": snippet(allcat, r"composite|dashi.{0,10}(kombu|katsuobushi|bonito)|roux|batter|mayonnaise") or "no composite expansion found",
    })

    # A6: Stage 07 operator sign-off sheet foregrounding inferred items
    has07 = "07_operator_review.md" in files or bool(re.search(r"operator review|sign-?off|確認シート|要確認|ご確認", allcat, re.I))
    foregrounds = bool(re.search(r"我々の推測|要確認|please confirm|✔|✖|confirm or correct|assumption", allcat, re.I))
    exp.append({
        "text": "Produces a Stage 07 operator sign-off sheet that foregrounds inferred items for confirmation",
        "passed": has07 and foregrounds,
        "evidence": (snippet(allcat, r"確認シート|我々の推測|operator review|sign-?off") or
                     ("sheet present but inferred items not clearly foregrounded" if has07 else "no operator sign-off sheet found")),
    })

    # eval-specific
    if eval_key == "eval-0-izakaya-full-ingest":
        sake = bool(re.search(r"黒龍", allcat)) and bool(re.search(r"substring|full identity|龍|product_master|canonical", allcat, re.I))
        exp.append({
            "text": "Handles the sake (黒龍) via canonical matching and avoids the 龍-substring brand error",
            "passed": sake,
            "evidence": snippet(allcat, r"substring|full identity|黒龍.{0,40}canonical|product_master") or "no canonical/substring handling for sake",
        })
        daily = bool(re.search(r"本日の|today'?s|varies (?:daily|by day)|daily[- ]rotating|per service", allcat, re.I))
        exp.append({
            "text": "Flags the daily-rotating sashimi (本日の) as not having a fixed allergen profile",
            "passed": daily,
            "evidence": snippet(allcat, r"本日の|daily[- ]rotating|varies (?:daily|by day)|per service") or "daily-variation not flagged",
        })
    elif eval_key == "eval-1-allergy-trap-verify":
        gel = bool(re.search(r"gelatin", allcat, re.I)) and bool(re.search(r"gelatin.{0,60}(not|own token|isn'?t).{0,20}(meat|beef|pork)|not (?:a )?meat allergen", allcat, re.I))
        exp.append({
            "text": "Keeps gelatin as its own token, not a meat allergen (dessert mis-tag pitfall)",
            "passed": gel,
            "evidence": snippet(allcat, r"gelatin.{0,80}(not|own token).{0,20}(meat|beef|pork)") or "gelatin/meat distinction not made explicit",
        })
        annin = bool(re.search(r"杏仁|annin", allcat, re.I)) and bool(re.search(r"(豆腐|tofu).{0,80}(not|no).{0,10}soy|soy.{0,40}(not|texture reference|misleading)", allcat, re.I))
        exp.append({
            "text": "Does not auto-derive soy from 豆腐 in 杏仁豆腐 (naming trap)",
            "passed": annin,
            "evidence": snippet(allcat, r"(豆腐|tofu).{0,80}(not|no).{0,10}soy|杏仁.{0,80}soy") or "annin-tofu soy trap not addressed",
        })
    elif eval_key == "eval-2-gap-finding-soba":
        buck = bool(re.search(r"buckwheat", allcat, re.I)) and bool(re.search(r"(十割|juwari|二八|ratio|blend|% ?buckwheat|wheat[- ]free)", allcat, re.I))
        exp.append({
            "text": "Identifies the soba buckwheat/wheat ratio as a top safety gap",
            "passed": buck,
            "evidence": snippet(allcat, r"(十割|juwari|二八|buckwheat.{0,30}(ratio|blend|wheat))") or "buckwheat/wheat ratio gap not identified",
        })
        curry = bool(re.search(r"(curry|カレー).{0,40}roux|roux.{0,40}(wheat|dairy|milk)", allcat, re.I))
        exp.append({
            "text": "Flags curry-udon roux as a hidden-allergen composite (wheat/dairy)",
            "passed": curry,
            "evidence": snippet(allcat, r"(curry|カレー|roux).{0,40}(wheat|dairy|milk|flour)") or "curry roux composite not flagged",
        })

    passed = sum(1 for e in exp if e["passed"])
    return {"expectations": exp, "passed": passed, "total": len(exp)}

for ekey in EVALS:
    for cond in ("with_skill", "without_skill"):
        cond_dir = os.path.join(ITER, ekey, cond)
        if not os.path.isdir(cond_dir):
            continue
        # support both cond/outputs and cond/run-1/outputs layouts
        for outdir, gdir in [
            (os.path.join(cond_dir, "run-1", "outputs"), os.path.join(cond_dir, "run-1")),
            (os.path.join(cond_dir, "outputs"), cond_dir),
        ]:
            if os.path.isdir(outdir):
                result = grade_run(outdir, ekey)
                with open(os.path.join(gdir, "grading.json"), "w", encoding="utf-8") as f:
                    json.dump(result, f, ensure_ascii=False, indent=2)
                print(f"{ekey}/{cond}: {result['passed']}/{result['total']}")
                break
