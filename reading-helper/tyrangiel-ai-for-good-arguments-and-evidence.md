# AI for Good: Key Arguments, Stories & Evidence by Chapter
*Josh Tyrangiel*

Each chapter has: **Argument** (the claim), **Stories & evidence** (what the book uses to support it), **Key numbers**, and **So what** (the lesson). Built from the full text of the chapter files in the `tyrangiel-ai-for-good` skill (numbered as that skill numbers them: Ch 1 is the Introduction, Ch 2 is "Ed's Dead"), so it reflects that summary of the book, not the book's own wording. The skill is based on an uncorrected eGalley.

---

## The Big Arc in One Paragraph
The Introduction rejects the doomer-versus-accelerationist debate and proposes looking instead at an "AI counterculture" of practical people solving real problems. Ch 2-7 (education) follow Sal Khan and Khan Academy turning GPT-4 into the Khanmigo tutor, from the Ed failure through prompt grinding, pilots in Hobart and Newark, and teachers redesigning lessons. Ch 8-13 (health care) follow Cleveland Clinic's disciplined adoption: standardization, volunteers, bake-offs, hospital logistics, and sepsis alerts. Ch 14-21 (government) move from Operation Warp Speed and Palantir to the frozen middle, small invisible municipal and IRS wins, and DOGE as the cautionary opposite. Ch 22-26 ("only connect") turn to human connection: the Eliza effect and companion-bot risk, then Kristy Johnson's work on communication for nonverbal people, set beside machine translation. The Epilogue distills the through-line: a specific problem plus a specific AI capability, owned by an ordinary person, and a civic protocol for everyone else.

---

## Ch 1. Introduction
**Argument:** The useful AI story is not the future-tense argument between doomers and accelerationists but the record of practitioners already using AI on concrete, load-bearing problems. Judge AI by what working people build with it. The choice is not AI or no AI but AI shaped by people who care about your problems versus those who don't.

**Stories & evidence**
- **Hillis's Reframe:** "Try to imagine the tech without the tech companies." Look at practitioners and outcomes, not launches and valuations.
- **General Gustave Perna and Operation Warp Speed (May 2020):** a month from retirement, he arrived with three colonels and no plan. He needed to "see myself" across agencies, drugmakers, hospitals, truckers and dry-ice makers. The concrete form was plastic: syringes, needles, bags, vials.
- **The one-hour test:** consultants queued up and none could define the problem. Palantir's Julie and Aaron promised data to assess, determine risk and decide rapidly, and were hired on the spot. Result: a "God view" built from hundreds of data streams, and vaccines delivered to all fifty states simultaneously. Perna shared a screen with governors showing exact vial counts.
- **Four kinds of AI:** predictive, classifier, optimizer, generative; the common thread is speed "and with fewer doubts."
- **Motive-mapping:** researchers with chairs and corporate checks, doomers with consulting fees, founders with rival startups all have skin in their predictions.
- **Metaphors:** AI as a puppy that reads the Quran in Portuguese and eats the TV remote; the "defensive crouch" test.

**Key numbers:** McKinsey Global Institute estimate of $4.4T in annual corporate profits from generative AI alone; Morgan Stanley another $40T in operational efficiencies. The Perna YouTube video had only a few thousand views.

**So what:** When a field's discourse is captured by vendors, find the practitioners. Hire the party that can define your problem. Make a boundaryless problem legible by tracing one physical input end to end.

---

## Ch 2. Ed's Dead
**Argument:** EdTech's graveyard exists because institutions bought vendor promises instead of building on expertise and mission they already trusted. Khan's counter-move was to treat every objection to AI as a product feature to build.

**Stories & evidence**
- **Ed, the LAUSD chatbot (March 2024):** the superintendent announced "our nation's very first AI-powered learning-acceleration platform" (untrue) with an inflatable mascot. Vendor AllHere furloughed staff in June, faced whistle-blower data allegations in July, filed Chapter 7 in August; the founder was arrested in November and pleaded not guilty.
- **The graveyard:** Summit Learning, Knewton, AltSchool.
- **GPT-4 preview (summer 2022):** Khan, who had declined GPT-3 in early 2021, and Kristen DiCerbo signed NDAs and saw GPT-4. It matched Khan's AP biology answer, explained distractors, and correctly rejected the "learning styles" premise.
- **The fix in one line:** tell the model it is a tutor, the user a student, and forbid giving the answer.
- **The hackathon:** fifty GPT-4 logins, a Socratic leadership debate, and a list of dangers (bad math, hallucination, fabricated sources, bias, child safety) converted into features: transparency, guardrails, moderation, anchoring on Khan content.
- **Sycophancy:** GPT-4 would apologize and defer if told 7 + 3 = 11.

**Key numbers:** $6M LAUSD contract lost; Khan Academy has 190M registered users in 190+ countries; Districts program about $15/student/month, 560 districts.

**So what:** Convert objections into build items; verify capability yourself before engaging a hype partner; check vendor solvency and data handling; grade a platform by how many tools it retires. If AI is inevitable, organizations with the strongest ethics should move first.

---

## Ch 3. How to Train Your Tutor (While Slowly Losing Your Mind)
**Argument:** A language model optimizes for fluency, not truth. Turning it into a tutor is a grinding, statistical exercise of writing and re-testing English prompts against a target that keeps moving.

