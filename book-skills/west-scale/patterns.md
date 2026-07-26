# Patterns & Techniques — *Scale* (Geoffrey West)

## Fit the Scaling Law
**When to use**: before any comparison, forecast, or benchmark across entities of different size.
**How**:
1. Choose the size variable (body mass, population, employees, revenue).
2. Plot the quantity of interest against it on **log-log axes**.
3. Read the slope — that is the exponent β.
4. Classify: β < 1 sublinear (economies of scale), β ≈ 1 linear (genuinely per-capita), β > 1 superlinear (increasing returns).
5. Only then interpret levels.
**Trade-offs**: needs many entities spanning at least 2–3 orders of magnitude; noisy for small samples and for companies, which have much higher variance than cities or organisms.

## Scale-Adjusted Metrics (Residual Analysis)
**When to use**: whenever you want to know whether a unit is genuinely performing rather than merely being large. The book's single most actionable technique.
**How**:
1. Fit the scaling law across all comparable units within **one system** (one country's cities; one exchange's companies).
2. For each unit compute the residual — the log-deviation of its actual value from its size-predicted value.
3. Rank by residual, not by raw value or per-capita value.
4. Interpret: positive residual = overperformer; negative = underperformer.
**Trade-offs**: only valid within a single system; residuals persist for decades, so they measure structure rather than recent management. Requires the correct exponent — using 1.0 reproduces the per-capita error you were trying to avoid.

## Doubling-Time Diagnosis
**When to use**: assessing whether a growth trajectory is safe, exponential, or headed for a wall.
**How**: measure the time to double at successive points in the history. Constant doubling time ⇒ exponential (unbounded but harmless in finite time). **Shrinking** doubling time ⇒ superexponential ⇒ a finite-time singularity exists and has a date.
**Trade-offs**: needs a long, clean series; the singularity date is highly sensitive to fit and should be treated as an order-of-magnitude estimate.

## The Three-Postulate Test
**When to use**: deciding whether network scaling theory should apply to a new system at all.
**How**: check for (1) **space filling** — does the network reach every active unit? (2) **invariant terminal units** — are the endpoints the same size at all system sizes? (3) **optimization** — is there a quantity (energy, time, cost) that competition or evolution has minimized? All three present ⇒ expect a clean power law.
**Trade-offs**: qualitative judgment; the third postulate is the hardest to establish and the easiest to assume.

## Dimensionless-Number Modeling (Similitude)
**When to use**: extrapolating from a small model, pilot, or prototype to full scale.
**How**: identify the dimensionless group governing the behavior (Froude number v²/Lg for hulls); match it between model and full scale; derive the required scaling of the other variables (speed ∝ √length).
**Trade-offs**: if you cannot construct a dimensionless number, do not extrapolate. A geometrically faithful 1:1 miniature transfers appearance, not dynamics.

## Detrend Growth for Market Expansion
**When to use**: evaluating any company's growth story.
**How**: divide out inflation **and** overall market/sector expansion before plotting the growth curve. What looks exponential and open-ended usually turns sigmoidal.
**Trade-offs**: choosing the right market baseline is contestable; do the analysis under two or three baselines and check robustness.

## Find the Invariant
**When to use**: looking for conserved quantities and hidden design constants in a scaling system.
**How**: multiply a rate that scales as x^(−α) by a duration that scales as x^(+α). The size dependence cancels. Example: heart rate (mass^−¼) × life span (mass^+¼) = ~1.5 billion heartbeats for every mammal.
**Trade-offs**: the invariant is an average with real spread; humans are a 2× outlier on heartbeats. Do not treat it as a personal budget.

## Weight the Network by Flow
**When to use**: when a real network looks non-fractal (a road grid, an org chart) and you suspect the theory still applies.
**How**: redraw each edge with thickness proportional to the flow originating from the hub of interest. Hierarchical, branching, fractal structure typically emerges from an apparently rectangular grid.
**Trade-offs**: requires flow data, which is often the hard part.

## Constant-Mortality Survival Analysis
**When to use**: estimating life expectancy for a population of firms, products, or projects.
**How**: build the survivorship curve, correct for censored (still-alive) units using the Kaplan–Meier estimator, and test whether survivorship is exponential. If it is, the mortality rate is age-independent and a half-life exists.
**Trade-offs**: age-independence is a strong empirical finding for US public companies but should be re-tested, not assumed, in a new domain.

## Track Dimensionality as a Health Metric
**When to use**: diagnosing organizational decline before it shows in financials.
**How**: measure the breadth of the product and idea space over time — number of distinct lines, share of revenue outside the core, genuine R&D breadth. Contracting dimensionality plus a finely balanced cost structure means reduced resilience.
**Trade-offs**: R&D spend is a poor proxy (tax-driven labelling, and its share falls with size). Prefer output diversity to input spend.

## Innovation-Interval Planning
**When to use**: career, R&D portfolio, and long-horizon strategic planning.
**How**: estimate the historical interval between paradigm shifts in your domain, note that it is shrinking, and plan for a working life spanning several of them rather than one.
**Trade-offs**: intervals are estimated from a handful of hand-picked events; directionally reliable, numerically soft.
