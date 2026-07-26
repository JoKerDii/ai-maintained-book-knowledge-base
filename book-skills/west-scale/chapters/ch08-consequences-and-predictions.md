# Chapter 8: Consequences and Predictions — From Mobility and the Pace of Life to Social Connectivity, Diversity, Metabolism, and Growth

## Core Idea
The scaling theory makes falsifiable quantitative predictions — about commute time, walking speed, phone connectivity, mobility flows, business diversity, and growth — that big data confirm. And because superlinear scaling is the correct baseline, per-capita rankings of cities are scientifically wrong and must be replaced by **deviations from the scaling curve**.

## Frameworks Introduced

- **Scale-Adjusted Metropolitan Indicators (SAMIs)** — Bettencourt, Lobo and Strumsky. *The single most actionable technique in the book.*
  - When to use: any time you want to know whether a city (or company, or team, or region) is genuinely performing, as opposed to merely being large.
  - How:
    1. Assemble the metric across all comparable units in one system (e.g. ~360 US Metropolitan Statistical Areas).
    2. Fit the scaling law on log-log axes — using the *correct* exponent (1.15 for socioeconomic metrics), not 1.0.
    3. For each unit compute the **residual**: the log-deviation of its actual value from its size-predicted value.
    4. Rank by residual. Left of zero = overperformer; right = underperformer.
  - Why it works: it removes the part of performance that is a pure consequence of size, leaving the part attributable to everything else.
  - Precedent: Galileo's ⅔ law applied to championship weightlifters. The middleweight who lifts above the curve is scientifically the strongest man, even though the heavyweight lifts more.

- **The increasing pace of life.** Superlinear social dynamics invert biology's sublinear slowdown. In organisms, bigger means slower (quarter-power laws). In cities, bigger means **faster** — diseases spread faster, businesses are born and die more often, commerce transacts more rapidly, people walk faster — all following the ~15 percent rule.

- **The city as the incredible shrinking time machine / the accelerating treadmill.** Distance didn't shrink; *time* did. Keynes and Sir Charles Darwin both predicted an Age of Leisure. They could not have been more wrong: we get *less* discretionary time, not more. The risk is being accelerated to death, not boredom.

- **Marchetti's constant** (discovered by Yacov Zahavi; generalized by Cesare Marchetti as "exposure time"): people spend about **one hour a day travelling, roughly half an hour each way commuting** — invariant across city size, transport mode, country, and century. Even prisoners serving life walk around for about an hour a day.
  - Consequence: speed gains were spent on **distance, not on time saved**. City size is set by transport efficiency at the half-hour radius. A walking city at 5 km/h is ~5 km across — and no pre-1800 city wall (Rome, Persepolis, Venice) exceeds that.

- **Walking speed scaling**: average pedestrian speed rises as a power law of population, with an exponent somewhat below the canonical 0.15 — closer to **~0.10** — nearly doubling from small towns to cities over a million (~6.5 km/h). Expected to saturate for biophysical reasons.

- **The gravity/mobility law**: the number of visitors to a location scales as the **inverse square (exponent −2)** of *both* distance travelled and visitation frequency. Verified in Boston, Singapore, Lisbon and Doha.

- **Social connectivity from mobile phone data** (Ratti, Schläpfer, Szell, Bettencourt, West): the number of an individual's reciprocated contacts scales at **~1.15**, matching income, GDP, patents and crime. The surprise: the size of your *modular cluster* of mutually-acquainted contacts is **invariant** with city size — Lisbon looks like a village of 4,000 in this respect. The difference is that a village imposes your community while a city lets you **choose** it.

- **Business diversity scaling**: total establishments scale **linearly** with population (~1 establishment per 22 people, ~8 employees each, at any city size), but the **diversity of business types scales logarithmically** — 100× the population gives 100× the businesses but only ~2× the diversity; doubling a city adds only ~5% more *kinds* of business. Mechanism: **preferential attachment** (Yule–Simon process; "the rich get richer"). Business types that scale superlinearly rise in rank as cities grow; sublinear ones fall.

- **Growth and the metabolism of cities**: apply the Ch 4 growth equation with a **superlinear** supply term. In biology, supply scales at ¾ while maintenance scales at 1, so demand overtakes supply and growth stops. In cities, **social metabolism scales at ~1.15**, so supply outruns maintenance and the surplus available for growth itself grows. **The bigger the city gets, the faster it grows** — mathematically faster than exponential.