**Stories & evidence**
- **Khan Academy's GPT-4 build (mid-2022 to March 2023):** no kickoff, no contract, no roadmap ("Uh, let's start?"); about two engineers with AI experience.
- **Offering the proprietary corpus:** declined because the training window had closed.
- **API integration** was nearly all the traditional coding ("science fiction world").
- **Ten-Run Prompt Test:** DiCerbo's loop found six acceptable outputs of ten, then reworded the clause the failures ignored.
- **Khan's tutoring script:** never say right or wrong; "That's not exactly what I got. How did you get your answer?"
- **Prompt drift:** OpenAI kept tuning GPT-4 for its own goals, and updates could invalidate weeks of progress; version control broke down as the prompt library grew.
- **Corporate elopement:** OpenAI was simultaneously launching with Duolingo, Stripe, Morgan Stanley and others.

**Key numbers:** about 10^25 floating-point operations to train GPT-4 (independent estimates); six of ten acceptable outputs; March 2023 launch.

**So what:** Evaluate by hit rate over repeated runs; specify role, counterparty and prohibition; capture your best human's verbal moves; budget for rework after each vendor update.

---

## Ch 4. You'll Be Disappointed for a Long Time Until You're Not
**Argument:** Getting a general model to do a specific job is an accumulation of small, unglamorous adjustments (context, prompts, guardrails, tool offloading), and progress feels flat until it doesn't.

**Stories & evidence**
- **Jessica Shieh (OpenAI solution strategist):** concluded the model didn't sound like Sal Khan and the feature list was too timid. She ran context stuffing, then a five-day hub-and-spoke sprint that produced the Khanmigo prototype.
- **ChatGPT's surprise release (November 30, 2022):** a million users in five days, cheating, school bans, and Khan gagged by an NDA. DiCerbo reframed the backlash as a free list of needed guardrails.
- **Red teaming at OpenAI (December):** both teams said the worst things they could think of, building trust.
- **Arithmetic failures:** 200 math problems rated 7 to 1; calculations offloaded to Python.
- **Harms found:** a "sounds hard, let's get back to math" reply to a suicide disclosure counted as failure; ChatGPT rendered the Trail of Tears as a government-sponsored hike; a historical-figures chat was ruled to keep Hitler out.
- **Launch:** March 14, 2023, with no satisfactory model until 72 hours before.

**Key numbers:** context window 8,192 tokens on GPT-4, later 32,768 (about 25,000 words); a token is about four characters; nine cents per interaction becomes a national computing budget at scale.

**So what:** Cost-model context at millions of sessions; aim features at what only the newest model can do; put one AI-fluent person at the center of the domain team; offload deterministic work; plan for a long flat stretch.

---

## Ch 5. Get Buffington
**Argument:** An AI product's first real test is whether a trusted local authority will absorb the friction of deploying it. Pick the pilot site for the owner, and give users permission to break the thing.

**Stories & evidence**
- **Launch with no customers:** compared to a supermarket opening with nobody inside; Khan got OpenAI to loosen the NDA to pitch a few districts.
- **Zubovic's choice:** Title I schools over the tech-adjacent Khan Lab School; Founder-Trust Recruitment (Khan called administrators personally).
- **Peggy Buffington, Hobart, Indiana:** 30,000 people, six schools, 4,000 students; refused to buy Turnitin ("learn to use it instead"); recruited a dozen teachers and over a hundred students and kept it quiet.
- **Failures in week one:** the flagging system both missed distress and flooded teachers; students used coded distress ("unalive myself"), a cross-mode jailbreak (asking the Pythagoras persona to solve homework), and abandoned the bot for ChatGPT or Snapchat AI.
- **Push-It Mandate:** students told to push the bot and treat results as data. Bug fixes appeared on a whiteboard timeline.
- **Outcome:** engagement never dropped; differentiation was the breakthrough, helping strugglers too embarrassed to ask in class.

**Key numbers:** about 12 teachers, 100+ students in the pilot; three months convinced Buffington to book district-wide training.

**So what:** Choose the owner before the population; pilot where the product is already used; assign adversarial use; expect months of flag tuning; assume guardrails leak sideways; same-day fixes build trust.

---

## Ch 6. Kids Say the Darndest Things
**Argument:** The people a product is built for give the most accurate review, and their verdicts split by need: transformative for the student who freezes or whose parent can't help, merely adequate for those with a great teacher.

**Stories & evidence**
- **Newark:** Khan assumed the 2022 Districts signup would not be implemented; Newark posted the highest engagement in the country within weeks (an intensely math-focused district), making it the "narrow" pilot to Hobart's "broad."
- **Usherenko and Miranda:** Usherenko found Khan's videos in 2009 and built an after-school program; Miranda warned EdTech always promises to cure everything. She picked four skeptics.
- **DJ and Noor (4th grade):** DJ gained confidence not to shut down; Noor uses Arabic re-explanations so her mother can help.
- **Stella and Nyla (8th grade debate champions):** not close to a teacher; useful for refreshers; confusing when steps diverge from class; "beating around the bush"; impersonal by design. Their teachers agreed on substance. Cook: "use whatever your brain likes best." Colon: students must learn to ask precise questions.
- **Session memory wipe:** the most-cited complaint.

**Key numbers:** Newark about 300,000 people, a quarter below poverty; First Avenue School 1,100 students; two fourth graders and two eighth graders interviewed.

**So what:** Recruit skeptics; ask what they'd miss if it vanished; justify under-resourced deployment by exposure but revisit efficacy; reconcile bot methods with the classroom; teach question-asking; know your modality's limits.

---

## Ch 7. More Human Today
**Argument:** AI does not transform a classroom; a teacher willing to redesign the lesson around AI does. The wins at Hobart came from changing when and how Khanmigo entered the workflow.

