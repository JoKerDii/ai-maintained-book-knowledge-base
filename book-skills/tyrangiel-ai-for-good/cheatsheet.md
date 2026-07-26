# Cheatsheet — AI for Good

## The Empowerment Test (apply first, to any AI proposal)
> **Who does this empower?** A teacher customizing lessons for thirty students ≠ a company eliminating teachers. A doctor spotting patterns in scans ≠ an insurer denying claims. Back the amplifier, resist the replacer.

## Should you build it? — decision path
- Is there a **specific problem that matters**, named by someone who lives with it?
  - No → stop. Solution-in-search-of-a-problem is the book's most common failure.
  - Yes ↓
- Does a **specific AI capability** map to it (predict / classify / optimize / generate)?
  - No → the answer is process or staffing, not AI.
  - Yes ↓
- Is there an **owner whose reputation is staked** on the outcome?
  - No → find your Buffington first. Championless pilots die.
  - Yes ↓
- Can you **standardize the data** first?
  - No → that IS the project (Perna: "see myself" before you optimize).
  - Yes → build, quietly, on notional data if real data is blocked.

## Consequence of being wrong → deployment posture
| If wrong, the cost is… | Posture |
|---|---|
| Trivial / reversible | Ship; learn from usage |
| Wasted time | Human reviews output |
| Clinical or legal harm | Human-in-the-loop mandatory; overrides logged as training data |
| Irreversible to a person | Don't automate the decision; automate the surfacing |

## Vendor selection — tells
| Green flag | Red flag |
|---|---|
| Restates your problem more precisely than you did | Demos before defining |
| Commits to a decision you'll make | Commits to a technology |
| Small enough that you have leverage | You are a rounding error to them |
| Works on your data | Works on their slideware |

## Institutional-resistance diagnosis
| Symptom | Name it | Move |
|---|---|---|
| Good strategy, willing leadership, nothing changes | **Frozen middle** | Fix incentives, not people |
| Rules nobody can explain | **Gall's Law limit** | Audit unused authorities before seeking new ones |
| Six-month review for a routine step | **Bureaucratic torture** | De facto ban — route around or get cover |
| Sixteenth report, same findings | Diagnosis is done | Work ratification + execution, not analysis |
| Reformers vs. civil servants | **Collaboration gate failure** | Build with, or lose the institutional knowledge |

## Adoption sequence for professionals (clinicians, teachers)
1. **Volunteers only** — never open with a mandate
2. **Bake-off** — competing tools, usage data decides
3. **Confidence first** — let them win before you ask them to change
4. **"You're the final check"** — preserve authority explicitly
5. **Mandate** — only after voluntary adoption plateaus

## Thresholds & numbers the book commits to
- Prompt validation: **10+ runs**, judge the *worst* output, not the best
- Admin burden in US healthcare: **25–30%** of spend
- Federal acquisitions workforce: **~30,000** people
- Prior military software studies since 1982: **15**, same conclusions
- Rule of thumb: **four singles > one home run** on politically exposed projects

## Failure tells — you are in trouble if…
- Evaluation is "vibes-based"
- The pilot was announced before it worked
- The champion is a title, not a person
- Success is measured in transactions, not outcomes (**transaction-count fallacy**)
- The model is fluent and nobody has checked whether it's right (**Eliza effect**)
- It agrees with you when you push back (**sycophancy**)
- The plan requires the frozen middle to volunteer for extra risk

## Personal protocol (Epilogue)
1. Flirt with the tools — know capability vs. claim
2. **Decline** what feels wrong; non-use is the strongest feedback tech has
3. Price the swap: what data, what attention, worth it?
4. Say loudly where AI should go — money follows taxes, purchases, votes
5. Or build it yourself; most people in this book had no software expertise
