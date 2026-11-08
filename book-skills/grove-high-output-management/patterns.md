# Patterns — Techniques from High Output Management

Concrete, repeatable procedures. Each is stated as: when to use, how, trade-offs.

---

## Limiting-Step Flow Design
**When to use**: Designing or debugging any process, or scheduling your own week.
**How**: (1) Identify the longest, hardest, most sensitive, or most expensive step. (2) Start at the committed delivery time and work *backward*. (3) Offset each shorter step to finish in sync. (4) Recheck when capacity changes — the limiting step moves.
**Trade-offs**: Optimizing anything else is wasted while the limiting step governs. Requires knowing real throughput times, which most organizations don't measure.

## Lowest-Value-Stage Rejection
**When to use**: Placing any quality gate — code review, hiring screens, design approval, incoming materials.
**How**: Find the point where accumulated value is lowest and still detectable. Reject the rotten egg at receiving, screen the candidate on campus, catch the defect at unit test.
**Trade-offs**: Earlier gates are cheaper per defect but see less information, so false rejections rise. Never applies to reliability defects — those admit no economic trade-off at all.

## Gate vs. Monitor Inspection
**When to use**: Whenever inspection interferes with flow.
**How**: *Gate* — hold everything until tests pass. *Monitor* — sample while the bulk keeps moving, stop the line after N successive failures. Rule of thumb: lean toward monitoring when experience says big problems are unlikely.
**Trade-offs**: Gates add throughput time; monitors let some bad material escape to a higher-value stage. For the same money you get far more monitoring than gating.

## Variable Inspection
**When to use**: Any recurring check whose subject's quality varies over time — including a manager's deep dives into a subordinate's work.
**How**: Check less often after a clean stretch; ramp up when problems appear.
**Trade-offs**: Cheapest and least disruptive, but rarely adopted "because we are creatures of habit." Applied to management, it is what separates sampling from meddling.

## Paired Indicators
**When to use**: Designing any metric or dashboard.
**How**: Pair every quantity measure with a quality counterpart, and every effect with its counter-effect. Inventory ↔ shortages. Vouchers processed ↔ errors found by audit or supplier. Square feet cleaned ↔ a manager's quality rating. Software delivery date ↔ capability delivered.
**Trade-offs**: Doubles measurement work, and the quality half is often partly subjective. Without it, indicators get over-optimized — "you will steer the bicycle where you are looking."

## Cutting Windows in the Black Box
**When to use**: Any opaque process whose failures currently surprise you.
**How**: Name inputs, output, and labor. Then install: **leading indicators** (early warnings you actually believe and will act on), a **linearity indicator** (cumulative actual vs. the straight line to target), **trend indicators** (vs. history *and* vs. a standard), and a **stagger chart** (rolling multi-month forecast re-issued monthly beside all prior forecasts, with actuals marked).
**Trade-offs**: A leading indicator you won't act on produces anxiety, not control. Stagger charts expose forecasters, which is the point and also the resistance.

## Work Simplification
**When to use**: Any tedious, time-consuming recurring task; whole administrative processes.
**How**: (1) Flow-chart every step *as actually performed* — omit nothing to make it look better. (2) Count the steps. (3) Set a reduction target: expect 30–50% in round one. (4) Question why each step exists; discard those surviving only on tradition or formal procedure.
**Trade-offs**: The mapping is tedious and politically uncomfortable. Some discarded steps turn out to have had non-obvious reasons — reintroduce deliberately, not by default.

## Calendar as Production Plan
**When to use**: Any week where others' requests fill your time.
**How**: Identify your genuinely immovable limiting steps and schedule around them. Batch similar work to reuse mental set-up. Actively fill gaps with non-time-critical work rather than waiting for incoming "orders." Say no at the start level, early. Build in slack. Keep a raw-material inventory of discretionary projects.
**Trade-offs**: Requires refusing work, and your capacity indicators are less credible than a factory's. Without the discretionary-project inventory, free time becomes meddling.

