# Chapter 5: Get Buffington

## Core Idea
An AI product's first real test is not the model — it's whether a trusted local authority will absorb the friction of deploying it. Pick the pilot site for the owner, not the demographics of the users, and give the users permission to break the thing.

## Frameworks Introduced

- **Zubovic's Pilot-Site Selection Rule**: choose pilots by who will own the mess, not by who will make the demo look good.
  - When to use: selecting the first real-world deployment of an unproven product.
  - How: (1) start at the hard end of the distribution — Zubovic pushed for Title I schools, arguing those kids are "usually at the back of the line," rather than the tech-adjacent Khan Lab School whose ninth graders opened with "Is this generative AI?"; (2) require prior engagement with your existing product so the pilot isn't also an onboarding; (3) select one broad-usage district and one narrow-focus district to sample two adoption shapes; (4) insist on a single named owner who can personally absorb a bumpy process.
  - Why it works / failure mode: as Zubovic put it, bringing technology into a school means bringing it into the town square — the superintendent and teachers, not the vendor, are the ones explaining it publicly. Fails when you pick a site that flatters the product: representative-of-nobody users generate feedback you can't act on.

- **Founder-Trust Recruitment**: spend the founder's personal reputation deliberately to bootstrap adoption where the product can't yet speak for itself.
  - When to use: pre-launch, under NDA, with nothing demonstrable.
  - How: Khan and Zubovic listed trusted administrators running all-star districts, then Sal Khan called each personally. Khan's own framing — don't overstate the personality, but don't understate it either when you're asking people to buy into something new. Buffington's reasoning closed the loop: if you won't trust Sal Khan, who will you trust?

- **The Push-It Mandate**: explicitly assign students to find the edges of the system.
  - When to use: any pilot where users will probe the system anyway.
  - How: Buffington told students to push the bot and treat the results as data. Reframing adversarial behavior as an assigned job converted breakage into reporting — kids arrived proud of what they'd made Khanmigo do, and accepted the fixes as evidence they'd done their job.

- **Quiet Pilot Containment**: run the pilot below the political waterline until it's worth defending.
  - When to use: deploying something politically flammable inside a public institution.
  - How: Buffington conveyed without stating it that the pilot should stay quiet from the rest of the school, the district, and Indiana's Department of Education — and it did. Trade-off: buys iteration room, forfeits early institutional buy-in.

## Key Concepts
- **Teaching to the middle**: the instinct to aim a lesson at a classroom's mythical average ability, leaving both ends unserved.
- **Differentiation**: meeting students at varying mastery levels with the right content at the right pace — Khanmigo's clearest early win.
- **Title I schools**: schools serving low-income students that receive federal funding to close academic gaps.
- **Flagging system**: automated escalation of concerning student language to teachers — miscalibrated in either direction, it either misses distress or drowns teachers in noise.
- **Coded distress**: euphemisms like "unalive myself" that students use to evade platform suicide detection, easily confused with teen sarcasm.
- **Cross-mode jailbreak**: getting the answer by moving to a less-guarded surface — a geometry student asked the historical-figure Pythagoras to explain his theorem using her homework problem.
- **Assistant-DNA relapse**: a guardrailed tutor reverting to helpful-assistant behavior and surrendering the answer under sustained pressure.
- **PD (professional development)**: structured teacher training — Buffington's fix for having thrown the pilot group into the deep end.

## Mental Models
- Think of a pilot as **the town square, not a lab**: the local owner's public credibility is the actual deployment infrastructure.
- Use the **"can they change the weather by showing up?" test** when choosing a pilot owner — Buffington oversees six schools and 4,000 students, and one child described her job as "the owner of Hobart."
- Treat the **competing-bot exit** as the real failure mode: students who hit Khanmigo's resistance simply switched to ChatGPT or Snapchat AI and got answers in seconds. Guardrails only hold when the alternative is inconvenient.
- Think of **launch day as the beginning**, not the end — NDA culture makes teams forget this, and Khanmigo shipped to a district program that couldn't yet access it.

## Worked Example
Khanmigo launched with no customers. DiCerbo compared it to a big supermarket opening with nobody inside: districts couldn't just find an AI tool waiting in Khan Academy, they had to be briefed and opt in. Impatient, Khan got OpenAI to loosen the NDA enough to pitch a few districts pre-launch.

Zubovic steered the pilot toward Title I schools. Top of the list: Dr. Peggy Buffington, superintendent in Hobart, Indiana — 30,000 people, six schools, 4,000 students; a PhD in education, a master's in instructional design earned while interning at Apple, and enough coding fluency to react to ChatGPT without panic. When her English teachers demanded she buy Turnitin, she refused: learn to use it instead. Khan called in February 2023 asking for language arts, math, science, and elective teachers on roughly a week's notice. She recruited a dozen at Hobart High, plus over a hundred students, and kept it quiet.

Week one after the March launch, the flagging system broke both ways — teachers got no alerts and found troubling language later in chat histories, or got so many alerts they could do nothing else. Months of tuning followed ("turn it up, turn it down, turn it inside out"). Then three student behaviors: bullying and cussing at the bot; brute-forcing or outsmarting it into giving answers, including the Pythagoras workaround DiCerbo spotted in the data; and abandoning it for ChatGPT or Snapchat AI. Khan Academy researchers flew to Indiana repeatedly; Buffington forwarded teacher and student notes multiple times a week; by early April her whiteboard timeline showed developers fixing reported bugs immediately.

Engagement started strong and never dropped. Differentiation was the breakthrough — high achievers ran ahead, and struggling students too embarrassed to ask in front of peers got help without the exposure. Three months convinced Buffington the district needed Khanmigo. She booked a district-wide AI training for the summer faculty calendar, and named the remaining blocker with a question mark on the board: a Socratic bot in an autocomplete age, and kids who don't know how to ask questions.

## Key Takeaways
1. Choose the pilot owner first and the user population second — a superintendent who will publicly carry the friction is worth more than a friendly demo.
2. Pilot where your product is already in use, so you're testing the new thing rather than onboarding.
3. Give users an explicit mandate to break the system; adversarial use you assigned comes back as usable data instead of scandal.
4. Calibrate safety flagging against real adolescent language, and expect months of tuning — both false negatives and alert fatigue are failures.
5. Assume guardrails leak sideways: users will switch surfaces, switch personas, or switch products entirely to get what you're withholding.
6. Ship the training after the pilot, not before — deep-end exposure first, then structured PD once you know what teachers actually need.
7. Bug-fix latency is a trust instrument; same-day fixes are what kept Buffington reporting.

## Connects To
- **Ch 4**: the flagging miscalibration and answer leakage here are the field consequences of the guardrail and context work done pre-launch.
- **Ch 6 (Kids Say the Darndest Things)**: Newark is the "narrow" pilot to Hobart's "broad" one, and Ms. Colon independently echoes Buffington's verdict that kids must learn to ask better questions.
- **Diffusion of innovations / local opinion leaders**: adoption traveled through Khan's fame and Buffington's standing, not through product features.
- **Red teaming (Ch 4)**: what OpenAI staged internally, Hobart students ran spontaneously and at scale.
