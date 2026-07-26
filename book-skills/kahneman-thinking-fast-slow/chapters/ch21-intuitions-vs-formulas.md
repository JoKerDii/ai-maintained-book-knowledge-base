# Chapter 21: Intuitions vs. Formulas

## Core Idea
In low-validity environments, simple statistical formulas match or beat expert clinical judgment — a result documented across ~200 studies since Paul Meehl, with no convincing exception. Experts underperform because they try to be clever with complex feature combinations, and because they are incorrigibly inconsistent (context-dependent System 1 gives different answers to identical inputs). To maximize accuracy, final decisions should be left to formulas. The practical remedy is to collect objective information on a few independent traits, score each separately to defeat the halo effect, and combine them with a fixed rule.

## Frameworks Introduced
- **Clinical vs. statistical prediction (Meehl)**: Comparison of subjective expert judgment against combining a few scores by a rule. ~60% of studies favor the algorithm; the rest tie (a tie favors the cheaper formula).
  - When to use: Any recurring prediction in an uncertain domain (admissions, hiring, credit, medical prognosis).
  - How: Replace or constrain holistic judgment with a mechanical combination of validated predictors.
- **Equal-weight / improper linear models (Dawes)**: Formulas with equal weights on standardized predictors match or beat optimally-weighted multiple regression, because they aren't distorted by sampling accidents.
  - When to use: When you lack data for formal regression but have predictors of some validity.
  - How: Pick a few valid, comparable predictors; standardize; sum with equal weights. "Back of an envelope" algorithms often beat experts.
- **Structured interview procedure (the "Do It Yourself" method)**: Defeat the halo effect and inconsistency in selection.
  - When to use: Hiring, selection, any personnel decision.
  - How: Choose ~6 independent traits; write factual questions per trait; score each 1–5 in a fixed sequence before moving on; sum the scores; hire the highest total. Resist inventing "broken legs" to override the ranking.

## Key Concepts
- **Low-validity environment**: A domain of significant uncertainty where accuracy is inherently limited (medical prognosis, credit risk, recidivism, wine prices).
- **Broken-leg rule (Meehl)**: You may override a formula only for a rare, decisive piece of information (like knowing someone broke a leg); such cases are genuinely rare — don't invent them.
- **Inconsistency of judgment**: Experts give different answers to identical information (radiologists contradict themselves 20% of the time); unreliable judgments cannot be valid predictors.
- **Multiple regression vs. equal weighting**: Optimal weights overfit the original sample; equal weights generalize better to new cases.
- **Apgar score**: Virginia Apgar's 1953 formula — 5 signs (heart rate, respiration, reflex, muscle tone, color) each scored 0/1/2 — standardized newborn assessment and cut infant mortality.
- **Hostility to algorithms**: Emotional/moral resistance to mechanical decisions (preference for the "natural"; a death by algorithm feels more poignant than the same death by human error).

## Mental Models
- Use a formula whenever you can, and at least consider it — especially in low-validity, high-volume decisions.
- Use equal weighting on a few good predictors when you don't have data for a proper regression — it's often good enough to beat experts.
- Use "collect facts first, intuition last" — a disciplined "close your eyes" holistic score adds value only after structured, factual scoring of separate traits.

## Anti-patterns
- **Letting interviewers make the final decision**: Overconfident interviewers overweight personal impressions and lower validity; interviews can diminish selection accuracy.
- **Adding cleverness and complexity**: Trying to consider complex combinations usually reduces validity; simple combinations win.
- **Overriding the formula on a hunch**: Human judges given the formula's own score still do worse when they override it "because they have more information."

## Worked Example
As a 21-year-old lieutenant, Kahneman redesigned the Israeli army's useless personality interview using Meehl. He had interviewers evaluate six specific traits (e.g., responsibility, sociability, masculine pride), each probed with factual questions about the recruit's past life and scored 1–5 in a fixed sequence before moving to the next trait — defeating the halo effect. The final fitness score was computed by formula, not interviewer judgment. Interviewers nearly mutinied ("You are turning us into robots!"), so he compromised: after the structured scoring, they could "close your eyes" and give an intuitive 1–5. Results improved from "completely useless" to "moderately useful." Surprise: the closed-eyes intuitive score predicted as well as the sum of the six ratings — but only because it followed the disciplined, factual collection. Lesson: don't simply trust intuition, but don't dismiss it either. Decades later the unit still tells recruits, "And then we tell them, 'Close your eyes.'"

## Key Takeaways
1. In low-validity environments, mechanical combination of a few predictors matches or beats expert judgment — a tie still favors the cheaper, consistent formula.
2. A key reason experts lose is inconsistency; formulas always return the same answer for the same input.
3. Equal-weight formulas often beat optimally-weighted regression because they don't overfit.
4. Structure interviews: independent traits, factual questions, sequential separate scoring, fixed combination rule — resist "broken-leg" overrides.
5. Intuition adds value only after disciplined, objective information collection — not as a substitute for it.
6. Resistance to algorithms is emotional and moral, but it is unethical to prefer intuition when a more accurate algorithm exists.

## Connects To
- **Ch 20**: The illusion of validity explains why clinicians resist Meehl and trust their own judgment.
- **Ch 22**: Defines when intuition (not formulas) can be trusted — regular environments with learnable feedback.
- **Ch 8**: The halo effect is what sequential, single-trait scoring is designed to defeat.
- **Ch 24**: Overconfidence of interviewers/experts underlies the preference for judgment over formula.
