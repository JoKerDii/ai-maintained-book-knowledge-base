# Chapter 21: Dilettantes and Vandals

## Core Idea
DOGE had the mandate, the money, the talent, and the technology to prove AI could fix government — and shipped nothing, because it was designed to demonstrate that government can't work rather than to make it work.

## Frameworks Introduced

- **POSIWID — "The purpose of a system is what it does"** (Anil Dash's formulation, applied by Tyrangiel):
  - When to use: Whenever an institution's stated mission and observed behavior diverge — evaluating a reform effort, a reorg, an agency, or your own team.
  - How: Ignore mission statements, org charts, and stated intentions. List what the system actually produced. Name that output as the purpose. Then ask who the audience for that output is.
  - Applied: DOGE's method was arrive, break things, leave — so its purpose was performance art disguised as policy, performing "government is useless" for an audience already convinced. The same test indicts the prior system: an IRS that left taxpayers on hold behind opaque friction was "a service that doesn't serve," even while employing tens of thousands of seemingly unfireable people.
  - Why it works: It's unfalsifiable by rhetoric — the more a system insists on its intentions, the more the test cuts.

- **The Collaboration Gate for Public-Sector AI**: Any real government AI fix requires messy human coordination, so an organization unwilling to do that work cannot ship regardless of technical talent.
  - How: Before scoping a fix, enumerate the parties whose cooperation the change requires — in Lavingia's VA case: the employees who manage veterans' care, the IT buyers, the sprawling hospital network, and members of Congress fielding constituent complaints. If the sponsoring org refuses that work, the technical plan is dead no matter how good the ROI.
  - Failure mode: DOGE's bosses told Lavingia they weren't interested in that kind of work and redirected him to contract cuts and layoffs.

- **The Self-Fulfilling Prophecy Choice** (the chapter's closing frame): The question is not whether AI can fix the federal government — it can — but whether a country wants systems designed to work or systems designed to prove government can't work. Both prophecies fulfill themselves.

## Key Concepts
- **DOGE (Department of Government Efficiency)**: Created by executive order on day one of Trump's second term, Elon Musk as de facto leader; premised on AI as the solution to nearly all federal incompetence.
- **Policy by provocation**: An agency created in contempt of other agencies, where the provocation is the product.
- **Ideological hiring screen**: Lavingia was told DOGE wouldn't hire anyone who hadn't voted for Trump — a possible violation of at least three federal anti-discrimination-in-hiring laws.
- **Federal Records Act**: Requires agencies to capture and preserve electronic communications; DOGE ran its recruiting over encrypted Signal texts.
- **United States Digital Service (USDS)**: DOGE's Obama-era predecessor, whose hiring process was so slow and confusing it lost Lavingia a decade earlier.
- **"A temp agency for software engineers to be deployed across the government to *not* build software"**: Lavingia's verdict on DOGE.
- **The transaction-count fallacy**: Sam Corcos's claim that the IRS should cost what a midsize bank costs because it processes similar transaction volume — ignoring that a $20 ATM withdrawal and a complex tax return differ in kind and in stakes.
- **Reinventing government**: The long lineage of waste-hunting efforts by both parties — Clinton's 1990s initiative, and one Werfel himself led at OMB in the 2010s.

## Mental Models
- Think of **credentials as insufficient, not irrelevant**: DOGE's initial hires had elite software and AI credentials and Musk is a first-rate engineering mind — and still nothing shipped. Capability without willingness to coordinate produces zero.
- Use the **pendulum frame** for institutional reform: dysfunction invites vandalism, vandalism restores sympathy for dysfunction. Werfel's incrementalism is what exists *between* the swings — slower than the private sector, but steady, constrained by laws DOGE ignored and budgets DOGE scorned.
- Think of a **loyalty screen as a talent tax**: filtering to Trump voters eliminated most of the engineering labor pool DOGE needed. Lavingia passed only because he didn't vote that cycle.
- Ask **"who stays to pick up the pieces?"** as the real measure of institutional damage. Pandya's reason for staying, after five interim commissioners and 2,000 lost employees in his division, was exactly that.

## Anti-patterns
- **Arrive, break things, leave**: The defining method. No transition plan, no ownership of consequences, no shipped replacement.
- **Optimizing the wrong layer**: The VA's most profound failure is veteran suicide — 6,407 in 2022, 13% of US suicides from 6% of the population, with ProPublica finding botched or skipped risk screenings — but Lavingia was assigned to hunt fraud, and found none.
- **Hunting fraud instead of inefficiency**: The trillions in waste is a white whale conservatives have chased since the 1930s; the actual money was in inefficiency, which requires collaboration to fix.
- **Compliance shortcuts as a founding culture**: Signal-only comms (Federal Records Act violation), no stated job or compensation, an unlawful political screen. An organization that starts by ignoring rules cannot then demand the system trust it.
- **Freezing work that was about to ship**: Corcos halted the modernization programs Pandya was on the verge of deploying and axed contracts — destroying sunk investment for no delivered alternative.
- **Reorging around engineers**: Redrawing the org chart so engineers manage themselves and everyone else orbits them mistakes a startup topology for an institution with statutory obligations.
- **Twentysomethings lecturing on fixing what they don't understand**: Domain ignorance presented as clarity.
- **Demonizing civil servants**: Many of them shared DOGE's own fantasy — they wished they could move faster.

## Worked Example
Sahil Lavingia — second employee at Pinterest as a teenager, founder of Gumroad (hundreds of millions in creator payments, most operations AI-automated), self-described patriot and Elon fan whose stated dream is to ship software for the US government — joined DOGE after a decade earlier abandoning a USDS application because federal hiring was too slow. DOGE hired him instantly via Signal texts, told him to move to DC without naming his job or pay, and ultimately paid him a few thousand dollars. Assigned to the VA after weeks of waiting, he found no fraud but a clean inefficiency: the VA lets veterans fax health claims, then pays IBM, Booz Allen, and others to scan the faxes into Rich Text Format for claims processors. His fix — ask veterans to upload smartphone photos, write code to automate the transformation, license a document-reading model (he liked Mistral's) — was a few weeks of work saving up to $200 million a year in contractor costs, with enough margin to buy every phoneless veteran an Android and still come out tens of millions ahead. It required collaboration with VA care staff, IT purchasers, the hospital network, and Congress. His bosses weren't interested and sent him back to cut contracts and organize layoffs. He was fired on day 55 for giving an interview about his company. Meanwhile at the IRS: Werfel resigned on Inauguration Day; 25-year-old ex-Databricks employee Gavin Kliger wrote email manifestos urging employees to quit and oversaw the mass firing of those who stayed; Sam Corcos froze Pandya's modernization work. Net AI shipped: none.

## Key Takeaways
1. Judge reform efforts by output, not manifesto — apply POSIWID to DOGE, to the pre-DOGE IRS, and to your own organization.
2. If a fix requires coordination and your sponsor won't fund coordination, the fix does not exist. Test for that before writing code.
3. Fraud is the politically satisfying target; inefficiency is where the money actually is — and inefficiency is a collaboration problem.
4. Ideological or loyalty screens on technical hiring destroy the talent pool you need to deliver.
5. Founding an organization on rule-breaking (records law, hiring law) forecloses the institutional cooperation that shipping requires.
6. Attack the problem that matters most, not the one that fits the mandate — no amount of contract-cutting at the VA addresses veteran suicide.
7. Someone has to stay. The people who endure the vandalism, like Pandya, are what makes recovery possible.
8. Dysfunction and vandalism feed each other; steady, law-constrained incrementalism is the only exit from the pendulum.

## Connects To
- **Ch 20 (AI Fight Club at the IRS)**: The direct casualty — Corcos freezes exactly the modernization Pandya described, and Werfel's incrementalism is the counterexample the chapter argues for.
- **Ch 19 (An Emotional Nudge)**: Walls proved a tiny, quiet, collaborative AI pilot ships; DOGE proved a loud, contemptuous, well-funded one doesn't.
- **Earlier chapters (Perna, Maddox, Karp, Schmidt)**: Completes the taxonomy of postures toward bureaucracy — outrun, sue, exit, hide, and now demolish.
- **POSIWID (Stafford Beer, via Anil Dash)**: Cybernetics-derived test for reading institutions by behavior rather than design.
- **Part 4 ("Only Connect")**: The book pivots from government to the argument that other countries are already using AI to reduce friction and restore trust.
