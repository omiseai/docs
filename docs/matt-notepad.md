---
title: "Matt-notepad"
---


get our Hermes instance to work with Line






MATT TODOS:
- implement the 'User account linking' plan `line-dm-pairing-plan.md`
- go through codebase
- understand how the whole docker thing works, what customizations we made like Caddy that make it work with Line, document it
- explain to Shingo new concept of one company agent but with multiple skills
- think about context window management for users. How can we make sure our costs aren't too high. Is there some auto way to set this up with Hermes Agent?
- redo Shingo and Matt's Telegram setup so we use the same bot token and both have a direct chat and group chat
    - make sure Hermes is set up for shared-context via `group_sessions_per_user: false`
    - check silos, get Hermes to run `hermes sessions list` -- should only show my sessions and group one, also `session_search`
- talk to Shingo about OpenAI plans, prob we need a team plan or we use API pricing, or OpenRouter
- now hermes agent endpoint is open, need to secure
- also note the repo becomes public automatically, needs to be made private
- need to make our own API, FastAPI, for things like Line webhook
- will also need to docker-ize my own image of a Hermes setup (ex. starts with latest Hermes version)
- build out list of per instance context, ex:
    - the company's org chart
- I guess the blueprint for Render should be looked over as well to make sure aach instance has parity.
- later, if disable terminal commands block, research more on this:
    - **Why Docker-as-terminal-backend needs a "sibling" container:** when `terminal.backend: docker` is set, Hermes doesn't run shell commands in its own container — it spawns and drives a *separate*, persistent sandbox container via the Docker API, so a destructive/misdirected command can only damage that disposable sandbox's mirrored filesystem, not Hermes' real `HERMES_HOME`. Confirmed: the sandbox's `/root/.hermes` is bind-mounted to a sandbox-local mirror directory, genuinely distinct from the real profile directory; skills/credentials mount in read-only; host cwd isn't shared unless opted in. To create that sibling container, Hermes needs to reach a Docker daemon, which means bind-mounting the host's `/var/run/docker.sock` (Docker-out-of-Docker) — which grants near-root host privileges and is why a managed PaaS like Render is unlikely to expose it. **Decision made:** since terminal is disabled for everyone anyway (see guardrails below), this is moot for now, but Modal/Daytona (cloud sandbox APIs, no local socket needed) would be the fallback if sandboxed execution is ever needed later.
    - I'm still not clear on how the docker sandbox via `terminal.backend: docker` works and is practically useful. For instance, does Hermes create a sandbox whenever it needs to run terminal commands or something? And is the sandbox a clone of the read computer's file system, or Hermes' folder or something? When something changes in the sandbox does it get merged into the real one or something? I don't have any clarit on how all of this works.
    - I still don't yet understand about `terminal.backend: docker`, like why is "Docker-out-of-Docker" even needed? If I'm using Render blueprints and some profile distribution methods, would it still be needed?
- find out more about the local "Holographic" SQLite fact store











- need to first update Hermes version
    1. Open the GitHub repo Render created when you deployed (from the Blueprint/one-click flow).
    2. Check the NousResearch/hermes-agent releases page for the tag you want.
    3. Edit the Dockerfile, bump that HERMES_IMAGE line to the new tag (e.g. v2026.7.x), commit, and push.
    4. This template's Blueprint has auto-deploy turned off, so it won't redeploy on its own — go to the service in the Render Dashboard and trigger a Manual Deploy (or use render deploys create from the Render CLI).


- then fix env vars
The fix — set three environment variables in Render, no shell/redeploy-of-code needed:
Go to your service in the Render Dashboard → Environment tab, and add:
HERMES_DASHBOARD_BASIC_AUTH_USERNAME=admin
HERMES_DASHBOARD_BASIC_AUTH_PASSWORD=<pick a strong password>
HERMES_DASHBOARD_BASIC_AUTH_SECRET=<a long random string, e.g. from `openssl rand -base64 32`>


- then add OpenRouter key
OpenRouter
<redacted - see password manager>

in chat, run /setup





Open the Hermes dashboard URL and navigate to the API Keys tab — You should see empty fields for OPENROUTER_API_KEY, ANTHROPIC_API_KEY, and other provider keys ready to configure

Configure at least one LLM provider key in the API Keys tab, then check the Status tab — You should see the gateway status change to 'running' and the model field display your configured model as reachable


Test the agent by opening the Chat tab and sending a simple message like 'Hello, what can you do?' — You should see a streaming response from the agent within a few seconds, confirming the LLM connection works






















