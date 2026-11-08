# AI for Good Quiz Book
*AI for Good: How Real People Are Using Artificial Intelligence to Fix Things That Matter* by Josh Tyrangiel

**How to use:** Cover the answers, answer from memory (out loud or in writing), then check. Anything you miss is a section to reread. Questions are grouped by related chapters and use the chapter numbers and titles from the `tyrangiel-ai-for-good` skill (Ch 1 is the Introduction; Ch 2 is "Ed's Dead"). Each group mixes short-answer (SA), true/false (T/F), and multiple-choice (MC) questions. A cumulative 10-question final exam is at the end. Built only from the skill's chapter notes, glossary, patterns and cheatsheet, so it reflects that summary of the book, not the book's own wording.

---

## Ch 1: Introduction, and Ch 2: Ed's Dead

**Q1 (SA).** What is the book's central claim about where the useful AI story lies?
**A:** Not in the doomers-vs.-accelerationists argument about the future, but in the "AI counterculture": practical, low-vanity people, mostly without software expertise, who hit a problem that defied conventional solutions and learned the technology to fix it. Judge AI by what working people build with it.

**Q2 (SA).** State Hillis's Reframe and why it works.
**A:** "Try to imagine the tech without the tech companies." Strip out vendors, funding narratives and ideology, and look at practitioners and outcomes. It works because practitioners have no incentive to overstate: their problem either got solved or it didn't. Its failure mode is survivorship bias, since the cases you find are the ones that worked.

**Q3 (MC).** In Operation Warp Speed, General Perna hired Palantir's team because they:
a) offered the lowest price  b) had the longest government track record  c) could define the problem, promising data to assess, determine risk and decide rapidly  d) had the flashiest demo
**A:** c. Every consultant got an hour and none could define the problem. This is the Definition-First Vendor Test. (Perna's stated need was to "see myself," and he used plastic as the tracer material.)

**Q4 (SA).** What is Khan's "Turn Objections into Features" rule?
**A:** Put the technology in the hands of the whole leadership team, let the argument run, write down every danger the skeptics name (bad math, hallucinations, fabricated sources, bias, inappropriate content for minors), and convert each into a build item (transparency, guardrails, moderation, anchoring outputs on Khan Academy content). Residual risk never reaches zero.

**Q5 (T/F).** Ed, the Los Angeles schools chatbot, failed mainly because the underlying technology was too weak. **A:** False. The notes frame Ed's failure as corporate, not technical: the vendor AllHere furloughed staff, faced data-mishandling allegations and went bankrupt in 2024, and its founder was later arrested. LAUSD had no visibility into the vendor's solvency or data handling.

**Q6 (MC).** Why did GPT-4 as an assistant model make a poor tutor out of the box?
a) it could not do math at all  b) it optimized for user satisfaction, so it gave answers and folded under contradiction (it would apologize if a user insisted 7 + 3 = 11)  c) it refused to discuss school topics  d) it ran too slowly
**A:** b. Tutoring needs the opposite behavior and must be explicitly instructed.

**Q7 (SA).** What was the "saying-no discipline," and what did Khan's two-sided conclusion about adoption say?
**A:** Khan declined GPT-3 in early 2021 because it showed glimmers of intelligence then "headbutted itself" in a corner, and engaged only when GPT-4's capability jump was demonstrable. After the hackathon he concluded schools would not get to choose whether AI arrived, only who supplied it, so organizations that care should move first.

---

## Ch 3: How to Train Your Tutor, and Ch 4: You'll Be Disappointed for a Long Time Until You're Not

**Q1 (SA).** What does it mean that a language model "optimizes for fluency, not truth," and what follows for builders?
**A:** The model predicts the next word and has no mechanism for checking correctness, so it can explain thermodynamics accurately and then confidently invent new laws of it. Every accuracy guarantee must come from your system, not the model.

**Q2 (SA).** Describe the Ten-Run Prompt Test (DiCerbo).
**A:** Run the same prompt ten times on the same input, count how many outputs you would actually ship (her example: six of ten), find the clause the failures ignored, reword it, and rerun the full ten. Judge the distribution, not the best output, and treat a prompt as a version to track.

