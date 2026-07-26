# Chapter 13: Sepsis

## Core Idea
An AI that is only ~90 percent accurate on the hardest cases can still be a major clinical win — if you pair it with committed human partners, standardized response protocols, and an honest accounting of what the model does and doesn't add. Cleveland Clinic cut sepsis mortality 40 percent (2021–2024) with an imperfect model plus disciplined administration.

## Frameworks Introduced

- **Chandra's Matched-Commitment Rule**: Rohit Chandra (Cleveland Clinic Chief Digital Officer) would not start an AI project until he found a clinical partner willing to match his own commitment to the problem — and a vendor willing to embed with that clinician.
  - When to use: before green-lighting any AI deployment inside an entrenched institution.
  - How: (1) verify the problem is big enough to justify organizational pain (sepsis: ~350,000 US deaths/year, 4–5 deaths a day in Cleveland Clinic facilities, $52B in US inpatient costs in 2021); (2) find a named clinical owner who will do the grinding audit work, not just endorse the project; (3) find a vendor with a single-problem focus, not a general "we do AI" pitch; (4) require the vendor to configure to your workflows on-site.
  - Why it works: the bottleneck in health-care AI is never the model — it's professional culture, entrenched vendors, and reimbursement politics. A committed clinician is the only force that survives that. Failure mode: "I just want to get some AI going" projects, which Suchi Saria (Bayesian Health CEO) refuses because unsponsored buyers jerk vendors around by the message of the day.

- **The Sepsis Alert Triage Ladder (Bayesian in Epic)**: a three-level flag on every patient on the floor.
  - When to use: any high-volume prediction system where alert fatigue is the real enemy.
  - How: Level 1 = no concern. Level 2 = moderate risk, primary team watches (pending labs, a few symptoms). Level 3 = immediate bedside attention; if unaddressed for minutes, the command-center nurse physically intervenes. Every flag is clickable to key stats plus the model's explanation of how it reached the assessment. Clinicians can override, and the override becomes training data.
  - Why it works: graded urgency plus explainability preserves clinician autonomy — the model reads as a physician's assistant with one obsession, not a supervisor.

- **The Override-as-Training-Data Loop**: disagreement is captured, not discarded.
  - How: nurse practitioners in the SERT command center reconcile each screen flag against what bedside staff see; accepted, rejected, and corrected calls all feed Bayesian's retraining. Allie Tallman also brought the model the *inverse* cases — patients she diagnosed correctly from skin pallor alone — and asked why the model missed them.

- **"Make it easy for people to do the right thing"** — the project mission statement repeated near-verbatim by Morrison, Tallman, Chandra, and Saria. Operationalized as: standardized sepsis protocols plus pre-written treatment orders in Epic, so a day-one resident executes the same sequence as an attending.