Menu update process:
- direct website changes
- 3rd party services like 
    - 食べログ
    - Retty
    - hot perpper
    - diny mobile order


    - Toreta
- possible stacks
    - claude managed agents, API cost + team min 5 cost
        - team
            Claude Teamプランの料金構造は以下の通りです。基本構造: 1ユーザーあたりの月額課金制（ユーザー数に応じた従量課金）最低人数: 最低 5名 から契約可能月額料金:一般席（Standard）: 1名あたり 25米ドル/月（年払いなら20米ドル/月）開発者向け席（Premium）: 1名あたり 125米ドル/月（年払いなら100米ドル/月）※組織内で一般席と開発者向け席を自由に組み合わせて契約できます。より具体的なお見積もりを出すために、以下について教えていただけますか？ご予定の合計メンバー数そのうち、開発者向け席が必要なエンジニアの人数最適な月額予算のシミュレーションを作成いたします。
        - min 
    - a hermes agent
        - local computer
        - hosted shell







- FDE
    - fix menu updates
- website maintenance model
- other
    - recommendations for other Bonta restaurants when full




- look into existing code
- Go through Claude session about how to construct the prototype, working backwards
- after come up with a design, circle back to the previous two implementations (skill one and python one), see what concepts can be utilized from that



- carefully read through DESIGN.md

- work backwards with Claude from the menu to build a one-off version of NFG
    - Python runtime pipeline
        -x build a schema from `menu_ingest.json`
        -x build a python script that uses `claude -p` to ingest a menu and output conforming menu data
        - build an orchestrator uv script
            - 
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

    - at restaurant flow
        - restaurant fills in pre-interviews via Shingo + encapsulated HTML apps
        - Shingo emails JSON exports to me
        - I plug JSON in with prompt 4 and attachments

    - Claude analog
        - look at menu data, look at my prompt sent to Claude from a prev session and the DESIGN.md doc Claude made based on that. Need to build the pre-interview and ingredient cluster questions in markdown format
        - simulate answers to the questions
        - look at menu data, question answers from prev step, `japan_allergens.json`, and make questions for any dish that is unclear that it has allergens



Great, now, you know about the menu data, you know the questions and the answers. I' going to attach data about allergens. I want you to generate a series of questions for the restaurant operator that correspond *only* to dishes that it's still unclear as to whether or not


I want to simulate OmiseAI's ability to create close to Verified Authenticated Data related to allergens from a restaurant menu. I'm attaching the Bonta menu, and some allergens data. I'm also attaching the restaurant operator's answers to questions from a previous survey they took. I need you to methodically go through the menu, and pick apart each dish into its most likely ingredients keeping in mind the operator's answers to the survey questions. Create an output of JSON data with each dish->recipe->ingredients->allergen-tags. If, based on the operator's answers (not your knowledge necessarily), it's unclear whether or not the dish contains allergens, create a second markdown file with follow-up questions on a dish-by-dish basis so we can get enough info to arrive at an answer. We should never directly ask operators about allergens, only ingredients. 


Then, for each dish, if there is any ambiguity at all about whether or not it contains allergens, I need you to 

        - look at results, make more questions if needed and repeat
        - make a final ingredient output with allergen tags for operator checking
        

Look at the attached menu data. I'm also pasting a prompt I passed to another Claude session with my ideas on doing pre-interviews and ingredient clustering interviews. The result was Claude making a DESIGN.md file, which I'm also attaching here.
I need you to do your best and go ahead and build me the pre-interviews and ingredient cluster interviews and save them in the @nfg-core-manual folder as markdown. 


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
- maybe compare a few years ago if Shingo and I were to come in and help them
    - few years ago
        - we'd build an app
        - the app would only do what Shingo and I built, based on Bonta's needs
        - Bonta could only ever ask us to make features and would have to wait until we do
    - now
        - we build agents
        - at first, the agents do mostly do what we set them up to do, based on Bonta's needs
        - Bonta can build new capabilities too, we can teach Bonta how to do that
        - Our ongoing responsibilities
            - help build capabilities as-needed
            - build and monitor guardrails
            - update agents and tools as newer technology is released and we can improve Bonta's use of it


Read-through notes:
- I'd recommend one container/VM per business rather than co-locating multiple businesses' profiles in one shared container, plus a Docker/sandboxed terminal backend per business if their agents ever run shell commands.
- A profile -- has its own config, memory, sessions, skills, credentials, and (optionally) its own messaging bot token, and can maintain an allow-list of users able to chat with it.
- Hermes' built-in authorization + session-isolation system
    - One Telegram/Slack/LINE bot, one profile, many employees — each employee gets their own private conversation thread with the shared agent automatically.
