# Chapter 9: Toward a Science of Companies

## Core Idea
Publicly traded companies obey coarse-grained power-law scaling with far more variance than cities or organisms; they grow sigmoidally once market expansion is factored out, and they die at a constant, age-independent rate — because they are dominated by economies of scale and top-down bureaucracy rather than by the superlinear social innovation that makes cities effectively immortal.

## Frameworks Introduced

- **Is Walmart a scaled-up Big Joe's Lumber?** West's answer: **statistically yes**. Walmart is an approximately scaled-up version of a modest-size company — but only in the coarse-grained average sense, with large spread around the curve. Companies are far noisier than cities or organisms, especially in their early years as they jostle for market position.

- **Three traditional theories of the firm, recast in scaling language**: (1) transaction costs = economies of scale via an optimization principle; (2) organizational structure = the internal network; (3) marketplace competition = evolutionary selection.

- **The myth of open-ended growth.** A company's effective metabolic rate (sales) scales roughly **linearly** with size — putting companies at the cusp between organisms and cities — while expenses start sublinear and transition to linear as the company grows. Absolute growth therefore looks exponential and open-ended. But once you divide out **both inflation and overall market expansion**, the curve is **sigmoidal**: companies grow rapidly when young, then taper and stop.
  - Diagnostic: if a CEO's growth chart is not detrended for market expansion, it is measuring the market, not the company.

- **The surprising simplicity of company mortality.** Survivorship is **exponential**, which means the **mortality rate is constant**: the risk of dying does not depend on the company's age, size, or sector. The **half-life of US publicly traded companies is ~10.5 years**. Method: Kaplan–Meier survival analysis (1958), which corrects for *censored* companies — those still alive at the end of the data window.
  - Data: the Compustat database, **28,853** companies traded on US markets 1950–2009.
  - Outcome: **22,469 (78%)** were dead by 2009. Cause of death: **~45% acquired or merged**, ~9% bankrupt or liquidated, ~3% privatized, ~0.5% LBO, ~0.5% reverse acquisition.
  - Fewer than 5% survive 30 years after IPO; essentially none reach 50.

- **Liability of adolescence**: young firms are buffered by their initial capital endowment and become acutely vulnerable once it is spent without reaching profitability.

- **Why companies die but cities don't** — the book's punchline.
  - Companies scale **sublinearly** ⇒ "the triumph of economies of scale over innovation."
  - Cities scale **superlinearly** ⇒ "the triumph of innovation over the hegemony of economies of scale."
  - Mechanism: companies are top-down hierarchies that accumulate rules, protocols, and bureaucracy at the expense of R&D. Their **dimensionality contracts** with age — the product and idea space narrows, specialization increases — while a city's dimensionality continually *expands* (Ch 8: business diversity grows with size).
  - Companies also sit near a **critical point** where sales and expenses are finely balanced. Reduced diversity plus criticality equals reduced resilience — *il bacio della morte*.

## Reference Table — Organisms vs. Cities vs. Companies

| Property | Organisms | Cities | Companies |
|---|---|---|---|
| Scaling exponent | **0.75** | infra **0.85** / socio **1.15** | **~0.9** (sales ~linear) |
| Class | sublinear | mixed, socio superlinear | sublinear |
| Variance around curve | very low | low | **high** |
| Growth | bounded, sigmoidal | open-ended, superexponential | bounded, sigmoidal |
| Pace of life with size | slows | **speeds up** | slows |
| Dimensionality with age | fixed | expands | **contracts** |
| Mortality | finite life span | effectively immortal | constant rate, half-life ~10.5 yrs |

## Mental Models
- **Think of your company as an organism, not as a city.** It will mature, stop growing, and die. The strategic question is whether you can engineer city-like superlinearity into it.
- **Use "is dimensionality expanding or contracting?" as your health metric.** A narrowing product and idea space is the reliable precursor of decline.
- **Think of bureaucracy as the metabolic cost of size.** It is not a management failure; it is what sublinear scaling *is*. Fighting it requires deliberate structural counter-pressure.
- **Treat M&A as the dominant mode of corporate death, not bankruptcy** — it outnumbers bankruptcy roughly five to one.

## Anti-patterns
- **Believing in open-ended growth.** Growth uncorrected for inflation *and* market expansion looks perpetual and isn't.
- **Assuming mortality depends on sector, size, age, or cause of death.** It doesn't. A 50-year-old company faces the same annual death risk as a 5-year-old one.
- **Equating "death" with bankruptcy.**
- **Treating R&D spend as innovation.** The label is often tax-driven, and R&D *share* falls as company size rises.
- **Trading innovation for protocol.** Every added rule is a small permanent tax on adaptability.
- **Shortsighted conservatism** — staying with the tried and true winners and becoming unidimensional.
- **Deconstructing the economy into semiautonomous subsystems and assuming equilibrium.**
- **"Too big to fail" (2008)** — mourning companies rather than people.

## Worked Example
**Kongo Gumi — the 1,400-year-old exception that proves the rule.**

Kongo Gumi was founded in Osaka in 578 to build Buddhist temples, and ran as a family business across dozens of generations — for roughly 1,429 years, the purported oldest company in the world.

It fits West's profile of the geriatric outlier precisely, and that profile is the opposite of what a growth-minded executive would design. It stayed **modest in size** (over 90% of companies more than a century old have fewer than 300 employees). It occupied a **single highly specialized niche**. It survived on reputation and consistency rather than on diversification or innovation. It barely grew at all.

Its dimensionality was minimal *by design* — which is survivable only so long as the niche itself persists. When postwar Japanese culture shifted and demand for temple construction dried up, Kongo Gumi had no adjacent product space to move into, could not adapt fast enough, and went into liquidation in 2006, absorbed by Takamatsu Corporation.

The lesson cuts both ways. Extreme specialization can defeat the 10.5-year half-life for centuries — but it makes the firm a one-dimensional system sitting near a critical point. One sufficiently large external shock and it dies. Long-lived does not mean immortal, and there is no strategy in the data that produces a genuinely immortal company. Of ~100 million companies worldwide, the theory expects a few thousand to reach 100 years and essentially none to reach 200.

## Key Takeaways
1. Companies scale sublinearly (~0.9) — like organisms, not like cities. That single fact explains bounded growth, maturity, and death.
2. Detrend growth for inflation *and* market expansion before believing any growth story.
3. Mortality is age-independent with a half-life of ~10.5 years. Being established buys you nothing.
4. M&A, not bankruptcy, is how most companies die (~45% vs. ~9%).
5. Expected tenure on the S&P 500 has fallen from ~61 years in 1958 to ~18 today; of the 1955 Fortune 500, 61 remained in 2014.
6. The lever that exists: keep dimensionality expanding. Protect the breadth of the idea and product space against the bureaucratic contraction that size makes inevitable.
7. Long-lived companies are small, specialized, and slow-growing — a trade most firms are unwilling to make.

## Connects To
- **Ch 4**: the identical mortality mathematics — constant rate, exponential survivorship, half-life.
- **Ch 7–8**: why cities' superlinear diversity growth is exactly what companies lack.
- **Ch 10**: the accelerating external clock that makes corporate adaptation ever harder.
- **Creative destruction (Schumpeter, Foster); Kaplan–Meier survival analysis; agent-based modeling of firms (Axtell).**