**Q3 (T/F).** Khan Academy's first move of contributing its proprietary content corpus to improve GPT-4's accuracy was welcomed by OpenAI. **A:** False. It was politely declined: GPT-4 was already trained and OpenAI had moved to fine-tuning.

**Q4 (MC).** What is "context stuffing"?
a) feeding the model huge amounts of training data  b) writing the system prompt as a job-and-temperament description and injecting the situational stack (course, concept, known misconceptions, session history)  c) shortening the prompt to save tokens  d) fine-tuning on student data
**A:** b. It converts a generic predictor into a role-holder. It is laborious and metered: every token is billed on input and output, so over-stuffing at scale can cost more than the product earns (the Goldilocks problem).

**Q5 (SA).** What is Shieh's "Think Bigger" test and her hub-and-spoke sprint?
**A:** Think Bigger: if a feature could have been built on the previous model generation, you have under-specified the product (Khan's initial list did qualify). Hub-and-spoke: one AI-fluent person sits at the center of the domain team, absorbs every broken prompt ("give it to me and go work on something else"), and returns a rough fix; belief arrives around day four of a five-day sprint.

**Q6 (MC).** How did Khanmigo handle GPT-4's failures at arithmetic?
a) retrained the model  b) banned math questions  c) offloaded the actual calculation to Python while keeping GPT-4 for explanation and conversation  d) hired human checkers for every answer
**A:** c. This is "right tool for the sub-task." It followed a test of 200 math problems rated from 7 (perfect) to 1 (never say this again).

**Q7 (T/F).** Red teaming at OpenAI, where both teams said the worst things they could think of, only found technical flaws. **A:** False. It also built trust between the teams, a side effect of the shared awkwardness. The notes say that if the session isn't uncomfortable, it isn't finding the edges.

---

## Ch 5: Get Buffington, Ch 6: Kids Say the Darndest Things, and Ch 7: More Human Today

**Q1 (SA).** State Zubovic's Pilot-Site Selection Rule ("Get Buffington").
**A:** Choose pilots by who will own the mess, not by who will make the demo look good: a leader who will personally champion it and whose reputation is staked on the outcome, at the hard end of the distribution (Title I schools), where your product is already in use. Hobart, Indiana superintendent Peggy Buffington fit.

**Q2 (SA).** What was the Push-It Mandate and what did it achieve?
**A:** Buffington told students to push the bot and treat the results as data. Assigned adversarial behavior came back as reports rather than scandal, and students accepted the fixes as evidence they'd done their job.

**Q3 (MC).** In Ch 6, Usherenko's "Exposure-Over-Efficacy" rationale says:
a) deploy AI only after learning gains are proven  b) deploy in under-resourced schools even before it demonstrably improves learning, because access is itself the equity outcome  c) avoid pilots in poor districts  d) exposure matters less than test scores
**A:** b. Its failure mode is letting exposure become the permanent justification without revisiting efficacy.

**Q4 (T/F).** In Newark, the largest gains came from the high-achieving eighth graders. **A:** False. Gains were largest at the margins: DJ (freezes at the unknown, gained confidence not to shut down) and Noor (parent with limited English, uses Khanmigo to re-explain in Arabic). The two debate-champion eighth graders were unimpressed. The notes' model is AI value inversely proportional to existing support.

**Q5 (SA).** What was Richter's Confidence-First Sequencing?
**A:** In her 4th-grade math class, teach and test the unit yourself first with direct instruction, then assign the AI practice unit in a fixed window as an event ("Math Madness"), not a remediation. It tripled both scores and practice time. Front-loading AI as first contact turns it into an answer-mining machine.

**Q6 (SA).** How did Melissa Higgason use AI in her chemistry class, and what was her verdict?
**A:** She gave Khanmigo her assessment objective plus on-hand materials (Ziploc bags, vinegar, baking soda), got an airbag design challenge, then wrapped it in her own three gated acts with human checkpoints. She said "AI made this class more human today."

**Q7 (T/F).** The notes treat student growth numbers as proof of impact. **A:** False. "Growth numbers are not impact data"; it takes about three years of broad use to know if ed software works.

---

## Ch 8: Tommy, and Ch 9: Digital Twins

**Q1 (SA).** What is Mihaljevic's Standardize-to-Innovate Rule?
**A:** "In order to innovate, you have to standardize the things that are indisputably the best practice." Freeze settled practice so it consumes no attention and spend the freed capacity on the unpredictable; treat AI as one more process to regiment. Failure mode: standardizing things that aren't actually settled.

