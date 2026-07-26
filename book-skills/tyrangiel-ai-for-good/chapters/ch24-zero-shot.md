# Chapter 24: Zero-Shot

## Core Idea
Machine translation only became genuinely useful when it stopped matching language A to language B and started mapping all languages into one shared space — and the same move applied to raw audio now lets two people talk in their own voices, affect intact, because most of what humans say is far more predictable than we like to believe.

## Frameworks Introduced

- **The Three Eras of Machine Translation**: rule-based → statistical → neural.
  - When to use: diagnosing why any pattern-matching system plateaus, and what kind of change actually breaks the plateau.
  - How: (1) *Rule-based* (SYSTRAN, Cold War origin, powered Google Translate's 2004 prototype) — hand-coded dictionaries plus thousands of grammar rules; works only on perfect syntax and no slang. (2) *Statistical* — stop matching terms, estimate the *probability* that a term in A corresponds to one in B, learned from examples. (3) *Neural (NMT, 2015, University of Montreal)* — ignore pairs entirely; embed all languages simultaneously in a shared numerical space where *dog*, *chien*, and *perro* cluster together, then learn cross-cutting patterns (how questions open, where adjectives land, how a request differs from a command).
  - Why it works: rules require abundant examples of translation already working, which only existed for English-X pairs. Failure mode of eras 1–2: every non-English pair routed through English — a trilingual game of telephone, "sending someone from Shanghai to O'Hare on their way to Tokyo."

- **Zero-Shot Translation**: translating a language pair the model was never trained on.
  - When to use: as the test of whether a system has learned structure or memorized mappings.
  - How: train on many languages into a shared representation; Japanese→Korean then works with no Japanese-Korean examples. The number of viable pairs grows exponentially rather than linearly.

- **AudioLM's Two-Token Decomposition**: split audio into semantic and acoustic tokens, then predict continuations the way an LLM predicts text.
  - When to use: any modality that looks like sprawling noise but may hide a common underlying structure.
  - How: *semantic tokens* carry meaning and structure — rhythm, phrasing, upspeak at sentence end. *Acoustic tokens* carry pitch, accent, room tone. Model both, then learn how audio typically unfolds — just as "once upon a…" predicts "time," a rising terminal pitch predicts a pause and then a second speaker. Bypasses text entirely.
  - Why it works: speech has statistical regularity at both the meaning and sound layers. Failure mode: languages with late-arriving critical information.

- **Verma's Rater-Traceback Loop**: grade output, trace low scores to data, replace data, retrain.
  - When to use: improving any generative system where quality is subjective.
  - How: hire raters to transcribe outputs and score them against top-quality human translation; score voice quality separately; when scores drop, sift the training sources, remove poor ones, add candidates that may or may not help, run expensive training again. No shortcut — "the misery behind the magic."

## Key Concepts
- **Treaty of Waitangi (Feb 6, 1840)**: New Zealand's founding document, signed by the Crown and ~40 Māori chiefs; its two language versions still diverge legally in 2025.
- **kāwanatanga katoa**: the Māori rendering of "sovereignty," closer to custodianship or protection — the core mistranslation.
- **tino rangatiratanga**: chiefly dominion over land, property, and treasure guaranteed in the Māori text while the English assigns ownership to Queen Victoria.
- **SYSTRAN**: rule-based translation system built for the US military; Google Translate's original engine.
- **Neural machine translation (NMT)**: 2015 shared-embedding approach that made direct, unpaired translation possible.
- **AudioLM**: Google model that predicts audio continuation from a few seconds of waveform while preserving the speaker's voice and affect.
- **Semantic vs. acoustic tokens**: *what* is being said vs. *how* it sounds.
- **Word-order lag**: real-time latency driven by grammar — ~1 second for Spanish/English, longer for German or Hindi where the verb arrives last.
- **Statistics Denmark**: government agency tracking Danish life since 1966 across medical, educational, income, and personality categories.

## Mental Models
- Think of **shared embedding space as the escape from pivot languages**. Any system routing everything through a hub inherits the hub's distortions twice.
- Use **"treat modality X the way NMT treated languages"** when a domain looks cacophonous — audio, gesture, sensor streams — and ask what the common structure underneath might be.
- Think of **grammar as a latency budget**: the further a language pushes critical information toward the end of a sentence, the more a real-time system must wait, and the less fluent the experience feels.
- Use **Lehmann's "we're not special"** to explain model performance: prediction works partly because human behavior and speech are highly repetitive. "Our lives are much more boring than they appear."
- Think of a **data moat as a language moat**: Google owns YouTube — fourteen billion videos, 500+ hours uploaded per minute, most featuring humans speaking.

## Anti-patterns
- **Pivoting through a hub language**: routing Mandarin→Japanese through English compounds errors at both hops and was pure artifact of where the parallel corpora happened to exist.
- **Encoding rules before you have examples**: you cannot write rules for how translation *should* work without abundant evidence of how it *already* works.
- **Assuming shared words mean shared concepts**: at Waitangi, "sovereignty" had no Māori equivalent, and two centuries of legal conflict followed a translation gap — not only, or even mainly, bad faith.
- **Treating translation as text-shaped**: text-first pipelines discard the affect — sarcasm, weariness, warmth — that carries the actual relationship.

## Worked Example
**Awaneesh Verma** grew up in Sheffield, moved to India at nine, and despite a daily Hindi tutor and passing written exams, could never speak it — "the kid who couldn't speak Hindi," unable to get complex thoughts *and* emotion out in real time. He majored in computer science at Carnegie Mellon in the early 2000s, was recruited by Google for the then-unreleased Google Translate, and spent his career on language: the "super janky" rules-and-statistics era at Google, then VP of product at **DuoLingo** (half a billion users), then back to Google in 2024 to run real-time communication.

Verma gave the author beta access to Google's first real-time translation tool over an ordinary **Google Meet**. His friend Jon spoke Puerto Rican-accented Spanish; AudioLM didn't subtitle it but *transformed* it — Jon arrived in lightly accented English, discussing a neighborhood bakery, still sounding like Jon. On Jon's end, the author spoke fluent Spanish he had never learned. Jon put his hands to his face: "This thing is crazy." There were lags and film-dub gaps when voices moved fast, but the affect that defined the friendship survived. The conversation then died — they ran out of words for what was happening, in both languages.

Behind it: thousands of rater-hours, iterative dataset surgery, audio compression that made large files scannable fast enough for ~1-second lag in Spanish/English, priority compute allocation, and model updates every few weeks.

## Key Takeaways
1. When a system plateaus, ask whether the representation is wrong before adding rules or data — pairwise mapping capped translation for fifty years; shared embedding uncapped it.
2. Treat zero-shot performance as the diagnostic for whether a model learned structure or memorized examples.
3. Preserve affect, not just content — meaning that arrives without tone loses the relationship it was meant to serve.
4. Expect quality gains to come from unglamorous data curation loops, not architectural cleverness, once the architecture is right.
5. Budget latency by language structure: verb-final languages (Hindi, German) inherently cost more real-time delay than word-order-aligned pairs.
6. Assume mistranslation between concept systems is the default risk in any cross-cultural agreement — Waitangi's gap survived two centuries and is still being legislated.
7. Remember prediction rides on human repetitiveness; the model's fluency is partly a measurement of how unoriginal we are.

## Connects To
- **Ch 23 (Felix)**: the mirror case — translation with abundant parallel data vs. Johnson's population with no parallel corpus at all; both need meaning extracted from non-text signal.
- **Ch 22 (Eliza and Her Descendants)**: this is Picard's third mode — AI as a bridge *between* humans rather than a substitute for one.
- **Large language models**: AudioLM applies next-token prediction to waveforms; the LLM insight generalizes past text.
- **The chapter's closing turn** — "Most of us, but not all of us" — sets up the population whose speech isn't predictable, returning the thread to nonverbal communication.
