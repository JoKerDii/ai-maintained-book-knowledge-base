# Intermission: Computing Ponds and Rabbit Holes

## Core Idea
The cyberneticians kept trying to build computation out of living or physical "fabric" — ponds, petri dishes, compass needles — rather than out of algorithms written down in advance. The appeal was that a system with no comprehensible logical structure that nonetheless produces good answers feels like real magic, and that appeal sits in direct tension with explainability.

## Frameworks Introduced

- **Fabric (computation without a pre-written algorithm)**: Beer's term for a substrate that has the properties of a computer but does not depend on anyone specifying the algorithm ahead of time.
  - When to use: When you want a system to produce results its designers could not have predicted, and efficiency is not the binding constraint.
  - How: Set up a medium with rich internal dynamics; arrange the initial conditions to correspond to your problem; apply feedback that stabilises or destroys structures until the medium is "tuned"; read the equilibrium as the solution.
  - Why it works / failure mode: The correspondence between problem and medium is the hard, under-specified part — Beer's pond collapsed because the iron filings he fed the *Daphnia* left the water full of suspended magnets, destroying any incipient organisation.

- **The explainability paradox**: Explanation is intrinsically demystifying — it shows how the conjurer put the rabbit into the hat. So "explainable" and "genuinely intelligent" pull in opposite directions.
  - When to use: Assessing claims that an AI system is both fully explainable and genuinely creative.
  - How: Ask whether the result could in principle have been produced with pencil and paper given unlimited time. If yes, there is no magic — just iterated simple operations, however many.

## Key Concepts
- **Computing pond**: Beer's tank of *Daphnia*, algae and larvae, manipulated so its evolutionary dynamics might represent the solution to a computing problem.
- **Tuning**: Using a feedback circuit to stabilise or destroy structures in a medium (Beer and Gordon Pask's ferrous sulphate petri dish, taught to discriminate frequencies) until it discriminates correctly.
- **Turtles / tortoises**: Electronic machines built to drive towards or flee from light sources — early demonstrations that complex behaviour arises from simple connections.
- **Getting out more than you put in**: The persistent dream of AI research — a machine whose ideas its creators can neither predict nor explain.
- **Spooky, fabric-like methods**: Programming approaches that obscure where the rabbit entered the hat; usually neither the fastest nor most efficient, but the ones that hold out the possibility of doing things conventional methods cannot do at all.

## Mental Models
- Think of an explainable AI as a calculating machine — impressive throughput, no wonder.
- Use fabric-style approaches when the problem resists a specification you could write down in advance; use algorithms when you can.
- Think of the tension between explainability and intelligence as a design trade, not a bug to be fixed: the more you can trace the logical structure, the less the output surprises you.

## Worked Example
Beer's computing pond. He stocked a tank with algae and insect larvae and included iron filings among the dead leaves, which the *Daphnia* ingested so that they would respond to an applied magnetic field — the intended input channel. The plan was to set the pond's initial conditions to correspond to a computing problem, then let the evolutionary process of the pond life develop into a representation of the solution. Both correspondences — problem to initial conditions, and evolved state to answer — were never specified. The experiment failed for a mundane physical reason: as more filings passed through the population, the water accumulated a steadily increasing suspension of tiny permanent magnets, which collapsed any organisation that began to form. The medium's own dynamics destroyed the signal it was supposed to carry.

## Key Takeaways
1. Ask of any impressive AI result whether it could in principle be done with pencil and paper and unlimited time — if so, the wonder is throughput, not intelligence.
2. Expect explainability and genuine surprise to trade off against each other; demanding both is close to a contradiction in terms.
3. When building on a physical or living substrate, the substrate's own dynamics are a failure mode, not a neutral carrier.
4. Inefficient, opaque methods earn their keep only when they do things conventional methods cannot do at all.

## Connects To
- **Ch 3**: Directly extends the explainability discussion — Ch 3 asks who gets an explanation, this asks whether an explainable system can be intelligent at all.
- **Ch 4**: The homeostat and the tortoises reappear as the concrete machines behind variety and regulation by veto.
- **Ch 5i**: Another episode of cyberneticians experimenting on living systems to get at principles of control.
