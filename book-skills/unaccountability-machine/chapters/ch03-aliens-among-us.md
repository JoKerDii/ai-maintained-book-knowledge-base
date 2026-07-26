# Chapter 3: Aliens Among Us

## Core Idea
Treat corporations and other large organisations as non-human decision-making systems — black boxes whose outputs must be attributed to the system rather than to any individual inside it. Individual accountability shrinks not because managers are sneaky, but because complexity forces everyone, insiders included, to treat the organisation as a whole they cannot inspect.

## Frameworks Introduced

- **Decision-making system (instead of "artificial intelligence")**: Drop the question of whether an organisation is "really" intelligent and ask only whether it makes decisions and whether those decisions can be traced to identifiable humans. If they can't, treat the organisation itself as the decider.
  - When to use: Whenever you are tempted to argue about whether a company "is" an AI, or to hunt for the one person who "really" decided.
  - How: (1) Identify the outputs that matter. (2) Ask whether the process producing them is comprehensible enough to name a decision maker. (3) If not, attribute the output to the system — "Boeing did this", not "this middle manager did this".
  - Why it works: It is a simplifying assumption, not a metaphor and not a literal claim about consciousness — it is more accurate than either enumerating every contributing decision or scapegoating one person.

- **Principle of diminishing accountability (cybernetic grounding)**: The amount of individual accountability a system can support is inversely related to how far it must be treated as a black box; since organisations get more complicated as they grow, accountability falls as a matter of structure.
  - When to use: Diagnosing why nobody is responsible for a large organisational harm.
  - How: Ask how many interconnected feedback circuits an insider would need to hold in mind. Ashby's point: with four mutually connected parts, twenty circuits can be traced, and knowing all twenty still does not describe the whole. Past that threshold, insiders adopt the intentional stance too.
  - Failure mode: It excuses too much if used as a defence rather than a diagnosis — the point is to redesign the system, not to absolve.

- **Conspiracy-versus-cock-up dissolution**: For systemic outcomes, stop asking whether it was deliberate or accidental. Systems don't make mistakes (if they do it, that is their purpose), and they have no inner desires (so they don't do it intentionally either) — there is only a network of cause and effect.
  - When to use: Post-mortems, inquiries, press narratives about corporate scandal.
  - How: Replace "who intended this?" with "what structure made this outcome the systematic output?"

- **Explainability as a political, not technical, fact**: To say a system has an "explainability problem" is to say it is complicated enough to be treated as a black box — and that decision is rarely neutral.
  - When to use: Reviewing AI governance claims or corporate opacity.
  - How: Notice that explainability research is almost never applied to favourable decisions; it is funded to explain refusals. Ask who benefits from the box staying closed.

## Key Concepts
- **Black box**: A system whose internals you deliberately do not open, because it is comprehensible only as a whole; respecting its integrity is the signature move of management cybernetics.
- **Accountability sink**: An organisational structure that severs the link between an outcome and any human who can be held responsible for it.
- **Intentional stance**: Treating a system as if it has mental states and attributing its actions to its intentions — the practical necessity for anyone dealing with a large organisation.
- **Chinese room argument**: Searle's thought experiment in which a bureaucrat follows a rulebook to converse in Chinese without understanding it — read here as an argument about accountability, since the operator cannot be held responsible for outputs he doesn't comprehend.
- **Paperclip maximiser**: Bostrom's self-improving machine that pursues a single simple objective past all human interest — the model for organisations that prioritise financial results even in the face of extinction-level harm.
- **Responsibility gap**: The problem of assigning liability when an automated system causes harm (self-driving car, loan-scoring algorithm).
- **Complicated vs. complex**: Most current machine-learning systems are complicated (many parts, traceable maths) but not complex in Ashby's sense; complex systems cannot be treated as an interlaced set of independent feedback circuits, only as a whole.
- **Ethics of AI as business ethics**: Corporations have operated above the black-box threshold for centuries, so AI's accountability problems are already here in non-computational form.

## Mental Models
- Use the black-box stance when opening the box is either impossible or actively misleading — partial knowledge of a few feedback circuits inflates confidence far faster than it improves reliability.
- Think of a corporation as hardware made of people, running an algorithm made of policies, handbooks and corporate communications.
- Use "systems don't have intentions" when someone demands to know whether a scandal was conspiracy or incompetence — the honest answer is usually neither.
- Think of public inquiries as attempts to do two impossible things at once: reconstruct causation in an incomprehensible system, and assign responsibility where it barely applies.

## Anti-patterns
- **Deep-but-partial expertise**: Knowing a great deal about a subset of a system raises confidence disproportionately to reliability — it's how financiers talk themselves into bubbles ("it's different this time") and how the State Department underperforms a parrot trained to say "don't start a war."
- **Scapegoating the traceable individual**: Charging the one person whose paperwork is legible (Boeing's technical pilot Mark Forkner) while corporate intent goes unproven — proof the accountability sink worked.
- **Fairness on average**: Optimising a system against an aggregate distribution when fairness or unfairness only ever happens to individuals.
- **Assuming explainability is neutral**: Framing opacity as a purely technical challenge, when the choice of what to treat as a black box carries the political weight.

## Worked Example
Fox News and the voting-machine defamation case. Reading the internal emails, there is no scheme: individual decision makers each react to their immediate pain points — audience figures, share price moves, angry viewer feedback — and each assumes someone else will stop anything catastrophic. No one weighed defending market share against the risk of defaming a party with the resources to sue. But calling it an accident fails too: the audience did not arrive believing in stolen elections by chance. A long series of local decisions to stir up rage for a quick ratings win accumulated into an institutional, system-wide commitment to serve the angriest and least-informed slice of the viewership. That commitment was a real decision with real consequences, and nobody made it. This is the template: not conspiracy, not cock-up, but a structure whose systematic output was the harm.

## Key Takeaways
1. Attribute systemic outputs to the system by name — it is more accurate than enumerating contributing decisions or scapegoating a middle manager.
2. Expect accountability to fall as organisations grow; it is a structural consequence of complexity, not a moral failing of managers.
3. Stop litigating conspiracy versus cock-up for organisational harms; ask what structure made the outcome inevitable.
4. Distrust your confidence in proportion to how much detail you know about a subset of a complex system.
5. Treat "we need explainability here" as a claim about who is allowed to see inside, and ask who chose the boundary.
6. Apply the AI-ethics agenda to corporations too — they crossed the black-box threshold centuries earlier and answer to far weaker rights of explanation.

## Connects To
- **Ch 1**: Supplies the cybernetic theory behind the accountability sinks and the "principle of diminishing accountability" first sketched there.
- **Ch 2**: Applies Beer's black-box method — respecting the integrity of the box — to corporations rather than factories.
- **Ch 3i**: Extends the explainability argument: a fully explainable system is demystified, so explainability and "real" intelligence pull against each other.
- **Ch 4**: Answers the closing question — if these systems can go bad, how do you diagnose them? Via requisite variety.
- **Ch 9**: The morbid symptoms are what these pathological decision-making systems produce at scale.