## Standard Responses to Interruptions
**When to use**: When the same questions keep reaching you.
**How**: Catalogue the recurring interruptions; prepare standard answers; delegate them to less experienced people. Batch the rest into regular one-on-ones and staff meetings. Keep an indicator archive so answers don't require fresh research. Post an explicit boundary ("don't interrupt unless it can't wait until 2:00") *paired with* a genuinely open office hour.
**Trade-offs**: Hiding fails — the problems are legitimate and accumulate. Regularity requires coordination with others (Intel reserved Monday mornings company-wide for planning groups).

## The One-on-One
**When to use**: With every professional who reports to you, permanently.
**How**: Subordinate owns it — he prepares a written outline and walks you through it. Minimum one hour. Held in or near *his* work area. Frequency set by his task-relevant maturity for current tasks and the pace of change in his area. Cover indicators (especially those signalling trouble), what's happened since last time, people and organizational issues, and **potential** problems. Both take notes on the outline. Keep a hold file. Invite heart-to-heart issues early. Schedule the next one as this one ends.
**Trade-offs**: Costs you ~90 minutes per subordinate per cycle, which is exactly why six-to-eight reports is the ceiling. Watch for the zinger.

## Ask One More Question
**When to use**: Any one-on-one, review, or diagnostic conversation.
**How**: When you think the subordinate has finished on a subject, ask another question. Keep prompting until *both* of you feel you've reached the bottom.
**Trade-offs**: Can feel like interrogation if the relationship is weak. The alternative — talking about *your* problems instead of surfacing theirs — is worse.

## Chairing a Mission-Oriented Meeting
**When to use**: Any meeting convened to produce a decision.
**How**: Before — know the decision needed, confirm a meeting is necessary/desirable/justifiable, secure commitments from attendees (or a proxy with power to speak), cap at eight, send an agenda stating the purpose *and each person's role*, handle logistics. During — enforce time discipline, confront lateness. After — send fast, specific minutes: what, who, when.
**Trade-offs**: Feels like regimentation to attendees until they're the one whose time got wasted. Price it: ten managers for two hours is a real, approvable expenditure.

## The Six-Question Decision Structure
**When to use**: Before any significant decision process starts.
**How**: Answer, in writing: (1) What decision needs to be made? (2) When? (3) Who will decide? (4) Who will be consulted first? (5) Who will ratify or veto? (6) Who will be informed? Give competing interest groups roughly equal representation on the deciding body.
**Trade-offs**: Slower to start. Prevents the late veto that demoralizes teams and creates the appearance of political maneuvering.

## Free Discussion → Clear Decision → Full Support
**When to use**: Any decision where knowledge and position power are separated.
**How**: Insist all views are voiced as equals with status ignored; withhold position power entirely during discussion. Then state the decision with utter clarity, especially when controversial. Then require commitment to support — not agreement. If no consensus arrives on time, the senior person decides.
**Trade-offs**: Onerous — Sloan's warning about the temptation to skip it. Demands that people be taught "nobody ever died from making a wrong business decision."

## The Peer-Plus-One Intervention
**When to use**: A peer group circling without converging.
**How**: Add one hierarchical level — someone who need not be the most knowledgeable, functioning as a repository of *how decisions get made*. Absent a formal chair, the person with the most at stake takes charge; failing that, the senior person present.
**Trade-offs**: Risks importing position-power distortion into free discussion; the plus-one must moderate, not decide, until the decision stage.

## Three-Step Planning
**When to use**: Annual planning, team planning, or personal roadmapping.
**How**: (1) Establish projected environmental demand — **without** discounting it by what you think you can deliver. (2) Establish present status in the same "currency," including timing and a realistic loss factor for work in flight (~20% in semiconductors). (3) Ask separately "what do I *need* to do?" and "what *can* I do?", then decide what you will do and when. The resulting action set is your strategy.
**Trade-offs**: The un-discounted demand forecast feels unrealistic to the people producing it — but pre-constraining it means never tooling up for real demand.

