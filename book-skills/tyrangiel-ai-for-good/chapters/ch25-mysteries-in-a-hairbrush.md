# Chapter 25: Mysteries in a Hairbrush

## Core Idea
Before you can build AI that understands people, you have to sit in the room and watch how understanding actually happens — for minimally verbal people, communication is rich, intentional, and already working between them and their caregivers; the engineering problem is transferring that fluency to strangers, not inventing it.

## Frameworks Introduced
- **Johnson's Burden-Side Rule**: put the translation burden on the side of the equation better equipped to carry it.
  - When to use: designing any assistive or accessibility tool where one party has far more cognitive/communicative load than the other.
  - How: (1) name who is currently being asked to translate; (2) check whether that party is also the one facing the most obstacles; (3) if so, invert — build the system so the *receiver* learns the sender's existing signals rather than forcing the sender into the receiver's format.
  - Why it works: Felix already communicates fluently — through vocalizations, touch, and objects. AAC (augmentative and alternative communication) devices fail him because they demand he first convert his thinking into English words and icons. Meeting him in his own modality preserves the signal instead of destroying it at the input stage.
- **Meet Him at the What**: when the "why" of a behavior is unanswerable, build around the observable "what."
  - When to use: any population or dataset where motivation is opaque but behavior is visible and consistent.
  - How: stop trying to infer intent; give the person a low-friction way to *show* you the object of their attention (Felix's phone photography of hairbrush bristles, castles, specific windows), then work from that shared referent.
- **The Caregiver-Labeled Signal**: caregivers hold years of interpretive knowledge that no sensor captures; make them the labeling layer.
  - When to use: small, highly individualized datasets where ground truth lives in a relationship, not an instrument.
  - How: capture a raw signal cheaply, have the person who already understands it attach meaning, store the pair.

## Key Concepts
- **AAC (augmentative and alternative communication)**: touchscreen devices that speak when a user taps words or images; they work best for people who already have some natural verbal fluency.
- **The autism binary**: the framing that you either "have" autism or don't, which erases the spectrum and, per Johnson, costs people dignity.
- **Neurotypical**: the preferred term over "normal," which implicitly codes autism as abnormal.
- **Nonverbal communication richness**: the organized, intentional vocalizations, touches, and gestures that carry real information but resist easy datafication.
- **Habitual vs. normal**: the distinction the Johnsons interrogate — whether connection has always been easy, or became easy through years of adaptation.
- **Euler's disk phenomenon**: the wobble-and-accelerate motion of a spinning disk as it slows; Felix's nightly ritual with tape rolls.
- **Base of operations**: the home as the one environment where a minimally verbal person's signals are understood without a designated translator present.

## Mental Models
- Think of a caregiver as a **trained but non-transferable translation model** — accurate, years in the making, and locked to one person. The research goal is exporting the weights.
- Use **"exposing your kids is exposing your heart"** as a reminder that in human-subject AI work, the dataset is somebody's family; consent and dignity are design constraints, not paperwork.
- When a tool "seems like the obvious solution," check whose problem it was actually designed around. Obvious solutions usually encode the designer's convenience.

## Anti-patterns
- **Designing for fluency you're assuming exists**: AAC boards presume the user can map internal state onto a fixed menu of pictures; for someone who can't, the device adds a translation step instead of removing one.
- **Treating a diagnosis as a complete description**: the categorical label obliterates the nuance of individual capability and forecloses the search for what a person *can* do.
- **Waiting for the "why"**: refusing to act until motivation is explained stalls indefinitely; the what is often sufficient to build a richer life.

## Worked Example
Kristy Johnson (MIT, later Northeastern) and her husband Michael — an astrophysicist whose work contributed to the first image of a black hole — host the author for pizza at their Boston-suburb home to demonstrate what their son Felix's communication actually looks like. Michael props an AAC tablet against a water pitcher, swipes to a screen of food illustrations including a pizza slice, and predicts flatly that it won't enrich the conversation. It doesn't. Felix ignores it entirely, instead vocalizing and brushing his fingers on his mother's arm and face — signals invisible to the author but resolved by his parents matter-of-factly with more food, a hug, a glissando on the keyboard, or a purple hairbrush he wants to inspect. Kristy sets a ten-minute phone timer so Felix can see how long dinner will last; the family counts down together. Later, Felix takes his mother's phone and shows the author dozens of artfully composed macro photographs of hairbrush bristles — forests of plastic spikes, each casting a shadow — the latest in a series after castles and specific neighborhood windows. For years he could not point at objects out of reach, and his parents had no way to know what he was looking at. A commodity phone camera solved a pointing problem that no assistive device had. The evening's real payload: the interaction was never a puzzle, only the *explanation* was — and Kristy's research question is how to give a new caretaker, on day one, the fluency the Johnsons took years to earn.

## Key Takeaways
1. Spend time with the people you're building for before you decide what the data should be — the interaction, not the diagnosis, tells you what to capture.
2. Check which side of the interaction you're taxing; if it's the side already carrying the most load, redesign.
3. The best assistive technology is often general-purpose and cheap (a phone camera), not purpose-built and expensive.
4. Individual fluency built over years is the ground truth; the research problem is transfer, not discovery.
5. When motivation is unknowable, build around the observable object of attention.
6. Language choices ("normal," "neurotypical") are part of the design; they shape whether users see themselves as broken.

## Connects To
- **Ch 26 (David and Goliath)**: this chapter establishes *why* audio-plus-caregiver-labels is the right signal; Ch 26 is the decade of engineering that follows from it — Comalla, ROSCO, and the data bottleneck.
- **Ch 27 (Epilogue)**: Tyrangiel's "amplify human judgment, not replace it" test is exactly what Johnson is doing — exporting caregiver expertise, not automating caregivers away.
- **Participatory design / co-design**: the users and their families are the labeling authority, not an outsourced annotation vendor.
