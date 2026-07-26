# Chapter 23: Felix

## Core Idea
Kristy Johnson turned a personal crisis — a nonverbal son the medical system dismissed — into a research program by changing the question from "why don't they speak?" to "how are they already communicating?", and discovered that the binding constraint on AI-assisted communication is not sensors or models but *labels*.

## Frameworks Introduced

- **Johnson's Question Shift**: stop asking "Why don't they speak?" and start asking "How are they already communicating?"
  - When to use: any domain where a population is defined by a deficit relative to a norm, and research has stalled on closing the gap.
  - How: (1) Accept the person's current behavior as signal, not noise. (2) Inventory the channels actually in use — vocalizations, gestures, physiological state, attention. (3) Build a framework to make that signal legible to outsiders. (4) Defer the "cure" question, which helps no one today.
  - Why it works: the deficit question serves the researcher's curiosity; the capability question serves the person right now. Failure mode: reframing can look unserious to reviewers who fund deficit research.

- **Zone of Proximal Development (applied to device design)**: build tools that sit in the gap between what a learner can do alone and what they can do with support.
  - When to use: designing any intervention or assistive device for a developing or impaired user.
  - How: establish what the person can do independently → design a task just beyond it → make the reward modality one they actually respond to (for Felix: glissando and light displays, not shapes or words) → instrument it so progress is measurable over time.
  - Why it works: engagement is the scarce resource; calibrating difficulty to the zone is what keeps the person in the loop long enough to learn. Failure mode: designing to a generic developmental benchmark rather than this individual's baseline.

- **SPRING (Smart Platform for Research, Intervention, and Neurodevelopmental Growth)**: a customizable interactive research-through-play platform, co-developed by Johnson and Rosalind Picard, that probes how different reinforcement modalities affect learning and physiological regulation.
  - When to use: when you need research-grade data from participants who can't consent to or tolerate a lab protocol.
  - How: embed the instrumentation (smartphone, sensors) inside a toy the child already loves, so data collection is a byproduct of play rather than an imposition.

- **Personal-Professional Blending (Picard's encouragement)**: put your own case inside the study.
  - When to use: when you are the world's foremost expert on a single participant.
  - How: enroll the person you know best in the research group so you can diagnose failure fast — Johnson could look at Felix and immediately know the protocol wasn't capturing him at his best.

## Key Concepts
- **MEF2C haploinsufficiency syndrome**: Felix's diagnosis — a missing gene critical to brain development, with only seven known cases worldwide at the time, all involving developmental delay, intellectual disability, epilepsy, autism, and no speech.
- **Microarray**: DNA-scanning tool for deletions and mutations; the instrument that finally produced a diagnosis after months of dismissal.
- **Nonverbal / minimally verbal**: over age five and able to speak twenty words or fewer; more than one million people in the US.
- **Glissando**: the smooth slide between notes; the sound that reliably elicited something like joy in Felix and became a design primitive.
- **The labeling problem**: sensors capture rich objective data, but without ground-truth annotation of internal states the data is illegible — even to the people who love the child.
- **Affective computing**: the field, led by Picard at the MIT Media Lab, of sensing and responding to human emotional and physiological state.
- **Expert generalist**: someone with broad cross-domain knowledge rather than one deep specialty; the MIT Media Lab is explicitly a refuge for them.
- **Specialization prejudice**: academia rewards mastery of a single instrument and reads field-hopping plus lived personal stake as a lack of seriousness.

## Mental Models
- Think of a caregiver as **the missing label layer**. Sensors have the signal; the parent has the ground truth; the whole engineering problem is transferring one into the other in real time.
- Use **"measure everything first"** when you don't yet know what the signal is — audio, video, accelerometers, wearables — but expect the bottleneck to move immediately from collection to interpretation.
- Think of **lived experience as a data asset, not a bias**. Johnson's stake in Felix is what let her recognize failure in the protocol faster than any credentialed observer could.
- Use **comfort as a hard design constraint**, not a nicety: participants who can't be told why they're wired up will simply stop being themselves under instrumentation.

## Anti-patterns
- **Diagnostic dismissal of the informed parent**: doctors saw two educated white parents, assumed Googled worst-case scenarios, and told Johnson "this is in your head." Felix's beauty and lack of dysmorphic features actively delayed his diagnosis — smug pattern-matching against outdated visual criteria.
- **Hiring for slots instead of missions**: universities conceded Johnson was interesting but "weren't interested in interesting," rejecting the one person who combined the technical range and the lived expertise the problem required.
- **Instrumenting participants who can't consent or self-regulate**: cameras, microphones, and body sensors change the behavior of autistic and nonverbal participants, corrupting the very data you're collecting.
- **Collecting data before solving labeling**: dozens of simultaneous streams and no way to mark the moment a child shifts from calm to frustrated produces volume, not knowledge.

## Worked Example
**Kristy Johnson** left a physics PhD at the University of Maryland (superfluid helium, neutron stars) when her son **Felix** was born in the tenth percentile, listless, unresponsive to his name. "He doesn't seem to be in there," she told doctors who repeatedly told her to stop worrying. A neurologist finally ordered genetic testing; a microarray returned **MEF2C haploinsufficiency**. Johnson felt relief — a name on paper.

She then re-specialized around him: American Sign Language when hand movement drew his gaze; home trials that identified **glissando** as a source of joy; and, because Felix was oblivious to shapes and struggled to control his hands, a **programmable spring-loaded box** with custom lights and music, calibrated to his zone of proximal development. First a shoebox, then wood via a $300 makerspace grant. She built a light-up balance beam that got him walking by age three, and the spring device produced gestures his parents could translate into needs — enough to get him into a Boston special-needs preschool and give her hours back.

Rejected by every graduate program, she found an *O* magazine article about the MIT Media Lab in her mother's stack of reading, applied, and pitched **Rosalind Picard** after a Cambridge talk. Picard (100+ patents) helped turn the wooden box into **SPRING**: an embedded smartphone, dense sensors, a hexagonal frame — "the kind of thing Jony Ive would make in residency at Fisher-Price." With collaborator **Jaya Narain**, Johnson wired participants for everything. The data arrived and was unusable: no labels. Her verdict: "This is science. You try and fail and keep going until you figure it out."

## Key Takeaways
1. Reframe deficit questions into capability questions — it changes what you build and who benefits now.
2. Identify the reward modality the individual actually responds to before designing the intervention; generic developmental toys assume abilities your user may not have.
3. Expect the bottleneck to move from data collection to data labeling, and design the label-capture mechanism as a first-class part of the system.
4. Treat the caregiver as an instrument: they hold expertise that exists nowhere else and currently cannot be exported.
5. When institutions demand specialization, find the ones that explicitly recruit expert generalists — the mismatch is structural, not a judgment of your work.
6. Put your own hardest case inside the study so you can detect protocol failure faster than metrics will show it.

## Connects To
- **Ch 22 (Eliza and Her Descendants)**: Picard's "third kind of connection" — AI as a bridge between humans — is exactly what Johnson pursues; this chapter is the payoff of that chapter's closing scene.
- **Ch 24 (Zero-Shot)**: both chapters are about translation; Google's problem was too much parallel data, Johnson's is that no parallel corpus exists at all for nonverbal communication.
- **Zone of proximal development (Vygotsky)**: repurposed from pedagogy into hardware calibration.
- **Ground truth in supervised learning**: the labeling problem here is the classic ML annotation bottleneck, made acute because only one person on earth can annotate each participant.