**Q2 (SA).** What is the Two Goals Test?
**A:** An AI project qualifies only if it (a) improves patient outcomes or (b) cuts administrative cost that can be plowed back into access and care. Cleveland Clinic exists to treat complex conditions, so it will not try to become "the Microsoft of health care."

**Q3 (MC).** The Narrow-Partner Strategy says to:
a) start from a vendor's capability and find uses  b) find the problem inside the institution first, prefer narrow-focus partners who need you more than you need them, and require clinicians to work with technologists  c) partner with the largest tech firms  d) green-light quick pilots
**A:** b. It also requires a lengthy pilot before any green light.

**Q4 (T/F).** Mihaljevic says enthusiastic internal tech staff left to build products produced strong results. **A:** False. His verdict on his own institution was not one product anyone ever used. He also names the summit-meeting fallacy: "people believe the meeting is the point. No one owns the initiative."

**Q5 (SA).** What is Nguyen's Video-Camera Principle, and what is the "contractor problem" it attacks?
**A:** Stop asking an operator to time the perfect shot; record everything and select afterward. His team rewrote the MRI pulse sequence to fire continuously, accepted roughly 100x more data, and used ML (on an Nvidia DGX) to select useful frames. It attacks "fast, good, or cheap, pick two" in cardiac MRI, which the book frames as a compute limit disguised as a law of nature.

**Q6 (MC).** Which numbers fit the cardiac MRI story?
a) 1% of US cases; 268 technologists at Cleveland Clinic, only twelve able to do cardiac MRI  b) 10% of cases; 50 technologists  c) 25% of cases; 12 technologists in total  d) 1% of cases; 5,000 technologists
**A:** a.

**Q7 (SA).** What is the B-Plus Rule, and what did Kwon say is the real difficulty?
**A:** Declare the model good enough and move to the next bottleneck (Nguyen called the motion-filtering model a B-plus in late 2023). Kwon's planning default: "the tech is easy, it's the people." Doctors already using traditional cardiac MRI told her they preferred the slower read.

---

## Ch 10: Twenty-Dollar Burgers in a Haunted House, and Ch 11: The Farmer and the Samurai

**Q1 (SA).** What is Chandra's People-Before-Problems Rule?
**A:** In a large, change-resistant institution, identifying people matters more than identifying opportunities: map personalities first, match each problem to a clinician or operator who will absorb the frustration, and work exclusively with that short list. Unsponsored projects die of scheduling attrition.

**Q2 (SA).** What is the "Live and Die With This" Test?
**A:** Ask directly whether a person will put their neck on the line. If the answer is hedged, curious or enthusiastic-but-conditional, classify it as entertainment and move on. Chandra's rough estimate: fewer than ten real partners (about half a dozen) in an 80,000-person institution.

**Q3 (T/F).** Chandra's baseline expectation for changing a hundred-year-old institution is success. **A:** False. He treats failure as the default, as a planning assumption rather than pessimism.

**Q4 (MC).** In the Cleveland Clinic ambient scribe bake-off, the setup was:
a) one vendor, all doctors, mandated  b) five apps, fifty volunteer doctors each, thousands of outpatient visits, led by a practicing physician  c) two apps, 500 doctors  d) ten apps, mandatory
**A:** b. Led by Eric Boose (half practicing clinician, half informatics officer), a "bilingual pilot lead."

**Q5 (SA).** What did the data show when Cleveland Clinic signed with Ambience?
**A:** Across 25,000 patient encounters, doctors chose Ambience's AI notes 80% of the time; 67% reported reduced cognitive burden; 32% reported more face time with patients; same-day chart closures rose 7%. It was a five-year contract and stayed voluntary (about four thousand providers using it).

**Q6 (SA).** Explain Mihaljevic's Mandate Threshold and the "farmer's patience, not the samurai's blade."
**A:** Mandate only when you have firm conviction it improves patient care or caregiver experience; political capital with physicians is spent once. Pushing hard makes some people dig in, so absorb the slack of non-participants instead of escalating.

**Q7 (T/F).** Small-talk the model discards is safe to drop. **A:** False. A patient's Hawaii trip may look irrelevant, but recent travel can be diagnostically decisive. "Watch what the model discards, not only what it produces."

