# Cheatsheet — *Scale* (Geoffrey West)

## Exponent Reference

| Quantity | System | Exponent | Class | Implies |
|---|---|---|---|---|
| Metabolic rate (**Kleiber's Law**) | organisms | **3/4** | sublinear | 25% energy saving per doubling; bounded growth |
| Life span | organisms | **+1/4** | sublinear | big animals live long |
| Heart rate, mitochondrial density, rate of evolution | organisms | **−1/4** | decreasing | pace of life slows with size |
| Growth rate, brain size, aorta cross-section | organisms | 3/4 | sublinear | |
| Aorta length, genome length, tree height | organisms | 1/4 | sublinear | |
| Blood volume | organisms | 1 | linear | the closure condition |
| Strength (Galileo) | any structure | **2/3** | sublinear | weight outruns strength → max size |
| Roads, cables, water/gas pipes, gas stations | cities | **~0.85** | sublinear | ~15% infrastructure saved per doubling |
| Houses, jobs, household water & electricity | cities | **~1.0** | linear | the only place per-capita is valid |
| Wages, wealth, GDP, patents, professionals | cities | **~1.15** | superlinear | ~15% per-capita gain per doubling |
| Violent crime, AIDS, flu | cities | **~1.15** | superlinear | the bad scales with the good |
| Social contacts (phone data) | cities | ~1.15 | superlinear | connectivity is the mechanism |
| Walking speed | cities | ~0.10 | superlinear | pace of life; saturates |
| Total business establishments | cities | ~1.0 | linear | ~1 per 22 people, ~8 employees each |
| Business *diversity* (types) | cities | logarithmic | — | doubling adds only ~5% more kinds |
| Visitors vs. distance × frequency | cities | **−2** | inverse square | footfall estimation |
| Sales / assets / income | companies | **~0.9** (sales ~1.0) | sublinear | mature, stop growing, die |
| Max possible (everyone meets everyone) | social | 2 | superlinear | never approached |

**The magic number 4** = 3 spatial dimensions + 1 from the fractal network → all biological exponents are multiples of ¼.

## Key Invariants & Thresholds

| Constant | Value | Note |
|---|---|---|
| Heartbeats per mammalian lifetime | **~1.5 billion** | humans ~2.5B, the great outlier |
| Human basal metabolic rate | ~2,000 kcal/day ≈ **90–100 W** | a lightbulb |
| US social metabolic rate | **~11,000 W** | ~a dozen elephants |
| Daily travel time (**Marchetti's constant**) | **~1 hour** (~½ hr each way) | invariant across size, mode, era |
| Half-life, US public companies | **~10.5 years** | age- and sector-independent |
| Company death by M&A vs. bankruptcy | **~45% vs. ~9%** | M&A dominates |
| Max human life span | **~125 years** | unchanged despite life-expectancy gains |
| Dunbar hierarchy | 5 / 15 / 50 / 150 / 500 / 1,500 | branching ratio ~3 |
| Predictive power of city size alone | **80–90%** | the other 10–20% is the residual |
| Temperature sensitivity | **±2 °C → 20–30%** rate change | ATP activation ~0.65 eV |

## Decision Rules — "How should this quantity scale?"

- **Is it infrastructure or a supply network?** → expect **sublinear** (0.75–0.9). Bigger should be cheaper per unit. If it isn't, your network is not optimized.
- **Is it a genuinely individual quantity (a house, a tap, a job)?** → expect **linear (~1.0)**. Per-capita comparison is legitimate here and *only* here.
- **Is it produced by people interacting?** → expect **superlinear (~1.15)**. Wages, ideas, crime, disease. Per-capita comparison is invalid.
- **Do the terminal units stay the same size as the system grows?** → yes ⇒ sublinear network scaling applies.
- **Does supply scale sublinearly while maintenance scales linearly?** → growth **will** stop. Sigmoidal, then death.
- **Does supply scale superlinearly?** → growth is **open-ended and faster than exponential**, with a finite-time singularity.

## Decision Rules — "What if it doesn't scale as expected?"

| Observation | Read it as | Do |
|---|---|---|
| Above the curve | genuine overperformance | study it; check it persists over decades before crediting management |
| Below the curve | genuine underperformance | look for structural cause, not recent policy |
| High raw value, zero residual | just big | stop congratulating; it's size |
| Exponent nearer 1.0 than 0.85 on infrastructure | network not optimized / not space-filling | look for redundancy or fragmentation |
| Company sales exponent drifting down | economies of scale beating innovation | dimensionality is contracting → decline ahead |
| Doubling time shrinking | superexponential | a wall exists with a date; plan a paradigm shift |
| Doubling time constant | exponential | unbounded but not singular; manageable |
| Growth still exponential after 20 years | you forgot to detrend | remove inflation **and** market expansion |

## Tells & Smells

- Someone ranks cities or companies **per capita** → the ranking is measuring size. 7 of the 20 largest US cities are top-20 on per-capita GDP; **none** are top-20 on scale-adjusted indicators.
- A leader claims credit for a **size effect** (New York's low per-capita carbon, Santa Fe's high) → it's the exponent, not the policy.
- A composite index built by **linear combination** (WEF, Forbes, Fortune, The Economist) → naive; recompute on residuals.
- A **1:1 scale model** offered as evidence → aesthetics, not dynamics. Demand the dimensionless number.
- A dose, load, or capacity scaled **per kilogram** → the LSD-elephant error. Use the ⅔ or ¾ law.
- A metaphor doing the work of a theory ("the DNA of the company", "the ecology of the marketplace") → evocative, predicts nothing.
- A **narrowing product line** described as "focus" → contracting dimensionality; the reliable precursor of corporate death.
- **R&D spend** cited as evidence of innovation → tax-driven label; R&D *share* falls with size. Measure output diversity.
- A **smooth EKG** or a rigid, low-variance system called healthy → in fractal systems, **rigidity is fragility; variance is resilience**.
- Gaussian statistics applied to city sizes, incomes, or crashes → power laws have fat tails. *Caveat emptor.*
- Comparing cities **across national systems** (Osaka vs. Chicago) with within-system laws → invalid without an anchor.

## The Punchline
**Companies scale sublinearly like organisms, not superlinearly like cities.** So they mature, stop growing, and die on a ~10.5-year half-life — while cities almost never do. The lever, if there is one, is keeping dimensionality expanding against the bureaucratic contraction that size makes inevitable.
