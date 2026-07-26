# Chapter 12: Hospitals and Hotels

## Core Idea
Cleveland Clinic's biggest AI win wasn't diagnostic — it was logistical: a custom-built dashboard, Hospital 360, that forecasts discharges and exposes bottlenecks, turning an institution that never knew when guests arrive or leave into something closer to a hotel.

## Frameworks Introduced

- **Pappas's Hospital-as-Hotel Model**: treat a hospital as a hospitality business with beds, staff, linens, maintenance, and food service — but no reservation system.
  - When to use: when patient throughput, wait times, or bed availability are the binding constraint rather than clinical quality.
  - How: (1) instrument current-state occupancy and pending admissions in one view; (2) integrate staffing platforms in real time (who is scheduled, available, or about to time out); (3) train on years of administrative data plus physician notes; (4) read free-text signals like "potential discharge for tomorrow" and convert them to per-floor discharge forecasts; (5) let a nonclinical operations team work the queue continuously instead of batching.
  - Why it works: it doesn't make anything move faster — it shows exactly *why* things aren't moving (in Pappas's Wednesday example, a nursing shortage), converting a diffuse complaint into an addressable cause.

- **Build-With, Don't Buy-Out-of-the-Box**: every vendor Cleveland Clinic met wanted to sell a packaged product; none would co-build. The clinic instead ran a quick hackathon with Palantir and shipped.
  - When to use: when your operational reality is genuinely non-standard (Cleveland Clinic has one of the highest case mix indexes in the country).
  - How: pair your most institutionally literate clinician directly with the vendor's engineers, in the room, translating operational requirements. First meeting October 2021; software ready to roll out that December.

- **Pappas's Influence-Without-Authority Pattern**: as a new doctor with no reports, she convened pulmonologists, respiratory therapists, residents, and nurses to build a pediatrics-wide asthma care path — standardizing variation to cut confusion and cost. Alignment across a coalition, not a mandate, is what got leadership's attention.

- **"You're the Final Check" Reassurance**: when automating a team's manual work, name their new role explicitly — Pappas told the twenty-five-person operations team their eyes on what's happening were the check on the system. Headcount doesn't shrink; it just stops growing as the system expands.

## Key Concepts
- **Hospitalist**: a physician who coordinates every aspect of a patient's hospital stay; introduced in a 1996 *New England Journal of Medicine* article by Dr. Robert Wachter and Dr. Lee Goldman, now over sixty thousand strong and one of the fastest-growing specialties in medical history.
- **Why hospitalists exist**: 1980s–90s insurer demands — prior authorizations, pre-certifications, documentation for reimbursement — plus 70,000+ ICD codes meant hospitals needed doctors with consultant-grade administrative skill.
- **Case mix index (CMI)**: a measure of patient acuity; a high CMI means the sickest patients, more specialists, longer stays, and less predictable flow.
- **Grand Central**: the Epic module Cleveland Clinic has used since 2011 for admissions, discharges, and transfers — indispensable but hard to customize.
- **Hospital 360**: the Palantir-built system providing a live "God view" of hospital state plus predictive discharge forecasts (in one session: 91 discharges predicted by end of day, 132 more the next).
- **Family-centered rounds**: Pappas's replacement for private conference-room discussions — clinicians discuss the case at the bedside in plain language, addressing family concerns in real time; patient and nurse satisfaction soared.
- **Short-order-cook workflow**: the pre-AI batch pattern where transfers waited until end of day, after beds were assigned and ORs closed; Hospital 360 made flow constant.
- **Clogged administrative arteries**: Pappas's term for the process bottlenecks she logs in to diagnose.

## Mental Models
- Use **prediction to expose causes, not to speed things up** — the dashboard's value is that it told Pappas *why* only seven of thirty-eight waiting patients had been admitted by 1:35 p.m.
- Think of free-text clinical notes as **an untapped forecasting dataset**: phrases physicians already write become discharge predictions with no new documentation burden.
- Think of an operations AI as **converting a hospital's two user types differently**: sophisticated users get diagnosis, task processors get throughput.
- Use **Pappas's "me, me, me" hypothesis** to predict adoption resistance: medical training selects and conditions for individual competition, then demands teamwork afterward — and the years-long deferred-gratification path selects for conservatism, not risk-taking.

## Anti-patterns
- **Buying out-of-the-box software for a non-standard operation**: vendors selling packaged products couldn't accommodate the clinic's requirements; only a co-build did.
- **Batching decisions to end of day**: waiting until everything is secured before moving transfers guarantees idle capacity all afternoon.
- **Calling doctors Luddites**: Pappas rejects this as an oversimplification that prevents diagnosing the real causes — training in individual competition and institutional conservatism.
- **Automating a team without redefining their role**: the twenty-five-person team's initial fear of job loss would have sunk adoption absent an explicit statement of what they were now for.

## Worked Example
Rita Pappas grew up in Cleveland, a first-generation Lebanese American who spoke Arabic at home and was steered toward nursing rather than medicine. After ten years as a Cleveland Clinic cardiac nurse — executing flawlessly while openly questioning physicians' orders — she quit at thirty-one for medical school at Wright State, then a residency at Rainbow Babies & Children's Hospital, returning to Cleveland Clinic in 2004 as a pediatric specialist and hospitalist. She standardized pediatric asthma care and converted pediatrics to family-centered rounds, then was moved to the adult side and handed patient flow. Cleveland Clinic had used Epic's Grand Central since 2011 but couldn't customize it, and no vendor would co-build. So the clinic ran a hackathon with Palantir; Pappas, now medical director of hospital operations, worked directly with Palantir's very young, medically inexperienced engineers. First meeting October 2021, rollout December 2021. Hospital 360 ingests staffing schedules and Epic physician notes, forecasts discharges per floor, and integrates real-time staffing availability. Results: daily transfer volume up 10%, patients admitted much earlier in the day, minutes cut from each stage of the surgical journey, and emergency room wait times reduced by ninety minutes. Version 2.0 is scoped to automate remediation — routing a stalled echo order to the echo lab rather than merely flagging it.

## Key Takeaways
1. Look for AI wins in logistics and throughput before diagnostics — patient flow is where the CFO, the physician, and the patient all benefit simultaneously.
2. Mine existing free-text notes for predictive signal instead of asking staff to enter new structured data.
3. Co-build with engineers in the room when your operation is genuinely non-standard; a hackathon-to-rollout cycle can run two months.
4. Send your most institutionally literate clinician to sit with the engineers — they translate "what we want to see" into requirements.
5. Tell an automated team what their new job is, explicitly, before they infer it themselves.
6. Realize efficiency gains through hiring restraint as you grow rather than layoffs — the team stayed; it just won't expand with acquisitions.
7. Treat physician resistance as a selection-and-training artifact to be designed around, not a character flaw to be argued with.

## Connects To
- **Ch 10**: Pappas is a second member of Chandra's "less than ten" — and her hypothesis explains why that list is so short.
- **Ch 11**: same partner pattern as Boose, applied to operations rather than documentation; both bought or built on measured outcomes.
- **Theory of constraints**: Hospital 360 is a bottleneck-identification tool; the constraint that Wednesday was nursing staff, not beds.
- **Revenue management / yield management**: the hotel discipline hospitals lack, now approximated by discharge forecasting.
