# Chapter 4: How to Psychoanalyse a Non-human Intelligence

## Core Idea
Diagnose an organisation by checking whether its regulators have as much variety as the things they are supposed to regulate. Ashby's law of requisite variety is the load-bearing principle: a system achieves stability only if every source of variability from the environment is matched by an equal or greater source of variety in the regulatory system.

## Frameworks Introduced

- **Ashby's Law / Principle of Requisite Variety**: Anything that aims to be a regulator of a system needs at least as much variety as that system. Stated fully: a given system has the potential to achieve stability only if every source of variability from the environment is matched by an equal or greater source of variety in the regulatory system. Beer called it the cybernetic equivalent of Newton's laws of motion.
  - When to use: At every point in a system where one thing is meant to regulate something else.
  - How: (1) Choose your black boxes and say which states and properties you will count — variety is not intrinsic, it is a property of how you choose to describe the thing. (2) For each regulatory relationship, compare the variety of potential disturbances with the variety of the regulator. (3) You rarely need a number: it is far easier to check whether regulator variety is greater or less than input variety than to count bits. We all know what someone looks like when they're overloaded. (4) Where it falls short, add variety to the regulator or attenuate the input.
  - Why it works / failure mode: Information and control are twin quantities — a channel's capacity to carry a message bears the same relationship as a control system's capacity to respond to disturbances. Failure mode: if a manager or team lacks information-handling capacity at least equal to the complexity of what they're in charge of, control is impossible and the system eventually becomes unregulated.

