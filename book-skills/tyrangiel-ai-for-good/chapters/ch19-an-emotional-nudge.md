# Chapter 19: An Emotional Nudge

## Core Idea
AI becomes public policy when it closes a feedback loop citizens never had — and it survives government when you deliberately make it look too small and too accidental to be worth killing.

## Frameworks Introduced

- **The Two-Nudge Ladder (Prairie Robotics)**: Pair machine detection with graduated behavioral feedback, escalating from generic instruction to personal evidence.
  - When to use: When a public service depends on thousands of individual behaviors you can now detect but historically couldn't attribute.
  - How: (1) Detect the violation automatically at the point of occurrence; (2) send an *educational nudge* — friendly illustration, "Do you know what to throw?", plus guidance and an app prompt; (3) send an *emotional nudge* — an actual low-resolution photo of the resident's own nonrecyclable item, with a neutral, non-accusatory sentence about what the crew noticed; (4) deliver within three days so the feedback is still attached to the behavior.
  - Why it works: Personal, timely, evidence-based feedback outperforms generic instruction — the emotional nudge roughly doubled the contamination reduction of the educational one. Failure mode: identity error. The photo can be right and the attribution wrong (the dog-poop-in-a-bag neighbor), so the copy must describe the cart, not accuse the person.

- **Walls's "Make It Seem Less Big" Rule**: Reduce the perceived scale of an AI initiative until it falls below the threshold that triggers institutional review.
  - When to use: Any AI pilot inside a budget-cycle-bound public institution where visibility invites veto.
  - How: Start in "softer places where nobody's paying attention" (Walls's phrase); don't try to beat the hard parts of the system into working your way; communicate slowly and clearly enough that no one is surprised, but never frame it as transformation; let it look accidental even when it isn't; ship the outcome first and ask for scale afterward.
  - Why it works: In government, opposition is mobilized by narrative, not by cost. A program described as "AI transforming municipal services" acquires enemies; one described as sanitation tooling doesn't. Failure mode: invisibility also means no institutional champion — Walls's colleagues responded to a national award with "Cool, Cliff."

- **Dietrich's Utility Feedback Test**: Ask whether the citizen ever receives a signal about their own behavior in this domain.
  - How: Compare against water, electricity, home heating — all send monthly usage feedback. Any service with no equivalent signal (recycling, tree clearance, road wear) is a candidate for AI-generated feedback loops.

## Key Concepts
- **Educational nudge**: Generic instructional postcard about what is and isn't recyclable, triggered by detected contamination.
- **Emotional nudge**: Postcard showing a photograph of the resident's own contaminant, observed at the truck.
- **Contamination**: Nonrecyclable material in a recycling load; above a threshold the processor rejects the entire load.
- **Load rejection cascade**: One neighbor's error forces the city to pay twice — to collect the rejected material and again to dispose of it.
- **Prairie Robotics**: Saskatchewan company (CEO Sam Dietrich, CTO Stevan Mikha) combining hopper cameras, GPS, and image recognition trained on hundreds of thousands of contaminant photos.
- **PASER**: Pavement surface evaluation and rating — a labor-intensive periodic road survey Walls saw as an obvious AI image-recognition target.
- **Bureaucratic angel**: An official at another agency who redirects existing funds so the buyer never has to run a procurement (here, Michigan EGLE moving money via The Recycling Partnership).
- **Benign neglect**: Leadership inattention that functions as protection for a small program.

## Mental Models
- Think of AI image recognition on existing municipal vehicles as **free continuous inspection**: police and sanitation trucks already drive every road daily, so any periodic manual survey (potholes, tree clearance, faded stop signs, hydrant paint) is a candidate for conversion into a live data stream.
- Use **"there's no such thing as an impulse buy"** as the real constraint in government procurement: a reasonable price is irrelevant if the budget cycle is annual. Solve for the funding path before solving for the price.
- Think of a delayed launch as **acclimation time**, not slippage — East Lansing's supply-chain delay accidentally gave residents months to absorb the idea before the first postcard arrived, which Walls counted as decisive.

## Anti-patterns
- **Announcing AI as transformation**: Overcommunicating that "your whole world is changing because of AI" invites the debate-haggle-neuter-kill cycle. Communicate the service change, not the technology.
- **Waiting for budgeting season**: Deferring a small pilot into the formal cycle exposes it to council debate and performative haggling, usually ending in a neutered or dead program.
- **Fighting the hard parts of the system head-on**: Trying to force rigid procurement or IT gates to bend costs more political capital than the pilot is worth.
- **Assuming public backlash before testing for it**: Experienced officials braced for outrage that never came — 336,000 stops produced two complaints.

## Worked Example
Cliff Walls, five weeks into being East Lansing, Michigan's (pop. ~47,000) environmental sustainability and resiliency manager — a stormwater specialist who inherited recycling because there's one environmental person for everything — took a cold-outreach meeting from Prairie Robotics because he "didn't know any better." Their rig: hopper-mounted cameras plus a GPS transmitter in the cab, running image recognition trained on contaminant photos, auto-generating postcards within three days. Price: $8,000 for a one-truck, 24-week trial — trivial anywhere but government. Michigan's Department of Environment, Great Lakes, and Energy (EGLE) redirected $30,000 already committed to The Recycling Partnership, covering two trucks plus printing and mailing; East Lansing did no political wrangling and no paperwork. Supply chain delays pushed the fall 2022 start back, accidentally giving 7,000 households months of advance notice. Over 24 weeks and 336,000 stops: educational nudge produced 11% less contamination and 32% more participation; emotional nudge produced 23% less contamination and 45% more set-outs versus control; postcard error rate 0.5%; two complaints total. A Recycling Partnership survey found 86% viewed it positively. The hidden win: AI plus GPS generated a citywide dataset of participation and contamination patterns, letting sanitation redeploy crews against live trends — "like having the lights turned on." AI-assisted recycling entered the city budget without argument; Prairie Robotics now holds contracts with nearly forty cities.

## Key Takeaways
1. Pair detection with personal, timely feedback — evidence about *your* behavior outperforms instruction about behavior in general.
2. Solve the funding path, not the price. Look for an adjacent agency or nonprofit already holding money earmarked for your outcome.
3. Size the announcement to the risk, not the ambition. Inform residents plainly; don't frame it as a technological revolution.
4. Start where nobody is watching — soft, low-stakes services — and let the result argue for expansion.
5. Harvest the byproduct data. The operational dataset (where, when, how often) is often worth more than the headline metric.
6. Naivete is an asset in institutional innovation when paired with domain expertise: enough knowledge to recognize a solution, not enough scar tissue to assume it's impossible.
7. Once one AI image-recognition workflow works, inventory every other periodic manual inspection your org runs — they share the same shape.

## Connects To
- **Ch 20 (AI Fight Club at the IRS)**: Danny Werfel runs the Walls "nothing to see here" strategy at 75,000-person scale — deliberate invisibility as a survival tactic.
- **Ch 21 (Dilettantes and Vandals)**: The direct inverse — DOGE's maximum-visibility, contempt-driven approach produced no shipped software.
- **Nudge theory (Thaler & Sunstein)**: Prairie Robotics operationalizes choice-architecture nudges with machine detection supplying the trigger.
- **Agile development**: Walls himself wondered whether he'd invented a policy version of iterative delivery — small releases, real feedback, expand on evidence.
