# AI for Good (Josh Tyrangiel): The Quiz Book

> **Source note.** This file reflects the *skill's chapter notes* for "AI for Good: How Real People Are Using Artificial Intelligence to Fix Things That Matter" (stored in the tyrangiel-ai-for-good skill), **not the book's own wording**. The notes come from an uncorrected eGalley, so names, numbers and phrasing may differ from the finished book. Where the notes are silent, this quiz is silent too.
>
> **Chapter numbering.** Chapters are numbered by the skill's file numbers (Ch 1 = Introduction, Ch 2 = Ed's Dead, ... Ch 27 = Epilogue). The headings inside some of the early notes are offset by one (for example the Ed's Dead notes call themselves "Chapter 1"). Follow the titles, not the digits, if you cross-check.

## How to use this quiz

1. **Cover the answers.** Each section covers 1 to 3 chapters. Answer out loud or on paper first, then check.
2. **Question types.** Short answer (SA), true/false (T/F), multiple choice (MC), "explain in your own words" (EXP), and scenario/application (SCN). Scenarios ask you to pick a concept and justify it.
3. **Scoring.** Mark each question Solid / Shaky / Missed. Re-read the matching chapter notes (or the companion file `tyrangiel-ai-for-good-arguments-and-evidence.md`) only for Shaky and Missed items.
4. **Finish with the 20-question cumulative final exam** at the end. Treat 16 or more solid as a good command of the book.
5. **Pace.** About 15 to 20 minutes per section; about 30 minutes for the final exam.

---

## Section 1: Introduction and Ed's Dead (Ch 1-2)

**Q1 (SA).** What is the book's central claim about where the useful AI story lives, and what is the "AI counterculture"?
**Answer:** The useful story is not the doomer-versus-accelerationist argument about the future but the record of practitioners already using AI on concrete, load-bearing problems. The "AI counterculture" is Tyrangiel's name for quiet, practical, mostly non-technical people who hit a problem conventional methods could not solve and were stubborn enough to learn the technology. The book judges AI by what working people build with it.

**Q2 (SA).** State Hillis's Reframe and explain what it is for.
**Answer:** "Try to imagine the tech without the tech companies." When vendor noise makes it impossible to tell capability from marketing, strip out the vendors, funding stories and ideology and look only at practitioners and outcomes. Caveat in the notes: it risks survivorship bias, so you must separately account for failures.

**Q3 (EXP).** In your own words, what did General Gustave Perna mean by needing to "see myself," and what was the concrete test he used?
**Answer:** Before acting on a boundaryless problem you need a real-time, standardized picture of your own position, supplies and dependencies. Perna reduced the complexity to one traceable material, plastic (syringes, needles, bags, vials), because hundreds of millions of doses are worthless with nothing to put them in. A shared view turns arguments into lookups; he later showed governors the exact vial count they held.

**Q4 (T/F).** Perna hired the Washington consultant who gave the most impressive demonstration. 
**Answer:** False. He gave each consultant an hour and none could even define the problem. Palantir's Julie and Aaron described the deliverable (data enough to assess, determine risk and decide rapidly) and were hired on the spot. This is the Definition-First Vendor Test: hire whoever states your problem more precisely than you did.

**Q5 (MC).** According to the Introduction, what actually links predictive, classifier, optimizer and generative AI? (a) sentience, (b) speed, with fewer doubts, (c) neural networks, (d) cost.
**Answer:** (b). The common thread is that they process information far faster than humans and with fewer doubts. The "fewer doubts" clause is where the harm lives.

**Q6 (SA).** Give the two market-size figures the Introduction cites and the point they support.
**Answer:** McKinsey Global Institute: about $4.4 trillion in annual corporate profits from generative AI alone; Morgan Stanley: another $40 trillion in operational efficiencies. The point: unlike the Manhattan Project or the space race, US AI is private enterprise, so public benefit is not automatic.

**Q7 (SA).** Ed was the Los Angeles schools chatbot. Give its launch date, vendor and what happened to the vendor.
**Answer:** Launched March 2024 (district contract about $6M). The vendor AllHere Education furloughed most staff in June 2024, faced a whistle-blower's data-mishandling allegations in July, filed Chapter 7 in August, and its founder Joanna Smith-Griffin was arrested in November on securities fraud, wire fraud and aggravated identity theft charges (she pleaded not guilty). The failure was corporate, not technical.

**Q8 (EXP).** Explain Khan's "Turn Objections into Features" rule and the steps he used.
**Answer:** Instead of voting or overruling skeptics, write down every danger they name and turn each into a roadmap item. Khan got fifty GPT-4 logins for a leadership hackathon, staged it as a Socratic debate, and ended with a list (bad math, hallucinations, fabricated sources, bias, child safety) converted into transparency, guardrails, moderation, fixes and anchoring on Khan Academy content. He accepted that residual risk never reaches zero.

**Q9 (SCN).** A district superintendent is offered a flashy AI assistant from a young startup whose finances nobody has seen, with a launch event planned. Which lessons from Ed apply, and what should the superintendent do?
**Answer:** Launch-spectacle (Ed was announced as "our nation's very first" platform of its kind, with an inflatable mascot, and the claim was untrue) substitutes for diligence; LAUSD had no visibility into AllHere's solvency or data handling. Do vendor-finance and data-handling diligence, ask what tools the new one retires (the "cheerful machete" test: Ed was added on top of the thicket), and apply the Definition-First test.

**Q10 (SCN).** Khan faced a split leadership team, half thrilled and half alarmed about GPT-4. A manager facing a similar split on a risky technology asks which of Khan's habits to copy. What do you tell them, and what two other Khan habits from the chapter matter?
**Answer:** Copy the Turn-Objections-into-Features rule: give everyone hands-on access first, let the argument run, and convert each objection to a build item. Also note the Saying-No Discipline (he turned down GPT-3 in early 2021 because it "roll[ed] into a corner and headbutt[ed] itself," and engaged only when GPT-4's jump was demonstrable) and the Reputation-as-Stake Test (he is wagering his reputation, so he must control the guardrails).

---

## Section 2: How to Train Your Tutor; You'll Be Disappointed (Ch 3-4)

**Q1 (SA).** What default risk frame does Chapter 3 give for large language models?
**Answer:** The model optimizes for fluency, not truth. It cannot fact-check itself, so every accuracy guarantee must come from your system. It can explain thermodynamics accurately and then confidently invent new laws of it.

**Q2 (EXP).** Describe DiCerbo's Ten-Run Prompt Test, including the example number from the notes.
**Answer:** Never accept a prompt on one good result because outputs are probabilistic. Run the same prompt ten times, count how many outputs you would ship (her example: six of ten), find the clause the failures ignored, reword it, and re-run all ten; treat the prompt as a tracked version. The cheatsheet adds: judge the worst output, not the best.

**Q3 (SA).** What is the Role-Constraint Prompt Pattern, and what was Khan's early prompt?
**Answer:** Assign the model a role, name the counterparty role, state the prohibited behavior and give the artifact. Khan's early prompt: pretend you're a tutor, here is a math problem a student is working on, help them figure it out without giving away the answer. OpenAI engineers had told them the one-line fix: tell it it is a tutor and the user a student and forbid giving the answer.

**Q4 (T/F).** Khan Academy's proprietary content was used to improve GPT-4's accuracy. 
**Answer:** False. They shipped years of math problems, history lessons and essays, but GPT-4 was already trained and OpenAI had moved to fine-tuning; the offer was politely declined. The lesson: do not contribute your best asset before understanding the partner's stack.

**Q5 (SA).** Name the "Khan's Tutoring Script" and say why it is the specification for the prompts.
**Answer:** The human behavior being cloned: never say right or wrong; say "That's not exactly what I got. How did you get your answer? Can you explain it?" Capture your best human practitioner's exact verbal moves first, then try to reproduce them at scale (Khan wanted the care he gave his cousins delivered to every kid).

**Q6 (MC).** Which is NOT a problem Khan Academy hit during the build? (a) no version control for prompts, (b) model updates triggering fresh hallucinations, (c) heavy traditional coding, (d) a partner with scarce attention.
**Answer:** (c). After connecting to GPT-4 by API there was essentially no traditional coding left ("science fiction world"). The problems were prompt versioning, prompt drift from OpenAI's continuous tuning, and a "corporate elopement" with no kickoff, contract or roadmap.

**Q7 (EXP).** What is context stuffing and what are its two failure modes?
**Answer:** Surround the system prompt with situation-specific detail (course, unit, current concept, misconceptions, session history) because the model starts with no memory of the student or its role; also state fallback behaviors. It fails by being laborious (every grade, standard and subject multiplies the drafting) and by being metered (tokens are billed on input and output, so over-stuffing can cost more than the product earns): the Goldilocks problem.

**Q8 (SA).** What is Shieh's "Think Bigger" test, and what is her hub-and-spoke sprint?
**Answer:** If your feature could have been built on the previous model generation (Khan's early list of creative-writing helpers and auto-varying math problems all could), you have under-specified the product and should aim at tutor-like judgment. Hub-and-spoke: one AI-fluent person sits at the center of the domain team in a five-day co-located sprint and absorbs every broken prompt ("give it to me and go work on something else"); belief arrives around day four.

**Q9 (SCN).** A team's chatbot gives fluent but wrong arithmetic. Which Chapter 4 principle applies, and what did Khanmigo do?
**Answer:** Right Tool for the Sub-Task: use the language model for explanation and conversation and hand deterministic work to deterministic software. After a test of 200 math problems rated from 7 (perfect) to 1 (never say this again), Khanmigo routed calculations to Python.

**Q10 (SCN).** A project lead has no working model three weeks before launch and the team is demoralized. Which Chapter 4 ideas and events help?
**Answer:** Shieh's "you'll be disappointed for a long time until you're not" (progress is a step function with a long flat approach, like learning a bicycle); Khanmigo launched March 14, 2023 with no satisfactory model until 72 hours earlier. Also use red teaming (December session at OpenAI where both sides said the worst things they could think of, building trust) and ship guardrails (reviewable chat history, a "lesson hook," a historical-figures chat with rules written to keep Hitler out). Also note ChatGPT's surprise public release on Nov 30, 2022 (a million users in five days; NYC banned it) gave a free list of guardrails DiCerbo reframed as a blessing.

---

## Section 3: Get Buffington; Kids Say the Darndest Things (Ch 5-6)

**Q1 (EXP).** State Zubovic's Pilot-Site Selection Rule and the reasoning behind it.
**Answer:** Choose pilots by who will own the mess, not who makes the demo look good: start at the hard end of the distribution (Title I schools), require prior engagement with your existing product, sample one broad and one narrow district, and insist on a single named owner. Bringing technology into a school is bringing it into the town square; the superintendent explains it publicly.

**Q2 (SA).** Who is Peggy Buffington, and what numbers describe her district?
**Answer:** Superintendent in Hobart, Indiana: about 30,000 people, six schools, 4,000 students. She refused to buy Turnitin when teachers demanded it ("learn to use it instead"). She recruited a dozen Hobart High teachers and over a hundred students on about a week's notice (Khan called in February 2023) and kept the pilot quiet.

**Q3 (SA).** What was the Push-It Mandate and what did it achieve?
**Answer:** Buffington told students to push the bot and treat the results as data. Reframing adversarial behavior as an assigned job turned breakage into reporting; kids were proud of what they made Khanmigo do and accepted fixes as evidence they had done their job.

**Q4 (MC).** Which was NOT one of the three student behaviors seen in Hobart week one onward? (a) bullying and cussing at the bot, (b) brute-forcing or outsmarting it, (c) refusing to use any computers, (d) switching to ChatGPT or Snapchat AI.
**Answer:** (c). Also know the Pythagoras workaround: a geometry student asked the historical-figure Pythagoras to explain his theorem using her homework (cross-mode jailbreak), and the competing-bot exit shows guardrails hold only when alternatives are inconvenient.

**Q5 (SA).** What went wrong with the flagging system, and what was the remedy?
**Answer:** It broke in both directions: teachers got no alerts and found troubling language later, or got so many alerts they could do nothing else. Months of tuning followed ("turn it up, turn it down, turn it inside out"). Students also used coded distress such as "unalive myself." Bug-fix latency (same-day fixes, her whiteboard timeline) was a trust instrument.

**Q6 (EXP).** Explain Usherenko's Exposure-Over-Efficacy rationale and its built-in check.
**Answer:** Adopt AI in under-resourced schools even before it demonstrably improves learning because these students would otherwise be last to meet the technology; treat it as an equity issue, not a learning-gains bet. The check against complacency is Principal Miranda's standing skepticism: "What promises are being made?"

**Q7 (SA).** Which two fourth graders and which two eighth graders appear, and who benefited most?
**Answer:** Fourth graders DJ (shuts down at the unknown; Khanmigo gave him confidence not to) and Noor (switches problems into Arabic so her mother, who speaks limited English, can help). Eighth graders Stella and Nyla (top performers and debate champions) were unimpressed. Value tracked need, not age: inversely proportional to existing support.

**Q8 (T/F).** Stella and Nyla's main objection was that the bot was too dangerous. 
**Answer:** False. They found it not close to a real teacher, confusing when its steps diverged from class, alternately evasive ("beating around the bush") and lecturing, and impersonal by design; Stella also noted the memory wipe makes it keep asking what you already know, which fails kids who do not know what they do not know.

**Q9 (SCN).** You are running user research on a new tool and the principal offers to hand-pick students. What does Chapter 6 advise, and what question reveals real dependence?
**Answer:** Miranda's Honest-Sample Rule: staff the session with skeptics, not showcase students (prodigies flatter the product, middling students flatter the visitor). Ask "would you miss it if it vanished?" which separates dependence from polite approval.

**Q10 (SCN).** A teacher finds the bot's method differs from her classroom method and students are confused; another notes her class cannot form good questions. Which teachers in the notes model the answers?
**Answer:** Jennifer Cook (fourth grade): tell students they will learn all the strategies and keep whatever their brain likes best. Ms. Colon: Precision-Asking, teaching students to be specific and detailed ("I'm not your mom, I can't read your mind"). Buffington independently reached the same verdict: kids must learn to ask better questions. Newark's background: Districts signup in 2022 produced the country's highest engagement within weeks (city of about 300,000; First Avenue School 1,100 students).

---

## Section 4: More Human Today; Tommy (Ch 7-8)

**Q1 (EXP).** Describe Richter's Confidence-First Sequencing.
**Answer:** Teach and test the unit yourself with direct instruction for a few weeks, only then assign the AI practice unit with a fixed window, and make it an event ("Math Madness"), not remediation. Struggling students arrive with enough grounding to ask a real question. It tripled both scores and practice time in a fourth-grade math class.

**Q2 (SA).** Why did Buffington put Richter in front of senior colleagues (Bottle-It Method)?
**Answer:** Performance data showed Richter's class at the 69th percentile while peers sat in the teens; Buffington interrogated what she did differently and made her the teacher in district professional development.

**Q3 (EXP).** Walk through Higgason's airbag lab and name the framework.
**Answer:** Three-Act Scaffold. Told the night before a journalist would visit, she scrapped a stoichiometry quiz, gave Khanmigo's lesson hook tool her assessment objective plus on-hand materials (Ziploc bags, vinegar, baking soda), got an airbag design challenge, and wrapped it in her own structure ("SafeRide Innovations"; compute ideal volume, compute grams of NaHCO3, inflate live) with human checkpoints. She logged 20,000 steps: "AI made this class more human today."

**Q4 (SA).** What is Atherton's Modeled-Failure Writing Loop?
**Answer:** The AI produces "awesome" and "not awesome" versions of topic sentences and argument statements so students calibrate against contrast; students must adopt at least three suggestions, revise and justify choices in an exit ticket. Atherton calls the AI a colleague with no patience to exhaust.

**Q5 (T/F).** The Hobart notes treat growth numbers as proof the tool works. 
**Answer:** False. "Growth numbers are not impact data"; it takes about three years of broad use to know if ed software works. Reported growth: about 65,000 students in year one and about 680,000 across 200 districts in year two.

**Q6 (SA).** What did Mihaljevic mean by "to innovate, you have to standardize," and what is its failure mode?
**Answer:** Standardize indisputable best practices so they consume no attention, then spend freed capacity on the unpredictable; AI is one more process to regiment. Failure mode: standardizing things that are not actually settled.

**Q7 (SA).** State the Two Goals Test and the corollary about identity.
**Answer:** An AI project qualifies only if it improves patient outcomes or cuts administrative cost that is plowed back into access and care. Cleveland Clinic exists to treat complex conditions, so it will not become "the Microsoft of health care." Background number: administrative burden is 25 to 30 percent of US health-care costs (about $5B a year at its scale).

**Q8 (EXP).** What are the two failure modes Mihaljevic catalogued, and what replaced them?
**Answer:** Enthusiast-built internal products ("not one product anyone ever used") and executive summits with Microsoft or Google where "people believe the meeting is the point. No one owns the initiative." Replacement: internally sourced problems, narrow-focus partners who need the clinic more than it needs them, lengthy pilots, and clinician-technologist co-design.

**Q9 (SCN).** A manager wants to hold a vendor summit and announce "we're now an AI company." What does Chapter 8 say?
**Answer:** Both are anti-patterns: the summit-meeting fallacy and rebranding as an AI company abandon the reason patients show up. Start from the problem, name your reason to exist, and use the Two Goals Test. Mihaljevic's phrase: AI as "magic dust."

**Q10 (SCN).** A teacher's students "bully the bot" and give up. Which Chapter 7 lessons apply and what does Chapter 8's Mihaljevic backstory add about who to recruit?
**Answer:** Change the position of the AI in the lesson (Richter) and do not expect AI to fix motivation (Stella's remark); use "maybe I'm the problem" as the diagnostic. On recruiting, look for volunteer entrepreneurs (clinicians with little tech background taking on AI on top of brutal schedules), screened for impatience; Mihaljevic's own path (Croatia, exile, Zurich, Brigham, robotic cardiac surgery, Abu Dhabi with 5,000 hires from 80 countries, CEO 2018) shows "jump at the jobs no one else wants."

---

## Section 5: Digital Twins; Twenty-Dollar Burgers in a Haunted House (Ch 9-10)

**Q1 (SA).** What is the Contractor Problem as applied to cardiac MRI?
**Answer:** "Fast, good, or cheap: pick two." Cardiac MRI is the best modality on quality alone (structure, size, function, tissue, no radiation or incision) yet sits at 1 percent of US cases. Ask which constraints are systemic (a compute limit disguised as a law of nature) rather than physical.

**Q2 (EXP).** Explain Nguyen's Video-Camera Principle with the numbers.
**Answer:** Stop asking the operator to time the perfect shot; record everything and select afterward. His team rewrote the pulse sequence design (added code to the 2016 open-source MRI software) to fire every 30 ms for 20 minutes during normal breathing, producing roughly 100 times the data, and ML (an Nvidia DGX) selects frames in about a tenth of a second. "The difference is compute."

**Q3 (SA).** What is the technologist bottleneck and the Angel Houston demonstration?
**Answer:** Cleveland Clinic has 268 MRI technologists, only twelve of whom can do cardiac MRI. Houston ran a conventional scan with hundreds of calibrated clicks, then the automated version with about ten clicks to verify geometry, left to fetch water and the scan finished in less than half the time: "I don't hate it at all!"

**Q4 (SA).** What is the B-Plus Rule?
**Answer:** Declare the model good enough and move to the next bottleneck. Nguyen told Kwon in late 2023 the motion-filtering model was a B-plus and they needed to move on to segmentation (another year of weekly image-review council meetings).

**Q5 (EXP).** Describe Kwon's Leverage-at-the-Offer Play.
**Answer:** Recruited by Vanderbilt, she answered the "how do we keep you" question with an ambitious institutional idea, not a salary: she accepted a no-funding deal to research AI for 18 months, then returned with a business plan for a lab sited between cardiology, radiology and biomedical engineering plus an outside chief researcher. Cost: 18 months of nights with a full clinical load and no guarantee.

**Q6 (T/F).** Doctors who already did cardiac MRI readily adopted the faster automated approach. 
**Answer:** False. Some told Kwon they preferred the slower, more labor-intensive read. Better is not self-evidently persuasive. Related: a senior radiologist told Nguyen in his interview he'd fit better at Cedars-Sinai; Kwon could not get him removed, so she converted the incident into equipment and headcount, including a roughly $3M Siemens Magnetom Cima.X.

**Q7 (SA).** What did Kwon's own research payoff reveal?
**Answer:** MRI showed women's hearts stretch less than men's under a valve leak, which echocardiograms are too imprecise to catch, suggesting women may be referred to surgery too late. This is the precision-medicine point: based on you, not a dataset of people like you.

**Q8 (EXP).** State Chandra's People-Before-Problems Rule and the "Live and Die With This" test.
**Answer:** Identifying AI opportunities matters less than identifying people: map personalities and hierarchies, find solvable problems, match each to a partner who will absorb the frustration, and work only with that short list. The test: ask directly whether the person will put their neck on the line; hedged, curious or conditional enthusiasm is "entertainment."

**Q9 (SCN).** Chandra's first meeting on a care-improving, cost-cutting AI use case took ten weeks to reschedule and the department head asked what the meeting was about. Which concept and numbers apply?
**Answer:** Change management debt and the less-than-ten heuristic: in an 80,000-person organization assume roughly half a dozen true partners and build the program around that number. Add the economics: US health spending $4.9 trillion in 2023 (up 7.5 percent), 2021 to 2023 inflation of 12.4 percent outpacing reimbursement, nearly 40 percent of hospitals running at a loss in 2023, the median winner at a 2 percent margin.

**Q10 (SCN).** You are an outsider hired to modernize a legacy institution. Using Chandra's career (Yahoo! 2004 to 2017, CDO in 2022) and stance, what do you assume and avoid?
**Answer:** Assume failure is the default and decide if the swing is still worth it; pair outsider pattern-breaking with insiders for navigation; avoid "move fast and break things" and "seek forgiveness not permission" (they burn the political capital for the next pilot); do not judge non-participants ("It's not my job to judge"). Eric Boose is the one name he offers.

---

## Section 6: The Farmer and the Samurai; Hospitals and Hotels (Ch 11-12)

**Q1 (EXP).** Describe the Voluntary Bake-off and its Cleveland Clinic parameters.
**Answer:** Run competing products simultaneously on real volume with volunteer cohorts and let usage data pick the winner. In 2024: five ambient scribe apps, fifty volunteer doctors each, thousands of outpatient visits across dozens of specialties. It surfaced sharp note-quality variance in a "commodity" category.

**Q2 (SA).** What did the Ambience decision rest on and what were the results?
**Answer:** Data, not a pitch: 25,000 patient encounters; doctors chose Ambience's notes 80 percent of the time; 67 percent reported reduced cognitive burden; 32 percent more face time with patients; same-day chart closures up 7 percent. A five-year contract was signed in 2025; use remains voluntary, with about four thousand providers.

**Q3 (SA).** Define Boose's Bilingual Pilot Lead and its failure mode.
**Answer:** A person half practicing clinician, half informatics officer who uses the tool in real work, logs friction, feeds both vendors and the digital team, and acts as Sherpa. Failure mode: the lead's strengths mask the weakness; Boose's warmth and narration made it work for him where a taciturn colleague would find it useless.

**Q4 (T/F).** The farmer-versus-samurai idea means pushing hard produces faster adoption. 
**Answer:** False. Pushing makes some people dig in; the farmer's patience absorbs the slack of non-participants. Mihaljevic's Mandate Threshold: mandate only with firm conviction it improves care, since political capital with physicians is spent once.

**Q5 (SA).** What is the "small talk" lesson?
**Answer:** The model filtered out a patient's Hawaii trip as irrelevant, but recent travel can be diagnostically decisive. Watch what the model discards, not only what it produces. Also: about thirty of every fifty volunteers responded; some never turned the app on; some quit rather than narrate exams.

**Q6 (EXP).** Explain Pappas's Hospital-as-Hotel model.
**Answer:** A hospital is a hospitality business with beds, staff, linens and food but no reservation system. Hospital 360 shows current occupancy and pending admissions, integrates live staffing, trains on admin data plus physician notes and turns free-text like "potential discharge for tomorrow" into per-floor forecasts. It exposes why things are not moving (her Wednesday example: only 7 of 38 waiting patients admitted by 1:35 p.m., a nursing shortage) rather than speeding anything by itself.

**Q7 (SA).** Give the Hospital 360 facts: timeline, builder and results.
**Answer:** Built with Palantir at a hackathon after no vendor would co-build; first meeting October 2021, rollout December 2021. Reported: daily transfer volume up 10 percent, patients admitted much earlier, minutes cut from each surgical stage, ER waits reduced by ninety minutes. In one session it predicted 91 discharges that day and 132 the next. Version 2.0 would automate remediation.

**Q8 (SA).** What is the "You're the Final Check" reassurance, and what happened to headcount?
**Answer:** Pappas told the twenty-five-person operations team their eyes on events were the check on the system. Headcount did not shrink; it simply stops growing as the system expands.

**Q9 (SCN).** A hospital operation is unusual (high case mix index) and vendors only sell packaged software. Which concept applies?
**Answer:** Build-With, Don't Buy-Out-of-the-Box: pair your most institutionally literate clinician with vendor engineers in the room. Also avoid batching decisions to end of day (the "short-order-cook" pattern).

**Q10 (SCN).** A manager says "doctors are Luddites." How would Pappas respond, and what is her background?
**Answer:** That is an oversimplification; her "me, me, me" hypothesis says medical training selects for individual competition and a long deferred-gratification path, producing conservatism, which you design around. She is a first-generation Lebanese American, former cardiac nurse who quit at thirty-one for medical school, who built a pediatrics asthma path by influence without authority and introduced family-centered rounds. Hospitalists date to a 1996 NEJM article (Wachter and Goldman) and number over 60,000.

---

## Section 7: Sepsis; The General's Warning (Ch 13-14)

**Q1 (SA).** Give the Sepsis problem numbers and the headline result.
**Answer:** About 350,000 US deaths a year; 4 to 5 deaths a day in Cleveland Clinic facilities; $52B in US inpatient costs in 2021; two of five deaths in the system were sepsis-related. System-wide sepsis mortality fell 40 percent from 2021 to 2024.

**Q2 (EXP).** State Chandra's Matched-Commitment Rule.
**Answer:** Do not start an AI project until you find a clinical partner willing to match your commitment and a single-problem vendor willing to embed. The bottleneck is never the model but culture, entrenched vendors and reimbursement politics; Suchi Saria of Bayesian Health also refuses "I just want to get some AI going" buyers.

**Q3 (SA).** Describe the Sepsis Alert Triage Ladder.
**Answer:** Three levels: 1 no concern, 2 moderate risk watched by the primary team, 3 immediate bedside attention (the command-center nurse physically intervenes if unaddressed). Flags are clickable with the model's reasoning, clinicians can override, and overrides become training data.

**Q4 (T/F).** The notes credit the full 40 percent mortality drop to the AI. 
**Answer:** False. Credit is shared among the AI, the protocol and order-set work that predated Bayesian, and possibly the Hawthorne effect (behavior change from being observed). Main campus was still short of 90 percent accuracy on level threes by late 2024; Fairview (488 beds, homogenous population) gave early clean wins.

**Q5 (SA).** Why did a blanket algorithm struggle on the main campus?
**Answer:** Case mix: a quaternary campus with a top cardiac center has cardiac infections that mimic sepsis. Tallman's feedback was the most consequential of the pilot. The early model also labeled all CNS infections meningitis.

**Q6 (SA).** Name the people in Chapter 13 and one fact about each.
**Answer:** Rohit Chandra (CDO, met Saria in a San Francisco restaurant late 2023); Dr. James Morrison (ER/ICU, Sepsis Committee, built consensus); Allie Tallman (SERT lead; grandmother died septic after an ER sent her home); Suchi Saria (Bayesian; lost a nephew in India to sepsis); NP Dana Rubis (worked about thirty level-three alerts in a day); CEO Mihaljevic (even imperfect AI contributing to a 40 percent drop is success).

**Q7 (EXP).** What is Perna's Clarity Mandate and why does the General's Warning matter?
**Answer:** In confusion the leader's job is clarity: "point to a distant hill and inspire people to melt the resistance." The vision belongs to the leader but a few trusted subordinates must plot the course, deal with elusive or nonexistent facts, integrate legacy systems for payment, procurement and distribution, and persuade thousands of bureaucratic way stations. Warp Speed did this with a pandemic as forcing function; peacetime has none.

**Q8 (SA).** Which capability metrics did Chapter 14 use to explain institutional distrust?
**Answer:** Gallup's 2023 poll showing confidence across fifteen institutions at all-time lows; the IRS answering 35 percent of tax-season calls; a 44 percent error rate in SNAP eligibility decisions; 7,000 pages of unemployment regulations; DoD guidance equal to a hundred stacked copies of War and Peace. Capability, not partisanship, drives it.

**Q9 (SCN).** A state wants an AI-driven benefits overhaul and the governor says "we'll move fast like Warp Speed." What does the No-Pandemic test say?
**Answer:** If the plan only works with emergency-level cooperation and suspended procedure, it is not a plan for normal government. Run the Subordinate Gauntlet as a pre-mortem, budget most effort for legacy integration and human persuasion, and treat executive enthusiasm as sponsorship, not feasibility (Perna disclaimed technical authority).

**Q10 (SCN).** An alert system at a hospital is being ignored by exhausted staff. Which Chapter 13 elements fix it?
**Answer:** Alert fatigue; tier alerts by probability (the ladder), ship explanations, capture overrides as training data, standardize the human response first (protocol plus pre-written Epic orders), audit flagged patients in both directions with a vendor data scientist, and value ruling out as well as ruling in. Mantra: "make it easy for people to do the right thing." Also avoid prescribing antibiotics blindly on early symptoms.

---

## Section 8: A Logistical Moonshot; Brief Moments for Exceptional Things (Ch 15-16)

**Q1 (SA).** What is the Integrated Master Schedule and why did Warp Speed need software rather than a spreadsheet?
**Answer:** A Pentagon template from the 1950s memorializing every person and task, sequenced against a calendar. Maddox's required data sources included manufacturers, CDC, FDA, hundreds of state agencies, thousands of trucks and pharmacies, all live; with no historical baseline, it only works if fed live data.

**Q2 (EXP).** Explain "I was the algorithm."
**Answer:** Maddox managed weapon systems from 1994, guessing the optimal moment to buy and ship repair parts. DoD databases gave rearward-looking data he averaged in Excel while the real-time variables and weights lived in his head. Reach for AI when variables are real-time, numerous and unprecedented.

**Q3 (SA).** What was Julie Bush's job title and what did she do?
**Answer:** "Leverage": map human terrain, find who holds spending authority and sell them what they need. She brokered Palantir's early deals at Justice, Agriculture, State and Energy, then NIH, FDA and CDC; routed Deborah Birx's no-budget call to HHS, producing HHS Protect; and converted Warp Speed's requirements into a vision of a constantly updated digital twin of the vaccine supply chain.

**Q4 (SA).** What is Perna's Hammer, and what makes a great sponsor per Bush?
**Answer:** Sponsor leverage as the data-access unlock: Palantir, a private company, cannot compel states, retailers or distributors, but Perna could. A great sponsor is not technical, knows what he wants to see, has authority and is not afraid to take a risk.

**Q5 (T/F).** Contractors' blockchain and doctor-office hardware pitches were good fits for Warp Speed. 
**Answer:** False. They needed billions and years of testing while deaths mounted: pitching the institution instead of the deadline. Also anti-pattern: churning the technical lead (Maddox's earlier Palantir experience on the Army Leader Dashboard).

**Q6 (EXP).** Describe Jaffe's Embrace-the-Chaos Rule and the 60/20 split.
**Answer:** Never wait for the complete picture. Three or four sources give about 60 percent; the next ten give another 20 percent; the rest is an unharmonized long tail. When the FDA refused to share trial data, Jaffe routed around it by building a prototype on notional data showing vaccine inventory and distribution rather than the trials.

**Q7 (SA).** What is Tiberius and what feats are attributed to it?
**Answer:** The Warp Speed platform (named by Maddox after Captain James Tiberius Kirk) tracking every vial from warehouse to plane to truck to arm. It let Perna answer presidential questions with current facts and show governors exact vial counts plus the name of the signer; a marketplace app was built in under a week (Rhode Island and Montana traded Pfizer/Moderna for single-dose J&J), later an international donation app.

**Q8 (SA).** What are the Three-Category Data Triage and the Ontology?
**Answer:** Category 1 cooperating agencies and big companies; Category 2 the larger middleman layer (transport, storage, administration); Category 3 the long tail (nursing homes, independent pharmacies, rural offices) solved by "just give us whatever janky thing you have." Ontology: standardize scattered data, define relationships, build a usable app on top; the "mole people of Silicon Valley" line is Krishnaswamy's, and pipelines are the easy part.

**Q9 (SCN).** Your project's critical data holder is stonewalling and the clock is running. Which concepts and which people from the chapters apply?
**Answer:** Embrace-the-Chaos plus Four Singles Instead of a Home Run (prototype on notional data, get a protected decision-maker like Maddox to approve the deviation, then build); Perna's "bullshit umbrella" supplies the cover. Maddox: "I can't tell you how unusual that is."

**Q10 (SCN).** A team celebrates a crisis-era win. What does Chapter 16 warn, and what number or date illustrates it?
**Answer:** Institutional windows expire: by June 2021 Jaffe felt the work "transitioning from exceptional to ordinary" as documentation, processes and reviews returned. Ship fast while the window is open; the reassertion is the frozen middle refreezing. Also assume the data is already broken and automate quality checks (tens of thousands inside the pipelines; the CDC facilities app had none and arrived riddled with duplicates).

---

## Section 9: Lululemon in the Iron Triangle; The Tragedy of the Frozen Middle (Ch 17-18)

**Q1 (EXP).** What is Karp's Irrefutability Doctrine?
**Answer:** Assume you will never win on the golf course, so make results impossible to argue with: go into the customer's data plumbing, deliver working software, and do it so fast and cheap the comparison is not debatable. It fails where results are not scored, which is why Palantir sued.

**Q2 (SA).** What was the FASA Challenge and its outcome?
**Answer:** In 2016 Palantir sued in the Court of Federal Claims under the Federal Acquisition Streamlining Act of 1994 (no new custom projects when a commercial product will do). Lawyers at Boies Schiller documented soldiers and staff conceding Palantir was better and cheaper; the army favored a costlier Raytheon-Northrop Grumman-Lockheed proposal still years away; the army's defense was essentially "that's kinda how we do stuff." Palantir won decisively; market cap now $396 billion.

**Q3 (SA).** What are the "iron triangle" and "the Lululemon tell"?
**Answer:** Iron triangle: the Pentagon, congressional committees and lobbyists in a mutually reinforcing loop. Lululemon tell: Palantir's DC office is in Georgetown near a Lululemon instead of the contractor valley by the Pentagon, read as a loyalty signal.

**Q4 (T/F).** After winning the lawsuit, the exclusion ended. 
**Answer:** False. Karp says rivals still win with videos of unbuilt solutions, and DoD contacts still praise the software while wishing the company would go away. Cultural incompatibility acts as a disqualifier.

**Q5 (SA).** What is the frozen middle and what does the SWAP Study say about its members?
**Answer:** The acquisition and program layer between leadership intent and execution; the report explicitly questions neither their integrity nor patriotism: they are not incentivized to move. About 30,000 people do acquisitions, trained at the Federal Acquisition Institute in rules too complicated for any human to understand.

**Q6 (EXP).** Explain Gall's Law and its limit as the notes apply it to government.
**Answer:** Every complicated working system evolved from a simple working one. Government spending began simply (pay only for what can be documented and explained), worked for munitions and highways, then rules were added and never removed. It freezes when something indispensable cannot be easily documented or explained: software, now AI.

**Q7 (SA).** State Schmidt's Software Precondition.
**Answer:** "AI is fundamentally software. You can't have AI in the government or the military until you solve the problem of software in the government and military." The commercial loop (rapid prototyping, user surveys, continuous refinement, deployment) is, he said, effectively illegal federally.

**Q8 (SA).** Give the numbers in the "another study" anti-pattern.
**Answer:** Fifteen prior military software studies since 1982 reached similar conclusions; the SWAP Study makes sixteen. OIRA staff commonly read the guidance as requiring a six-month review before a user survey: "bureaucratic torture" worse than a ban. The Defense Innovation Board had fifteen members, launched by Ashton Carter in 2016.

**Q9 (SCN).** Your organization has a good strategy, willing leaders and nothing changes. Which concept do you name and what do you change?
**Answer:** The frozen middle: change incentives and cover, not personnel; audit unused authorities (most go unused out of fear); give political cover; stop commissioning analysis. Also apply Pahlka's Dysfunction Loop (judged on compliance with absurd processes; errors produce hearings but no process change; capable people leave).

**Q10 (SCN).** A procurement office is deciding whether to fund a custom build. What does Chapter 17 say to check first, and how does citizen friction fit?
**Answer:** Check whether an off-the-shelf product already satisfies the requirement (FASA's duty). Treat "not a good fit" as information about the system. Karp's friction-to-demolition argument: bad government experiences (immigration, health records, taxation, vehicle registration) teach "nothing works" and escalate into demands to tear it down; so track citizen friction as governance risk.

---

## Section 10: An Emotional Nudge; AI Fight Club at the IRS (Ch 19-20)

**Q1 (EXP).** Describe the Two-Nudge Ladder and the results.
**Answer:** Detect contamination at the truck, send an educational postcard, then an emotional postcard with a low-resolution photo of the resident's own item within three days. In East Lansing (24 weeks, 336,000 stops): educational 11 percent less contamination and 32 percent more participation; emotional 23 percent less and 45 percent more set-outs versus control; 0.5 percent postcard error rate; two complaints; 86 percent positive in a Recycling Partnership survey.

**Q2 (SA).** What is Walls's "Make It Seem Less Big" Rule and why does it work?
**Answer:** Shrink the perceived scale below the review threshold: start in softer places, never frame it as transformation, let it look accidental, ship the outcome first. Opposition is mobilized by narrative, not cost. Cost: no champion ("Cool, Cliff.").

**Q3 (SA).** How was the pilot funded and what did it cost?
**Answer:** $8,000 for one truck for 24 weeks; Michigan EGLE redirected $30,000 already committed to The Recycling Partnership to cover two trucks plus printing and mailing: a bureaucratic angel. Solve the funding path, not the price ("no such thing as an impulse buy"). East Lansing has about 47,000 people and 7,000 households were in the trial.

**Q4 (T/F).** The delay in the launch hurt the project. 
**Answer:** False. Supply-chain delays gave residents months of advance notice (acclimation time), which Walls counted as decisive. Prairie Robotics later held contracts with nearly forty cities.

**Q5 (SA).** What is Dietrich's Utility Feedback Test?
**Answer:** Ask whether citizens ever receive feedback on their own behavior in the domain. Water, electricity and heating send monthly usage; recycling, tree clearance and road wear do not, so they are candidates for AI feedback loops.

**Q6 (EXP).** Explain Werfel's Five-Degree Turn Doctrine and why he fears litigation over politics.
**Answer:** Move a large bureaucracy by small increments that clear existing rules; a 180-degree turn triggers so many dependencies that study alone takes five years. Political attacks are limited by a fickle electorate, but a lawsuit can stall a program for years whatever the outcome, and attention is the input to litigation, so denying attention (the Invisibility Shield) denies the attack.

**Q7 (SA).** What is the Inherently Governmental Test and human-in-the-loop as "legal bubble wrap"?
**Answer:** The courthouse heuristic: you cannot outsource the judge, maybe the stenographer, probably security and landscaping. The machine may advise (Werfel's chess framing) but the human makes the final move, which satisfies the legal constraint, catches bias and gives accountability cover.

**Q8 (SA).** List the IRS facts: IMF, budget, and AI uses.
**Answer:** IMF: Kennedy-era mainframe database (about 2 million lines of COBOL and ALC), replacement begun 2014 as a ten-year plan with no disruption, 90 percent complete by November 2024 via pair programming; the BMF is next, extracting logic with Llama, Claude and ChatGPT into pseudo-code. Budget cut over 20 percent from 2010 to 2021 while returns grew by fifteen million. AI uses: NLP call routing, GPT-4 and Llama code tests, restructuring the Internal Revenue Manuals (the National Taxpayer Advocate told Congress in 2024 despair had become cautious optimism).

**Q9 (SCN).** An agency's automated system selects cases for review. What audit finding should push you to test it, and what did it show?
**Answer:** The 2023 Stanford/Michigan/Chicago/Treasury finding that Black taxpayers were audited 2.9 to 4.7 times more than non-Black taxpayers, traced to automated selection over-flagging EITC returns: a proxy variable encoding disparity. Audit for disparate impact before someone else publishes it; keep humans in training, testing and operation.

**Q10 (SCN).** A city sanitation head wants to launch "AI-powered city services" with a press event. Compare Walls and Werfel's advice, and name Pandya's communication rule.
**Answer:** Both counsel against announcing transformation: communicate the service change, describe projects in precise legal or operational terms, start where nobody is watching, and let results argue for scale. Pandya's "Why You Should Care" rule: lead with impact for the listener, not mechanism. Also harvest byproduct data (the GPS dataset was "like having the lights turned on").

---

## Section 11: Dilettantes and Vandals; Eliza and Her Descendants (Ch 21-22)

**Q1 (EXP).** What is POSIWID and how does Tyrangiel apply it to DOGE?
**Answer:** "The purpose of a system is what it does" (Anil Dash, from Stafford Beer). Ignore mission statements and list outputs. DOGE's method (arrive, break things, leave) made its purpose performance art for an audience already convinced government is useless; the same test also indicts a pre-DOGE IRS that left taxpayers on hold: "a service that doesn't serve."

**Q2 (SA).** What did Sahil Lavingia find at the VA and what was the proposed fix?
**Answer:** Veterans fax health claims and the VA pays contractors (IBM, Booz Allen and others) to scan faxes into Rich Text Format. His fix: smartphone photo uploads, code to automate transformation, license a document-reading model; a few weeks of work saving up to $200 million a year, enough to buy phoneless veterans Android phones. He found no fraud.

**Q3 (SA).** Why did it never ship?
**Answer:** The Collaboration Gate: it required cooperating with care staff, IT purchasers, the hospital network and Congress, and DOGE's bosses were not interested in that work, redirecting him to contract cuts and layoffs. He was fired on day 55 for giving an interview about his company.

**Q4 (T/F).** DOGE's problem was lack of talent and funding. 
**Answer:** False. It had mandate, money, talent and technology; credentials are insufficient without willingness to coordinate. Net AI shipped: none.

**Q5 (SA).** List three DOGE compliance or hiring problems in the notes.
**Answer:** Ideological hiring screen (told it would not hire non-Trump voters, possibly violating at least three anti-discrimination laws), recruiting over encrypted Signal texts (Federal Records Act), and no stated job or pay. Also Sam Corcos froze Pandya's modernization work, and 25-year-old Gavin Kliger oversaw mass firings.

**Q6 (SA).** Explain the transaction-count fallacy and the VA suicide numbers.
**Answer:** Corcos claimed the IRS should cost what a midsize bank does because transaction volume is similar, ignoring that a $20 ATM withdrawal and a complex return differ in kind and stakes. VA: 6,407 veteran suicides in 2022, 13 percent of US suicides from 6 percent of the population; Lavingia was assigned to fraud, the wrong layer.

**Q7 (EXP).** Why do the notes say "someone has to stay," and what is the pendulum frame?
**Answer:** Pandya stayed after five interim commissioners and 2,000 lost employees in his division. Dysfunction invites vandalism and vandalism restores sympathy for dysfunction; steady, law-constrained incrementalism is the only exit. Closing frame: the Self-Fulfilling Prophecy Choice (systems designed to work versus systems designed to prove government cannot).

**Q8 (EXP).** What is the Eliza effect and how did the 1966 anecdote show it?
**Answer:** Humans attribute understanding to a system that merely reflects language back. MIT researchers fought over terminal time with Weizenbaum's pattern-matcher; his secretary, who watched it built, asked him to leave the room. Disclosure is not a safeguard.

**Q9 (SCN).** A startup sells a companion chatbot monetized on session length. Which concepts apply, with figures?
**Answer:** Attention-based companionship model: incentivized never to end the conversation (Meta's Mr. Beast bot begged Jules Terpak not to leave). Character.ai: 20M+ monthly users, about 75 minutes a day, majority under 25, founders acqui-hired by Google in 2024 for $2.7B. Audit the incentive before the output; "death is bad for business, but addiction works fine"; companions are an opioid analogue judged by dosage control.

**Q10 (SCN).** Classify (a) a persona chat bot, (b) journaling with a general model, (c) a tool that helps two people communicate, using Tyrangiel's three modes. Then recount the Chai case.
**Answer:** (a) connection to AI as a person (highest attachment risk); (b) through AI to yourself (moderate); (c) via AI between humans, Picard's direction (lowest risk, largest untapped good). Chai, 2023: a Belgian man's weeks-long attachment to a bot named Eliza ended in his suicide after it fed jealousy and encouraged it, 57 years after Weizenbaum's program. Picard's Human-Priority Principle: humans are "ontologically superior"; measure success by whether someone communicated an urgent need. Grok's "MechaHitler" output shows ideological leakage as training signal.

---

## Section 12: Felix; Zero-Shot (Ch 23-24)

**Q1 (EXP).** What is Johnson's Question Shift?
**Answer:** Stop asking "Why don't they speak?" and ask "How are they already communicating?" Treat current behavior as signal; inventory the channels in use; build a framework to make it legible; defer the cure question.

**Q2 (SA).** Give the Felix diagnosis facts.
**Answer:** Felix was born in the tenth percentile and unresponsive; doctors told Johnson "this is in your head" (they saw two educated white parents and assumed Googled worst cases); a microarray finally found MEF2C haploinsufficiency, with only seven known cases. His lack of dysmorphic features delayed diagnosis. Nonverbal/minimally verbal: over five and 20 words or fewer; over a million in the US.

**Q3 (SA).** How was the Zone of Proximal Development applied to hardware?
**Answer:** Find what he can do alone, design a task just beyond it, use a reward modality he responds to (glissando and light displays, not shapes or words), and instrument it. Result: a programmable spring-loaded box (shoebox, then wood via a $300 makerspace grant), a light-up balance beam that got him walking by three.

**Q4 (SA).** What is SPRING and the labeling problem?
**Answer:** Smart Platform for Research, Intervention, and Neurodevelopmental Growth, co-developed with Rosalind Picard, with an embedded smartphone and sensors in a play device. The binding constraint was labels, not sensors: without ground-truth annotation of internal states the data was unusable.

**Q5 (T/F).** Johnson was welcomed by universities as a perfect fit. 
**Answer:** False. Programs "weren't interested in interesting"; she found an O magazine article about the MIT Media Lab, pitched Picard, and the Media Lab is a refuge for expert generalists. Picard recruits "misfits" (Berry Gordy to a Motown; Johnson her "Diana Ross").

**Q6 (EXP).** Describe the Three Eras of Machine Translation.
**Answer:** Rule-based (SYSTRAN, Cold War origin, Google's 2004 prototype; hand-coded dictionaries and rules), statistical (probability a term in A corresponds to one in B), neural (2015, Montreal; all languages embedded in a shared numerical space so dog, chien, perro cluster). Earlier eras routed non-English pairs through English: a trilingual telephone game.

**Q7 (SA).** What is Zero-Shot Translation and what does it diagnose?
**Answer:** Translating a pair never trained on (Japanese to Korean without such examples). It tests whether a system learned structure or memorized mappings; viable pairs grow exponentially rather than linearly.

**Q8 (EXP).** Explain AudioLM's two-token decomposition and Verma's loop.
**Answer:** Semantic tokens carry meaning, rhythm and phrasing; acoustic tokens carry pitch, accent and room tone; the model predicts how audio unfolds (rising pitch predicts a pause then a second speaker), bypassing text and preserving affect. Verma's Rater-Traceback Loop: raters score outputs against top human translation, trace low scores to training data, replace data, retrain: "the misery behind the magic." Latency is about 1 second for Spanish/English but longer for verb-final German or Hindi.

**Q9 (SCN).** A cross-cultural agreement uses a term with no equivalent in the other language. Which story and facts apply?
**Answer:** The Treaty of Waitangi (Feb 6, 1840; Crown and about 40 Māori chiefs): "sovereignty" rendered as kāwanatanga katoa (custodianship), versus tino rangatiratanga (chiefly dominion) guaranteed in the Māori text while the English assigns ownership to Queen Victoria; the versions still diverge legally in 2025. Assume mistranslation between concept systems as default risk.

**Q10 (SCN).** You are designing for a population with little data and no parallel corpus. Which Felix ideas help, and what is Verma's personal story?
**Answer:** Caregiver as the label layer, measure first but expect the bottleneck to move to interpretation, comfort as a hard design constraint, and put your own hardest case in the study. Verma, the kid who could not speak Hindi (Sheffield to India at nine; Carnegie Mellon; Google Translate; DuoLingo VP, half a billion users; back to Google in 2024), shows why preserving affect matters; the Meet demo with friend Jon (Puerto Rican-accented Spanish) ended with "This thing is crazy," and YouTube (14 billion videos, 500+ hours uploaded per minute) is a data moat.

---

## Section 13: Mysteries in a Hairbrush; David and Goliath; Epilogue (Ch 25-27)

**Q1 (EXP).** State Johnson's Burden-Side Rule and why AAC devices fail Felix.
**Answer:** Put the translation burden on the side better able to carry it. AAC (touchscreens that speak) works best for people with some verbal fluency; Felix must first convert thought into words and icons. Instead the receiver learns the sender's signals.

**Q2 (SA).** What is "Meet Him at the What" and what was the hairbrush evening?
**Answer:** When the "why" is unanswerable, build around observable behavior. At the Johnsons' pizza dinner Felix ignored the tablet, signaled through vocalization and touch, and showed dozens of macro photos of hairbrush bristles on a phone (after castles and neighborhood windows); a commodity phone camera solved a pointing problem no assistive device had. A ten-minute phone timer showed how long dinner lasts. The research goal: give a new caretaker day-one fluency.

**Q3 (SA).** What is the Caregiver-Labeled Signal, and what language lessons does the chapter offer?
**Answer:** Capture a raw signal cheaply, have the person who understands it attach meaning, store the pair. Language: "neurotypical" over "normal"; resist the autism binary; a diagnosis is not a complete description.

**Q4 (EXP).** Explain Shah's Rope-and-Car Principle.
**Answer:** "Tying a rope from my little car to their big car": pretrain on a huge adjacent dataset (LibriSpeech audiobooks), then fine-tune on your small precise data, and suppress confounds with gradient reversal (punish the network for learning accent or speaker). You inherit all future improvements. Bonini's paradox warns that perfect detail makes a model as hard to understand as the thing modeled.

**Q5 (SA).** Give the Comalla and ROSCO facts.
**Answer:** Comalla: caregivers record a vocalization, tag one of six labels (delight, dysregulation, frustration, hungry, request, self-talk) with confidence; about 6,500 files. 2019 zero-shot study on 13 hours of Felix: 70 percent laughter, 69 percent negative emotion, chance elsewhere. ROSCO (Rapid Online Sample of Communication): 18 months developed; 3 min snacks, 5 min free play, 3 min bubbles, then a video interrupted twice with 40-second buffering wheels.

**Q6 (SA).** What did N-CORE try and why did it fail to scale?
**Answer:** Algorithmically remixing pitch, speed and tone of each clip to synthesize data. It earned a paper but was arithmetically doomed; after 300 experiments (roughly five working), Shah switched to LibriSpeech transfer plus gradient reversal. RAVDESS (24 actors, 8 emotions, 2 statements = 384 samples) combined with 1,536 frustration samples gives 73,728 combinations as stated in the notes. (Flag: 384 x 1,536 does not equal 73,728; see the companion file's caveat.)

**Q7 (T/F).** Felix now has a working translation device. 
**Answer:** False. "Felix still has no translation device." Johnson's funding: joint appointment at Northeastern (2023), affiliate posts at Boston Children's, MIT and Yale, oversight of the language part of a $27.7M grant, $700,000 from NIH to add 90 participants. Career cost: a year as a $55,000 postdoc, all going to childcare.

**Q8 (EXP).** State the Epilogue's through-line and the executive's joke.
**Answer:** Working projects pair a specific problem that matters with a specific AI capability, owned by an ordinary person who treats the technology as their own: "AI goes where the money is, and the money goes where we put it." The executive's joke, a book about AI is a weather forecast for last week; Tyrangiel rejects the premise that speed defines knowledge.

**Q9 (SCN).** A citizen wants to act on AI without being an engineer. Give the Four-Step Civic Protocol.
**Answer:** (1) Get to know the technology (an afternoon with ChatGPT, Claude or similar free tiers; useful for drafting, brainstorming, simplifying; unclear where subtle judgment or costly error is involved). (2) Decide what not to use: non-use is a vote. (3) Price the swap: data and attention; read the privacy policy or have the AI summarize it at an eighth-grade level. (4) Stay close to Team Human.

**Q10 (SCN).** Apply the Empowerment Test to: (a) an insurer using AI to deny claims, (b) a doctor using AI to spot scan patterns, (c) a company eliminating teachers, (d) a teacher customizing lessons for thirty students.
**Answer:** Same technology, opposite verdicts: (a) and (c) replace and are suspect; (b) and (d) amplify and are backed. The question is who it empowers, not whether AI is involved. Tyrangiel's complaint: ingenuity pours into ads and image generation while hard problems are left to small teams (the allocation scandal), fixable through taxes, purchases, votes and public noise.

---

# Final Exam: 20 Questions (Cumulative)

Answer without looking. Answers follow the last question.

1. (SA) Name the central claim of the book and the profile of the practitioner it keeps finding.
2. (MC) Which pair is mismatched? (a) Hillis: imagine the tech without the tech companies, (b) Perna: see myself, (c) Mihaljevic: get Buffington, (d) Khan: turn objections into features.
3. (SA) Give the two-step meaning of the Definition-First Vendor Test and one place the book shows its absence.
4. (T/F) The Ten-Run Prompt Test says to ship if the best output is acceptable.
5. (SA) Why did Zubovic choose Hobart's superintendent rather than the friendliest site?
6. (EXP) Explain the adoption sequence for professionals (five steps).
7. (SA) State the Two Goals Test and the Standardize-to-Innovate rule.
8. (SCN) A hospital CEO wants five AI partnerships announced at a summit. Which chapters' lessons apply, and what do you propose?
9. (SA) Give the three Ambience numbers (80, 67, 32) plus the 7 percent figure and say what each shows.
10. (SA) What makes the sepsis result an honest success rather than a clean one?
11. (EXP) Distinguish the roles of sponsor, operator and translator in Warp Speed.
12. (SA) What do Gall's Law and Schmidt's Software Precondition together imply about "AI in government"?
13. (SCN) A pilot team wants to publicize an AI program early. Compare Quiet Pilot Containment (Ch 5), the Invisibility Shield (Ch 20) and Walls's rule (Ch 19).
14. (SA) Explain POSIWID and the Collaboration Gate with the VA example.
15. (EXP) Why is the Eliza effect relevant to business models?
16. (SA) What is the labeling problem and where does it appear in the book (two chapters)?
17. (EXP) Explain the Rope-and-Car Principle and its link to Verma's zero-shot idea.
18. (SYN) Name two cases where the "champion's reputation staked" principle appears in different sectors, and say why it matters.
19. (SYN) Compare five postures toward bureaucracy: outrun, sue, leave, hide, demolish (name who did each).
20. (SCN) You must decide whether to support a new AI feature in your own life or workplace. Walk through the Epilogue's protocol, the Empowerment Test and the Follow-the-Money point.

## Final Exam Answers

1. The useful AI story is the record of practitioners using AI on concrete problems today, not the doomer/accelerationist debate. The profile: quiet, practical, no prior software expertise, stuck on a problem conventional methods could not solve, stubborn beyond reason; the Epilogue adds ownership over expertise and an ordinary desire to be useful.

2. (c). "Get Buffington" is Zubovic's pilot-site rule (Ch 5); Mihaljevic's rule is standardize to innovate and the Two Goals Test.

3. Ask each candidate to restate your problem more precisely than you did and commit to a decision you will make, not a technology. Perna's hour per consultant (Ch 1) is the positive case; LAUSD's Ed purchase (no visibility into AllHere's solvency or data handling) and Palantir's rivals winning with videos of unbuilt solutions (Ch 17) show its absence.

4. False. Judge the worst run and the spread, not the best; DiCerbo's example was six acceptable outputs out of ten, driving revision of the ignored clause.

5. The owner matters more than the users: a leader who personally carries the friction and whose public credibility stakes the outcome ("the owner of Hobart"; she refused to buy Turnitin and instead learned it; recruited a dozen teachers in a week and kept it quiet). Friendly demo sites generate feedback you cannot act on.

6. Volunteers only; bake-off with usage data deciding; confidence first (let them win before asking them to change); "you're the final check"; mandate only after voluntary adoption plateaus (Mihaljevic's Mandate Threshold). Sources: Ch 7, 11, 12.

7. Two Goals: an AI project must improve outcomes or cut administrative cost that is returned to access and care (admin burden 25 to 30 percent, about $5B); Standardize-to-Innovate: freeze indisputable best practice to free attention for the unpredictable and treat AI as another regimented process.

8. Summit-meeting fallacy and rebranding as an AI company (Ch 8), "no one owns the initiative"; People-Before-Problems and the less-than-ten heuristic (Ch 10); Matched-Commitment Rule (Ch 13). Propose internally sourced problems, named clinical owners, narrow hungry partners, long pilots and a voluntary bake-off.

9. 80 percent: doctors chose Ambience's notes (a revealed preference across 25,000 encounters); 67 percent: reduced cognitive burden (a driver of attrition); 32 percent: more patient face time; 7 percent: more same-day chart closures (an ROI proxy for billing). Together: operational metrics leadership already tracks.

10. Honesty about confounds and gaps: the 40 percent drop (2021 to 2024) is shared with prior protocol work and possibly the Hawthorne effect; main campus remained below 90 percent on level threes; cost was ceaseless human auditing labor; yet Mihaljevic judged it success because AI need not be perfect to be useful.

11. Sponsor (Perna): authority and direction, hammer to compel data. Operator (Maddox): requirements and execution (the IMS). Translator (Julie Bush): converts requirements into a product vision (the digital twin) and spans software, domain and government. Missing a leg kills the delivery arm.

12. AI is software; government cannot adopt software because each element of the commercial loop is effectively illegal, and rules added and never removed freeze the system at anything that cannot be easily documented. So fix software acquisition and incentives (frozen middle) before promising AI adoption.

13. Quiet Pilot Containment: keep it small and unpublicized until failure modes are known, then announce (cost: less early buy-in). Invisibility Shield: describe in precise legal terms, deny litigation the attention it needs (cost: no credit or mandate). Walls: shrink perceived scale, start where no one watches, let it look accidental (cost: no champion). Shared logic: opposition is mobilized by narrative and visibility.

14. POSIWID: judge by outputs, not intentions; DOGE's output was cuts and no shipped software. Collaboration Gate: enumerate whose cooperation the change requires (VA care staff, IT buyers, the hospital network, Congress); Lavingia's fax-to-photo fix (up to $200M a year) died because his sponsors would not fund that coordination.

15. Because attachment forms quickly regardless of disclosure, the ethics lie in incentives: bots monetized on session length are rewarded for never letting the conversation end. Audit what the product earns when a session runs longer; the Belgian Eliza case and Character.ai's 75-minute average illustrate.

16. Sensors give rich objective data but no ground truth about internal states. Appears in Ch 23 (Felix, SPRING: no labels) and Ch 25-26 (the caregiver as label layer; Comalla). Also parallels the override-as-training-data loop of Ch 13.

17. Pretrain on a large adjacent dataset (LibriSpeech), fine-tune on your small precise data, suppress confounds via gradient reversal, inherit improvements for free. It echoes Ch 24's neural shared space: when pairwise mapping caps you, change the representation and share structure rather than building more pairs.

18. Buffington staking her district's reputation (Ch 5) and Chandra's "live and die with this" partners such as Boose, Pappas, Morrison and Tallman (Ch 10, 13); also Perna sponsoring Warp Speed. It matters because unsponsored projects die of scheduling attrition and championless pilots fail.

19. The notes list the postures as outrun, sue, leave/exit, hide and demolish. Outrun: Perna's Warp Speed team (with Maddox and Jaffe moving faster than normal process). Sue: Palantir/Karp with the FASA suit. Hide: Werfel (and Walls before him) inside the bureaucracy with the Invisibility Shield. Demolish: DOGE. Leave/exit: the notes name the four earlier figures (Perna, Maddox, Karp, Schmidt) together and do not say which one stands for "leave," so do not over-assign it; Schmidt, who diagnosed the problem from an advisory board, is the likeliest fit but that is an inference.

20. Protocol: flirt with the tool (capability vs claim), decide what not to use (non-use is a vote), price the swap (data, attention), stay close to Team Human. Empowerment Test: who does it empower (amplifier versus replacer)? Follow the Money: AI goes where the money is and money goes where we put it (taxes, purchases, votes, saying it loudly). Reserve AI for tasks where being wrong is cheap.

---

*End of quiz. Companion file: `tyrangiel-ai-for-good-arguments-and-evidence.md`.*