- **Variety engineering (Beer's name for what he did)**: The process of checking that the law of requisite variety is being respected at all points in the system where one thing is meant to regulate something else.
  - When to use: Designing or diagnosing any management structure, reporting line, or control system.
  - How: Name the black boxes and the connections between them; define the survival set (acceptable output ranges); compare varieties across each regulatory link; then close gaps by attenuating variety on the input side, amplifying variety on the regulator side, or splitting the problem.
  - Why it works / failure mode: The engineering is scientific once the description is fixed, but the original description is subjective and fallible — the art is in the metaphors and analogies, in deciding whether the national wheat production system is more like a brain or a stopwatch.

- **Variety attenuation**: Deliberately throwing away information on the assumption it isn't relevant, so that a smaller regulator suffices. Turning continuous ambient temperature into "too hot / too cold" so a two-state heater can match it — that is a thermostat.
  - When to use: Whenever a regulator faces more variety than it can handle and some of the incoming distinctions genuinely don't matter.
  - How: Reduce the information set to the distinctions that drive action; match those states to regulator states.
  - Failure mode: You may have thrown away what you needed (the thermostat is useless when the lab is on fire and the temperature passes 100 degrees). Note: you are *always* attenuating unless you are describing the whole universe — the simple act of drawing black boxes is attenuation, since it states what you will pay attention to.

- **Variety amplification**: You cannot literally amplify variety (information relates to entropy; amplifying it would breach the second law). You do the stereo-amplifier trick — a small voltage switching a much larger one — by building regulatory subsystems inside the wider regulator.
  - When to use: When one regulator must cover far more instances than it can attend to individually.
  - How: Make a one-time investment in subsystems that use a *different* source of variety (a heat-sensitive switch responding to the environment) to replicate decisions you could never make one by one. If you can build one thermostat, you can build a thousand — the limits are only practical.

- **Regulation by veto**: Divide the potential range into acceptable and unacceptable regions; a subsystem vetoes the current state when it is unacceptable, and the system searches until nothing vetoes.
  - When to use: Huge, complicated search problems where evaluating full configurations is prohibitive.
  - How: Give each relevant sensor a veto over the shared control variable. The system either settles into a state satisfying all vetoes, or oscillates and requires higher-level intervention.
  - Why it works: Vetoing a situation as unacceptable is an informationally very cheap action.

- **Splitting the problem (separation into sub-problems)**: Separating one large regulatory problem into several smaller independent ones — almost as important to organisational cybernetics as amplification and attenuation.
  - When to use: When variables genuinely can be treated independently (ambient temperature vs. food vs. water in a squirrel cage).
  - How: Check the variables are actually separable, then regulate each independently. The more variables you can do this with, the more your ability to regulate is amplified.
  - Failure mode: Splitting non-separable problems destroys the problem rather than solving it — smashing a Rubik's Cube into twenty-six sub-cubes "solves" them all and solves nothing.

## Key Concepts
- **Variety**: The number of states a system can be in — a quantity like information but used in contexts of large systems and control rather than transmission; not intrinsic, but a property of how you choose to describe the system.
- **Regulator**: The black box whose inputs include the outputs of the regulated system, and whose outputs are that system's inputs; its job is keeping outputs inside the survival set.
- **Survival set**: The defined ranges of output variables corresponding to the regulated thing continuing to exist — possibly a simple list, possibly complicated if variables interact.
- **Stability / regulated**: The regulator succeeds in holding outputs inside their survival ranges; not an objective property of anything physical, but a property of how you chose to analyse the system.
- **Ultrastability (Ashby)**: A system that can adapt to at least some shocks *outside* the range anticipated by its designer — as opposed to one stable only across a known range.
- **Viability (Beer)**: The potential to persist as an independent entity; the descendant concept of Ashby's ultrastability.
- **Information as entropy**: Wiener's version treats information as entropy with a negative sign — the amount of order in a sequence; Shannon's drops the sign and treats it as unpredictability, whether a sequence constitutes "news". British cyberneticians followed Wiener, which is why they reached for "variety".
- **Translation capacity**: Ensuring each black box receives inputs in a format it can convert to outputs — in large organisations, much of the staff exist to do this (getting the vet's prescription onto the squirrel's feeding tray).
- **Dynamic matching in time**: The regulator must take in information faster than the system generates variety and respond quickly; observation frequency must match the frequency with which the system's state can change.
- **Ataxia and purpose tremor**: The two failure modes Wiener found in the automated gunsight — feedback too weak, so the gun trails its target; feedback too strong, so it oscillates and overcorrects. Named after cerebellar injury symptoms; the moment control engineering became cybernetics.
- **Viable system model**: Beer's further set of principles for structuring how you draw the black boxes and which connections must exist — built on Ashby's law, and the basis of his claim to be the father of management cybernetics.

## Mental Models
- Think of the control system as a model of its environment: if the model misses real sources of environmental variety, the system drifts out of control without anyone understanding why.
- Use the vehicle-controls test for a quick variety check — a train goes forward and back, so one handle; a car turns, so a steering wheel; a plane makes two kinds of turn, so a joystick. Match control dimensions to system dimensions.
- Think of an accountability sink as a *solution* as much as a problem — building cause-and-effect subsystems so managers don't decide case by case is exactly variety amplification, and unappealability is its side effect.
- Use "is the regulator's variety greater or less than the input's?" rather than trying to count bits — the comparison is tractable where the measurement is not.

## Anti-patterns
- **Regulator variety below system variety**: Control is not possible; the system will eventually become unregulated regardless of anyone's effort or good intentions.
- **Attenuating away information you needed**: The thermostat design that ignores everything above "too hot" fails silently until the lab is on fire.
- **Overestimating regulatory variety**: Assuming a part of your control system can handle more than it can, or assuming information is being transmitted when it isn't — both produce slow, unexplained drift out of control.
- **Splitting interconnected problems**: Sub-dividing variables that actually interact destroys the problem instead of decomposing it.
- **Automating inside the existing structure**: Wiener's wartime design choices pushed research towards automating what could be automated rather than redesigning whole processes — Beer's gibe was that 1970s companies recruited the greatest geniuses of humanity, then set them to memorising the phone book to save a few seconds turning pages.

## Worked Example
The squirrel survival facility. Treat squirrel-plus-cage as one black box with outputs — weight, body temperature, heart rate, ambient temperature, light/dark — and define the ranges over those outputs that mean "this squirrel survives until the next reading". Left alone, disturbances push some variable out of the survival set and the squirrel dies, so the model needs a second black box: the regulator, taking cage outputs as inputs and supplying cage inputs as outputs. Now compare varieties. Lighting has two states and needs roughly equal amounts of each, so a switch — one bit — matches it exactly. Ambient temperature varies continuously: either build a continuously variable heater (matched variety) or define "too hot"/"too cold" and use an on/off heater — attenuation, and a thermostat. Scale to a hundred cages in different rooms and you cannot watch every thermometer: fit mechanical thermostats to each, amplifying your variety by delegating to a different source of it. Add staff to weigh rodents and clean cages, and standard husbandry policies to attenuate incoming variety. That is a squirrel farm, and it is also an organisation.

## Reference Tables

| Move | What it does | Example |
|---|---|---|
| Attenuation | Discards distinctions so a smaller regulator suffices | Continuous temperature → "too hot"/"too cold" |
| Amplification | Builds regulatory subsystems using another source of variety | One thermostat per cage, across a hundred cages |
| Regulation by veto | Cheap rejection of unacceptable states until all constraints are satisfied | Ashby's homeostat; thermostat plus CO2 monitor both vetoing the window |
| Splitting the problem | Separates independent variables into smaller regulatory problems | Temperature regulated apart from food and water |

Ashby's homeostat: four connected compass needles, each acting as a voltmeter. A needle dragged to one side made its dial cycle randomly through its settings — a veto of the current configuration; a needle floating mid-range stopped cycling — acceptance. Four inputs with thirty states each gives 810,000 combinations, yet the homeostat reached stability quickly and recovered it whenever settings were disturbed.

## Key Takeaways
1. Check requisite variety at every regulatory link before blaming people: if the regulator's variety is below the system's, no amount of effort produces control.
2. Fix variety mismatches with three moves — attenuate the input, amplify the regulator by building subsystems, or split the problem into separable ones.
3. Prefer comparison to measurement: ask whether regulator variety exceeds input variety rather than trying to count states.
4. Treat every black-box boundary you draw as an act of attenuation, and be explicit about what you decided not to look at.
5. Use regulation by veto for large search problems — rejecting unacceptable states is informationally cheap and converges fast.
6. Match observation frequency and response speed to the rate at which the system generates variety, not just the volume.
7. Diagnose drift by auditing the control system as a model of its environment: what sources of variety are missing, what regulatory capacity is overestimated, what information is assumed transmitted but isn't.

## Connects To
- **Ch 2**: Beer's black-box method supplies the descriptive step that variety engineering depends on.
- **Ch 3**: Answers the closing question of Ch 3 — this is how you psychoanalyse the corporate non-human intelligence, and it recasts the accountability sink as a variety-amplification device.
- **Ch 5**: Beer's viable system model, named at the end of this chapter, is the further set of principles for drawing the boxes.
- **Ch 6/Ch 7**: Economics is assessed as a regulatory system whose variety may not match the economy it regulates.
- **Ch 7i**: Chile is the attempt to run variety engineering on a national economy in practice.
