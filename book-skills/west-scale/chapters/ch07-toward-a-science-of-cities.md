# Chapter 7: Toward a Science of Cities

## Core Idea
Cities within a national urban system are nonlinear scaled versions of one another: physical infrastructure scales **sublinearly at ~0.85** (economies of scale) while socioeconomic output scales **superlinearly at ~1.15** (increasing returns) — and the two exponents are mirror images because social networks must be anchored to space-filling physical networks.

## Frameworks Introduced

- **The urban scaling laws** (West, with Dirk Helbing, Christian Kuhnert, Luis Bettencourt, José Lobo; validated across the US, Europe, Japan, China, Colombia, Brazil).
  - When to use: any comparison, forecast, or benchmark involving cities of different sizes.
  - How: fit Y ∝ N^β where N is population. Then classify β.

- **The three network postulates, transposed from biology to cities**:
  1. **Space filling** — roads and utilities must reach every building; social interaction must fill socioeconomic space.
  2. **Invariant terminal units** — in cities these are **people and their houses**. A house, an electrical outlet, a water tap is the same size in a village and a megacity.
  3. **Approximate optimization** — minimizing travel time, distance, and energy cost.

- **The 15 percent rule** — the single number that ties both halves together. **Double a city's population and you get ~15% more socioeconomic output per capita while needing ~15% less infrastructure per capita.** Same magnitude, opposite sign.

- **The good, the bad, and the ugly scale together.** Wages, wealth, patents, GDP, restaurants and "supercreative" professionals all scale at ~1.15 — and so do violent crime, AIDS cases, and flu. You cannot buy the upside without the downside; they share a mechanism.

- **The quadratic interaction ceiling.** N people have N(N−1)/2 possible pairwise links, so the theoretical maximum superlinear exponent is **2**. Observed reality is 1.15, because space, time, and cognitive limits (Dunbar) throttle how many of those links you can actually realize.

- **Dunbar's numbers** (Robin Dunbar): a nested hierarchy of social group sizes — **5 / 15 / 50 / 150 / 500 / 1,500** — with a roughly constant branching ratio of about three. Interaction *strength* decreases as group size increases, which is the inverse of how infrastructure flows behave. Underpinned by the **social brain hypothesis** (primate group size scales as a power law with neocortex volume). West cautions that the precise values carry significant variance.

- **Zipf's law for city sizes** (George Kingsley Zipf, 1935/1949; anticipated by Pareto): a city's rank is inversely proportional to its size. Take the largest city, divide by 2 for the second, by 3 for the third, and so on. West explicitly **demotes** it: "another phenomenological scaling law among many others but without special fundamental significance" — and there is no agreed explanation of its origin.

- **Fractal cities** (Michael Batty, CASA/UCL) — measuring urban fractal dimension in Richardson's tradition. Values cluster around **1.2** with large variance up to ~1.8; the dimension *rises* as a healthy city grows and *falls* in contraction.

- **Central place theory** (Walter Christaller, 1930s; extended by August Lösch): a hexagonal lattice of nested central places. West's critique: static, symmetric, untested against data. Its two redeeming features are that it *is* space filling and hierarchically self-similar, and it embeds minimal travel time.

## Reference Table — Urban Scaling Exponents

| Quantity | Exponent β | Class | Implication |
|---|---|---|---|
| Roads, electrical cables, water/gas lines, gas stations | **~0.85** | sublinear | ~15% infrastructure saved per doubling |
| Number of houses; number of jobs | **~1.0** | linear | genuinely per-capita quantities |
| Household water and electricity use | ~1.0 | linear | per-capita metrics are valid *here only* |
| Wages, wealth, GDP, patents, supercreative professionals | **~1.15** | superlinear | ~15% per-capita gain per doubling |
| Violent crime, AIDS cases, flu | **~1.15** | superlinear | the same 15% bonus, unwanted |
| Restaurants, lawyers, doctors | ~1.15 | superlinear | |
| Theoretical max (everyone interacts with everyone) | 2 | superlinear | never approached in practice |