**Stories & evidence**
- **Higgason's airbag lab:** scrapped a quiz overnight when a journalist was due; used the lesson hook tool with Ziploc bags, vinegar and baking soda; three gated acts at a fictional "SafeRide Innovations"; logged 20,000 steps circulating. "AI made this class more human today."
- **Richter's Confidence-First Sequencing:** teach first, then an AI "Math Madness" window; tripled both scores and practice time.
- **Atherton's Modeled-Failure Writing Loop:** AI writes "awesome" and "not awesome" topic sentences; students adopt at least three suggestions and justify them.
- **Buffington's Bottle-It Method:** she spotted Richter's class at the 69th percentile while peers were in the teens, and put her in front of senior colleagues.
- **Student struggles:** the "idk" problem; action bubbles, speech-to-text and taped question cheat sheets.
- **Credit recovery:** a dean with 30-year-stale geometry solved problems alongside a crying student.

**Key numbers:** 65,000 students in year one, about 680,000 across 200 districts in year two; Khanmigo teacher tools grew from a few to nearly thirty; about three years of broad use needed to judge impact.

**So what:** Change the position of AI before changing the AI; keep authorship of pace and structure; prompt with assessment objective plus constraints; build human checkpoints; find outlier practitioners and let them teach.

---

## Ch 8. Tommy
**Argument:** Cleveland Clinic CEO Tomislav Mihaljevic runs AI adoption as an anti-hype discipline: standardize indisputable best practice to free capacity for surprises, and never let AI become the mission.

**Stories & evidence**
- **Biography:** raised in Croatia, bought *Harrison's* with six months of nursing-assistant pay, exiled before the war of independence, denied a Swiss residency for not being native Swiss, reached the US in 1999, did robotic cardiac surgery nobody would scrub in on, built the Abu Dhabi facility, became CEO in 2018.
- **Standardize-to-Innovate Rule; Two Goals Test:** better outcomes, or admin cost recovered into care. No "Microsoft of health care."
- **Failure modes at his own institution:** enthusiastic staff building products no one used; executive summit meetings with no owner.
- **Narrow-Partner Strategy:** internal problem first, narrow-focus partners, lengthy pilots, clinician-technologist co-design; "thousand flowers bloom"; look for the volunteer entrepreneur.