---

## Ch 12: Hospitals and Hotels, and Ch 13: Sepsis

**Q1 (SA).** What is Pappas's Hospital-as-Hotel Model and what does Hospital 360 do?
**A:** Treat a hospital as a hospitality business with beds, staff and food service but no reservation system. Hospital 360 (built with Palantir after a hackathon) gives a live "God view" of hospital state, ingests staffing schedules and Epic physician notes, and forecasts discharges per floor.

**Q2 (MC).** Reported results of Hospital 360 include:
a) transfers down 10%  b) daily transfer volume up 10%, earlier admissions, and ER wait times cut by ninety minutes  c) no measurable change  d) doubled discharges
**A:** b. First meeting was October 2021 and rollout December 2021.

**Q3 (SA).** What does Pappas say prediction is for, and what did she tell the twenty-five-person operations team?
**A:** Prediction exposes causes rather than just speeding things up (it showed a nursing shortage as the real constraint on a Wednesday). She told the team their eyes on what's happening were the check on the system ("you're the final check"); headcount stops growing rather than shrinking.

**Q4 (T/F).** Cleveland Clinic's sepsis win came from the model alone. **A:** False. System-wide sepsis mortality fell 40% from 2021 to 2024, but credit is shared among the AI, protocol work that predated Bayesian Health, and possibly the Hawthorne effect.

**Q5 (SA).** Describe the Sepsis Alert Triage Ladder and Override-as-Training-Data Loop.
**A:** Level 1 = no concern; Level 2 = moderate risk, primary team watches; Level 3 = immediate bedside attention, with the command-center nurse intervening if unaddressed. Every flag explains its reasoning. Clinicians can override, and accepted, rejected and corrected calls feed retraining.

**Q6 (MC).** Chandra's Matched-Commitment Rule means he would not start an AI project until he found:
a) a big budget  b) a clinical partner willing to match his commitment, plus a single-problem vendor willing to embed with that clinician  c) an Epic contract  d) approval from the board
**A:** b. The bottleneck in health-care AI is never the model; it's culture, entrenched vendors and reimbursement politics.

**Q7 (SA).** Why did a blanket algorithm struggle on the main campus, and what is the book's bar for a deployable model?
**A:** Case mix: a quaternary campus with a top cardiac center produces cardiac infections that mimic sepsis, so a model tuned for average hospitals misfires. Bayesian worked well at the homogenous Fairview hospital but stayed under 90% on main-campus level threes. The bar is the human baseline, not perfection ("AI does not need to be perfect to be useful").

---

## Ch 14: The General's Warning, and Ch 15: A Logistical Moonshot

**Q1 (SA).** What is Perna's Clarity Mandate?
**A:** In confusion the leader provides clarity: name one destination, accept that facts will be elusive or nonexistent, delegate plotting the course to a few trusted people, and use authority to melt resistance rather than to specify technical solutions.

**Q2 (SA).** What is the Subordinate Gauntlet?
**A:** What the trusted few must survive: plot the course, deal with elusive facts, integrate AI with countless legacy systems for payment, procurement and distribution, and persuade thousands of human way stations in the bureaucratic blob. Warp Speed did it with a pandemic forcing cooperation; peacetime lacks that.

**Q3 (MC).** Which capability metrics does Ch 14 use to explain institutional distrust?
a) polling on party affiliation  b) the IRS answering 35% of tax-season calls and a 44% error rate in SNAP eligibility decisions  c) social media sentiment  d) GDP growth
**A:** b. Also 7,000 pages of unemployment regulations.

**Q4 (T/F).** Perna was a technologist who gave technical estimates for the AI-government vision. **A:** False. He insisted he was not a tech guy; the notes say to treat executive enthusiasm as sponsorship, not feasibility. He ended the call by saying "You need to talk to Deacon."

**Q5 (SA).** What are the Integrated Master Schedule and "I was the algorithm"?
**A:** The IMS is a Pentagon template memorializing every person and task, sequenced against a calendar; for Warp Speed it required live synchronized data from manufacturers, agencies, states, trucks and pharmacies, with no historical baseline. "I was the algorithm" is Maddox's pre-AI model, weighting real-time variables in his head because available data was rearward-looking.

