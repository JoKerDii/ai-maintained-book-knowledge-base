# Patterns — AI for Good

Techniques practitioners in this book actually used. Each is attributed to the person who ran it.

## Hillis's Reframe
**When**: you cannot tell what AI is good for because vendor noise dominates.
**How**: "Try to imagine the tech without the tech companies." Ask what the capability enables for someone with a real problem, stripped of who profits from the answer.
**Trade-offs**: clarifies use, ignores cost and vendor lock-in — reintroduce those after.

## Perna's "See Myself" Principle
**When**: coordinating anything across organizations that don't share data.
**How**: before optimizing, build one live standardized picture of positions, supplies, and flows. Reduce complexity to a single tracer material (Perna used plastic) to test whether the picture is real.
**Trade-offs**: data standardization is the expensive, unglamorous majority of the work.

## The Definition-First Vendor Test
**When**: selecting an AI vendor.
**How**: give each an hour. Reject any who cannot state the problem back to you more precisely than you stated it. Hire the ones who commit to a decision you'll be able to make, not a technology.
**Trade-offs**: filters for clear communicators, which correlates with but does not guarantee capability.

## The Ten-Run Prompt Test (DiCerbo)
**When**: validating any prompt before it faces users.
**How**: run the same prompt ten-plus times and inspect the spread, not the best output. Ship only if the worst run is acceptable.
**Trade-offs**: slow and manual; replaces vibes-based evaluation, which is worse.

## The Role-Constraint Prompt Pattern
**When**: a model must refuse to do the user's work for them.
**How**: specify role, what it must never do, and the recovery move when pushed. Khan's tutoring script: ask what the student thinks first, never give the answer, decompose into the next smallest step.
**Trade-offs**: constraints erode under adversarial pressure and after model updates — retest on every version bump.

## Context Stuffing
**When**: you need answers anchored to your material, not the model's priors.
**How**: load authoritative source content into the context window and instruct the model to answer only from it.
**Trade-offs**: bounded by window size; does not eliminate hallucination, only reduces it.

## Zubovic's Pilot-Site Selection Rule
**When**: choosing where to run a first deployment.
**How**: pick the site with a leader who will personally champion it and whose reputation is staked on the outcome — not the easiest or largest site. "Get Buffington."
**Trade-offs**: success may not generalize to sites without a champion; plan the second site deliberately.

## Quiet Pilot Containment
**When**: piloting anything that could be politically destroyed by early failure.
**How**: keep the pilot small and unpublicized until the failure modes are known. Announce after it works.
**Trade-offs**: limits learning volume and can read as secrecy if discovered.

## The Voluntary Bake-off (Boose)
**When**: introducing a tool into a professional workforce that resents mandates.
**How**: let clinicians volunteer, run competing vendors side by side, let usage data pick the winner. Escalate to a mandate only after voluntary adoption plateaus (Mihaljevic's Mandate Threshold).
**Trade-offs**: volunteers self-select as enthusiasts; ghosting is common, so recruit more than you need.

## The Sepsis Alert Triage Ladder
**When**: an automated alert system is being ignored.
**How**: tier alerts by probability instead of firing uniformly; route each tier to a different response. Treat every clinician override as training data (the Override-as-Training-Data Loop).
**Trade-offs**: tiering requires a calibrated model; miscalibration moves harm rather than removing it.

## Build-With, Don't Buy-Out-of-the-Box (Pappas)
**When**: deploying into a workflow whose practitioners must trust the output.
**How**: co-build with the people who will use it; ship the reassurance that they remain the final check.
**Trade-offs**: slower than procurement, and the result is harder to resell elsewhere.

## Four Singles Instead of a Home Run (Jaffe)
**When**: the full problem is too large or too political to solve at once.
**How**: ship four small, independently useful wins rather than one transformative system. Start on notional data so building begins before real data clears.
**Trade-offs**: risks a pile of tools with no coherent ontology unless the data model is planned up front.

## Werfel's Five-Degree Turn Doctrine
**When**: reforming an institution that cannot survive visible upheaval.
**How**: make small course corrections continuously, keep the work below the threshold of political attention (the Invisibility Shield), and let compounding do the rest.
**Trade-offs**: invisibility forfeits the credit and the mandate that would let you move faster.

## Pandya's "Why You Should Care" Rule
**When**: pitching technical work to non-technical stakeholders.
**How**: lead with the consequence for the listener's constituency, never the architecture.
**Trade-offs**: none; the omission is the common error.

## The Collaboration Gate for Public-Sector AI
**When**: judging whether a government AI effort will help or damage.
**How**: ask whether the team is building with the civil servants who run the system or against them. Provocation-first efforts (Ch 21) destroy the institutional knowledge they need.
**Trade-offs**: collaboration is slower and dilutes the reformer's narrative.

## Johnson's Burden-Side Rule
**When**: designing for someone who cannot easily self-report.
**How**: put the sensing and interpretation burden on the technology and the caregiver's observations, not on the person being helped. Meet him at the *what* — start from observed behavior, not a diagnostic label.
**Trade-offs**: caregiver-labeled signal carries the caregiver's interpretation; validate against outcomes.

## Shah's Rope-and-Car Principle
**When**: a system must survive real-world conditions it wasn't trained on.
**How**: design the protocol so it can be perturbed and still function, rather than optimizing for clean-condition accuracy.
**Trade-offs**: costs benchmark performance to buy field robustness.

## Tyrangiel's Four-Step Civic Protocol
**When**: you are a non-expert deciding how to engage with AI.
**How**: (1) flirt with the tools enough to know real capability vs. claim; (2) decline features that feel like a solution seeking a problem — non-use is the strongest feedback signal; (3) price the swap (data, attention) and read the terms; (4) back AI that amplifies human judgment, oppose AI that replaces it.
**Trade-offs**: individually slow; the mechanism is aggregate, not personal.