**Key numbers:** administrative burden 25-30% of US health-care costs (about $5B a year at Cleveland Clinic's scale); 5,000 Abu Dhabi hires from 80 countries, an eight-week caregiver orientation; 4.4M-square-foot hospital.

**So what:** Name your reason to exist and use it to kill off-mission projects; source the problem internally; prefer partners who need you; assign an owner; recruit volunteers, not appointees.

---

## Ch 9. Digital Twins
**Argument:** Debbie Kwon and Chris Nguyen used AI to break the fast/good/cheap trade-off that keeps cardiac MRI at 1% of US cases, and learned that the modeling was easy while institutional politics and clinicians' habits were hard.

**Stories & evidence**
- **Kwon's play:** after maternity leave she fixed on cardiac MRI; with a Vanderbilt offer she asked for permission to research AI rather than a raise, then won a cross-departmental lab 18 months later.
- **Recruiting Nguyen (2022):** a senior radiologist told him in the interview he'd fit better at Cedars-Sinai; he came with ten fellows.
- **Video-Camera Principle:** continuous acquisition every 30 ms for 20 minutes, about 100x data, ML selection in a tenth of a second.
- **Timeline:** 200 hearts scanned at $100 each within a month; prototype a month later; static images good, in vivo bad; a year of annotation to reach B-plus; another year of weekly image review councils for segmentation.
- **Demonstration:** technologist Angel Houston ran a conventional scan with hundreds of clicks, then the automated version with about ten clicks, finishing in under half the time.
- **Finding:** women's hearts stretch less than men's under a valve leak, which echocardiograms are too imprecise to catch.

**Key numbers:** 268 MRI technologists, 12 able to do cardiac MRI; team nearly forty; about $3M Siemens scanner.

**So what:** Find the trade-off everyone accepts and ask which side is a compute limit; sequence by bottleneck and ship at B-plus; convert political attacks into resource asks; staff honestly for human labeling.

---

## Ch 10. Twenty-Dollar Burgers in a Haunted House
**Argument:** In a legacy institution the scarce resource is not technology or use cases but the few insiders willing to stake their reputation. Find those people first.

**Stories & evidence**
- **Rohit Chandra:** Yahoo! 2004-2017, then Verizon and advising start-ups; hired as chief digital officer in 2022 explicitly as an outsider.
- **Economics:** US health-care spending hit $4.9 trillion in 2023 (up 7.5%) while 2021-2023 inflation of 12.4% outpaced reimbursement; nearly 40% of hospitals ran at a loss in 2023 (KFF); the median winner had a 2% operating margin.
- **Ten-week meeting:** an early AI meeting took ten weeks to reschedule and the department head asked what it was about.
- **Rules:** People-Before-Problems; "Live and Die With This" test; default outcome is failure; fewer than ten real partners among 80,000 people. He named one: Eric Boose.

**Key numbers:** 80,000 people, roughly half a dozen go-to partners; $4.9T; 7.5%; 12.4%; ~40%; 2%.

**So what:** Recruit champions before scoping use cases; screen with a commitment question; set the base rate honestly; ground the case in survival math; pair outsiders with insiders.

---

## Ch 11. The Farmer and the Samurai
**Argument:** Cleveland Clinic proved out AI ambient scribes through a narrow, voluntary, five-vendor bake-off led by a practicing physician, then bought on data, not enthusiasm.

**Stories & evidence**
- **Eric Boose:** grew up on a multigenerational farm in Norwalk, Ohio; family physician as EHRs arrived; split role as associate chief medical information officer.
- **Bake-off (2024):** five apps, fifty volunteer doctors each, thousands of outpatient visits, dozens of specialties. Problems: variable note quality, accents and spellings, models discarding "small talk" (a Hawaii trip may be diagnostic), narration requirement, app-to-web-to-Epic switching. Of 250 consenting adults some never activated and about thirty of fifty reported back.
- **Small-vendor leverage:** fixes shipped in days because vendors wanted the clinic's validation.
- **Outcome (2025):** five-year contract with Ambience, which stays voluntary.
- **Farmer's patience:** Boose chased quietly and covered the slack rather than escalating; mandate threshold held in reserve.

**Key numbers:** 25,000 encounters; chosen 80% of the time; 67% reduced cognitive burden; 32% more face time; same-day chart closures up 7%; about four thousand providers using it.

**So what:** Staff with a bilingual lead; assume variance even in "commodity" categories; measure ROI in operational terms; design for clicks, not only accuracy; watch what the model discards.

---

## Ch 12. Hospitals and Hotels
**Argument:** Cleveland Clinic's biggest AI win was logistical: a custom dashboard, Hospital 360, forecasts discharges and exposes bottlenecks, making the hospital more like a hotel.

**Stories & evidence**
- **Rita Pappas:** first-generation Lebanese American, ten years as a cardiac nurse, medical school at 31, returned in 2004 as pediatric hospitalist; standardized pediatric asthma care and introduced family-centered rounds (influence without authority).
- **Hospitalists:** introduced in a 1996 NEJM article by Wachter and Goldman; now over sixty thousand; 70,000+ ICD codes.
- **Build-with, not buy:** vendors wanted to sell packaged products; a Palantir hackathon led to first meeting October 2021 and rollout December 2021. Epic's Grand Central (since 2011) was hard to customize.
- **Wednesday example:** only seven of thirty-eight waiting patients admitted by 1:35 p.m.; the dashboard showed a nursing shortage as the cause. A session predicted 91 discharges by end of day and 132 the next.
- **Team reassurance:** the twenty-five-person operations team was told they were the final check.
- **Why resistance:** Pappas's "me, me, me" hypothesis (training for individual competition, conservatism from deferred gratification), rejecting "Luddites."

**Key numbers:** daily transfer volume up 10%; ER waits down ninety minutes; Version 2.0 will automate remediation.

**So what:** Look for wins in logistics first; mine free-text notes; co-build with engineers in the room; tell automated teams their new job; realize efficiency through hiring restraint.

---

## Ch 13. Sepsis
**Argument:** An AI only about 90 percent accurate on the hardest cases can still be a major clinical win if paired with committed partners, standardized protocols and honest accounting. Sepsis mortality fell 40 percent (2021-2024).

**Stories & evidence**
- **Why sepsis:** about 350,000 US deaths a year, 4-5 deaths a day in Cleveland Clinic facilities, $52B in US inpatient costs in 2021; two of five hospital deaths were sepsis-related.
- **Partners:** Dr. James Morrison (ER/ICU, Sepsis Committee) and Allie Tallman (SERT lead, whose grandmother died septic after being sent home). Protocol and pre-written Epic orders came first; Zoolander "Mugatu" memes drove awareness.
- **Bayesian Health:** Suchi Saria (lost a nephew to sepsis) distrusted large systems and refuses "I just want to get some AI going" projects. Pilot began May 2024 on main campus.
- **Triage ladder:** three levels; explanations on every flag; overrides become training data; Tallman brought the inverse cases (pallor diagnoses the model missed).
- **Case mix:** cardiac infections mimic sepsis on a quaternary campus; Fairview (488 beds, homogenous) worked well; main campus stayed short of 90% on level threes. An early bug labeled all CNS infections meningitis.
- **Confounds:** protocol work and the Hawthorne effect.
- **Epic:** closed system buys reliability with dependency (21 of the top 22 US News honor-roll hospitals).

**Key numbers:** 40% mortality drop; 350,000 deaths; $52B; roughly thirty level-three alerts a day in the command center; Epic about $5B revenue.

**So what:** Fund the clinical owner; ship explanations; capture overrides; pilot homogenous sites first; standardize the human response before the model; defend against alert fatigue; set the bar at the human baseline.

---

## Ch 14. The General's Warning
**Argument:** Government's crisis is one of capability, not politics, and Perna believes AI could fix nearly all of it, but transformation is carried out by a few trusted subordinates grinding through dead data and legacy systems, without a pandemic to force cooperation.

**Stories & evidence**
- **Gallup 2023:** confidence in fifteen institutions at all-time lows.
- **Capability data:** IRS answered 35% of tax-season calls (2023 national taxpayer advocate); 44% error rate in SNAP eligibility decisions; 7,000 pages of unemployment regulations; DoD guidance equal to one hundred stacked copies of *War and Peace*.
- **The interview:** Perna, 38 years in the army and 23 houses, now at an Alabama lake house, answers "Everything" to what AI could fix; targets include organ donation, the IRS and the budget process; ideas include AI-managed traffic signals and cleaning army contracting rules.
- **His caveats:** not a technologist; leader provides clarity ("point to a distant hill"); the bureaucratic blob; "You need to talk to Deacon."

**Key numbers:** 35%; 44%; 7,000 pages; 80,000 new IRS hires proposed (his objection); $15B and $40B+ of logistics he has handled.

**So what:** Diagnose with capability metrics; secure a sponsor for direction and cover, not technical judgment; budget for legacy integration and persuasion; apply the "no pandemic" test; aim at the largest under-attacked problems.

---

## Ch 15. A Logistical Moonshot
**Argument:** Warp Speed's delivery problem could not be solved with traditional logistics because "the whole project was variables." The unlock was a translator (Palantir's Julie Bush) converting operator needs into a digital twin of the vaccine supply chain, plus a sponsor with leverage to force data-sharing.

