# Chapter 6: Kids Say the Darndest Things

## Core Idea
The people the product is built for give the most accurate review of it — and their verdicts split by need, not by age or aptitude: Khanmigo is transformative for the student who freezes or whose parent can't help, and merely adequate for the student who already has a great teacher.

## Frameworks Introduced

- **Usherenko's Exposure-Over-Efficacy Rationale**: adopt AI in under-resourced schools even before it demonstrably improves learning, because access itself is the equity outcome.
  - When to use: deciding whether to deploy an immature technology in a low-income district.
  - How: separate two questions — does it improve outcomes now, and will these students otherwise be last to encounter it. Newark's district judged that exposure mattered more than immediate usefulness, and framed it explicitly as an equity issue rather than a learning-gains bet.
  - Why it works / failure mode: it sets an honest, achievable success criterion for a pilot instead of an inflated one. Fails if exposure becomes the permanent justification and efficacy is never revisited — Miranda's standing skepticism ("What promises are being made?") is the built-in check.

- **Miranda's Honest-Sample Rule**: staff the user-research session with skeptics, not showcase students.
  - When to use: any site visit, demo day, or customer interview where you control the roster.
  - How: Principal Neysa Miranda selected students "in her own image" — two fourth graders, two eighth graders — with no interest in showing off or cutting the bot a break. The eighth graders were top performers and debate champions, which made their critique sharper, not softer. Choosing middling students to flatter a visitor is malpractice; choosing prodigies to flatter the product is the same error inverted.

- **Colon's Precision-Asking Instruction**: teach students to formulate specific, detailed requests as a general skill that serves both teacher and bot.
  - When to use: rolling out any interrogative AI to passive users.
  - How: Ms. Colon's framing to her class — I'm not your mom, I can't read your mind; be specific, be detailed; whether you want a response from me or from Khanmigo, think it through and ask with precision. She models it live by constantly prodding students to explain their reasoning so she can see where to help.

- **"Use Whatever Your Brain Likes Best"**: reconcile conflicting instructional strategies by treating them as a menu rather than a contradiction.
  - When to use: when the bot's method differs from the method taught in class.
  - How: fourth-grade teacher Jennifer Cook tells students they will learn from all the strategies and keep the one that suits them — defusing the confusion without discrediting either source.

## Key Concepts
- **Khan Academy Districts**: the paid district-wide program Newark bought in 2022, which produced the highest student engagement in the country within weeks.
- **Narrow pilot**: a deployment focused on a single subject area — Newark's math-heavy profile made it the natural counterpart to Hobart's broad pilot.
- **Session memory wipe**: Khanmigo's deliberate erasure of student context after each session for privacy reasons — the single most-cited student complaint.
- **Self-regulation breakthrough**: the shift from shutting down at the first unknown to continuing to work — DJ's account of what Khanmigo actually gave him.
- **Language bridging**: using the bot to translate and re-explain a problem so a non-English-speaking parent can help with homework — Noor's use case.
- **Strategy mismatch**: the bot adding, dropping, or renaming steps relative to classroom instruction, creating confusion rather than reinforcement.
- **Beating around the bush**: students' name for Socratic evasion that reads as withholding rather than teaching.
- **Passive questioner**: the student who won't or can't formulate a specific request — the limiting factor on an interrogative tool.

## Mental Models
- Think of **AI value as inversely proportional to existing support**: DJ (freezes under uncertainty) and Noor (parent can't help in English) got the most; Stella and Nyla, who have Ms. Colon, got the least.
- Use the **"would you miss it if it vanished?" question** in user research — it separates real dependence from polite approval faster than any satisfaction rating.
- Treat the **privacy/personalization trade-off** as a design decision users can see: Stella's objection is that if the system won't retain data it should stop asking "what do you already know?" — and that the students who most need it can't answer, because they don't know what they don't know.
- Think of a **modality gap** as a hard limit, not a prompt problem: a text-only bot says "distribute from this to this"; Ms. Colon draws the arrows and solves it in space.

## Worked Example
Sal Khan assumed Newark's 2022 Districts signup would never be implemented — a city of 300,000 with a quarter below the poverty line and a reputation for decay. Within weeks Newark posted the highest engagement of any district in the country; Zubovic's team assumed something was broken, then found the district was simply intensely math-focused. That made it the top choice for the narrow Khanmigo pilot.

At First Avenue School in the North Ward — 1,100 students, pre-K through eighth — the visit was hosted by Alan Usherenko, now special assistant for math across fourteen schools, and principal Neysa Miranda. Usherenko had found Khan's YouTube videos in 2009 while failing as a young math teacher, bought whiteboard panels and a projector with his own money, got YouTube unblocked, and built an after-school Khan Academy program whose test scores drew district attention; he later championed Newark's purchase of Districts. Miranda supplied the counterweight: EdTech always promises to cure everything and never does, because you're dealing with unique children.

Miranda produced four skeptics. Fourth graders DJ and Noor found Khanmigo unremarkable — just another part of school — but each named something real. DJ, who shuts down and quits the moment he hits something he doesn't know, said the bot talks to him like a person and gives him confidence not to shut down; the year before, he simply couldn't finish assignments. Noor's mother speaks limited English and learned math differently, so they switch problems into Arabic and have Khanmigo re-explain until her mother can help. DJ's remaining wish — word problems about pro wrestlers — is blocked by the memory wipe.

Eighth graders Stella and Nyla, top performers and debate champions, were unimpressed: not close to an actual teacher; useful only for a formula refresher or post-hoc explanations; confusing when its steps diverge from class; alternately evasive and lecturing; and impersonal by design. Their teachers thought the kids were harsh but agreed on substance — Cook with the "use whatever your brain likes best" reframe, Colon with an echo of Buffington in Hobart: students need to be taught to ask better questions, because most are passive. The joint verdict from Usherenko and Miranda: promising, imperfect, improving, and desperately in need of humans to succeed.

## Key Takeaways
1. Recruit skeptics for user research and ask what they'd miss if the product disappeared — you learn more from a debate champion's teardown than a demo-day success.
2. Expect the largest gains at the margins: students who freeze, and students whose home support can't reach the material in English.
3. Deploying to under-resourced users can be justified by exposure and equity — but state that as the criterion, and revisit efficacy later.
4. Reconcile the bot's methods with classroom instruction explicitly, or the mismatch becomes confusion rather than reinforcement.
5. If you strip memory for privacy, redesign the interaction around that constraint — don't keep asking users to re-supply what you refuse to store.
6. Know what your modality can't do; text cannot substitute for a teacher drawing the arrows in space.
7. Question-asking is the prerequisite skill for interrogative AI, and it has to be taught alongside the tool.

## Connects To
- **Ch 5 (Get Buffington)**: Newark is the narrow pilot to Hobart's broad one, and Colon's conclusion about question-asking independently confirms Buffington's.
- **Ch 4**: the memory wipe, the Socratic no-answers rule, and the guardrails students find annoying are the deliberate design choices made pre-launch.
- **Zone of proximal development / scaffolding**: DJ's non-shutdown is scaffolding working; Stella's "kids who don't know what they don't know" is the case where it can't start.
- **Digital equity**: access to emerging tools as an outcome distinct from measured learning gains.
