# Chapter 11: The Farmer and the Samurai

## Core Idea
Cleveland Clinic proved out AI ambient scribes not by mandating adoption but by running a narrow, voluntary, five-vendor bake-off led by a practicing physician who translated doctor complaints into fast vendor fixes — then bought on data, not enthusiasm.

## Frameworks Introduced

- **Boose's Bilingual Pilot Lead**: put a person who is half practicing clinician, half informatics officer in charge of a clinical AI pilot.
  - When to use: any AI deployment where the end user's tacit workflow knowledge determines whether the product works.
  - How: (1) use the software with the clinician half of your brain and log real friction; (2) feed notes and feedback to both the internal digital team and the outside vendors; (3) act as Sherpa for less technical colleagues; (4) return to vendors with specific, prioritized instructions rather than general dissatisfaction.
  - Why it works: the pilot lead can distinguish "the model is wrong" from "the workflow is wrong," which a pure technologist cannot. Failure mode: the lead's own strengths mask the product's weakness — Boose's warmth and narration made the scribe work for him where a taciturn colleague would find it useless.

- **The Voluntary Bake-off**: run several competing products simultaneously against real volume, then let usage data pick the winner.
  - When to use: when a category looks like a commodity and you can't tell vendors apart from demos.
  - How: pick a narrow problem; recruit volunteers; assign roughly equal cohorts to each product (Cleveland Clinic: five apps, fifty doctors each, 2024, thousands of outpatient visits, dozens of specialties); collect qualitative complaints and quantitative usage; contract with the product clinicians actually choose.
  - Why it works: it surfaces the variance the team assumed away — note quality varied sharply, some apps required so much editing they were useless.

- **Mihaljevic's Mandate Threshold**: mandate only when you have firm conviction the mandate translates into improved patient care or caregiver experience — not before. Political capital with physicians is spent once; hold it until the data justifies the cost.

- **Small-Vendor Leverage**: pair a narrow problem with small companies who crave the validation of your logo, and requested fixes ship in days rather than release cycles.

## Key Concepts
- **Ambient scribe**: phone-based software that listens, with permission, to the doctor–patient conversation and drafts orders, medications, and clinical notes in real time.
- **How it works**: real-time transcription with noise filtering → NLP extraction of symptoms, diagnoses, medications, and plans → context disambiguation (patient concern vs. physician recommendation) → note formatted for the EHR in the physician's style.
- **Doctor-in-the-loop review**: nothing is initiated without physician review of the generated notes before sending.
- **Cognitive burden**: not busyness, but the load of listening, diagnosing, and planning while simultaneously typing notes precise enough for billing codes, legal standards, and future clinical reference.
- **Ghosting volunteers**: pilot participants who opt in and then never turn the app on — Boose heard back from about thirty of every fifty.
- **Narration requirement**: scribes only work if the physician verbalizes the exam, a behavior change some doctors refused.
- **Same-day chart closure**: finishing documentation the day of the visit; it accelerates billing and served as an ROI proxy.
- **Epic**: America's dominant EHR; the app-to-web-to-Epic context switching Boose flagged as the top adoption killer.

## Mental Models
- Think of small talk as **clinical signal until proven otherwise** — a patient's Hawaii trip looks irrelevant to the model but recent travel can be diagnostically decisive. AI trained to strip irrelevance will strip relevance.
- Use the **farmer's patience, not the samurai's blade**: pushing hard makes some people dig in their heels. Absorb the slack of non-participants rather than escalating; you get results without spending authority.
- Think of clicks as the real adoption metric — if a workflow forces switching between app, browser, and EHR, no accuracy gain rescues it.
- Use **voluntary adoption as the honest evaluation signal**: when nobody is compelled, usage rates are a truthful product review.

## Anti-patterns
- **Assuming a category is commoditized**: Chandra's team expected scribes to be interchangeable and were surprised by the quality spread between apps.
- **Mandating early**: the 2000s EHR rollout only worked because a government mandate tied it to payment; Boose had no such leverage and didn't fake it.
- **Grand speeches to non-participants**: Boose neither lectured nor escalated to leadership; he chased quietly and covered the gap.
- **Buying on demos or vendor promises**: the Ambience decision rested on 25,000 patient encounters, not a pitch.

## Worked Example
Eric Boose grew up on a multigenerational fruit and vegetable farm in Norwalk, Ohio — sweet corn, cabbage, greens — and was the first in his family to enter health care. After Ohio State medical school he became a family physician in the early 2000s, just as EHRs arrived; his aptitude for documentation turned into promotions and eventually a role split evenly between practicing medicine and serving as associate chief medical information officer. In 2024 he led Cleveland Clinic's ambient scribe pilot: five apps, fifty volunteer doctors each, thousands of outpatient visits across dozens of specialties. Problems surfaced as intended — variable note quality, trouble with accents and complex condition spellings, and models discarding contextually vital "small talk." Human problems were harder: of 250 consenting adults, some never activated the app and others quit rather than narrate exams. Boose hounded engaged colleagues, took diligent notes on complaints, and returned to small vendors with specific instructions; because the problem was narrow and the vendors wanted the Cleveland Clinic validation, fixes shipped in days. In 2025 the clinic signed a five-year contract with Ambience, a San Francisco company, on the data: across 25,000 patient encounters doctors chose Ambience's AI notes 80% of the time; 67% of clinicians reported reduced cognitive burden (a major driver of attrition); 32% reported more face time with patients; same-day chart closures rose 7%. Ambience remains voluntary, with four thousand providers using it — including one physician who told Boose he could now work another year or two before retiring.

## Key Takeaways
1. Staff pilots with a bilingual practitioner who uses the tool in real clinical work — not a project manager and not a pure technologist.
2. Run competing vendors head-to-head on real volume; assume variance even in "commodity" categories.
3. Choose a narrow problem and a hungry vendor to convert feedback into fixes in days.
4. Hold mandates in reserve until data proves the benefit; voluntary usage rates are then your evidence.
5. Measure ROI in operational terms leadership already tracks — chart closure speed, cognitive burden, patient face time, retention.
6. Design for workflow friction, not just model accuracy: every extra app switch cancels out the time saved.
7. Watch what the model discards, not only what it produces — filtered-out context is where clinical errors hide.

## Connects To
- **Ch 10**: Boose is the partner Chandra names; this chapter is the People-Before-Problems Rule paying off.
- **Ch 12**: Rita Pappas plays the same clinician-translator role with Palantir engineers, and explains the physician resistance Boose absorbed.
- **Human-in-the-loop system design**: physician review as the safety layer that makes an imperfect generative model deployable.
- **Procurement by pilot data**: buying on measured in-situ usage rather than RFP scoring.