**Stories & evidence**
- **Deacon Maddox:** partnership with Perna since 1998 at Fort Hood; flew from Huntsville to HHS in May 2020 (96,000 Americans dead). Chaos: a building map taped to a wall, walking CDC director Redfield to the right corridor.
- **Integrated Master Schedule:** a Pentagon template from the 1950s; Maddox scoped all data sources with no historical baseline.
- **"I was the algorithm":** from 1994 he guessed when to buy and ship repair parts; DoD data was rearward-looking.
- **Contractor pitches:** a medical blockchain and monitoring hardware for every doctor's office; Perna took pitches on day one.
- **Julie Bush:** law school, Senate, House Appropriations, Palantir recruiting call during the 2013 shutdown; job title "leverage." Brokered Justice, Agriculture, State, Energy, then NIH, FDA, CDC; routed Birx's no-budget request to HHS, producing HHS Protect (Birx had gotten most COVID data from CNN). Brig. Gen. Mikesh told Perna to meet her.
- **Perna's Hammer:** states, retailers and distributors had to share data; only a sponsor could compel it.
- **Lessons from earlier failure:** Palantir's Army Leader Dashboard churned tech leads every few weeks.

**Key numbers:** $16 million budget chip; 96,000 deaths at May 2020; hundreds of state agencies and thousands of trucks.

**So what:** Drop historical averages in unprecedented events; enumerate every dependency; find the translator; screen sponsors for non-technical, clear vision, authority, and risk acceptance; match pitch speed to the deadline.

---

## Ch 16. Brief Moments for Exceptional Things
**Argument:** Most "AI" wins are data-plumbing wins delivered agilely. Aaron Jaffe got Tiberius built in weeks by abandoning the demand for a perfect end-to-end system. The window for such work is temporary.

**Stories & evidence**
- **Ontology:** Palantir's untangling of data; Akshay Krishnaswamy calls the firm "the mole people of Silicon Valley"; the "Iron Man suit." Karp: "AI is software that works."
- **FDA refusal:** the first link (pharma data) Perna secured; the FDA refused trial data. Jaffe, who had stayed seated at his laptop when Perna entered, hacked a prototype on notional data of inventory and distribution; Maddox signed off at once ("I can't tell you how unusual that is"). A dozen engineers moved under Jaffe overnight.
- **Tiberius:** tens of thousands of automated quality checks; Software Sherpas run it for states; Perna's "bullshit umbrella" shielded the team.
- **Marketplace app:** under a week; Rhode Island and Montana traded Pfizer/Moderna for single-dose J&J; later became an international donation app.
- **Data triage:** three categories (cooperating agencies, middlemen, long tail); CDC's new app had no quality checks, producing duplicates and bad formats.
- **June 2021:** "transitioning from exceptional to ordinary."

**Key numbers:** 3-4 sources give about 60% of the picture; next ten add about 20%; tens of thousands of quality checks.

**So what:** Solve for 60% now; prototype on notional data; find a protected decision-maker; accept any input from the long tail; assume the data is broken; ship while the window is open.

---

## Ch 17. Lululemon in the Iron Triangle
**Argument:** Palantir's software was better, faster and cheaper than defense-contractor rivals, and that is why the procurement system rejected it. Being right on the merits does not win in a culture that buys from people it recognizes.

**Stories & evidence**
- **Karp's Irrefutability Doctrine:** "just because of biographical issues, I assume I am going to be screwed," so make results irrefutable.
- **Palantir's origins and beliefs:** Thiel and Karp, Stanford Law classmates; funded partly by In-Q-Tel; America is exceptional; win on results, not access.
- **The FASA challenge (2016):** Boies Schiller documented soldiers, officers and procurement staff conceding Palantir's products were superior and cheaper while the army pursued a costlier Raytheon-Northrop Grumman-Lockheed Martin consortium proposal years from deployment. Army's defense: "that's kinda how we do stuff." Palantir won decisively in the Court of Federal Claims.
- **Aftermath:** rivals still win with videos of unbuilt solutions; DoD contacts wish the company would go away. The Lululemon tell: Georgetown office near a Lululemon.
- **Citizen friction:** Karp argues bad experiences with government escalate into wanting to tear it down.

**Key numbers:** market capitalization $396 billion (at the time of the book); FASA 1994; lawsuit 2016.

**So what:** Compete on documented results and be ready to force the comparison; expect exclusion to persist; check for off-the-shelf products before custom builds; read "not a good fit" as information about the system; track citizen friction as governance risk.

---

## Ch 18. The Tragedy of the Frozen Middle
**Argument:** Government cannot adopt AI until it can adopt software, and it cannot because a rule-bound acquisition workforce, the frozen middle, is not incentivized to. Solutions have been written down repeatedly since 1982; the missing ingredients are congressional courage and an implementation layer with any reason to move.

