# Chapter 4: You'll Be Disappointed for a Long Time Until You're Not

## Core Idea
Getting a general model to do a specific job is not a single breakthrough but an accumulation of small, unglamorous adjustments — context, prompts, guardrails, tool offloading — and progress feels flat right up until it doesn't. Build a partner who can hold your team's confidence through that flat stretch.

## Frameworks Introduced

- **Context Stuffing**: surround the system prompt with all the detailed, situation-specific information the model needs, because the model starts every interaction with no memory of the student, the problem, or its own role.
  - When to use: whenever a stateless model must behave like someone who already knows the user and the task — tutoring, support, casework.
  - How: (1) write the system prompt as a job-and-temperament description ("You are Khanmigo, a Socratic tutor; encouraging, patient; you do not give direct answers"); (2) inject the situational stack — course, unit, current concept, known misconceptions, session history; (3) state the fallback behavior for predictable off-ramps ("if the student asks for the answer, redirect to their reasoning"); (4) start manual, then automate injection from real-time curriculum and student data.
  - Why it works / failure mode: it converts a generic predictor into a role-holder. Fails two ways — it's laborious (every grade, state standard, and subject multiplies the drafting work) and it's metered: every token of context is billed on input and output, so over-stuffing at scale can cost more than the product earns.

- **Shieh's "Think Bigger" Test**: if the feature you're scoping could have been built on the previous model generation, you have under-specified the product.
  - When to use: when scoping an AI product against a frontier model still in training.
  - How: list the intended features; ask which ones GPT-3.5-class capability already handles (Khan Academy's initial list — creative-writing helpers, auto-varying math problems — all did); discard those as the ceiling and re-aim at the behavior only the new model's nuance could support, i.e. tutor-like judgment rather than content generation.

- **Shieh's Hub-and-Spoke Sprint**: one AI-fluent person sits at the center of the domain team and absorbs every broken prompt so domain experts never stall.
  - When to use: teaching a subject-matter team to build with a model they don't yet trust.
  - How: five-day co-located sprint; rule is "if a prompt isn't working, give it to me and go work on something else"; the center returns a rough fix — Shieh's "a very ugly shape" — and the domain experts refine it with their own expertise; demonstrate context-stuffing limits, nudging prompts, and adversarial-input spotting live rather than in docs. Belief arrives around day four, and the team then does most of the optimizing itself.

- **Right Tool for the Sub-Task (AI + Python)**: use the language model for what it is good at and hand deterministic work to deterministic software.
  - When to use: any workflow where a fluent-sounding wrong answer is unacceptable.
  - How: Khanmigo kept GPT-4 for mathematical explanation and conversation and routed actual calculation to Python.

## Key Concepts
- **System prompt**: the standing role-and-temperament instruction that runs in the background of every user interaction.
- **Token**: the billing and context unit of a model, roughly four characters of text; cost = input tokens + output tokens.
- **Context window**: the token ceiling per interaction — Khanmigo began on an 8,192-token GPT-4, later 32,768 (~25,000 words).
- **Red teaming**: a military/cybersecurity practice of playing adversary against your own system to surface vulnerabilities before real users do.
- **Adversarial input**: a prompt that overrides a model's purpose ("ignore all previous instructions") or deliberately confuses it with false premises.
- **Hallucination**: confident, fluent output that is wrong — dangerous precisely because the swagger delays detection.
- **Vibes-based evaluation**: DiCerbo's retroactive name for rating model outputs by feel rather than by a defined rubric.
- **Solution strategist**: OpenAI's in-house role combining account manager, solution architect, deployment engineer, and sales.
- **The Goldilocks problem**: too little context makes the product ineffective; too much makes it unaffordable.

## Mental Models
- Think of the system prompt as the job description and context stuffing as **the stack of notes left on the desk** for a substitute teacher — who the student is, what they're stuck on, what happened last session.
- Use the **bicycle model** when judging AI progress: there is no click moment, only trial-by-trial accumulation until you stop explaining to the model and start riding it.
- Treat **model capability as a step function with a long flat approach** — Shieh's line, "you'll be disappointed for a long time until you're not," is the planning assumption, not an excuse.
- Assume **computers are bad at math** unless a calculator is wired in: a language model guesses what a correct-looking answer resembles, which is why it is fluent and wrong at once.

## Anti-patterns
- **Prompting without context**: Khan Academy burned a month getting nowhere because nobody had stuffed the model with student, curriculum, or session detail.
- **Scoping to today's model**: building features the prior generation already handled wastes the partnership and the launch window.
- **Treating a safe deflection as a safe answer**: "that sounds hard, let's get back to math" is a failure on a suicide disclosure; the right behavior is a prevention line or a named adult.
- **Assuming untrained models inherit your institutional care**: ChatGPT, never trained on Khan Academy's vetted history materials, rendered the Trail of Tears as a government-sponsored hike.
- **Sanitized red teaming**: if the session isn't uncomfortable, it isn't finding the edges.
- **Trusting the model with arithmetic** because it is otherwise sophisticated.

## Worked Example
Khan Academy had five months to launch Khanmigo and nothing worked. OpenAI sent solution strategist Jessica Shieh — a McKinsey/Deloitte alum from Taipei who moved her alarm to 4 a.m. for the project. After listening sessions she concluded the model didn't sound like Sal Khan and the feature list was too timid. She ran the team through context stuffing, then a five-day hub-and-spoke sprint that produced the Khanmigo prototype.

Two shocks bracketed the work. On November 30, 2022, OpenAI released ChatGPT publicly without telling Khan Academy; within five days it had a million users, students were cheating, and districts including New York City banned it — while Sal Khan, gagged by an NDA, couldn't respond to reporters. Within a week Kristen DiCerbo reframed it as a blessing: being first to market would have been worse, and the public backlash produced a free list of every guardrail Khanmigo would need. A December on-site red-teaming session at OpenAI forced both teams to say the worst things they could think of; the shared awkwardness built the trust the partnership had been missing.

Then GPT-4 kept failing at arithmetic. Shieh had Khan, DiCerbo, and others test 200 math problems, rating exchanges 7 (perfect) to 1 (never say this again) with model answers attached. The verdict: one of the most sophisticated systems ever built could not be trusted with basic math, so calculations were offloaded to Python. Launch held on March 14, 2023 — with no satisfactory model until 72 hours before. Guardrails shipped alongside: reviewable chat history for parents and teachers, DiCerbo's "lesson hook," and a historical-figures chat with rules (dead for decades, no genocidal maniacs) written specifically to keep Hitler out.

## Key Takeaways
1. Write the system prompt as a role, then stuff context as a per-user situation brief — and budget the tokens before you scale it.
2. Cost-model your context at millions of sessions, not one; nine cents per interaction becomes a national computing budget.
3. Aim your feature list at what only the newest model can do; anything the last generation handled is table stakes.
4. Put one AI-fluent person at the center of the domain team to absorb every failing prompt, and expect belief around day four, not day one.
5. Red-team with real profanity, real distress language, and real curricular landmines; the discomfort is the product of the exercise, and it builds trust as a side effect.
6. Offload deterministic sub-tasks to deterministic tools — fluency is not correctness.
7. Plan for a long flat stretch of disappointment; the schedule should survive not having a working model until days before launch.

## Connects To
- **Ch 3 (Khan Academy's bet on GPT-4)**: this chapter is the execution phase of the partnership formed earlier — the same actors, now under deadline.
- **Ch 5 (Get Buffington)**: everything built here meets real students in Hobart, where the flagging system and answer-leakage failures resurface as field problems.
- **Ch 6 (Kids Say the Darndest Things)**: the deliberate memory-wipe and the model's slightly-different-from-class strategies become the top student complaints.
- **Trust as infrastructure**: Shieh's "the most expensive commodity is trust" — a reputation like Sal Khan's, not a benchmark, is what carried the product through the flat stretch.
- **Retrieval-augmented generation**: context stuffing done manually here is the ancestor of automated dynamic context injection.