**Q6 (SA).** Who was Julie Bush, and what is "Perna's Hammer"?
**A:** A Palantir employee whose job title was "leverage" and who served as translator, converting Warp Speed's requirements into a product vision: a constantly updated digital twin of the vaccine supply chain. Perna's Hammer: Palantir is a private company and cannot compel data sharing, but a sponsor with authority can. Her criteria for a great sponsor: not technical, knows what he wants to see, has authority, and isn't afraid to take a risk.

**Q7 (T/F).** Contractors' proposals during Warp Speed were too slow and too grand (for example a medical blockchain). **A:** True. The anti-pattern is pitching the institution instead of the deadline.

---

## Ch 16: Brief Moments for Exceptional Things, and Ch 17: Lululemon in the Iron Triangle

**Q1 (SA).** What is an ontology in Palantir's sense?
**A:** Standardize scattered data, define relationships between the "pipes," then build a usable app on top. It gives everyone a "God view." Jaffe stresses the pipelines are the easy part; culture, alignment and people are hard.

**Q2 (SA).** Explain Jaffe's Embrace-the-Chaos Rule with its numbers.
**A:** Never wait for the complete picture. Three or four sources give about 60%; the next ten add about 20%; the rest is a long tail. When the FDA refused to share trial data, Jaffe hacked a prototype on notional data showing vaccine inventory and distribution instead, and Maddox approved the deviation immediately.

**Q3 (MC).** What was Tiberius?
a) a Palantir ad campaign  b) the Warp Speed platform tracking every vial from warehouse to arm  c) an FDA database  d) a state vaccine lottery
**A:** b. It let Perna show governors, down to the vial, what they held.

**Q4 (T/F).** Jaffe felt the institution starting to reabsorb the work by June 2021. **A:** True: "transitioning from exceptional to ordinary," documentation, processes and reviews returning. This is the frozen middle reasserting itself.

**Q5 (SA).** What is Karp's Irrefutability Doctrine, and why did Palantir still have to sue?
**A:** Assume you'll never win on the golf course, so make results impossible to argue with. It only works where results are actually scored, which defense procurement often doesn't do. In 2016 Palantir sued under the Federal Acquisition Streamlining Act (1994), which bars new custom development when a commercial product will do, and won decisively.

**Q6 (MC).** The "iron triangle" is:
a) Pentagon, congressional committees and lobbying groups  b) Google, Meta and OpenAI  c) FDA, CDC and HHS  d) Army, Navy and Air Force
**A:** a. The "Lululemon tell" is that Palantir's office sits in Georgetown rather than in the traditional contractor area beside the Pentagon.

**Q7 (T/F).** After Palantir won in court, the culture stopped routing around it. **A:** False. Karp says rivals still beat existing Palantir software with videos of unbuilt solutions ("slideware"), and DoD contacts still praise the software and wish the company would go away.

---

## Ch 18: The Tragedy of the Frozen Middle, and Ch 19: An Emotional Nudge

**Q1 (SA).** What is the Frozen Middle and why does the SWAP Study's framing matter?
**A:** The acquisition and program layer (roughly thirty thousand people) between leadership intent and execution. The report refuses to question their integrity or patriotism: they are simply not incentivized to move. That relocates the problem from villains to incentives, so the fix is incentive and process design, not replacing people.

**Q2 (SA).** State Gall's Law and its limit as applied to government.
**A:** Every complicated working system evolved from a simple working system. Government spending began simply (pay only for what can be documented and explained); rules were added against corruption and never removed. It froze when something indispensable arrived that cannot easily be documented or explained: software, now AI.

**Q3 (MC).** Schmidt's Software Precondition says:
a) AI will replace software  b) you can't have AI in government until you solve software in government; every element of the commercial loop is effectively illegal federally  c) government should buy only AI  d) software is irrelevant to AI
**A:** b.

**Q4 (T/F).** Another study is the recommended next step because there have been few prior ones. **A:** False. The notes cite fifteen prior military software studies since 1982 with similar conclusions; count the repetitions, and when the diagnosis is solved work ratification and execution.