## Mental Models
- **Think of per-capita ranking as a category error, not a rough approximation.** It silently assumes a linear null hypothesis — that a city is the linear sum of its citizens — which denies the emergent nonlinearity that is the entire point of a city.
- **Use residuals as the unit of judgment.** The question is never "how big is this number?" but "how far is it from what size alone predicts?"
- **Think of movement in a city as directed, not gaslike.** Averaged over months, routes approximate radial straight lines to hubs.
- **Expect a city's character to persist for decades.** Change is slow; political horizons are not.

## Anti-patterns
- **Per-capita ranking** — West calls it "particularly egregious." Applies to official statistics and to composite indices from the World Economic Forum, Fortune, Forbes and The Economist, which are naive linear combinations.
- **Mayors taking credit for high per-capita GDP.** Seven of the twenty largest US cities rank in the top twenty on per-capita GDP; **none** rank in the top twenty on SAMIs.
- **Reverse causation.** Silicon Valley did not create San Jose's success — San Jose was already overperforming to almost the same degree in the 1960s, before Silicon Valley existed.
- **Confusing diversity counts with resolution.** Diversity is scale-dependent, exactly like Richardson's coastlines.
- **Big data and smart cities hype** — West flags naïveté and even danger in data without a theoretical frame.

## Worked Example
**SAMI rankings of US metros — who actually overperforms.**

Fit the ~1.15 scaling curve across ~360 US Metropolitan Statistical Areas for 2003, take each city's log-deviation from its size-predicted value, and rank.

The results demolish intuition. **New York City** turns out remarkably average: 88th in income, 184th in GDP, 178th in patents — but 267th in violent crime, i.e. surprisingly *safe* for its size. **San Francisco** is the most exceptional large city: 11th in income, 19th in patents, 181st in violent crime.

The truly exceptional cities are small. **Bridgeport** tops income (New York bankers and hedge-fund managers living in the suburbs). **Corvallis** ranks first in patents — an HP research lab plus Oregon State. **San Jose** ranks high on patents. **Logan** and **Bangor** stand out for safety. **McAllen** ranks last on patents; **Brownsville** is a persistent underperformer.

The most important finding is **persistence**. With forty to fifty years of data, cities that overperformed in the 1960s still overperform, and those that underperformed still do. San Jose was already an overperformer before Silicon Valley, and relaxed back to its baseline trend after the 1999–2000 boom and bust. Cities are, in West's phrase, hard to change and almost impossible to kill — Detroit, New Orleans, Dresden, Hiroshima.

Policy implication: meaningful change to a city's residual takes decades, while for most politicians two years is infinity.

**Second example — the inverse-square mobility law, Park Street, Boston.** Suppose 1,600 people visit from 4 km away once a month. Double the distance to 8 km at the same frequency: one quarter as many, **400**. Five times the distance (20 km): 1/25, **64**. Now hold distance at 4 km and raise frequency instead — twice a month gives 400, five times a month gives 64. The 20 km once-monthly case and the 4 km five-times-monthly case both give 64, because **distance × frequency = 20** in both. Visitor flux depends only on the product. Data from four cities on three continents collapse onto one line of slope −2. Practical use: estimating footfall for a new mall or housing project from principles rather than local simulation.

## Key Takeaways
1. Replace every per-capita comparison with a scale-adjusted residual. This is the book's most transferable method.
2. Detrend before you benchmark — and use the right exponent (1.15 for social output, 0.85 for infrastructure), not 1.0.
3. Rankings are persistent over decades. A city's residual is a structural property, not a policy outcome.
4. The pace of life speeds up with size following the same ~15% rule that governs wages and crime.
5. Commute time is invariant at ~half an hour each way. Faster transport buys sprawl, not free time.
6. Cities let you choose your ~150 close contacts rather than having them imposed; the cluster size itself doesn't change with city size.
7. Superlinear social metabolism means the bigger the city, the faster it grows — open-ended and faster than exponential, which sets up Ch 10.

## Connects To
- **Ch 2**: deviations from the weightlifting scaling curve — the original residual analysis.
- **Ch 4**: the same growth equation, with a superlinear rather than sublinear supply term.
- **Ch 7**: the exponents being applied here.
- **Ch 10**: superexponential growth and the finite-time singularity.
- **Marchetti's constant; gravity models in transport planning; preferential attachment / Yule–Simon.**