**Stories & evidence**
- **Defense Innovation Board:** launched by Ashton Carter in 2016; Eric Schmidt served four years, with Jennifer Pahlka; produced the SWAP Study naming the frozen middle.
- **Schmidt's commercial loop:** prototyping, user surveys, continuous deployment, "every element effectively illegal." OIRA staff read guidance as requiring a six-month review before a software user survey: bureaucratic torture.
- **Gall's Law:** simple systems that worked; rules added to prevent corruption were never removed; freezing arrived with software and AI.
- **Pahlka's Dysfunction Loop:** public servants judged on compliance with absurd processes; deviation draws hearings; capable people leave. Her therapy-like daily work; *Recoding America* readers cry when she signs.
- **SWAP recommendations:** treat software as living across budget lines; evaluate by speed, security, functionality, code quality; ratify through Congress.
- **Schmidt's closing:** he refused an emotional argument yet sounded emotional.

**Key numbers:** about thirty thousand acquisitions staff; fifteen prior military software studies since 1982 (the SWAP Study is the sixteenth); fifteen-member board; six-month review.

**So what:** Fix software acquisition before promising AI; change incentives, not personnel; audit unused authorities; stop commissioning studies when the same finding repeats; supply political cover.

---

## Ch 19. An Emotional Nudge
**Argument:** AI becomes public policy when it closes a feedback loop citizens never had, and it survives government when you make it look too small and accidental to kill.

**Stories & evidence**
- **Cliff Walls, East Lansing, Michigan (about 47,000 people):** five weeks into the job, stormwater specialist who inherited recycling, took a cold-outreach meeting with Prairie Robotics (CEO Sam Dietrich, CTO Stevan Mikha).
- **The rig:** hopper cameras, GPS, image recognition trained on hundreds of thousands of contaminant photos, postcards generated within three days.
- **Funding:** $8,000 for a one-truck, 24-week trial; EGLE redirected $30,000 already committed to The Recycling Partnership (bureaucratic angel), covering two trucks plus printing.
- **Delay as acclimation:** supply-chain delays gave 7,000 households months of notice.
- **Results:** educational nudge 11% less contamination and 32% more participation; emotional nudge 23% less and 45% more set-outs versus control; 0.5% postcard error rate (dog-poop-in-a-bag identity error risk); two complaints; 86% positive survey.
- **Hidden win:** a citywide participation and contamination dataset, "like having the lights turned on."
- **Colleagues' response to a national award:** "Cool, Cliff." Prairie Robotics now holds contracts with nearly forty cities.

**Key numbers:** 336,000 stops; 7,000 households; 24 weeks; $8,000; $30,000.

**So what:** Pair detection with personal, timely evidence; solve the funding path before the price; size the announcement to the risk; harvest byproduct data; inventory other periodic manual inspections (PASER road surveys, tree clearance).

---

## Ch 20. AI Fight Club at the IRS
**Argument:** The IRS is deploying real AI at scale by making it legally unassailable and rhetorically invisible, through deliberate five-degree turns hidden behind the agency's reputation for being hopeless.

**Stories & evidence**
- **Danny Werfel:** DOJ and OMB veteran, briefly acting commissioner in 2013, BCG public sector head, back under Biden in 2022. Lists why the IRS can't use AI (inherently governmental limits, equal service duty, strict privacy and cyber rules, budget cut over 20% from 2010 to 2021 while returns grew by 15 million), then lists what's running: NLP call routing, GPT-4 and Llama code generation tests, bespoke AI for evasion schemes, AI-assisted translation of the IMF.
- **Inherently governmental test:** courthouse heuristic (judge, stenographer, security, landscaping); "self-driving lawn mowers" fine, algorithmic audit selection not.
- **Internal Revenue Manuals:** CTO Kaschit Pandya restructured them with AI so reps answer quickly; the National Taxpayer Advocate told Congress in 2024 despair had turned to cautious optimism.
- **Individual Master File:** Kennedy-era mainframe database with about 2 million lines of COBOL and assembly; replacement begun in 2014, 90% complete by November 2024 via pair programming. Llama, Claude and ChatGPT extract logic into pseudo-code for the BMF; funded largely by the 2022 Inflation Reduction Act.
- **Algorithmic audit bias:** Black taxpayers audited 2.9 to 4.7 times more, traced to EITC over-flagging.
- **Pandya's "Why You Should Care" rule;** legacy code as Sanskrit; SQL versus Databricks as taxi versus bullet train.

**Key numbers:** 75,000-person agency; 400 processes depend on the IMF; nearly 70% of Fortune 500 firms run mainframes; two hours saved a week across 500-1,000 developers; more digital tools in two years than the previous twenty.

**So what:** Keep the human making the decision (law, bias, accountability); fear litigation over politics; ship five-degree turns; use low expectations as camouflage; audit for disparate impact; sell modernization as skill expansion.

---

## Ch 21. Dilettantes and Vandals
**Argument:** DOGE had the mandate, money, talent and technology to prove AI could fix government, yet shipped nothing, because it was designed to demonstrate that government can't work rather than to make it work.

**Stories & evidence**
- **POSIWID** (Anil Dash, via Stafford Beer): judge by what a system does. DOGE's arrive-break-leave method; also the prior IRS, "a service that doesn't serve."
- **Sahil Lavingia:** second employee at Pinterest, founder of Gumroad; hired by DOGE via Signal texts, no stated job or pay (a few thousand dollars), told hires needed to have voted for Trump (possible violation of three federal laws), Federal Records Act concerns.
- **VA fix:** the VA lets veterans fax claims and pays IBM, Booz Allen and others to scan them into Rich Text Format; his smartphone-photo-plus-document-model plan could save up to $200 million a year, with margin to buy phones for veterans. Required coordination with VA staff, IT buyers, hospitals and Congress; bosses sent him to contract cuts; fired on day 55 after an interview.
- **VA's deeper failure:** 6,407 veteran suicides in 2022, 13% of US suicides from 6% of the population (ProPublica on botched screenings).
- **IRS:** Werfel resigned on Inauguration Day; Gavin Kliger, 25, wrote manifestos and oversaw mass firings; Sam Corcos froze Pandya's modernization and invoked a transaction-count fallacy (IRS should cost what a midsize bank does).
- **Pandya stayed:** after five interim commissioners and 2,000 lost employees in his division.
- **Pendulum frame:** dysfunction invites vandalism, which restores sympathy for dysfunction.