## Key Concepts
- **Sepsis**: a dysregulated host response to infection causing organ dysfunction (Morrison's clinical definition); Tallman's version — it looks like rotting from the inside out.
- **SERT (Sepsis Emergency Response Team)**: Tallman's few dozen nurse practitioners and PAs operating in the main-campus ICU where sepsis is most volatile.
- **Epic**: the dominant US electronic health record, founded by Judith Faulkner in 1979; ~$5B revenue, seven salespeople worldwide, 21 of the top 22 US News honor-roll hospitals, ~26% of hospitals but ~46% of beds.
- **Closed-system lock-in**: Epic's closed architecture buys security and reliability but leaves clients dependent on Epic's priorities and integration fees when an outside vendor is better at something.
- **Bayesian Health**: Suchi Saria's company (Johns Hopkins ML/AI health lab) commercializing a sepsis prediction model that integrates two-way with Epic and returns results into a bespoke Epic module.
- **Case mix**: the subpopulation diversity of a hospital's patients (cardiac, digestive, surgical, neuro-oncology) — the variable that made a blanket algorithm fail on main campus.
- **Alert fatigue**: the pre-Bayesian failure state — Epic's native best-practice alert was so sensitive the team exhausted itself on constant beeps; the older IT rule was too unspecific to help.
- **Hawthorne effect**: behavior change caused by being observed — the honest confound Tallman and Morrison flagged against crediting AI for all 40 percent.
- **Auditing and reinforcement**: the only way to tune a deployed model — reviewing every flagged patient with a vendor data scientist to determine why and when an alert fired.

## Mental Models
- **Think of sepsis detection as finding one dangerous needle in a pile of identical needles**, not a needle in a haystack. That is precisely why rules-based alerts flood you with false positives and why ML — which doesn't get fooled by familiarity or overwhelmed by volume — is the right tool.
- **Use ruling-out as a value driver, not just ruling-in.** A minor scrap of patient data that lets the model correctly exclude sepsis preserves the integrity of every remaining alert.
- **Think of a bigger, more prestigious hospital as a deeper stack of needles.** Bayesian flagged earlier with fewer false positives at 488-bed Fairview (homogenous population, routine cases) while still under 90 percent on main-campus level threes.
- **Use Mihaljevic's maxim when judging deployment readiness**: AI does not need to be perfect to be useful.

## Anti-patterns
- **Hot mess problems**: Chandra learned to avoid initiatives spanning too many departments with longshot medical odds — they consume years and produce nothing.
- **Blanket algorithms across heterogeneous populations**: Tallman's most consequential pilot feedback — a quaternary main campus with a top cardiac center generates cardiac infections that mimic sepsis; one model tuned for average hospitals misfires.
- **Buying AI before securing a clinical owner**: yields vendor churn and abandoned pilots.
- **Treating vigilance as free**: too much alerting is as damaging as too little; an exhausted response team stops responding.
- **Blindly prescribing antibiotics on early symptoms**: mimicking conditions (pancreatitis, autoimmune disease) get delayed diagnoses, patients risk severe reactions, and overuse accelerates drug resistance.

## Worked Example
Cleveland Clinic, 2022–2024. Two of five patient deaths in the system were sepsis-related — normal for the industry, unacceptable to leadership. Rohit Chandra, who hadn't known what sepsis was when colleagues suggested it at a CFO going-away party, got two clinical partners: Dr. James Morrison (ER/ICU, Sepsis Committee — the war-strategy general building system-wide consensus across Cleveland, Florida, and overseas) and Allie Tallman (SERT lead, whose grandmother died septic days after being sent home from an ER with muscle relaxers). They first standardized a sepsis protocol, wrote treatment orders into Epic to cut variation, and ran an awareness campaign using Mugatu memes from *Zoolander* on scrubs and walls.

Chandra then spent months courting Suchi Saria of Bayesian Health, whom he met in a dingy San Francisco restaurant in late 2023; Saria — who lost a nephew in India to sepsis and had Epic relationships from her Hopkins research that permitted integration — initially didn't want the account, distrusting large prestigious systems. The pilot launched on main campus in May 2024. Early friction: confusing drop-downs, and a model that labeled all CNS infections meningitis. Tallman met regularly with a Bayesian data scientist to audit every flagged patient in both directions. In the ICU command center, NP Dana Rubis worked the triage list — roughly thirty level-three alerts in a day — reconciling each with bedside teams.

Outcome by late 2024: reliable, low-friction wins at Fairview Hospital; main campus still short of 90 percent accuracy on level threes. System-wide sepsis mortality down 40 percent from 2021 to 2024, with credit shared between AI, the protocol work that predated Bayesian, and possibly the Hawthorne effect. Cost: $16M-scale vendor spend is not stated here; the real cost was ceaseless human auditing labor. CEO Tomislav Mihaljevic's verdict: even imperfect AI contributing to a 40 percent mortality reduction is success.

## Key Takeaways
1. Fund the clinical owner, not just the model — no committed nurse or physician, no project.
2. Ship explanations with predictions; a model that shows its reasoning preserves clinician autonomy and earns repeat use.
3. Capture overrides as training data — the disagreements are your highest-value labels.
4. Pilot where the population is homogenous first (Fairview) to bank wins, then attack the hard, heterogeneous site.
5. Standardize the human response before you deploy the model; protocol plus pre-written orders is what converts a flag into a saved life.
6. Grade your alerts and defend against fatigue — sensitivity without specificity destroys trust faster than missing cases.
7. Set the accuracy bar against the human baseline, not perfection; a 40 percent mortality drop is worth accepting an unfinished model.

## Connects To
- **Ch 11–12 (Ambience, Hospital 360)**: Chandra's other Cleveland Clinic deployments — lower-risk operational modernization; sepsis is the "big swing" he'd joined to take.
- **Jessica Shieh's frontier maxim**: you'll be disappointed for a long time until you're not — the emotional contract of deploying frontier models against human problems.
- **Ch 14–15 (Perna, Warp Speed)**: same pattern one scale up — the technology is easy relative to entrenched stakeholders, and success requires a sponsor with authority plus an operator willing to grind.
- **Vendor lock-in / platform economics**: Epic's closed system is a textbook case of security and reliability purchased with strategic dependency.
