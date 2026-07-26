# Chapter 20: AI Fight Club at the IRS

## Core Idea
The IRS is deploying real AI at scale by making it legally unassailable and rhetorically invisible — a series of deliberate "five-degree turns" hidden behind the agency's reputation for being hopeless.

## Frameworks Introduced

- **Werfel's Five-Degree Turn Doctrine**: Move a large bureaucracy in small increments, never in 180-degree pivots.
  - When to use: Any change inside an institution with heavy legal, security, and stakeholder dependencies.
  - How: Scope each change so it clears existing rules without needing new ones; ship it; repeat. Refuse the big-bang program even when it's the "right" answer.
  - Why it works: A 180-degree turn triggers so many dependencies, equities, concerns, laws, security issues, and protocols that the study phase alone runs five years — by which time the technology has changed and you have a failure to launch. Failure mode: incrementalism can become an excuse for stasis if no one tracks cumulative progress.

- **The Invisibility Shield (Werfel's version of the Cliff Walls strategy)**: Shrink an AI program's public profile until the institution's bad reputation becomes its cover.
  - When to use: When your program would be an obvious target for litigation or political attack if noticed.
  - How: Let the outside world keep believing the agency is slow, boring, and technologically hopeless; never claim transformation; describe each project in precise legal terms rather than aspirational ones; carve room inside existing budget and rule constraints rather than asking for exceptions.
  - Why it works: Litigation is forever, unlike politics — political attacks are a force majeure limited by a fickle electorate, but a lawsuit can stall a program for years regardless of outcome. Attention is the input to litigation, so denying attention denies the attack.

- **The Inherently Governmental Test (courthouse heuristic)**: Sort functions by whether the Constitution assigns them to government and therefore forbids outsourcing.
  - How: Werfel's example — you cannot outsource the judge; you could debate outsourcing the stenographer; you can probably outsource security and landscaping. Apply the same sort to AI: the machine may advise, but the constitutionally assigned decision stays with a federal employee. "Self-driving lawn mowers" are fine; algorithmic audit selection is not.

- **Human-in-the-Loop as Legal Bubble Wrap**: Preserve employee decision-making as both a technical design principle and a litigation defense.
  - How: Use Werfel's chess framing — the computer sits beside the employee and suggests the move because it may be the better and faster player, but the human makes the final move. Humans actively participate in training, testing, refining, and operating the models, creating a continuous feedback loop.
  - Why it works: It simultaneously satisfies the inherently-governmental constraint, catches model bias before it becomes policy, and supplies accountability cover. The term evolved from aerospace/defense, where human authority over automated systems exists partly so no one has to testify that they assumed the drone knew better.

- **Pandya's "Why You Should Care" Rule**: Lead technology explanations with impact, not mechanism.
  - How: Replace "here's some tech and here's what it does" with why it matters to this listener, how it affects them, how it's transformative. Pandya learned this after consulting feedback that he deployed well and explained terribly.

## Key Concepts
- **Inherently governmental**: Constitutionally assigned core functions (law enforcement, taxation, national defense) that cannot be outsourced — the central legal constraint on AI at the IRS.
- **Individual Master File (IMF)**: The Kennedy-era mainframe database holding every American's tax record *and* every change ever made to it; ~2 million lines of COBOL and ALC.
- **Tier 1 / Tier 2**: Tier 1 is critical tax-record infrastructure (the IMF); Tier 2 is everything that integrates with it — fraud detection, smaller databases, the taxpayer portal.
- **COBOL / ALC**: Common Business-Oriented Language and Assembly Language Code — efficient inside the mainframe, isolating everywhere else.
- **Middleware**: Translation layer between modern Tier 2 software and graying Tier 1; the reason hold times exist.
- **Pair programming (modernization sense)**: A retiring COBOL/ALC engineer sits beside a modern developer and explains the logic so it can be rebuilt in a current language.
- **The frozen middle**: The Defense Innovation Board's term for the layer of staff whose skills gap becomes a cultural gap that blocks modernization.
- **Algorithmic audit bias**: The 2023 Stanford/Michigan/Chicago/Treasury finding that Black taxpayers were audited 2.9–4.7x more than non-Black taxpayers, traced to automated selection over-flagging Earned Income Tax Credit (EITC) returns.

## Mental Models
- Think of **legacy code as Sanskrit**: perfectly functional if you know others who speak it, catastrophically isolating when the speakers retire and die faster than you can replace them.
- Think of the mainframe as **hardware-modern, software-ancient** — Pandya updates hardware every two to three years; what looks obsolete is the 60-year-old language running on it. Nearly 70% of Fortune 500 firms also run mainframes.
- Use **SQL vs. Databricks as taxi vs. bullet train**: an obvious upgrade — unless you feed your family by driving a taxi. Every efficiency argument reads as a threat to the person whose skill it obsoletes.
- Think of **AI on legacy code as a logic extractor, not a translator**: it digests COBOL/ALC into pseudo-code that gives Java developers a foundation. Pandya's caution — there is no magic bullet.

## Anti-patterns
- **Force-feeding digital services**: The IRS must serve taxpayers who file on smartphones and taxpayers who file with pencil and paper equally; mandating chatbots violates that duty.
- **Rip-and-replace of critical systems**: By law there could be no disruption to filing or the 400 processes depending on the IMF — so replacement was never an option.
- **Unmonitored automated decision-making**: Left unsupervised, AI replicates the worst biases of the system it was meant to improve; the EITC audit disparity is the proof.
- **Dismissing small per-person savings**: Two hours a week saved on documentation sounds trivial until you multiply by 500–1,000 developers.
- **Treating modernization as purely technical**: The skills gap creates a cultural gap, and culture is the hardest thing to change.

## Worked Example
Commissioner Danny Werfel — DOJ and OMB veteran, briefly acting IRS commissioner in 2013, then head of BCG's public sector practice, back under Biden in 2022 — opens by cataloging why the IRS *can't* use AI: inherently-governmental limits, an equal-service duty, world-strictest privacy and cybersecurity rules many AI vendors won't meet, and a budget cut more than 20% from 2010 to 2021 while annual returns grew by fifteen million. Then he quietly lists what's already running: natural language processing routing callers to the right human expert; GPT-4 and Llama tested for code generation; bespoke AI helping employees spot complex evasion schemes; and AI assisting the translation of the IMF from 1960s code. CTO Kaschit Pandya's team used AI to restructure the dense Internal Revenue Manuals — previously searched with something he compares to AltaVista or Ask Jeeves — so reps answer callers fast in plain language; the National Taxpayer Advocate told Congress in 2024 that despair had turned to cautious optimism. The IMF replacement, begun in 2014 as a ten-year plan with no allowed disruption, hit 90% complete by November 2024 via pair programming. The Business Master File (BMF) migration is next and will not take ten years: Llama, Claude, and ChatGPT extract logic from COBOL/ALC into pseudo-code, doing in days what took months. Much of it was funded by the 2022 Inflation Reduction Act. Werfel admitted none of the strategy; the closest to swagger was noting the IRS launched more digital tools in two years than in the previous twenty. The chapter closes on the day after the 2024 election, with a president elected on chainsaws rather than incrementalism.

## Key Takeaways
1. Design AI so the human keeps the decision — it satisfies the law, catches bias, and gives you accountability cover simultaneously.
2. Fear litigation more than politics. Politics passes with the electorate; a lawsuit stalls you for years whether you win or lose.
3. Ship five-degree turns. If a change requires studying every dependency at once, you will launch nothing.
4. Use your institution's low reputation as camouflage — the less people expect of you, the more room you have.
5. Modernize the boring surface area. Restructured manuals aren't sexy, but faster answers on the phone are real modernization.
6. Audit your automated selection systems for disparate impact before someone else publishes it.
7. Sell modernization as skill expansion, not extraction — Pandya's line is that the employee, not the tech, should be the reason it succeeded.

## Connects To
- **Ch 19 (An Emotional Nudge)**: Werfel scales Cliff Walls's "make it seem less big" tactic to a 75,000-person agency.
- **Ch 21 (Dilettantes and Vandals)**: Sam Corcos freezes Pandya's modernization programs; the chapter's incrementalism is the thing DOGE arrives to destroy.
- **Earlier chapters (Perna, Maddox, Karp, Schmidt)**: Four postures toward bureaucracy — outrun it, sue it, leave it — versus Werfel's fifth: hide inside it.
- **Algorithmic fairness / disparate impact**: The EITC audit finding is a canonical case of a proxy variable encoding racial disparity.