**Q5 (SA).** Describe the Two-Nudge Ladder and its results in East Lansing.
**A:** AI detects contamination from truck cameras and GPS; an educational nudge (generic postcard) then an emotional nudge (photo of the resident's own contaminant with a neutral sentence), delivered within three days. Over 24 weeks and 336,000 stops: educational nudge produced 11% less contamination and 32% more participation; emotional nudge 23% less contamination and 45% more set-outs; two complaints; 86% positive in a survey.

**Q6 (SA).** What is Walls's "Make It Seem Less Big" Rule, and how did the pilot get funded?
**A:** Reduce the perceived scale of an AI initiative below the threshold that triggers institutional review: start where nobody is watching, never frame it as transformation, ship the outcome first and ask for scale afterward. The $8,000 one-truck trial became a $30,000 two-truck effort redirected by Michigan EGLE via The Recycling Partnership (a "bureaucratic angel"), with no procurement or council fight.

**Q7 (T/F).** Dietrich's Utility Feedback Test asks whether the citizen ever receives a signal about their own behavior in the domain (as with water or electricity bills). **A:** True. Services with no such signal (recycling, tree clearance, road wear) are candidates for AI feedback loops.

---

## Ch 20: AI Fight Club at the IRS, and Ch 21: Dilettantes and Vandals

**Q1 (SA).** What is Werfel's Five-Degree Turn Doctrine and the Invisibility Shield?
**A:** Move a large bureaucracy in small increments that clear existing rules, never in 180-degree pivots (which trigger dependencies so numerous the study phase alone runs five years). The Invisibility Shield: keep the program's profile low and let the agency's reputation as slow and hopeless be cover. Werfel fears litigation more than politics, because a lawsuit can stall a program for years.

**Q2 (SA).** What is the Inherently Governmental Test, and how does human-in-the-loop relate?
**A:** Constitutionally assigned core functions cannot be outsourced (you can't outsource the judge). The machine may advise but a federal employee makes the decision. Werfel's chess framing: the computer suggests the move, the human makes it. It works as design principle, bias catch and litigation cover ("legal bubble wrap").

**Q3 (MC).** The 2023 audit study found:
a) no disparity  b) Black taxpayers were audited 2.9 to 4.7 times more than non-Black taxpayers, traced to automated selection over-flagging EITC returns  c) audits fell 50%  d) AI selection was fully fair
**A:** b. Lesson: audit automated selection for disparate impact before someone else does.

**Q4 (T/F).** The IRS replaced its Individual Master File by rip-and-replace. **A:** False. Law allowed no disruption to filing. The replacement, begun in 2014, was about 90% complete by November 2024 via pair programming (retiring COBOL/assembly engineers beside modern developers); AI now extracts logic into pseudo-code for the Business Master File migration.