## MBO (Objectives and Key Results)
**When to use**: Translating plans into work you can steer by, at least quarterly.
**How**: Two questions — where do I want to go (objective), how will I pace myself (key results with specific wording and dates). Keep objectives few. Nest them so a subordinate's objective supports the supervisor's. Set them at roughly 50/50 odds of success.
**Trade-offs**: It is a stopwatch, not a contract. Mechanical use by the supervisor (as a review basis) or the subordinate (refusing an unlisted opportunity) is "petty and unprofessional."

## Delegation with Quality-Assurance Monitoring
**When to use**: Every delegated task.
**How**: Share the information base and operational values first. Prefer delegating what you know best (easier to monitor). Check at the lowest-added-value stage — review the *rough draft*. Sample randomly and partially. Set frequency by the subordinate's TRM on that specific task, decreasing as performance improves. To delegate a decision, monitor the *decision-making process* by asking probing questions about the request.
**Trade-offs**: Delegating what you know best goes against emotional grain. Under-monitoring is abdication; 100% checking is meddling.

## Matching Style to Task-Relevant Maturity
**When to use**: Continuously, and immediately after any promotion, transfer, or change of pace.
**How**: Low TRM → structured, tell what/when/how. Medium → individual-oriented, two-way communication, mutual reasoning. High → minimal involvement, objectives and monitoring. Monitor at every level. Revert instantly when the task or pace changes.
**Trade-offs**: Managers systematically skip the medium row and overrate their own delegation (90% rated themselves higher than their subordinates did). Reverting feels regressive to both parties.

## Dual Reporting
**When to use**: Any hybrid organization where a manager cannot technically supervise what reports to him.
**How**: Split supervision — mission supervisor gives priorities and daily monitoring; functional supervisor gives standards, technical oversight, and career ownership. The functional half may be a **peer group** rather than an individual, chaired by a coordinating manager.
**Trade-offs**: Ambiguity, which most people dislike, and patience-taxing cross-peer negotiation. Requires trust — a cultural property, not a structural one — and voluntary surrender of individual decision-making.

## Choosing a Control Mode
**When to use**: Deciding how to govern any activity, team, or new hire.
**How**: Score individual motivation (self- vs. group-interest) and the environment's CUA factor (low/high). Self-interest + low CUA → market. Group-interest + low CUA → contract. Group-interest + high CUA → culture. **Self-interest + high CUA → chaos**: lower the CUA or build group-interest, but don't try harder.
**Trade-offs**: Culture is not universally superior — it can't govern tire purchases or a tax system. Building it requires accumulated shared experience, which takes years.

