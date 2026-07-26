# Chapter 18: The Tragedy of the Frozen Middle

## Core Idea
Government cannot adopt AI until it can adopt software, and it cannot adopt software because a rule-bound acquisition workforce — "the frozen middle" — is not incentivized to. The solutions have been written down repeatedly since 1982; the missing ingredients are congressional courage and an implementation layer with any reason to move.

## Frameworks Introduced

- **The Frozen Middle** (named in the Defense Innovation Board's SWAP Study): the mass of acquisition and program personnel between leadership intent and actual execution whose inertia blocks reform.
  - When to use: diagnosing why an organization with good strategy and willing leadership still changes nothing.
  - How to read it: the report explicitly questions neither this group's integrity nor its patriotism. They are simply not incentivized toward modern software acquisition, and the inertia they represent is a profound barrier to change. Roughly thirty thousand people do acquisitions, trained by a dedicated school (the Federal Acquisition Institute) in rules so complicated no human understands them — Schmidt's joke was that AI's primary use was to understand acquisition rules.
  - Why it works as a diagnosis: it relocates the problem from villains to incentives, which means the fix is incentive and process design, not replacing people.
  - Failure mode of ignoring it: leadership keeps commissioning reports (fifteen prior software studies since 1982, all reaching similar conclusions) while nothing reaches execution.

- **Gall's Law and its limit** (John Gall, *Systemantics: How Systems Work and Especially How They Fail*): every complicated system that works originated from a simple system that worked.
  - How it applies: government spending began simply — taxpayers pay only for what can be documented and explained. That worked for munitions, highways, and the postman. Growth added rules to prevent corruption, and rules are never removed, so speed and innovation were traded away. The system creaked but held.
  - The limit: when something indispensable arrives that cannot be easily documented or explained — software, and now AI — it defies the original premise and the system freezes.

- **Schmidt's Software Precondition**: "AI is fundamentally software. You can't have AI in the government or the military until you solve the problem of software in the government and military."
  - How: adopt the commercial loop Schmidt described — rapid prototyping with a small engineering group, heavy user surveys, continuous refinement, iteration, deployment. His verdict: every element of that is effectively illegal in the federal government.

- **SWAP Study recommendations** (Defense Innovation Board): treat software as a living thing that crosses budget lines; evaluate cost against speed, security, functionality, and code quality; collect data from weapons systems and build a secure space to evaluate effectiveness; then get Congress to ratify the changes.

- **Pahlka's Dysfunction Loop**: absurd processes are handed to public servants who are judged on compliance with the absurdity. Do the job correctly and the nation gets obsolete, overpriced software. Deviate or err, and politicians hold hearings and attack them — while never changing the process. Each round of recrimination drives more capable people out of public service.

## Key Concepts
- **Gall's Law**: complicated working systems evolve from simple working systems; they cannot be designed complex from scratch.
- **Defense Innovation Board**: fifteen-member advisory body launched by Defense Secretary Ashton Carter in 2016; Eric Schmidt served four years, joined by Jennifer Pahlka.
- **SWAP Study**: the board's "Software Acquisition and Practices" white paper — a solutions-based critique of federal software buying.
- **OIRA (Office of Information and Regulatory Affairs)**: the small office reviewing America's most significant rule-making, whose staff commonly read the guidance as requiring a six-month review before a software user survey is permitted.
- **Bureaucratic torture**: Tyrangiel's framing — a six-month approval for a routine practice on a product that never stops moving is worse than an outright ban.
- **Unused authorities**: the workarounds and special authorities Congress has granted the Defense Department, mostly forgotten or ignored by public servants too scared to use them.
- **Rules that are added and never removed**: the accretion mechanism that converts anti-corruption safeguards into paralysis.

## Mental Models
- Use Gall's Law to predict where reform will fail: the freeze happens at the first thing the original documentation premise cannot describe.
- Think of the frozen middle as an incentive vacuum, not an obstruction: nobody there is rewarded for speed, and everybody there is punished for error.
- Use "is this practice legal, or merely six months slow?" as the real test — de facto illegality by process delay is the more common blocker.
- Treat repeated identical reports as the finding: sixteen studies with the same conclusions means the diagnosis is solved and the ratification and execution layers are the problem.

## Anti-patterns
- **Commissioning another study**: fifteen prior military software reports since 1982 reached similar conclusions; another one changes nothing without congressional ratification and middle-layer incentives.
- **Granting authorities without cover**: special authorities go unused when the people holding them fear being the one who took the risk.
- **Judging public servants on compliance rather than outcomes**: it guarantees obsolete, overpriced software and drives out the competent.
- **Post-failure hearings that never touch the process**: recrimination without process reform is pure attrition on the workforce.
- **Buying AI before fixing software practice**: the AI initiative inherits every pathology of the acquisition system underneath it.

## Worked Example
A few months before Palantir sued the United States in 2016, Defense Secretary Ashton Carter called Eric Schmidt to join a new Defense Innovation Board. Schmidt declined; Carter told him to do it anyway. The fifteen-member board's biggest takeaway was that the entire federal apparatus had accidentally evolved to resist software. Schmidt — whose early career at Bell Labs and Sun Microsystems was much like Aaron Jaffe's work at Palantir — laid out the ordinary commercial loop of prototyping, user surveys, and continuous deployment, then said every piece of it is illegal in the federal government. The board produced the SWAP Study, a stylish, solutions-oriented critique with common-sense recommendations, and named the obstacle: the frozen middle. On the same board sat Jennifer Pahlka, Obama's deputy CTO, central to the healthcare.gov rescue, and the person Governor Gavin Newsom summoned in 2020 when California's unemployment insurance system buckled under COVID. Her working assumption about the people she helps: they are having a nervous breakdown. Most of her daily work, she says, is therapy — telling public servants their feelings are normal. She dedicated *Recoding America* to public servants everywhere, telling them not to give up; people have brought it to her to sign and started crying. Schmidt, after four years on the board, closed his conversation by insisting he would not make an emotional argument, only that government will perform suboptimally until it adopts industry software practices. He sounded emotional.

## Key Takeaways
1. Fix software acquisition before promising AI adoption — AI is software, and it inherits the acquisition system it is bought through.
2. Locate the frozen middle in your own organization: the layer with no incentive to move and every incentive to comply.
3. Change incentives, not personnel — the SWAP authors explicitly refuse to impugn the integrity or patriotism of the people they identify as the barrier.
4. Audit which existing authorities and workarounds already permit what you want; most are unused out of fear, not prohibition.
5. Count how many times the same recommendation has been made. If it is sixteen, stop analyzing and work the ratification and execution layers.
6. Give people political cover, or the safeguards you built against corruption will keep functioning as safeguards against speed.

## Connects To
- **Ch 16 (Brief Moments for Exceptional Things)**: Jaffe's "exceptional to ordinary" transition is the frozen middle refreezing after a crisis thaw; Perna's "bullshit umbrella" was the cover this chapter says is normally absent.
- **Ch 17 (Lululemon in the Iron Triangle)**: Palantir's FASA lawsuit is one company forcing the frozen middle to justify itself on the record.
- **Jennifer Pahlka, *Recoding America***: the book-length version of the dysfunction loop.
- **Agile development**: the industry practice Schmidt says federal process makes effectively illegal.
- **Institutional accretion / regulatory ratchet**: the general pattern of rules being added and never removed.