- So I guess if we want to make true group chats where users share context, we set `group_sessions_per_user: false`?
    - but how would that reflect DMs? Or can `group_sessions_per_user: false` be set only for specific channels, leaving DM channels (if they do have a channel) default private?

- By default, `group_sessions_per_user: true`, meaning two employees messaging the same bot — even in the same channel — do **not** see each other's conversation history, and one person's long tool-heavy task doesn't pollute another's context window or get interrupted by their messages. If you actually want one shared "room brain" (single conversation everyone contributes to), that's a one-line config flip (`group_sessions_per_user: false`). [Sessions doc](https://hermes-agent.nousresearch.com/docs/user-guide/sessions#shared-vs-isolated-group-sessions)
- a profile is a state boundary, not a security boundary
- SSH keys, git credentials, npm auth, and similar tool-level credentials are shared across every profile on that host unless you explicitly set terminal.home_mode: profile per profile
- On centralizing the same setup across businesses: this is what "Profile Distributions" are for — you package a profile's SOUL, config, skills, cron jobs, and MCP connections as a git repo and hermes profile install github.com/you/template --alias it into any new business's instance. Credentials, memories, and sessions stay per-install, which is exactly right for you: you'd centralize and reuse the template (persona definitions, tool config
-Disable the terminal/execute_code tools entirely for employee-facing profiles via hermes tools. Toolset exposure is separate from tool registration in Hermes' architecture, so you can register the tool set broadly but simply not expose shell/code execution to a given profile at all. If a virtual employee doesn't need to run commands, this removes the risk category entirely rather than gating it.
approvals.deny lets you hard-block specific dangerous glob patterns (e.g., git push --force*) unconditionally for a profile — this can't be bypassed by yolo mode or "always approve," so it's a good belt-and-suspenders layer if you do need some command execution.
What Hermes does not currently have built-in is per-user role-based permissions within a shared allowlist (e.g., "employee can chat, only admin can approve risky commands") — that's the same open GitHub RBAC issue mentioned above (Owner/Admin/User/Guest tiers), still a feature request, not shipped. Today, approval prompts route back to whoever's chat triggered them, not to a separate admin channel — you could build that routing yourself via Hermes' gateway lifecycle hooks (which can intercept pre/post tool-call and approval-request events), but it's custom work, not out of the box.
Practical recommendation: don't expose terminal/code-execution tools to employee-facing profiles at all. If a business genuinely needs an agent that runs commands, do that in a separate, restricted profile that only your team (not the business's employees) can reach.

- For Honcho, is it recommended to turn off Hermes agent's memory system and only use Honcho?
- regarding Honcho, is this noted in our plan?
    """
    **The critical Honcho config decision:** in the gateway, `userPeerAliases` must map each employee's platform runtime ID (LINE/Slack user ID) to their own distinct peer name. **`pinUserPeer: true` must NOT be used** — it collapses every human talking to a virtual employee into one shared peer identity, recreating the exact blending problem Honcho exists to solve. This is called out explicitly in the checklist (Phase 3) as the detail most likely to be gotten wrong.
    """
- Hermes may have some easier way, possibly "DM pairing", that can be used to connect human users, does the plan include that?
- Is this included in our plan?
    """
    | Chat type | Session key pattern | Behavior |
    |---|---|---|
    | DM | `agent:main:<platform>:dm:<chat_id>` | One session per person |
    | Group/channel | `agent:main:<platform>:group:<chat_id>:<user_id>` | Per-user session inside the shared group, when the platform exposes a user ID |
    | Group thread/topic | shared by default, or per-user if configured | `thread_sessions_per_user: true` splits it |
    """
- are all of these reccommendations incuded in our plan? Should they be if they are not?
    """
    -Disable the terminal/execute_code tools entirely for employee-facing profiles via hermes tools. Toolset exposure is separate from tool registration in Hermes' architecture, so you can register the tool set broadly but simply not expose shell/code execution to a given profile at all. If a virtual employee doesn't need to run commands, this removes the risk category entirely rather than gating it.
    approvals.deny lets you hard-block specific dangerous glob patterns (e.g., git push --force*) unconditionally for a profile — this can't be bypassed by yolo mode or "always approve," so it's a good belt-and-suspenders layer if you do need some command execution.
    What Hermes does not currently have built-in is per-user role-based permissions within a shared allowlist (e.g., "employee can chat, only admin can approve risky commands") — that's the same open GitHub RBAC issue mentioned above (Owner/Admin/User/Guest tiers), still a feature request, not shipped. Today, approval prompts route back to whoever's chat triggered them, not to a separate admin channel — you could build that routing yourself via Hermes' gateway lifecycle hooks (which can intercept pre/post tool-call and approval-request events), but it's custom work, not out of the box.
    Practical recommendation: don't expose terminal/code-execution tools to employee-facing profiles at all. If a business genuinely needs an agent that runs commands, do that in a separate, restricted profile that only your team (not the business's employees) can reach.
    """