## Building a Racetrack
**When to use**: Any group whose performance is mediocre and unresponsive to pressure or inducement.
**How**: See the work as the people doing it see it. Define rules of the game and a way for people to measure themselves against peers doing the same work. Score periodically, by someone whose esteem that group values, and publish comparative results.
**Trade-offs**: Removing the competition removes the motivation. Contests between internal groups for a shared resource (e.g. divisions bidding for salespeople's time) produce exactly the self-interested behavior you'll later resent.

## The Performance Review Worksheet
**When to use**: Preparing any review.
**How**: (1) Scan progress reports, performance against quarterly objectives, one-on-one notes. (2) Blank paper — write everything down without editing, major to trivial, no order. (3) Put documentation away and find relationships: which items are manifestations of the same phenomenon, and *why* the strength or weakness exists. (4) Name those "messages." (5) Gather specific examples. (6) Apply the memory test — delete anything the subordinate won't remember; it can wait for next time.
**Trade-offs**: Deleting true observations feels like dishonesty. It isn't: "the purpose is not to cleanse *your* system… but to improve *his* performance."

## Delivering a Review — The Three L's
**When to use**: Every review delivery.
**How**: **Level** — total frankness, including in praise. **Listen** — use every sensory capability to verify the message landed; watch the person; if their verbal and nonverbal responses don't assure you, it is *your* responsibility to keep at it. **Leave yourself out** — it is the subordinate's day in court.
**Trade-offs**: Verification takes time and can feel repetitive. A paraphrase is not sufficient evidence of receipt.

## Moving Someone Through the Problem-Solving Stages
**When to use**: A review or confrontation with a serious performance problem.
**How**: Track which stage you're in — ignore → deny → blame others → assume responsibility → find the solution. Supply facts and examples against ignoring and denial. **Do not attempt the solution while they are still denying or blaming.** Get them to assume responsibility (the emotional step); then solve jointly (the intellectual step, and easier).
**Trade-offs**: The blame-others stage is where things stick. If they won't move, invoke position power explicitly, secure a **commitment** without agreement, and monitor performance against it.

## Interviewing
**When to use**: Every hire.
**How**: Let the candidate talk 80% while you control by active listening and interruption. Steer to subjects familiar to both, in your vocabulary. Mine four categories: technical skill; what he *did* with it; **discrepancies** between the two; operational values. Ask blunt direct questions. Use a hypothetical when domains don't overlap — supply the domain yourself and watch the derivation. Ask what he wants to know about you. Build a personal bond with references (the last ten minutes beat the first ten), then re-interview.
**Trade-offs**: Hiring is the one deliberate exception to the potential trap. Even done well it "merely increases your odds of getting lucky." No tricks — the candidate is forming durable first impressions.

## The "I Quit!" Response
**When to use**: The moment a valued, dedicated employee says they're leaving.
**How**: Drop everything immediately — the delay itself confirms the reason they're going. Sit them down, ask why, let the rehearsed speech run without arguing. Then ask more questions; the real issues surface after the prepared points. Don't lecture, don't panic, don't try to change their mind — buy time and commit to follow through. Escalate to your supervisor and make it his problem too. Pursue every retention avenue including transfer, project-managing it yourself.
**Trade-offs**: You may lose them from your own org to keep them in the company. Answer the blackmail objection ("you shook us up and made us aware of the error of our ways") and the accepted-offer objection (two commitments, and the one to daily colleagues is stronger).

## Designing a Performance Bonus
**When to use**: Structuring variable pay for managers.
**How**: Scale the bonus percentage with total compensation (~50% senior, 10–25% middle). Split across three factors — individual performance judged by the supervisor, immediate team's objective performance, overall corporate financial performance. Answer five questions: team or individual, which team, what period (close enough that they remember the work), what basis (avoid the beauty contest), and what floor (never pay lavishly into bankruptcy).
**Trade-offs**: "No matter what way you choose, none gives you exactly what you want." Splitting dilutes each signal but calls attention to all three.

## Recycling an Over-Promoted Person
**When to use**: Someone performing below average for too long after a promotion.
**How**: Return them to the job they previously did well. Name management's misjudgment openly rather than theirs. Support them through the embarrassment. Do it visibly.
**Trade-offs**: Society reads it as personal failure, which is why the default is a forced exit rationalized as "for his own sake." Done openly, the embarrassment is short-lived — and these people often succeed on a later promotion.

## Manager-Delivered Training
**When to use**: Any recurring capability gap; continuously as a process.
**How**: List everything your people should be trained in, from trivial to value-system level; ask them what they need. Inventory available teachers and materials. Prioritize. Build one three-to-four-lecture course on the most urgent topic. Set deadlines; outline the whole, write lecture one, and go — write lecture two after delivering one. Treat the first delivery as a throwaway and give it to your *most* knowledgeable subordinates for critique. If many repetitions are needed, train instructors from your first set. Collect anonymous numerical plus open-ended feedback.
**Trade-offs**: Costly — Intel priced one new one-day middle-management course at over a million dollars in student time alone. Canned outside courses that contradict your practice demoralize rather than merely fail. Expect feedback split evenly between "too detailed," "too superficial," and "just right."
