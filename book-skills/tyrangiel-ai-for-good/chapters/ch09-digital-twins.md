# Chapter 9: Digital Twins

*(Part 2 — "Physician, Heal Thyself" — Chapter 2)*

## Core Idea
Debbie Kwon and Chris Nguyen used AI to break the trade-off that keeps cardiac MRI at 1% of US cases — and learned that the modeling was the easy part; the institutional politics and the clinicians' attachment to their own habits were the hard part.

## Frameworks Introduced

- **The Contractor Problem (applied to diagnostics)**: your heart exam can be fast, good, or cheap — pick two.
  - When to use: any diagnostic or process choice where quality, speed, and cost visibly trade off and everyone has accepted the trade as permanent.
  - How: (1) Identify the modality that is best on quality alone (cardiac MRI: structure, size, function, and tissue in one scan, no radiation, no incision). (2) Locate the exact constraints that make it slow and expensive — scan duration, technologist scarcity, data volume, read time. (3) Ask which constraints are *systemic* rather than physical. (4) Attack those with compute.
  - Why it works: the trade-off was a compute limit disguised as a law of nature. Failure mode: mistaking a physical limit (magnet cost) for a systemic one.

- **Nguyen's Video-Camera Principle**: stop asking the operator to time the perfect shot; record everything and select afterward.
  - When to use: any expert-timing bottleneck where skill scarcity gates throughput — "like being a sports photographer who has to time the perfect shot."
  - How: (1) Rewrite the acquisition step to capture continuously (his team added lines of code to the 2016 open-source software that runs most of the world's MRI machines, creating a new *pulse sequence design* that fires every 30 ms for 20 minutes while the patient breathes normally). (2) Accept the resulting ~100× data explosion as the price. (3) Add ML to sort the useful frames from breathing and fidgeting — Cleveland Clinic gave him an Nvidia DGX system; selection runs in a tenth of a second. (4) Then automate the setup itself.
  - Why it works: "The difference is compute." People always knew continuous capture was better; only now can the output be organized.

- **Kwon's Leverage-at-the-Offer Play**: convert a competing job offer into a mandate rather than a raise.
  - How: (1) Get recruited (Vanderbilt). (2) When leadership asks how to keep you, present the ambitious institutional idea, not a salary number. (3) Accept a bad-sounding deal — go research it and come back with a business plan, no funding guaranteed. (4) Return 18 months later with a structural ask: a new lab deliberately sited between cardiology, radiology, and biomedical engineering, plus an outside chief researcher.
  - Failure mode: you spend 18 months of nights and keep your full clinical load with no guarantee. Kwon did both.

- **Nguyen's B-Plus Rule**: declare the model good enough and move to the next bottleneck. He pulled Kwon aside in late 2023 to say the motion-filtering model was a B-plus — not great — and that they needed to move on.

## Key Concepts
- **Digital twin**: an AI-generated simulation of *your* actual heart, built from real imaging and health data, that can be shared, tested, and improved — a single source of truth that travels with you.
- **The model that disappears**: every doctor builds a mental model of your heart from available data, and it vanishes when you leave the room; the next doctor rebuilds it differently, colored by personal bias and treatment preference.
- **Pulse sequence design**: the coordinated instruction set governing an MRI's RF field, magnetic field, and gradients — Nguyen's team rewrote it.
- **Image segmentation**: teaching a model to carve an image into meaningful anatomical pieces; trivial for toddlers, newly approximable by machines, and the key to delivering scans "preloaded" with heart geometry to a doctor's inbox.
- **In vivo failure**: static prototype images were crisp; live scans were bad, because the model had to learn to filter motion blur.
- **CIRC**: Nguyen's Cardiovascular Innovation Research Center at Cleveland Clinic; team grew to nearly forty.
- **The technologist bottleneck**: Cleveland Clinic has 268 MRI technologists; only twelve can do cardiac MRI.
- **Weekly image review council meetings**: clinicians moving pixel by pixel through thousands of ventricle and valve images, correcting anatomical mistakes for the engineers — roughly a year of it.

## Mental Models
- Think of AI adoption as **a sequence of bottlenecks**, not a project: technician → patient → radiologist read time → FDA. Each is a separate build.
- Use **"the tech is easy, it's the people"** (Kwon) as the planning default. Budget most of your effort below the technical line.
- Treat **the human capacity for boredom as currently indispensable to AI progress** — unlike apprentice drafting or document review, the reward here is watching the machine outgrow you.
- **We're all warriors for the change we want, and build citadels around what we don't.** Apply it to yourself before applying it to the resisters.

## Anti-patterns
- **Assuming clinicians will adopt something demonstrably better**: doctors already using traditional cardiac MRI told Kwon they *preferred* the slower, more labor-intensive read.
- **Waiting for resisters to age out**: Nguyen's instinct — focus on younger fellows and let the old guard become obsolete. Kwon wouldn't write off colleagues, though the chapter shows her hedging.
- **Underestimating internal sabotage**: a senior radiologist told Nguyen to his face during the recruiting interview that he'd be a better fit at Cedars-Sinai.
- **Superficial collegiality**: Kwon's own pre-AI mode — compartmentalized, not connecting deeply. The immersion in data science, where everything is posted publicly for others to use and improve, was the culture shock that changed her.
- **Escalating for a firing instead of resources**: Kwon couldn't get the radiologist removed, so she converted the incident into equipment and headcount — including a ~$3M Siemens Magnetom Cima.X.

## Worked Example
**Cleveland Clinic cardiac MRI, 2018–2024.** Kwon returns from maternity leave dreading her stacks of EKGs and cardiac CTs, afraid exhaustion is making her miss things. She fixes on cardiac MRI as the superior modality stuck at 1% national use. Recruited by Vanderbilt, she trades the offer for permission to research AI solutions — knowing, by her own admission, nothing about AI, only that imaging looked like low-hanging fruit because it is "so computationally based." Eighteen months later she wins funding for a cross-departmental lab and keeps treating patients while running it.

She targets Chris Nguyen, a biomedical-engineering PhD who had built an AI cardiac imaging lab at Mass General, and recruits partly on a shared Korean-Christian connection — withholding until his visit that her own husband is a Korean pastor. Despite the sabotaged interview and a competing Cedars-Sinai offer, Nguyen moves in 2022 with ten fellows and millions in grants.

Within a month they scan 200 hearts at $100 per participant; a month later, a prototype. Static images excellent, in vivo bad. A year of annotation, parameter tuning, and validation gets the motion model to B-plus. Then segmentation: another year of weekly council meetings. Result, witnessed on a February day at the Mellen Center: lead technologist Angel Houston runs a conventional scan with hundreds of precisely calibrated mouse clicks and sympathetic breath-holding, then runs the automated version — roughly ten clicks to verify geometry, then she leaves the room to fetch a bottle of water while the scan completes in less than half the time. "I don't hate it at all!"

Kwon's own payoff isn't throughput: MRI reveals that women's hearts don't stretch as much as men's under a valve leak, which echocardiograms are too imprecise to catch — meaning women may be referred to surgery too late, risking heart failure before intervention.

## Key Takeaways
1. Find the trade-off everyone has accepted as permanent, then ask which side of it is a compute limit.
2. Replace expert timing with total capture plus AI selection wherever skill scarcity gates throughput.
3. Sequence your builds by bottleneck and ship at B-plus; the next bottleneck is worth more than the last 10%.
4. Convert political attacks into resource asks — you often can't win the personnel fight, but you can win the equipment.
5. Site a new lab structurally between the departments whose cooperation you need.
6. Plan for adoption resistance from the very experts the improvement helps most; better is not self-evidently persuasive.
7. Expect a long stretch where meticulous human labeling is the rate-limiting input, and staff for it honestly.

## Connects To
- **Ch 8 (Tommy)**: Kwon is precisely the volunteer entrepreneur Mihaljevic described, and the Kwon–Nguyen lab is his narrow-focus, clinician-plus-technologist model executed.
- **Ch 7 (More Human Today)**: same adoption pattern as Hobart — the tool works only where a practitioner redesigns the workflow around it, and resisters cite craft attachment.
- **Digital twin engineering (aerospace, manufacturing)**: the concept ported from simulating jet engines to simulating a specific patient's organ.
- **Precision medicine**: "based on *you*, not just a dataset of people like you" — the argument against population-average guidelines.