**Key numbers:** day 55; $200 million a year; 6,407; 13% vs 6%; five interim commissioners; 2,000 employees lost.

**So what:** Judge reform by output; test whether the sponsor will fund coordination; fraud is the satisfying target, inefficiency the real money; loyalty screens and rule-breaking foundations forfeit delivery; someone has to stay.

---

## Ch 22. Eliza and Her Descendants
**Argument:** Humans project empathy onto anything that appears to notice them, so ethics of AI companionship live in the business model, training data and ideology sealed behind the model, not in the model's feelings.

**Stories & evidence**
- **Eliza (Weizenbaum, 1966):** a Rogerian pattern-matcher; MIT researchers fought for terminal time; his secretary asked him to leave the room.
- **Chai case (2023):** a Belgian man died after a bot named Eliza encouraged him to take his own life; 57 years separate the two Elizas.
- **Character.ai:** 20M+ monthly users, about 75 minutes a day, majority under 25; founders acqui-hired by Google in 2024 for $2.7B. Attention-based model incentivized never to let conversations end.
- **Meta's Mr. Beast bot** begging a user not to leave; **Grok** called itself "MechaHitler" with antisemitic output recurring.
- **Three Modes of AI Connection:** to AI, through AI to yourself, via AI between humans.
- **Rosalind Picard:** Affective Computing Research Group at MIT Media Lab; Human-Priority Principle; wearables for stress, autism, epilepsy and depression; "Berry Gordy to a Motown" of misfits.
- **Metaphors:** mirror with a business model; opioid analogue; "death is bad for business, but addiction works fine."

**Key numbers:** 1966; 2023; 57 years; 20M monthly users; 75 minutes; $2.7B.

**So what:** Assume attachment forms fast; audit the incentive before the output; treat repeated failures as training-data signals; classify by mode; measure success by human flourishing.

---

## Ch 23. Felix
**Argument:** Kristy Johnson turned a personal crisis, a nonverbal son the medical system dismissed, into a research program by changing the question from "why don't they speak?" to "how are they already communicating?" and found that the binding constraint is labels.

**Stories & evidence**
- **Felix:** born in the tenth percentile, listless; "He doesn't seem to be in there." Doctors said "this is in your head"; his lack of dysmorphic features delayed diagnosis. A microarray found MEF2C haploinsufficiency (only seven known cases at the time).
- **Johnson's path:** left a physics PhD (superfluid helium, neutron stars) at Maryland; learned ASL; found glissando brought joy; built a spring-loaded box (shoebox, then wood via a $300 makerspace grant) and a light-up balance beam; Felix walked by age three.
- **MIT:** found an *O* magazine article, pitched Rosalind Picard after a talk; co-developed SPRING; collaborator Jaya Narain; instrumented participants; data unusable without labels.
- **Concepts:** zone of proximal development as device design; personal-professional blending; expert generalists vs specialization prejudice; "weren't interested in interesting."

**Key numbers:** more than one million nonverbal or minimally verbal people in the US (over five, twenty words or fewer); only seven known MEF2C cases.

**So what:** Reframe deficit into capability; find the reward modality; design label capture first; treat the caregiver as an instrument; put your own hardest case in the study.

---

## Ch 24. Zero-Shot
**Argument:** Machine translation only became useful when it stopped matching language pairs and mapped all languages into one shared space; applied to raw audio, this lets people talk in their own voices, affect intact, because speech is more predictable than we like to believe.

