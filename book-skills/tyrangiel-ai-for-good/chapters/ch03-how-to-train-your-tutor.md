# Chapter 2: How to Train Your Tutor (While Slowly Losing Your Mind)
*Part 1 — I Believe the Children Are Our Future*

## Core Idea
A large language model optimizes for fluency, not truth — so turning one into a tutor is not an engineering problem but a grinding, statistical exercise in writing and re-testing English prompts against a target that keeps moving underneath you.

## Frameworks Introduced

- **The Ten-Run Prompt Test (DiCerbo's Method)**: Never accept a prompt on one good result. Because language models are probabilistic, judge a prompt by its hit rate across repeated runs of identical input.
  - When to use: any time an LLM output will be shown to real users, especially where a bad output causes harm (a child taught wrong math).
  - How: (1) write the prompt; (2) run it ten times on the same input; (3) count how many outputs you'd actually ship — DiCerbo's example was six of ten; (4) identify which clause of the prompt the four failures ignored; (5) reword that clause specifically and re-run the full ten; (6) repeat. Treat a prompt as a version to be tracked, never as a solved artifact.
  - Why it works: it measures the distribution rather than a sample, which is the only honest evaluation of a stochastic system. Failure mode: without version tracking and environment labeling you lose track of which prompt is live where — precisely the frustration Khan Academy hit as prompt count grew.

- **The Role-Constraint Prompt Pattern**: Assign the model a role, name the counterparty role, and state the prohibited behavior. Sal Khan's early prompt: pretend you're a tutor, here's a math problem a student is working on, help them figure it out without giving away the answer.
  - When to use: whenever the default assistant behavior (be helpful, supply the answer) is the wrong behavior for your domain.
  - How: role + counterparty + explicit prohibition + the artifact in question. Then escalate to the harder behaviors — when to give a hint, when to ask a probing question, when to encourage.

- **Khan's Tutoring Script**: The human behavior being cloned — never say right or wrong; say "That's not exactly what I got. How did you get your answer? Can you explain it?"
  - When to use: as the target specification when encoding pedagogy into a model.
  - How: capture the specific verbal moves of the best human practitioner you have, then treat prompt iteration as the attempt to reproduce those moves at scale. Khan wanted the blend of knowledge, nuance, care, and enthusiasm he gave his cousins, delivered to every kid in the world.

## Key Concepts
- **Large language model**: a giant prediction engine trained to guess the next word based on everything preceding it — GPT was fed hundreds of billions of words from books, Wikipedia, papers, appliance manuals, news, Reddit threads, and help desk transcripts.
- **Transformer**: the 2017 deep learning architecture behind GPT (generative pre-trained transformer) that processes all words at once, weighting each numerically against every other, rather than reading in order.
- **Context weighting**: why the model knows a "hot dog" isn't a "warm canine" — and why the same logic extends to images, sound, and video, anything convertible to data.
- **FLOPs**: floating point operations; independent analysts estimate training GPT-4 took roughly 10^25 of them — tens of trillions of trillions of math steps.
- **Fluency over truth**: the model has no mechanism to assess correctness, which is why it can explain thermodynamics accurately and then confidently invent new laws of it.
- **Probabilistic output**: a fresh calculation for every input, so identical prompts produce varied responses.
- **Prompting**: giving the model direction in plain English about what to do or how to behave — Khan Academy's engineers described it as pioneering work in a new coding language.
- **Fine-tuning**: the post-training phase OpenAI was in when Khan Academy shipped over its proprietary corpus — too late to add new training material.
- **API integration**: essentially the only conventional engineering required; Khan's verdict was that from a coding perspective there was very little work.
- **Prompt drift from model updates**: OpenAI tuned GPT-4 continuously for goals unrelated to Khan Academy, and each update could invalidate weeks of prompt progress with fresh hallucinations.

## Mental Models
- **Think of ChatGPT as Teller's definition of magic with compute swapped in for time** — "someone spending more time on something than anyone else might reasonably expect," except it's computing power. The awe and the trick are the same thing.
- **Use "the model optimizes for fluency, not truth" as your default risk frame**: it doesn't fact-check because it doesn't understand facts, so every accuracy guarantee must come from your system, not the model.
- **Think of a prompt as a probability distribution, not a setting** — you don't configure it, you tune its hit rate.
- **Use the "corporate elopement" warning when partnering with a much faster company**: no kickoff meeting, no contract, no roadmap, and only so much attention to go around. Assume you will get less support than the relationship implies.

## Anti-patterns
- **Contributing your best asset before understanding the partner's stack**: Khan Academy shipped years of proprietary math problems, history lessons, and reading essays hoping to improve the model's accuracy. OpenAI "yeah thanks"-ed them — GPT-4 was already trained and the research team wasn't reopening it for anyone.
- **Enshrining a prompt that worked once**: a successful run is a sample, not a result.
- **Managing prompts without version control**: Khan Academy could not tell which versions were live in which test environment, and the frustration scaled with the prompt count.
- **Assuming your vendor's model is a stable foundation**: it was still an experiment being tuned toward someone else's goals, and no one could promise when stability would arrive despite the March 2023 launch date.
- **Expecting a marriage of equals**: Khan Academy was lean, mission-defined, hands-on, with one AI partner and maybe two engineers with AI experience; OpenAI was simultaneously launching with Duolingo, Stripe, Morgan Stanley, and others, while chasing AGI.

## Worked Example
**Khan Academy's GPT-4 build, mid-2022 to March 2023.** The partnership began with none of the usual rituals — no executive vows, no legal agreements, no engineering kickoff. DiCerbo's account of the product conversation: "Uh, let's start?" She calls it shockingly informal, with no big-picture feature roadmap and roughly two engineers who had AI experience.

The team's first instinct — shipping their proprietary content corpus to improve accuracy — was politely declined, because the training window had closed and OpenAI had moved to fine-tuning. Once connected to GPT-4 via API, there was essentially no traditional coding left. Khan's read: "That was the first real understanding that we were in science fiction world."

So the work became weeks of prompt writing in English. Khan's tutor-role prompt stopped the model blurting answers fairly quickly. The hard part was everything after answers: teaching the model when to hint, when to ask a probing question, when to encourage — how to be Sal. That got messy, because the model recalculates every response. DiCerbo's loop was to run a promising prompt ten more times, find it delivered six acceptable outputs, then keep tweaking the specific clause the four failures ignored and run it again.

Meanwhile the ground moved. Prompt versioning broke down as the library grew, nobody could tell which version was live in which environment, and every OpenAI tuning update could trigger a fresh cascade of hallucinations that obsoleted earlier progress. OpenAI's assurance was that this was normal and stability would come as the March 2023 launch approached — with no one able to say when.

## Key Takeaways
1. Evaluate prompts by hit rate over ten identical runs, not by a single output you liked.
2. Build prompt version control before your prompt library grows — you will need to know which version is live in which environment.
3. Specify the model's role, the user's role, and the forbidden behavior explicitly; the default assistant behavior is answer-giving.
4. Capture your best human practitioner's exact verbal moves first; that transcript is your specification.
5. Never assume accuracy comes from the model — it optimizes for fluency and cannot fact-check itself, so guardrails belong in your system.
6. Treat a vendor's pre-launch model as a shifting foundation, and budget for rework after every update.
7. When partnering with a far larger and faster company, expect informality and scarce attention; get your own people close to the technology rather than waiting for support.

## Connects To
- **Ch 1 (Ed's Dead)**: this chapter is the execution of Khan's "turn objections into features" list — fixing the math, the hallucinations, and the answer-giving.
- **Introduction**: the puppy metaphor and the "speed, not sentience" framing get their mechanical explanation here.
- **Test-driven development**: the ten-run loop is the LLM analogue — a failing case drives the next prompt revision.
- **Vendor lock-in and platform risk**: building on a partner's unstable, continuously tuned model.
