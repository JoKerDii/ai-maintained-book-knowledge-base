# Chapter 16: Brief Moments for Exceptional Things

## Core Idea
Most "AI" wins are actually data-plumbing wins delivered agilely: Palantir's Aaron Jaffe got Operation Warp Speed's vaccine-tracking platform (Tiberius) built in weeks by abandoning the demand for a perfect end-to-end system and shipping a partial one. The window for such work is temporary — institutions reabsorb exceptional efforts and pull them back to ordinary.

## Frameworks Introduced

- **Ontology (Palantir's core product logic)**: standardize an organization's scattered data, define the relationships between the "pipes," then build a usable app on top.
  - When to use: any organization whose data lives in dozens of incompatible systems bought at different times from different vendors (Palantir's chief architect Akshay Krishnaswamy calls the firm "the mole people of Silicon Valley").
  - How: (1) inventory every data source; (2) clean and standardize formats; (3) define entities and how they relate; (4) run automated quality checks inside the pipelines; (5) hide the plumbing behind an interface a non-technical user can operate.
  - Why it works: cleaned data + a useful app gives every level of the org the same "God view" — Krishnaswamy's "Iron Man suit" — so decisions are made on current facts rather than stale reports.
  - Failure mode: teams treat it as an engineering problem. Jaffe: the pipelines are the easy part; culture, alignment, and people are the hard part.

- **Jaffe's Embrace-the-Chaos Rule**: never wait for the complete picture; ship on the partial one.
  - When to use: when one critical data holder is stonewalling and the clock is running.
  - How: three or four sources give you ~60% of the picture — take it. The next ten give an incremental 20%. The rest is an unharmonized long tail you figure out as you go. If a source refuses (the FDA refused to share vaccine-trial data), move on rather than stall.
  - Why it works: partial visibility that exists today beats total visibility that never arrives.

- **Four Singles Instead of a Home Run**: deliver most of the value in a fraction of the time by narrowing scope.
  - How: hack a prototype on *notional data* (placeholder), show the narrower capability that is actually achievable, get a decision-maker to approve the deviation in flight, then build for real.

- **The Three-Category Data Triage**: sort incoming sources by tractability before building.
  - How: Category 1 — a handful of cooperating federal agencies and large companies (wholesale distribution view). Category 2 — the much larger middleman layer handling transport, storage, and administration. Category 3 — the long tail of nursing homes, independent pharmacies, and rural offices, many not digitized. Solve the long tail by lowering the bar: "just give us whatever janky thing you have."

## Key Concepts
- **Ontology**: in AI practice, the untangling of data messes into a functional information ecosystem with defined relationships.
- **Agile development**: building software iteratively — deploy a little, get user feedback, repeat — rather than blueprinting a finished product first.
- **Notional data**: placeholder data used to demo an interface before real feeds exist; discarded on contact with reality.
- **Tiberius**: the Operation Warp Speed platform (named by Deacon Maddox for Captain James Tiberius Kirk) that tracked every vial from warehouse to plane to truck to arm.
- **The long tail**: the unknowable mass of small, undigitized participants that a system must accommodate rather than exclude.
- **Bullshit umbrella**: Gen. Gus Perna's deflection of political games and schemes so the working team could decide without fear.
- **Software Sherpa**: an on-site operator sent to each state to run Tiberius for them — which also removed any excuse for nonparticipation.
- **Alex Karp's definition of AI**: "AI is software that works."

## Mental Models
- Think of an organization's data as a knotted pile of garden hoses in the backyard — bought at different times, different sizes, maintained by no one. The product is untangling.
- Use agile framing when the artifact is malleable: design software as rigid as a bridge and people will want to throw themselves off it.
- Ontology builders assume everything is already wrong — the opposite of the baker's Zen moment when materials are assembled and nothing has gone wrong yet.
- Treat institutional openings as expiring: you get brief windows to do exceptional things before documentation, reviews, and process reabsorb the work.

## Anti-patterns
- **"One big system" thinking**: the government reflex to demand a single nice, tidy platform. It guarantees the project stalls behind whichever holdout refuses to share.
- **Waiting for the blocking data source**: everyone assumed Perna needed perfect vision, so the FDA's refusal left the mission adrift until Jaffe routed around it.
- **Renegotiating a contract through normal channels**: consultation with dozens of bureaucrats and multi-agency approval means something bad gets built, slowly.
- **Shipping data without automated quality checks**: the CDC's new facilities app had none, so its feed arrived riddled with duplicates, missing fields, invalid numbers, and mismatched formats.
- **Silver-bullet AI narratives — and their inverse**: Jaffe undersold the machine learning; colleagues insist Warp Speed would have failed without AI as accelerant. Be precise about what the software actually did.

## Worked Example
Palantir was contracted to build an end-to-end digital twin of the vaccine supply chain for Operation Warp Speed. The first link — pharma company data — Perna largely secured. The second — the FDA's trial data — was refused, because agencies are made of people who flinch at being seen, blamed, or outmaneuvered; the FDA's self-image was *wait, test, prove*, the opposite of Warp Speed. Aaron Jaffe, a Northwestern Medill graduate and Palantir product engineer who made a terrible first impression (he stayed seated at his laptop when Gen. Perna entered the room), thought the contracted deliverable was impossible. Over a few days he hacked a prototype on notional data showing not the trials but a microscopic view of vaccine inventory and distribution — most of the problem, operational in weeks. Deacon Maddox, running Perna's protected M*A*S*H-style unit, signed off on the deviation immediately. Maddox: "I can't tell you how unusual that is." Palantir moved a dozen engineers under Jaffe overnight. They diagnosed thousands of data issues, called counterparts at pharmacies and HMOs, wrote code so the data would behave, and ran tens of thousands of automated quality checks inside the pipelines. The result, Tiberius, let Perna answer any presidential question with current facts and share his screen with governors who claimed they'd been shorted — down to the vial, plus the name of the official who signed for it. Maddox played the rollout like a video game. Because the build was agile, a marketplace app letting vaccine-skeptic states cede doses to believers took under a week to bolt on (Rhode Island and Montana traded Pfizer/Moderna for single-dose J&J); when the Biden administration objected to insider advantage, it became an international donation app. By June 2021 Jaffe felt the shift — documentation, processes, reviews — "transitioning from exceptional to ordinary."

## Key Takeaways
1. Solve for 60% of the picture now rather than 100% eventually; name the missing sources and move on.
2. Prototype on notional data to make the scope change concrete before you argue about it.
3. Get one protected decision-maker who can approve a mid-flight deviation without a committee — that person is the whole difference.
4. Accept any input format from the long tail; forcing digitization on the smallest participants excludes them entirely.
5. Assume the data is already broken and budget for triage, outreach, and automated quality checks as the main work.
6. When a crisis window opens, ship fast — the institution will reassert itself, and Maddox's lesson is that the reassertion becomes part of the problem again.

## Connects To
- **Ch 15 / Operation Warp Speed chapters**: Perna's data access, Maddox's integrated master schedule, and the Julie Bush meeting set up everything Jaffe builds here.
- **Ch 17 (Lululemon in the Iron Triangle)**: explains why Palantir's speed-and-cost advantage still gets it frozen out of defense procurement.
- **Ch 18 (The Frozen Middle)**: Jaffe's "exceptional to ordinary" transition is the frozen middle reasserting itself.
- **Debbie Kwon, Cleveland Clinic**: same conclusion from a different sector — culture, alignment, and people are the hard part.
- **Agile manifesto / Gall's Law**: the iterative-versus-blueprint argument that Ch 18 formalizes.
