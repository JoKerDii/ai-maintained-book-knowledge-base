# Chapter 1: Ed's Dead
*Part 1 — I Believe the Children Are Our Future*

## Core Idea
EdTech's graveyard exists because institutions bought vendor promises instead of building on mission and expertise they already trusted; Sal Khan's counter-move was to treat every objection raised against AI as a product feature to be built, rather than a reason to refuse or a risk to ignore.

## Frameworks Introduced

- **Khan's "Turn Objections into Features" Rule**: When the internal debate over adopting a risky technology splits your organization, don't vote and don't overrule — write down every danger the opposition names and convert each into a specific feature on the roadmap.
  - When to use: adopting a powerful, unproven technology where the skeptics are competent and the risks are real but unquantified.
  - How: (1) put the technology in the hands of the whole leadership team, not just believers — Khan requested fifty GPT-4 logins for a hackathon; (2) let the argument run for hours until positions are fully articulated; (3) transcribe each objection as a named defect (bad math, hallucinations, fabricated sources, training-data bias, inappropriate content for minors); (4) convert each into a build item — transparency, guardrails, moderation, anchoring outputs on your own vetted content; (5) accept explicitly that residual risk never reaches zero.
  - Why it works: it keeps the skeptics inside the project as the specification writers rather than pushing them into opposition, and it produces a concrete safety roadmap instead of a posture. Failure mode: only works if leadership genuinely intends to ship the features — otherwise it's a listening exercise that buys consent and delivers nothing.

- **Khan's Tutor-Not-Teacher Leadership Model**: Khan leads by explaining, encouraging, and nudging rather than imposing authority or setting expectations — colleagues call the patience legendary and occasionally infuriating.
  - When to use: decisions where you need the organization's genuine judgment, not compliance, because you don't yet know the right answer.
  - How: stage the decision as a Socratic debate (Khan used a distributed-team hackathon in Mountain View), give everyone hands-on access to the thing in question first, and let the room converge before you state your position.

- **The Reputation-as-Stake Test**: Before a partnership, ask what the other side gains from your credibility, and price that asymmetry in.
  - When to use: any collaboration where one party's main contribution is trust rather than capital or technology.
  - How: name explicitly what they get (OpenAI would be aligning itself with the paragon of educational integrity), name what you're wagering ("this is my life's work"), and only proceed if you control the product's guardrails.

- **The Saying-No Discipline**: Khan passed on GPT-3 in early 2021 when Greg Brockman first offered it, because the model showed glimmers of intelligence and then "roll[ed] into a corner and headbutt[ed] itself." He engaged only when the capability jump was demonstrable.
  - When to use: repeated vendor overtures during a hype cycle.
  - How: decline until you can personally verify a capability that maps to your mission; re-evaluate on each new offer rather than on each new announcement.