**City size alone predicts these quantities with 80–90% accuracy.** The remaining 10–20% is the city's individuality — the subject of Ch 8.

## Mental Models
- **Think of a big city as a hotter gas.** More people means a higher collision rate means more interactions. The melting pot, made literal.
- **Use "which of the three classes is this?"** as your first question about any urban metric: sublinear infrastructure, linear per-capita stuff, or superlinear social output.
- **Think of social networks as embedded in space, not floating in hyperspace.** Every interaction has a physical location and a mobility cost. This is the error most of network science makes — and correcting it is what produces the exponents.
- **Expect fat tails.** Power-law distributions produce far more rare large events than Gaussians. Financial models assuming normality systematically underprice catastrophe. *Caveat emptor.*

## Anti-patterns
- **Comparing cities across national urban systems** using within-system scaling laws. The laws predict Chicago vs. LA, and Kyoto vs. Osaka — but not Osaka vs. Chicago, until you fix a cross-system anchor.
- **Crediting or blaming leadership for scaling effects.** New York is the greenest US city per capita (Santa Fe emits nearly twice the carbon per person) — not because of planners' wisdom, but because of size. Attributing a size effect to a policy is the commonest urban-policy error.
- **Assuming urban quantities are independent.** Wages, disease, patents, and gas stations are driven by the same dynamics; you cannot tune one without moving the others.
- **Treating social networks as disembodied topology.**
- **Assuming Gaussian distributions** for city sizes, incomes, word frequencies, or market crashes.
- **Treating Zipf's law as fundamental.** It is a robust regularity without a mechanism.
- **Believing a static hexagonal geometry describes real urban form.**
- **Touting big data and smart cities as panaceas.** Data without theory does not explain.

## Worked Example
**Laredo, Texas — finding the fractal hidden in the interstate.**

The US interstate system was built for defence (its official name is the National System of Interstate and Defense Highways) and deliberately laid out straight, to minimize distance between major cities. On a map it looks like a rectangular grid — about as un-fractal as a network can be. So where is the hierarchical, circulatory structure the theory demands?

The answer is that the road network is not the object of interest; the **traffic on it** is.

Take Laredo. Every truck leaving the port must use the sections of highway immediately outside the city, so those carry the heaviest Laredo-origin flow. As the trucks fan out they branch onto other interstate sections, then onto state roads, then onto local delivery streets — each carrying a smaller share of that original flow.

Now redraw the map with each road's thickness proportional to its Laredo-origin flow. The rectangular grid dissolves into a hierarchical, branching, fractal structure. Laredo is the heart; the trunk road is the aorta; the terminal delivery streets are the capillaries — and, exactly as the theory requires, those terminal streets are the same size whether the city is Laredo or Los Angeles.

Every city is such a pump: a "central place" in Christaller's vocabulary, but organic rather than crystalline. The lesson generalizes: when a network looks non-fractal, weight its edges by flow before concluding the theory fails.

## Key Takeaways
1. Infrastructure ~0.85, per-capita quantities ~1.0, socioeconomic output ~1.15. Memorize these three.
2. The 15 percent rule works both ways per doubling — and the savings and the gains are causally linked.
3. Size predicts 80–90% of a city's measurable behavior. Never benchmark cities without detrending for size first.
4. Superlinear scaling has **no biological analog**. It arrived with human social networks and is why cities, unlike organisms, do not stop growing.
5. Crime and disease come bundled with wages and patents at the same exponent. Policy that targets one without acknowledging the shared mechanism will disappoint.
6. One large city beats two half-sized ones on infrastructure (~15% less) *and* on output — which is the quantitative case for agglomeration.

## Connects To
- **Ch 3**: the identical three network postulates, with capillaries replaced by people.
- **Ch 6**: Jacobs' qualitative argument, now quantified.
- **Ch 8**: the 10–20% residual — scale-adjusted metrics, pace of life, and diversity.
- **Ch 9**: why companies scale at ~0.9 instead, and therefore die.
- **Agglomeration economics; Zipf/Pareto distributions; Dunbar's number.**
