# Chapter 17: Regression to the Mean

## Core Idea
Whenever a measure is influenced by luck as well as skill — that is, whenever the correlation between two observations is less than perfect — extreme scores tend to be followed by more average ones. Regression to the mean is a mathematical inevitability with an explanation but no cause. Yet the mind, hungry for causes, invents stories (praise hurts, criticism helps, the Sports Illustrated jinx) to explain a purely statistical regularity.

## Frameworks Introduced
- **success = talent + luck**: Any extreme outcome reflects both a stable component (talent) and a transient one (luck).
  - When to use: When interpreting an unusually good or bad performance and predicting the next one.
  - How: An extreme score implies extreme luck as well as extreme talent. Since luck won't repeat, expect the next score to move toward the mean. Greater success = a little more talent + a lot more luck.
- **Regression toward the mean**: The best prediction of a second observation is more moderate — closer to the average — than the first; the more extreme the first score, the more regression to expect.
  - When to use: Predicting any repeated performance (day 2 from day 1, follow-up test from baseline).
  - How: Do not simply repeat the extreme score. Move the prediction partway toward the population mean, in proportion to how much luck (imperfect correlation) is involved.
- **Correlation = proportion of shared determinants**: The correlation coefficient (0 to 1) measures the relative weight of factors two measures share; imperfect correlation guarantees regression.
  - When to use: Estimating how much to regress a prediction, and debunking "interesting" correlational claims.
  - How: Correlation and regression are two views of one concept. Lower correlation → stronger regression. Use ranks or standard scores to compare measures on different scales.

## Key Concepts
- **Regression to the mean**: Extreme observations tend to be followed by less extreme ones when correlation is imperfect.
- **Regression fallacy**: Attaching a spurious causal explanation to what is merely regression.
- **Correlation coefficient**: A 0-to-1 index of the shared determinants between two measures; drives the amount of regression.
- **Imperfect correlation**: The necessary and sufficient condition for regression; if correlation is 1 there is none.
- **Random fluctuation / luck**: The transient component whose non-repetition produces regression.
- **Control group**: Needed to separate genuine treatment effects from improvement that regression alone would produce.
- **Symmetry of regression**: Predicting an earlier event from a later one shows the same regression — proof it has no causal direction.

## Mental Models
- Use "success = talent + luck" when a standout or disastrous performance tempts a causal verdict; expect the next result to be more average.
- Use the correlation-to-regression rule when a correlational claim sounds fascinating (bright women marry less-bright men): restate it as "correlation is imperfect" and the mystery dissolves.
- Use a control group when any extreme group (depressed children, worst branches) improves over time; regression, not the intervention, may be the cause.
- Use the two-direction test when unsure whether an effect is causal: if regression appears predicting the past from the future, it is statistical, not causal.

## Anti-patterns
- **Regression fallacy**: Concluding punishment works and praise fails because good performances deteriorate and bad ones improve — the flight-instructor error.
- **Jinx and hot-hand stories**: Explaining the Sports Illustrated "jinx" by pressure or overconfidence instead of prior luck regressing.
- **Uncontrolled before-after claims**: Crediting an energy drink (or cat-hugging) for improvement in an extreme group with no control group.
- **Flat percentage forecasting**: Adding a uniform 10% to every store's sales instead of regressing low and high performers toward the mean.

## Worked Example
Kahneman taught Israeli Air Force instructors that rewarding good performance beats punishing mistakes. A veteran objected: cadets praised for a clean maneuver did worse next time, while cadets screamed at did better — so punishment works. He was observationally right but causally wrong. Instructors praise only after unusually good runs (probably lucky) and shout only after unusually bad ones (probably unlucky); both regress toward each cadet's average regardless of feedback. Kahneman demonstrated it with coins thrown blind at a target: those best on throw one mostly worsened on throw two, those worst mostly improved — no praise or punishment involved. The perverse consequence: because we are nice when people please us and harsh when they don't, we are statistically punished for being nice and rewarded for being nasty.

## Key Takeaways
1. Imperfect correlation guarantees regression to the mean; extreme scores are followed by more moderate ones.
2. Regression has an explanation (luck doesn't repeat) but no cause — beware the causal stories the mind supplies.
3. The best prediction of a repeat performance is more moderate than the original, proportional to the luck involved.
4. Correlation and regression are one concept; the coefficient is the proportion of shared determinants.
5. Any "interesting" correlational claim is equivalent to the trivial statement that the correlation is imperfect.
6. Interventions on extreme groups need control groups, because those groups improve by regression alone.

## Connects To
- **Ch 16**: Causal-story hunger drives both base-rate neglect and misexplained regression.
- **Ch 18**: Regression is the correction that must be applied to nonregressive intuitive predictions.
- **Ch 10**: The law of small numbers — extreme outcomes are more likely in small samples, amplifying luck and regression.