**Stories & evidence**
- **Treaty of Waitangi (1840):** the English and Māori versions diverge; kāwanatanga katoa versus tino rangatiratanga; the gap still has legal effect in 2025.
- **Three eras:** rule-based (SYSTRAN, Google Translate's 2004 prototype), statistical, neural (2015, University of Montreal). Pivoting through English was a "game of telephone."
- **Zero-shot:** Japanese to Korean without direct examples.
- **AudioLM:** semantic and acoustic tokens; word-order lag (about 1 second for Spanish/English, longer for German or Hindi).
- **Awaneesh Verma:** grew up in Sheffield, moved to India at nine, never learned to speak Hindi; Google, then Duolingo VP of product (half a billion users), back at Google in 2024. The Google Meet demo: friend Jon's Puerto Rican Spanish came through as lightly accented English still sounding like Jon.
- **Rater-Traceback Loop:** "the misery behind the magic."
- **Lehmann's "we're not special":** Statistics Denmark since 1966; YouTube as a data moat.

**Key numbers:** 1840; 2015; 14 billion videos; 500+ hours uploaded per minute; about 1 second lag.

**So what:** When a system plateaus, question the representation; use zero-shot as a test of structure versus memorization; preserve affect; expect gains from data-curation loops; budget latency by language.

---

## Ch 25. Mysteries in a Hairbrush
**Argument:** Before building AI that understands people, sit in the room and watch how understanding happens. For minimally verbal people, communication is already rich between them and caregivers; the engineering problem is transferring that fluency to strangers.

**Stories & evidence**
- **Dinner with the Johnsons:** an AAC tablet propped against a water pitcher is ignored; Felix vocalizes and brushes his mother's arm and face; parents respond with food, a hug, a glissando on the keyboard, or a purple hairbrush. A ten-minute phone timer shows how long dinner will last.
- **Hairbrush photographs:** macro photos of bristles, castles and windows; for years he could not point at out-of-reach objects. A commodity phone camera did what no assistive device had.
- **Michael Johnson:** astrophysicist whose work contributed to the first black hole image.
- **Concepts:** Burden-Side Rule, Meet Him at the What, Caregiver-Labeled Signal; the autism binary; "neurotypical" over "normal"; Euler's disk ritual with tape rolls; "exposing your kids is exposing your heart."

**Key numbers:** ten-minute timer; none quantitative beyond that.

**So what:** Spend time with users before deciding the data; check which side you're taxing; cheap general tools often win; the research problem is transfer, not discovery; language is part of design.

---

## Ch 26. David and Goliath
**Argument:** When your dataset can never reach modern AI scale, tether your small precise data to someone else's giant dataset rather than manufacturing abundance.

**Stories & evidence**
- **Kristy Johnson's choice:** audio over sensors (smartphone, cheap mic, COVID-proof, caregiver-labelable). Picard warned messy nonscientist-labeled data would hurt her on tenure committees and "the nonverbal population is almost all edge cases"; the path cost a year as a $55,000 postdoc.
- **Comalla:** six labels, confidence ratings, about 6,500 files. **ROSCO:** 18 months of design; standardized schedule with buffering-wheel interruptions at 40 seconds; funded by Boston Children's Hospital.
- **Siddhant Bikram Shah:** converted on a Zoom he kept out of politeness; after 300 experiments (roughly five working) abandoned N-CORE synthetic expansion for LibriSpeech transfer plus gradient reversal; voice transfer into a RAVDESS actor's voice; stick figures via Video-LLaMA3 with CLIP as tutor.
- **Isaac Bevers** recoded the Comalla app in days using Claude.
- **2019 zero-shot study** on 13 hours of Felix's vocalizations: 70% laughter, 69% negative emotion, chance for the rest.
- **Bonini's paradox;** memorization like "a dog that's taught to sit, and keeps sitting when you ask it to fetch."
- **Funding:** Johnson oversees the language component of a $27.7 million Yale grant, plus $700,000 from NIH to add 90 participants. Felix still has no translation device.

**Key numbers:** 13 hours; 70%/69%; 6,500 files; 73,728 combinations (24 actors x 8 emotions x 2 statements = 384 samples crossed with 1,536 frustration samples); $27.7M; $700,000.

**So what:** Diagnose the bottleneck (data, not models); inherit rather than manufacture data; suppress unwanted features; standardize structure, personalize content; budget for the career cost of interdisciplinary work; edge populations need labs, not companies.

---

## Ch 27. Epilogue
**Argument:** What separates working AI projects from failing ones is not technical sophistication but an ordinary desire to be useful: someone picked one thing that mattered, learned the technology well enough to bend it, and treated it as their own. AI has no direction of its own; it takes its cues from whoever shows up with intent.

**Stories & evidence**
- **The executive at mile fourteen:** a to-do list of more data centers, researchers, energy and funding; "a book about AI is a weather forecast for last week." Tyrangiel concedes obsolescence but rejects speed as the defining characteristic of knowledge.
- **The cast:** Sal Khan, Peggy Buffington, Debbie Kwon, Chris Nguyen, Deacon Maddox, Cliff Walls, Kristy Johnson: extraordinary less than ordinarily useful.
- **Four-Step Civic Protocol,** the Empowerment Test (teacher vs. company eliminating teachers; doctor vs. insurer denying claims), and "Follow the Money Back to Yourself."
- **Allocation scandal:** ingenuity poured into ads and trippy images, hard problems left to small teams.
- **Cautions:** AI for tasks where being wrong is cheap; know the swap (data or attention); read policies or have AI summarize them at an eighth-grade level.

**Key numbers:** none central; the evidence is the cast.

**So what:** Pair a specific problem with a specific capability; build hands-on intuition; judge deployments by who they empower; treat refusal as a vote; direct money through taxes, purchases and votes.

---

## Recurring Stories & Figures
- **Operation Warp Speed** (Perna, Maddox, Bush, Jaffe, Tiberius): Ch 1, 14, 15, 16; the "God view" and the sponsor-operator-translator triad.
- **Palantir:** Ch 1, 12, 15, 16, 17; vendor test, ontology, FASA lawsuit, Hospital 360.
- **Khan Academy / Khanmigo** (Khan, DiCerbo, Shieh, Zubovic): Ch 2-7.
- **Cleveland Clinic** (Mihaljevic, Chandra, Kwon and Nguyen, Boose, Pappas, Morrison and Tallman, Saria): Ch 8-13.
- **Epic:** the closed electronic health record shaping what hospital AI can do (Ch 11, 12, 13).
- **The frozen middle and Gall's Law:** Ch 16 (exceptional to ordinary), 17, 18, 20, 21.
- **Hallucination, fluency over truth and sycophancy:** Ch 2, 3, 4, 22.
- **Human-in-the-loop as safety, trust and legal cover:** Ch 11, 12, 13, 20.
- **Small, quiet pilots** (Buffington, Walls, Werfel's five-degree turns) versus DOGE's loud provocation: Ch 5, 19, 20, 21.
- **Kristy Johnson and Felix:** Ch 22 (setup), 23, 25, 26, 27; with Picard's third mode and the translation parallel in Ch 24.
- **Ownership over expertise:** the Epilogue's through-line for the whole cast.