## Key Concepts
- **Ed**: the Los Angeles Unified School District AI chatbot, launched March 2024, meant to give students and parents one assistant across grades, attendance, lunch menus, bus times, and tutoring.
- **AllHere Education**: Ed's vendor — furloughed most staff June 2024, whistle-blower data-mishandling allegations in July, Chapter 7 bankruptcy in August, founder Joanna Smith-Griffin arrested in November on securities fraud, wire fraud, and aggravated identity theft charges (she pleaded not guilty). The $6M LAUSD contract evaporated.
- **The EdTech graveyard**: Summit Learning (Zuckerberg-backed, screen-heavy, data-collection backlash), Knewton (claimed AI could predict student needs, didn't predict its own collapse), AltSchool (ex-Google exec, $150M+ raised, a few thousand students educated).
- **Khan Academy**: nonprofit learning platform, 190M registered users in 190+ countries, ad-free, spanning pre-K phonics to AP courses to adult financial literacy.
- **Districts program**: Khan Academy's 2019 offering linking students, teachers, administrators, and state boards — ~$15/student/month, 560 districts, focused on the poorest schools.
- **Hallucination**: the model inventing facts, and on request inventing sources to support them.
- **Sycophancy under pressure**: GPT-4 trained as an assistant, not a tutor, would apologize and defer if a user insisted 7 + 3 = 11.
- **Learning styles**: the visual/auditory/kinesthetic theory that feels right and lacks research support — Kristen DiCerbo's trick question, which GPT-4 answered correctly by pointing to retrieval, practice, and classroom design instead.
- **Anchoring on your own content**: Khan's proposed mitigation — grounding model outputs in Khan Academy's vetted material to constrain error.

## Mental Models
- **Use the "cheerful machete" test on any new platform**: Ed was sold as cutting through LA's software thicket but was added on top of it. If the new tool doesn't remove tools, it is more thicket.
- **Think of a partnership offer as a wager on two assets**: their technology and your reputation. The graveyard is full of failed bets, but few were fused to one person's name.
- **Use "the secret to integrity is saying no a lot"** as the default posture during a hype cycle — engagement is the exception you justify, not the baseline.
- **Think of adoption as non-optional and the ethics of the adopter as the real variable**: Khan's conclusion was that schools wouldn't get to choose whether AI arrived, only who supplied it — so the organizations that actually care should move first.

## Anti-patterns
- **Superintendent-launch theater**: Carvalho declaring Ed "our nation's very first AI-powered learning-acceleration platform" — a claim that was untrue, staged with an inflatable mascot, months before the vendor's collapse. Launch spectacle substitutes for diligence.
- **Outsourcing the mission to a startup with unverified finances**: LAUSD had no visibility into AllHere's solvency or data handling until a whistle-blower and a bankruptcy filing supplied it.
- **Adopting software that takes student data with it when it dies**: for-profit EdTech that jacked up prices or disappeared without warning is exactly the gap Khan Academy's Districts program was built to close.
- **Assuming an assistant model is a tutor**: an assistant optimizes for user satisfaction, so it hands over answers and folds under contradiction. Tutoring requires the opposite behavior and must be explicitly instructed.
- **Deferring the risk inventory**: the Khan team hadn't even begun cataloguing training-data bias or what a twelve-year-old could get the model to tolerate — the point is that they named the unexplored risks out loud rather than letting them stay invisible.

## Worked Example
**Sal Khan and Kristen DiCerbo, GPT-4 preview, summer 2022 → hackathon decision.** Khan declined Brockman's GPT-3 invitation in early 2021. When Brockman returned in summer 2022, adding Sam Altman and a cryptic hint of progress, Khan and DiCerbo (Khan Academy's chief learning officer) signed NDAs and joined a Zoom, becoming among the only people outside OpenAI to know GPT-4 existed — six months before GPT-3.5 even reached the public.

Khan tested it on an AP biology multiple-choice question: the model matched his answer, explained its reasoning, explained why each distractor was wrong, then generated ten more well-written questions on demand. DiCerbo probed pedagogy instead of content, asking whether teachers should tailor instruction to learning styles; the model correctly rejected the premise and offered evidence-backed alternatives. Both told the story separately and both broke into the same disoriented post-rollercoaster laugh a year later.

Their feedback to Brockman was split: clearly valuable for Khan Academy's content team generating curriculum-aligned questions, but unacceptable for students because it gave away answers. OpenAI's engineers taught them the fix in one line — tell the model it is a tutor and the user is a student, and forbid giving the answer. It mostly complied.

Khan went home convinced Khan Academy could be rendered obsolete, but didn't know what to do. Rather than decreeing a direction, he obtained fifty GPT-4 logins and staged the next leadership hackathon as a Socratic debate. The room split: half saw the fulfillment of everything they'd tried to scale — personalization, mastery, tutoring, engagement; half raised the math failures, the sycophancy, the hallucinations and fabricated citations, the unexamined bias, and the child-safety exposure. Hours of "spirited debates" later, Khan concluded adoption was inevitable and that the right question was who would supply it — closing with the instruction to write every danger down and turn it into a feature: transparency, guardrails, moderation, fixed math, fixed hallucinations, and anchoring on Khan Academy content.

## Key Takeaways
1. Convert every credible objection into a named feature; a skeptic with a build item is an asset, a skeptic who was outvoted is a liability.
2. Verify a capability yourself before engaging a hype-cycle partner — and be willing to say no more than once.
3. When your contribution to a deal is trust, you are the one taking the larger risk; keep control of the guardrails.
4. Grade a new platform on how many tools it retires, not how many features it adds.
5. Assume the general-purpose model is trained to please, not to teach; specify the pedagogical behavior explicitly.
6. If a technology's arrival is inevitable in your sector, the organizations with the strongest ethics have an obligation to move early rather than abstain.
7. Diligence on a vendor's finances, data handling, and survivability matters as much as its product demo — Ed's failure was corporate, not technical.

## Connects To
- **Introduction**: Perna's definition-first vendor test is exactly what LAUSD skipped and Khan applied.
- **Ch 2 (How to Train Your Tutor)**: the "turn objections into features" list becomes the prompt-engineering grind of actually building it.
- **Innovator's dilemma (Christensen)**: Khan's fear that Khan Academy would be rendered obsolete by a wave it could instead ride.
- **Principal-agent problems in public procurement**: a $6M district contract with no visibility into vendor solvency.
