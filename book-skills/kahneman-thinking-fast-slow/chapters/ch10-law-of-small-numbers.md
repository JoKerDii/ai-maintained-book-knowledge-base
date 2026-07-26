# Chapter 10: The Law of Small Numbers

## Core Idea
Small samples produce extreme results far more often than large samples, yet the mind treats this statistical artifact as a fact demanding a causal explanation. System 1 automatically manufactures causal stories for outcomes that are actually driven by chance and sampling variation. We over-trust small samples, believe that small samples resemble the populations they come from, and see pattern and order in randomness. The remedy is to distrust statistical intuition and replace impression with computation.

## Frameworks Introduced
- **Law of large numbers (the correct principle)**: Large samples are more precise; their results deserve more trust than small samples.
  - When to use: Whenever you evaluate an estimate, rate, or effect derived from data.
  - How: Ask how many observations underlie the number. Recognize that "large samples are more precise" and "small samples yield extreme results more often" are the same statement; trust the finding only when the second version feels intuitive.
- **Law of small numbers (the bias, named tongue-in-cheek)**: The mistaken intuition that the law of large numbers applies to small numbers too — that small samples closely resemble their population.
  - When to use: As a warning label for your own reasoning about limited data (streaks, rankings of "best" units, replication decisions).
  - How: Suspect any inference drawn from a handful of cases; wait for adequate sample size before concluding.
- **Replace impression with computation**: Regard statistical intuitions with proper suspicion; compute required sample size rather than guessing it.
  - When to use: Designing studies, forecasts, or any inference where sampling error matters.
  - How: Estimate the risk of error for the sample size before committing; keep results secret until the sample is large enough to avoid premature conclusions.

## Key Concepts
- **Artifact**: An observation produced entirely by the research method (here, by differences in sample size) rather than by any real feature of the world.
- **Sampling variation**: The random fluctuation in results across repeated draws; a nuisance that makes every small-sample study a gamble.
- **Bias of confidence over doubt**: System 1's disposition to construct coherent, certain stories; sustaining doubt is effortful System 2 work.
- **WYSIATI (What You See Is All There Is)**: The message (the "story") dominates; the reliability of its source gets little attention.
- **Hot hand**: The widely believed but illusory streak of a "hot" scorer; sequences of hits and misses actually pass tests of randomness.
- **Cause and chance**: The associative machinery seeks causes; statistics instead relate an event to what could have happened otherwise. Causal explanations of chance events are inevitably wrong.

## Mental Models
- Use the urn model when judging variability: extreme rates (highest and lowest) cluster in small samples because a 4-marble draw yields homogeneous results roughly 8x more often than a 7-marble draw.
- Use "what could have happened instead" (statistical view) when a fact seems to beg for a cause but may just be an accident of sampling.
- Use "is this signal or noise?" when tempted to reward a streak — an investment adviser's good years, a CEO's acquisitions, a squadron's losses — before declaring skill.

## Anti-patterns
- **Explaining both extremes with the same cause**: Rural lifestyle "explains" both the highest and lowest kidney-cancer counties — a tell that the real driver is small population, not any cause.
- **Choosing samples too small**: Psychologists routinely accepted ~50% risk of failing to confirm true hypotheses by trusting intuition over computation of sample size.
- **Investing in artifacts**: The Gates Foundation and others spent ~$1.7B favoring small schools because top performers were disproportionately small — ignoring that the worst schools are also disproportionately small (small = more variable, not better).

## Worked Example
Kidney cancer across the 3,141 US counties. The counties with the *lowest* incidence are mostly rural, sparsely populated, Republican — inviting a clean-living explanation (no pollution, fresh food). But the counties with the *highest* incidence are *also* mostly rural, sparsely populated, Republican — inviting a poverty explanation (poor medical care, alcohol, tobacco). Both stories are seductive and both are wrong. The operative factor is that rural counties have small populations, and small samples produce extreme outcomes (high and low) far more readily than large ones. Picture the US as a giant urn of marbles, some marked KC; populating small counties draws small samples, which land at the extremes. There is, in a deep sense, nothing to explain — the pattern is an artifact of sample size, and next year's extreme counties will be different ones.

## Key Takeaways
1. Extreme outcomes (both high and low) are more likely in small samples than in large ones — this is a mathematical fact, not a causal effect.
2. The mind pays more attention to the content of a message than to the reliability of its source, yielding a world simpler and more coherent than the data justify.
3. Even sophisticated researchers have poor intuitions about sampling; expertise in statistics does not immunize you from misusing it in practice.
4. Random processes routinely produce sequences and clusters that look non-random (WWII bomb map, hot hand, unequal squadron losses).
5. Replace statistical intuition with computation; wait for adequate samples before concluding.
6. We are far too willing to classify random events as systematic.

## Connects To
- **Ch 7 (WYSIATI / jumping to conclusions)**: The law of small numbers is a machine for jumping to conclusions acting as if small samples were representative.
- **Ch 11 (Anchors)**: Both show System 1 accepting information regardless of its reliability, once it is not immediately rejected.
- **Ch 17 (Regression to the Mean)**: Extreme results reverting over time is the same statistical fact seen from another angle.
- **Ch 19–21 (Illusion of understanding, intuitions vs. formulas)**: Rewarding streaks as skill is the misclassification of chance as system.