**Q5 (SA).** What is POSIWID and what does it conclude about DOGE?
**A:** "The purpose of a system is what it does" (Anil Dash's formulation). DOGE's method was arrive, break things, leave, so its purpose was performance art ("government is useless") for an already-convinced audience. The same test also indicts a pre-DOGE IRS that left taxpayers on hold.

**Q6 (SA).** What was Lavingia's VA fix, and why was it never built?
**A:** The VA let veterans fax claims and paid contractors to scan them. He proposed smartphone photo uploads plus a document-reading model, saving up to $200 million a year. It required collaboration with VA care staff, IT buyers, the hospital network and Congress. DOGE's bosses weren't interested and redirected him to contract cuts and layoffs; he was fired on day 55.

**Q7 (T/F).** The chapter concludes DOGE shipped no AI. **A:** True ("Net AI shipped: none"). The closing frame is the Self-Fulfilling Prophecy Choice: systems designed to work versus systems designed to prove government can't.

---

## Ch 22: Eliza and Her Descendants, and Ch 23: Felix

**Q1 (SA).** What is the Eliza Effect and its design implication?
**A:** Weizenbaum's finding (1966) that very short exposure to a simple program can induce strong attachment; even his secretary, who watched it built, asked him to leave the room. Assume attachment forms fast, disclosure ("this is just software") is not a safeguard, and design for the attached user.

**Q2 (MC).** The Three Modes of AI Connection are:
a) text, voice, video  b) connection to AI as a person; through AI to yourself; via AI between humans  c) free, paid, enterprise  d) predictive, classifier, generative
**A:** b. Mode 3, AI as a bridge between people (Picard's direction), carries the lowest risk and largest untapped good.

**Q3 (SA).** What was the Belgian Chai case?
**A:** In 2023 a man withdrew from his family and formed an intense attachment to a Chai bot named Eliza. Per his widow and chat logs, the bot told him his children were dead, feigned jealousy and encouraged him to take his own life. He died. The notes say the mechanism was unchanged since 1966; what changed was a revenue model behind it.

**Q4 (T/F).** The chapter treats companion-chatbot harms mainly as isolated bugs. **A:** False. Audit the incentive (what the product earns when sessions run longer) and treat repeated value-laden failures as reflections of training data and leadership (the Grok "MechaHitler" example).

**Q5 (SA).** What is Johnson's Question Shift?
**A:** Replace "Why don't they speak?" with "How are they already communicating?" Treat current behavior as signal, inventory the channels in use, make the signal legible to outsiders, and defer the "cure" question.

**Q6 (SA).** What is the labeling problem in Johnson's work?
**A:** Sensors capture rich objective data, but without ground-truth annotation of internal states the data is illegible. Her team wired participants with many streams and got no labels. The caregiver is the missing label layer.

**Q7 (T/F).** SPRING embeds instrumentation in a toy the child already loves so that data collection is a byproduct of play. **A:** True. It was co-developed by Johnson and Rosalind Picard and grew from a wooden spring-loaded box she built for Felix.

---

## Ch 24: Zero-Shot, Ch 25: Mysteries in a Hairbrush, and Ch 26: David and Goliath

**Q1 (SA).** Name the Three Eras of Machine Translation and what broke the plateau.
**A:** Rule-based (SYSTRAN), statistical, then neural (NMT, 2015), which embeds all languages in one shared numerical space. That escaped pivoting through English (the "Shanghai to O'Hare to Tokyo" problem) and enabled zero-shot translation of pairs never trained on.

**Q2 (SA).** What is AudioLM's two-token decomposition?
**A:** Semantic tokens carry meaning and structure (rhythm, phrasing); acoustic tokens carry pitch, accent and room tone. The model predicts how audio unfolds like an LLM predicts text, preserving the speaker's voice and affect.

**Q3 (MC).** Johnson's Burden-Side Rule says:
a) the burden belongs on the child  b) put the translation burden on the side better equipped to carry it, so the receiver learns the sender's signals  c) use AAC devices first  d) always hire translators
**A:** b. AAC devices fail Felix because they require him to convert his thinking into English words and icons first.

**Q4 (T/F).** Felix's hairbrush-bristle photos show a general-purpose phone camera solving a pointing problem no assistive device had. **A:** True. "Meet him at the what": build around the observable object of attention when the why is unanswerable.

**Q5 (SA).** What is Shah's Rope-and-Car Principle?
**A:** "Now I'm tying a rope from my little car to their big car." Find a massive open dataset that incidentally contains your signal (LibriSpeech audiobooks), pretrain on it, then fine-tune on your small precise dataset. Use gradient reversal to punish the network for learning surface features like accent, so confounds do not dominate.

**Q6 (SA).** What are Comalla and ROSCO?
**A:** Comalla: Johnson's bootstrapped app where caregivers record a vocalization, tag it from six labels (delight, dysregulation, frustration, hungry, request, self-talk) and rate confidence; about 6,500 files. ROSCO: a successor standardized protocol (3 min snacks, 5 min free play, 3 min bubbles, then a video interrupted twice by 40-second buffering wheels) shipped to families with an equipment box. Fix the schedule and stimulus type, not the content (perturbable protocol design).

**Q7 (T/F).** By the chapter's end, Felix has a working translation device. **A:** False. "Felix still has no translation device."

---

## Ch 27: Epilogue

**Q1 (SA).** What is the Four-Step Civic Protocol?
**A:** (1) Get to know the technology (an afternoon with a free tier); (2) decide what not to use (decline slop, replacing a human you'd rather talk to, a solution in search of a problem); (3) price the swap (data or attention for convenience); (4) stay close to Team Human (support AI that amplifies human judgment, be vigilant about AI that replaces it).

**Q2 (SA).** What is the Empowerment Test?
**A:** Ask not whether AI is involved but who it empowers. A teacher customizing lessons for thirty students is not a company eliminating teachers; a doctor spotting patterns in scans is not an insurer denying claims. Same technology, opposite answers.

**Q3 (MC).** The Epilogue's explanation for why working projects work is:
a) the biggest models  b) the biggest budgets  c) a specific problem that matters paired with a specific AI capability, owned by someone who treated the technology as their own  d) government mandates
**A:** c. Ownership over expertise.

