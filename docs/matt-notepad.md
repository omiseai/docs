---
title: "Matt-notepad"
---

- look into existing code
- Go through Claude session about how to construct the prototype, working backwards
- after come up with a design, circle back to the previous two implementations (skill one and python one), see what concepts can be utilized from that



- carefully read through DESIGN.md

- work backwards with Claude from the menu to build a one-off version of NFG
    - Python runtime pipeline
        - build a schema from `menu_ingest.json`
        - build a python script that uses `claude -p` to ingest a menu and output conforming menu data
        - know that I already have the fixture menu to use
        - make two new schema -- one for pre-interviews and one for ingredient cluster interviews
        - new python script w/ `claude -p` takes conforming menu output as context and special prompt, outputs the JSON representing both the pre-interviews and ingredient cluster interviews appropriate for that particular menu
        - make an orchestrator python script that calls the first script
        - new python script w/ `claude -p` converts the JSON from prev step into two encapulated HTML apps that both save JSON locally
        - new python script w/ `claude -p` optionally directly makes sample JSON results data for testing
        - new schema for menu items ingredient decomposition
        - new python script w/ `claude -p` -- takes in menu JSON as context, and the pre-interviews and ingredient cluster interviews JSON outputs, creates conforming ingredient decomposition with ingredients inference based on the pre-interviews and ingredient cluster data
        - new python script w/ `claude -p` -- takes in ingredient decomposition JSON and `japan_allergens.json` and applies allergen tags to conforming ingredient decomposition data
        - new schema for dish-by-dish questionnaire
        - new python script w/ `claude -p` -- takes in ingredient decomposition data and makes schema conforming questions based on anything that is low confidence (so hopefully most dishes don't need clarification)
        - new python script w/ `claude -p` -- creates encapsualted HTML app for dish-by-dish questionnaire based on questions output data. Outputs JSON with results
        - new python script w/ `claude -p` with loop -- ingest questionnaire results, update appended ingredient decomposition data, repeat if any incomplete instances still exist, stop if not
        - new python script w/ `claude -p` -- converts ingredient final/complete decomposition data into a presentable final HTML encapsulated app for restaurant operator to fill out and sign off on
            - sign off on this via button outputs a record
    - Claude analog
        - look at menu data, look at my prompt sent to Claude from a prev session and the DESIGN.md doc Claude made based on that. Need to build the pre-interview and ingredient cluster questions
        - simulate answers to the questions
        - look at menu data, question answers from prev step, `japan_allergens.json`, and make questions for any dish that is unclear that it has allergens
        - look at results, make more questions if needed and repeat
        - make a final ingredient output with allergen tags for operator checking
        

- later dig around in prev attempts with Claude to find certain conventions that may be useful, like "[INFERRED]" and so on

















I need your expert help designing a prototype of NFG. Please do not be overly verbose in how you approach our discussion, tho you should definitely be thorough and deliberate.  There are actually a   couple folders in the root of this repo that represent two previous   attempts. They did not turn out well. This time I want to work from the   ground up. I'd like to continue our principle of instrumentation and evals being weaved into what be build. The goal is to arrive at a prototype that achieves our objectives and can serve as a reference for an implementation.

Don't look through our previous attemps just yet. I want to work through the idea in an unbiased way, tho later we may dig into them.

Let's start with one of the major pain points from our previous attempts, which was to consider that a menu may over a hundred items. And working through them one-by-one is not viable. Imagine you are the restaurant operator and we give you a questionnaire that ask you about the oil you use for a great number of your dishes. That would be a burden that most operators would be unwilling to bear. Yet at the same time we need to arrive at VAD (Verified Authentic Data) since one major component of NFG is to identify possible allergens. So my idea is that we can approach the matter uniquely for each restaurant.

The first step would be to ingest the restaurant menu and identify a set of pre-interviews taht we would conduct. For example, one pre-interview in the set may be about oils, asking questions that bucket oil use into things like "oil used for deep frying", "oil used when searing meats" and so on. Others may be related to sauces and dressing but specific to Japanese food restaurants. So in such a case the pre-interview might ask what dashi a restaurant uses. Note, that a pre-interview for Japanese restaurants that asks about things like dashi would be irrelevant to a French restaurant. So by default we would not ask a French restaurant operator to complete such a pre-interview, however if they did some fusion type of dish we would allow them at some point in the process to note that they use dashi and in what dish.

So let's say we went through a number of pre-interviews that were drawn from a set of pre-interviews he menu we ingested. We would be left with a poollow us to moreconfidently connect the dots between that information and the items on the    menu, so we don't have t. For example, if arestaurant has both Karaage and Aji fry, then and earlier asked the restaurant about the oilen we would have a highconfidence in our inference that both dishes use that oil. Later, once we are done with the whole procdings to the operatorand give them the opportunity to correct us (they would sign off on it all awell).
                                                                        I'm trying to think of aht utilize that wouldboth reduce the question load on restaurant operators and give us a high    confidence in the informto think superhard about all of this and tell me your thoughts. For example, there may likely be a   clustering of certain dints. An Italianrestaurant may utilize the same pasta noodles for a number of their spaghettdishes. I'm thinking anore any dish-by-dishquestions may be to identify any ingredient clusters like that. So for      example, we could enumerrom the menu we believelikely use the same noodles and ask a single question to the operator about that. Then, if there is at uses those noodles,we know already know about a possible wheat allergen, and most importantly, if it's a simple pasta dredients, we can omit it from the dish-by-dish question set alltogether. At the end, we would still  present our high confideo the restaurantoperator, but at least they would face less questions during our NFG process
                                                                        So I guess the two ways large number ofdish-by-dish questions to the operator are:                                 
1) pre-interviews (ex. "tell us about your oils")
2) ingredient cluster inour menu and it seemslikely you use the same noodles for dishes X, Y and Z")                     