- ChatGPT, Claude, etc. are all agents
- An agent is an AI with tools
- Tools for AI agents are things like accessing and reading documents, connecting to external services to get data and interact with it, and memory so an agent can remember certain important things you told it.
- Agents can also take on a persona, like becoming an expert in responding to customer reviews about your restaurant
- They can also learn/re-learn skills that you teach them, for example how to do your expenses.
- ChatGPT and Claude are personal agents. The tools, persona, and skills are very specific to you. 
- Agents can also be team agents, so they are accessible by everyone in the company, for example via Line or Slack.
- Team agents also use tools, have a persona and can learn/re-learn skills, but they 



- IP is owned 

- agents can do asynchronous tasks


- What is an AI Agent?
    - An agent is simply AI you can chat with that with tools
    - Tools for AI agents are things like accessing and reading documents, connecting to external services to get data and interact with it, and memory so an agent can remember certain important things you told it.
    - Agents can also take on a persona, like becoming an expert in responding to customer reviews about your restaurant
    - They can also learn/re-learn skills that you teach them, for example how to do your expenses.
    - Agents can do scheduled tasks, for example generating a report for you every day before you start your work day.
    - Agents can also be team agents, so they are accessible by everyone in the company, for example via Line or Slack.
    - The tools, persona, skills and scheduled tasks that are specific to your company become your intellectual property.
    - Companies that use AI agents can relieve themselves of repetative and mundane work so everyone can operate more efficiently.
- Today vs. a few years ago
    - few years ago
        - we'd build Bonta an app
        - the app would only do what Shingo and I built, based on Bonta's needs
        - Bonta could only ever ask us to make features and would have to wait until we build them
    - now
        - we build agents
        - at first, the agents do mostly do what we set them up to do, based on Bonta's needs
        - Bonta can build new capabilities too, we can teach Bonta how to do that
        - Ngraph's ongoing responsibilities
            - help build capabilities as-needed
            - build and monitor guardrails so the agents and their data are secure
            - update agents and tools as newer technology is released and we can improve Bonta's use of it





- just using basic features is fine, 
- About Agent エイジェントとは？
    - 


- personal AI
    - AI is an assistant for one person, has memory for just one human-agent interaction
- a company agent
    - AI is an employee who potentially helps all human employees, has memory of all employee interactions with it
    - has its own memory, skills, tools, credentials that multiple employees benefit from

- Bonta can create IP that is unique to them and valuable, and they can own it
- Anthropic, OpenAI can go away as companies and Bonta can continue



- Our Hermes setup
    - one cloud Hermes instance per business
    - multiple profiles reflect multiple virtual employees, each with their own tools, skills and so on
    - each human user adds multiple Line chats, one per virtual employee chat
    - a shared group for each agent exists, multiple employees can join



A follow-up question. For terminal.backend, what is the point of the sibling container? And are the files and file system different there from the container where Hermes is running?

And I think I'm starting to coalesce our setup here. Here is what I'm thinking:

- one Render server with Docker of Hermes installation per business
- multiple profiles for a business represent virtual employees all human employees have access to
- integrate Honcho so an appropriate memory regime can support our use case
- set appropriate guard rails so agents can't run certain destructive actions via CLI
- establish some auto-bakup of data, and auto-commit of Hermes settings

Now, we've discussed quite a bit. I'd like you to very carefully review our entire conversation up until now so nothing falls through the cracks. If a decision/preference of mine is unclear, ask me for clarification. I think we need to disable termainal commands for all employees for instance. Yet, I'd like to still be able to run them myself, which perhaps I could do via SSH into an instance. Once you're totally clear, build a comprehensive yet concise outline of our setup that includes all aspects that I laid out above, but enriched with the numerious things we'll need to set up, like I guess if we want to make true group chats where users share context, so we set `group_sessions_per_user: false`, right? But how would that reflect DMs? Or can `group_sessions_per_user: false` be set only for specific channels, leaving DM channels (if they do have a channel) default private? Maybe there are still some things we need to clear up first, you tell me. But ultimately I want a comprehensive outline I can go through and check items off as I create our first instance.


