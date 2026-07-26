# Patterns — Diagnostic Techniques

## The Sink Test
**When to use**: You suspect a policy, algorithm, or process is an accountability sink rather than a decision.
**How**: Ask the defining question — *is there any information the affected person could supply that would change the outcome?* If no, it is a sink. Then run the override test: who, by name, can overrule this? If the answer is "nobody" or "the policy", the sink is complete. Check whether an exceptions mechanism exists **and is actually used** — an unused exceptions process is decoration.
**Trade-offs**: Sinks are not automatically bad. They are variety-amplification devices — a solution as much as a problem. The good ones (Davies' common-law test) retain slow reputational feedback and can be revised; the bad ones are unappealable and unrevisable.

## The Requisite-Variety Audit
**When to use**: Assessing whether any regulator — a manager, a regulator, a control system, a project plan — can possibly do its job. Davies flags this in a footnote as the most useful advice in the book.
**How**: For each regulatory link, *compare* rather than measure: is the regulator's variety greater or less than the variety arriving from the environment? Use the vehicle-controls test as a quick dimensional check (a train has one control dimension, a car two, a plane three — match the controls to the environment's degrees of freedom). Then check observation *frequency* against the rate at which the system generates variety.
**Trade-offs**: Gives you a clean verdict on impossibility-in-principle, and distinguishes "fails for lack of resources" from "cannot work at all" — but it tells you the mismatch exists, not which of attenuation or amplification is the cheaper fix.

## Hunt the Three Model Defects
**When to use**: A control system exists and is well-resourced but keeps being surprised.
**How**: Treat the control system as a *model of its environment* and look for exactly three defects: (1) sources of environmental variety the model omits entirely; (2) regulatory variety that is overestimated; (3) information assumed to be transmitted that is not actually transmitted. Then ask the complementary question: **what does the control system not monitor?** (Pre-2008, deficits were watched; private-sector debt was not.)
**Trade-offs**: Requires knowing the domain well enough to name the missing variety sources; the method won't generate them for you.

## VSM Role Audit
**When to use**: Diagnosing a chronically dysfunctional organisation, division, or programme.
**How**: Name which actual component performs each of Systems 1–5. Map functions, not org-chart boxes — the functions exist whether or not anyone holds the title. Check both directions: the larger system this unit is embedded in, **and** the organisation inside its own operations. A missing role is a predicted failure point.
**Trade-offs**: Tempting to force five labels onto existing boxes; resist. Stopping at one level of recursion is the most common error.

## The System 2 / System 3 Test
**When to use**: Working out whether a management layer is coordination or control.
**How**: System 2 is the management everyone agrees is necessary (timetables, scheduling, the quartermaster). System 3 is the management people complain about. The tell: System 3 managers routinely disguise themselves as System 2 — presenting control as harmless coordination.
**Trade-offs**: Useful for reading org politics, but the distinction is functional, so the same person can do both.

## The Decerebration Check
**When to use**: An organisation is performing well but you suspect it has cut away its own brain.
**How**: Ask what the leadership's attention actually runs to. If it runs only to this quarter's revenue and current staffing, System 4 is absent and the organisation is coasting on a stable environment. Distinguish **forecasting from System 4**: if the forecasts are extrapolations of the current model, they are here-and-now extended, not intelligence.
**Trade-offs**: Decerebrate organisations look fine — sometimes excellent — until the environment changes structurally. The check has no short-run confirming evidence.

## Red-Handle Frequency as Diagnostic
**When to use**: Judging the health of levels below you.
**How**: Count algedonic signals. Frequent emergency escalations mean systems further down are missing, misidentified, or dysfunctional — the signal is doing work that should have been absorbed lower. Also resource the *receiving* end: an algedonic channel with no translation capacity delivers noise.
**Trade-offs**: Zero red handles is not health; it may mean the channel doesn't exist.

## The Problem-Child Diagnostic
**When to use**: One division bounces from crisis to crisis while others don't.
**How**: Treat it as an unrecognised System 1 — a unit that could in principle exist independently but has been denied its own internal 2/3/4/5. Give it the missing internal functions rather than more supervision from above.
**Trade-offs**: Occasionally the unit genuinely isn't a viable system and should be merged or dissolved instead.

## Boundary-Crossing Audit Before Cuts
**When to use**: Before any restructuring, outsourcing, or headcount reduction.
**How**: Trace a real signal end to end. Identify every organisational boundary it crosses and what capacity translates it at each crossing. Then run the **channel-state test for outsourcing**: if the contract can only carry "OK" and "stopped working", there is no bandwidth for "conditions are changing" — you have bought a decerebration.
**Trade-offs**: Slow, and it makes cuts look more expensive than the accounting does. That is the point.

## POSIWID Divergence
**When to use**: A system's stated purpose and delivered outcomes disagree, and you are being invited to argue about intentions.
**How**: Ignore stated purpose. Read the purpose off the outputs. Then ask "what structure made this the *systematic* output?" — which dissolves the conspiracy-versus-cock-up question entirely.
**Trade-offs**: Reads as cynicism if stated aloud; it is actually a claim about System 5, not about anyone's motives.

## The Four-Condition Check Before Trusting an Optimisation Model
**When to use**: An economic or quantitative model is being used to settle a real decision.
**How**: Confirm all four: commodity good; observable marginal cost curve; spot markets independent of later periods; negligible strategic interaction. If any fails, you are watching the Ricardian Vice. Separate the assumptions made for tractability from those equivalent to assuming the conclusion. Translate "however you look at the numbers" as "however *I* look at *these* numbers."
**Trade-offs**: Beating a Ricardian requires either data collected for a different purpose or a flaw internal to their model — the four-condition check tells you which fight you're in.

## Ask What Decision the Number Was Collected For
**When to use**: Reusing any metric, report, or dataset outside its original context.
**How**: Trace the number to the decision it was designed to support. Apply the attributability test to costs: a cost is attributable exactly to the extent it would be avoided by not producing the output. Rule of thumb — learn the numbers by looking at the business, never the business by looking at the numbers.
**Trade-offs**: Most available numbers fail this test, which leaves you with less data and better judgement.

## The Feedback-Location Method
**When to use**: Designing a fix, instead of writing another rule.
**How**: Don't specify behaviour. Ask where feedback is currently amplified, attenuated, or removed — then restore the missing loop. Corollary target-regime diagnostic: **demand the impossible and you get the unethical**.
**Trade-offs**: Harder to audit than a rulebook, and it produces no compliance artefact.
