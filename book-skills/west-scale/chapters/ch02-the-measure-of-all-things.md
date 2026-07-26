# Chapter 2: The Measure of All Things — An Introduction to Scaling

## Core Idea
Because areas grow as the square and volumes as the cube of length, nothing can simply be made bigger while keeping its shape. Galileo's square-cube argument is the origin of all scaling thinking, and naive linear extrapolation from small to large is the master error it corrects.

## Frameworks Introduced

- **Galileo's square-cube argument** (*Discourses… Relating to Two New Sciences*): two parts.
  - (a) Geometric: hold shape fixed and **area ∝ length², volume ∝ length³**. Double the length → 4× area, 8× volume.
  - (b) Structural: the strength of a pillar, limb, or trunk is proportional to its **cross-sectional area**, independent of its length.
  - Consequence: **strength ∝ weight^(2/3)**. Weight outruns strength, so there is a maximum size for any fixed design and material. "A small dog could probably carry on his back two or three dogs of his own size; but… a horse could not carry even one of his own size."

- **Isometric vs. allometric scaling**: isometric = shape preserved, all exponents multiples of ⅓. Allometric = shape changes with size (the biological case, Ch 3).

- **Orders of magnitude and logarithmic scales**: when a quantity spans many factors of ten, use logs. On log-log axes a power law is a **straight line whose slope is the exponent**. The Richter scale is the everyday example.

- **Similitude / dimensionless numbers** (Lord Rayleigh, "The Principle of Similitude", *Nature*): all physical laws must be expressible in **scale-invariant, dimensionless** quantities. Ratios like π survive any change of units or size.

- **The Froude number**, Fr = v²/(L·g) — dimensionless.
  - When to use: whenever you want a small model to tell you about a large system.
  - How: match the dimensionless number between model and full scale. Equal Froude number ⇒ dynamically similar motion ⇒ **speed must scale as √length**.
  - This is the origin of modeling theory: towing tanks, then wind tunnels, then computer models.

- **BMI / the Quetelet index** (Adolphe Quetelet, *On Man… Essays on Social Physics*, 1835): weight ÷ height². Quetelet also gave us *l'homme moyen* — the average man — and the idea of "social physics."

## Key Concepts
- **Square-cube law** — surface-to-volume ratio falls as size rises; this governs strength, heat loss, and drug dosage.
- **Order of magnitude** — a factor of ten.
- **Richter scale** — logarithmic; amplitude→energy costs 3/2 orders per order, so **1.0 magnitude step ≈ 31.6× the energy**; a 2.0 step ≈ 1,000×.
- **Dimensionless number** — a ratio with no units; identical for model and original when they are dynamically similar.
- **Ponderal index** — weight ÷ height³; the theoretically correct alternative to BMI.
- **Deviation from scaling** — the residual after fitting the curve; where individual excellence actually lives.

## Mental Models
- **Think of size as a design constraint, not a parameter.** You cannot scale a design up; you must redesign. Bigger animals need disproportionately thicker legs.
- **Use dimensionless numbers when you want to transfer knowledge across scales.** If you cannot form one, your model will not generalize.
- **Think of a log-log plot as a truth serum.** Curvature, kinks, and outliers are visible there and invisible on linear axes.
- **Use rule-of-thumb incremental design only for small changes.** Fine for a 5% adjustment; catastrophic for a doubling.

## Anti-patterns
- **The Superman fallacy**: the 1938 comic argued Superman could leap an eighth of a mile because ants lift 100× their weight. The facts are right; the inference assumes strength scales *linearly* with size. Humans are ~10 million times heavier than an ant, so the ⅔ law says we should carry roughly one person — which we can.
- **Linear drug-dose extrapolation**: the LSD/Tusko case. A safe cat dose (0.1 mg/kg) was scaled linearly to a ~3,000 kg elephant, giving ~300 mg (297 mg injected). Tusko died in 1 hour 40 minutes. The ⅔-scaled dose would have been a few milligrams. The same error persists in children's Tylenol charts, which scale dose linearly with weight (6 lb → 40 mg; 36 lb → 240 mg, exactly 6×; the ⅔ law gives 6^⅔ ≈ 3.3× ≈ 132 mg).
- **BMI's height² assumption**: no theoretical basis; weight should scale closer to height³. It systematically over-diagnoses tall people as overweight and under-diagnoses short ones.
- **Averaging across a heterogeneous cohort** instead of deconstructing by age and gender — Quetelet's own sin.
- **Making a "to scale" model**: a 1:1 faithful miniature is aesthetically satisfying and dynamically useless. Only dimensionless-number matching transfers behavior.
- **Dismissing basic research as impractical**: John Russell mocked Froude's tank experiments, then claimed the credit.

## Worked Example
**Froude's towing tank — how to learn about a 700-foot ship from a 10-foot model.**

Brunel's *Great Eastern* (launched 1858, ~700 ft, displacing roughly ten times the *Great Britain*) was an enormous leap in scale, and nobody knew how a hull that large would behave. Brunel hired William Froude — Oxford mathematician and former Great Western Railway engineer — to study rolling and hull drag.

Froude towed model hulls 3 to 12 feet long down water tanks, measuring resistance and stability. His insight was to identify the governing dimensionless group, v²/(Lg). Because the underlying physics is identical at both scales, two vessels behave identically when their Froude numbers match. Setting them equal gives **v ∝ √L**.

So to make a 10-foot model mimic the 700-foot *Great Eastern* steaming at 20 knots: √(700/10) = √70 ≈ **8.4**, therefore the model must be towed at 20 ÷ 8.4 ≈ **2.5 knots** — walking pace. Run the model at 20 knots and you learn nothing.

This replaced trial-and-error shipbuilding (the *Vasa* capsized in harbour after the king demanded a ship 30% longer with an extra gun deck) with principled modeling, and its descendants are the Wright brothers' wind tunnel and every computational model since.

## Key Takeaways
1. Strength scales as the ⅔ power of weight. Anything supported by cross-sections obeys this.
2. When a quantity spans orders of magnitude, plot logarithmically or you will see nothing.
3. Before extrapolating from a model, find the dimensionless number. If you cannot, do not extrapolate.
4. Scale drug dosages, structural loads, and capacity by the appropriate power law — not per kilogram.
5. Empirical confirmation matters: Lietzke's 1956 analysis of Olympic weightlifting totals measured a log-log slope of **0.675** against Galileo's predicted **0.667**.
6. Individual excellence is the *deviation from* the scaling line, not the raw total. The middleweight who lifts above the curve is scientifically the strongest man, even though the heavyweight lifts more.

## Connects To
- **Ch 1**: linear thinking as the recurring error.
- **Ch 3**: why biology escapes ⅔ and lands on ¾ — networks add an effective fourth dimension.
- **Ch 8**: deviations from scaling become Scale-Adjusted Metropolitan Indicators.
- **Dimensional analysis / Buckingham π theorem**: the formal machinery behind similitude.