The idea would be to shed questions that we need to ask dish-by-dish.       
Ultimately we need two deliverables from this process. One would be an      ingredient breakdown of tor to sign off on. That may have been an interative process, for example moving through various     pre-interviews and ingre then what is hopefullya small set of dish-by-dish questions. We would want the operator to sign ofon it, or if they have che ingredient breakdown for them to sign off on. The second would be a data model-conforming data   set specific to that resuld be our context for a restaurant patron chat with the OmiseAI system, so if they ask questions    about dishes, and a dishwith norms for a certain recipe and contains allergens for example, our chat agent would *not*       hallucinate and would gi keeping them safe.

Ok, that was a lot. I nepert insights here,think superhard, research whatever you need to research on the web in order to formulate your ideas.e you do your absolute best.








- needs
    -x able to select model when running the pythong script, ex. to use Haiku
    -x make sure there is an output that could be used as context for a chat session
    -x get some running statuses to be printed
    -x Help me think this through -- `06_nfg_output.md` is what I ultimately want to pass to a chat app as context, but it's not until `07_operator_review.md` that we get the operator to provide feedback and possibly correct some inaccuracies of our system, right? And if that's the case, don't we need first gather the feedback from the operator and then fix our assessment? Possibly, should there be a loop, where it's only until we've received complete/satisfactory answers that we can continue? And once we have, then our output would be the verified authentica data we're looking for?
    - maybe we should have it so the operator can throw any flags he wants about a given dish, so we basically show our assumptions and let them correct us

    - bug in generated HTML survey -- all buttons get selected

    - verbose logs are hard to parse, can the ones I really should know about be made more clear/obvious?
    - get a full run through, look at outputs
    - read through everything
    - this seems funky, how 07 then back to 06? -- **Stage 07** — the operator review sheet is built; an optional `07_operator_signoff.json` finalizes Stage 06.



- we shouldn't be promoting canonical stuff. They should all be pre-defined




- really the flow should be
    - build the skill fully, test live
    - before implementing, check the live algo to see what could be adopted, or maybe do this ahead of time


- want Evals to all be HTML surveys that user takes and then we save the JSON to local disk, then continue


- emitted by instrumentation
    - ledger.jsonl (every factual claim + provenance)
    - burden.json (question counts)
    - gate.json (safety enforcement)
    - scorecard.md (human-readable summary)

- important features
    - instrumentation: records timing, counts, decisions, errors

- burden
- ledger

- allergens master
- ingredients -> allergens


- should have two versions of the SKILL.md
    - Claude only version
    - Claude forked version using the context from Shingo

- should we have the skill create questions and report results in a standardized way?


1) operator burden — how many questions, how hard to answer — and (2) safety/auditability — did any unverified allergen claim slip through


start with this one:

https://bonta.co.jp/kurufu/menu/dinner/


- what from the handoff prompt should instead now just be included in the skill itself, so invoking the skill with a URL or attached PDF will let it just go do its thing?


- building evals for question quality
    - make sure agent also updates nested AGENTS.md




- a skill
- running it produces HTML assets
    - A questions survey for the operator (step 5)
        - should always be the same HTML format
    - after the process, evals for the operator survey (including their questions)
    - 

- what is instrumentation? What is it in the context of what we're doing here?

- are we deriving the allergens from an existing list somewhere? Or can we populate one?