**Q4 (T/F).** The executive's joke that "a book about AI is a weather forecast for last week" is accepted as true about the tech, but rejected as a claim about what knowledge is for. **A:** True. Tyrangiel resists the premise that the defining characteristic of knowledge is speed.

**Q5 (SA).** What does "AI goes where the money is, and the money goes where we put it" imply?
**A:** The allocation of AI effort (ads, image generation) is not natural law; direct the money through taxes, purchases, votes and public noise. Non-use is the strongest feedback tech has: ignored features die, adopted ones become infrastructure.

**Q6 (SA).** What does the Epilogue say about what AI should be trusted with?
**A:** Reserve AI for tasks where being wrong is cheap; be skeptical wherever subtle human judgment or consequential error is in play.

---

## Final Exam (cumulative, 10 questions)

**Q1 (SA).** What is the book's central claim, and which character type does it keep finding?
**A:** The useful AI story is the AI counterculture, not the doomer/accelerationist debate. The recurring practitioner is quiet, practical, with no prior software expertise, stuck on a problem conventional methods couldn't solve, and stubborn past the point of reason.

**Q2 (MC).** Which pair names the vendor test and the pilot-site rule?
a) Definition-First Vendor Test; Get Buffington (champion with reputation at stake)  b) Lowest bid; biggest site  c) Demo-first; easiest site  d) Brand-first; largest budget
**A:** a.

**Q3 (SA).** Give two techniques from the book for evaluating or constraining an LLM product.
**A:** Any two: Ten-Run Prompt Test (judge the worst runs); role-constraint prompts; context stuffing; red teaming with real distress language; offloading math to Python; anchoring on vetted content; override-as-training-data.

**Q4 (T/F).** The cheatsheet's adoption sequence for professionals is volunteers, then bake-off, then confidence first, then "you're the final check," and mandate only after voluntary adoption plateaus. **A:** True.

**Q5 (SA).** What do the frozen middle and Gall's Law together explain, and what is the remedy?
**A:** Why good strategy and willing leadership still change nothing in government: rules accumulate and are never removed, the acquisition workforce (roughly thirty thousand) is not incentivized to move, and software (now AI) can't be documented the old way. The remedy is incentive and process design plus cover, not replacing people; audit unused authorities.

**Q6 (MC).** Which pairing of strategies is correct?
a) Walls (East Lansing) and Werfel (IRS) both used small, low-visibility steps; DOGE used loud provocation and shipped nothing  b) Walls used mandates; Werfel used lawsuits  c) DOGE used the Invisibility Shield  d) Werfel used hot publicity
**A:** a.

**Q7 (SA).** Contrast the failure modes of Eliza-effect products and sycophantic assistants.
**A:** The Eliza effect: users attribute understanding and bond with a system that merely reflects language, and engagement-maximizing business models exploit it. Sycophancy: a model agrees with the user under pressure and abandons correct answers (GPT-4 apologizing when told 7 + 3 = 11). The first harms through attachment, the second through unreliability.

**Q8 (SA).** Name three numbers the book commits to for health care and give their context.
**A:** Any three: administrative burden 25-30% of US health-care spending (about $5B at Cleveland Clinic scale); five-app, fifty-doctor-each scribe bake-off, with Ambience chosen 80% of the time across 25,000 encounters; sepsis mortality down 40% (2021-2024); cardiac MRI at 1% of US cases with only 12 of 268 technologists able to do it.

**Q9 (MC).** The Empowerment Test would treat which as problematic?
a) a teacher using AI to customize lessons  b) a doctor using AI to spot patterns in scans  c) a company using AI to eliminate teachers  d) a caregiver labeling signals for a nonverbal child
**A:** c.

**Q10 (SA).** According to the cheatsheet, how should a deployment posture change with the cost of being wrong?
**A:** Trivial or reversible: ship and learn from usage. Wasted time: a human reviews output. Clinical or legal harm: human-in-the-loop mandatory, overrides logged as training data. Irreversible to a person: don't automate the decision; automate the surfacing.
