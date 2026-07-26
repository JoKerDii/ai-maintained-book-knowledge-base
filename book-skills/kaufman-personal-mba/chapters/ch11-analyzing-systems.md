# Chapter 11: Analyzing Systems

## Core Idea
Before you can improve a system you must understand how well it currently operates, but you can't stop the world to measure it. Analyzing a live system means breaking it into parts you can grasp, measuring only what matters, and reading the data honestly enough to act on it.

## Frameworks Introduced
- **Deconstruction**: Separate a complex system into the smallest possible subsystems, understand each in isolation, then rebuild understanding from the ground up.
  - When to use: A system has more than seven or eight variables and exceeds your Cognitive Scope Limitation.
  - How: Identify major subsystems (engine, transmission, radiator); for each, find where it begins, its Inflows, internal processes, Feedback Loops, conditionals (if-then / when-then), triggers, endpoints, and Outflows; keep Interdependence in view; draw flowcharts.
- **Measurement**: Collect data about a system's core functions while it operates.
  - When to use: Whenever you want to know how well a system is performing or compare options. "What gets measured gets managed."
  - How: Identify the system's core functions, collect data on them continuously, and track how changes move the numbers. Measurement defeats Absence Blindness by surfacing problems you can't see directly (e.g. blood glucose).
- **Key Performance Indicator (KPI)**: A measurement of the critical parts of a system — the few numbers that actually drive improvement.
  - When to use: Always; measuring everything drowns you in meaningless data.
  - How: For a business, tie KPIs to the Five Parts of Every Business or Throughput (Value Creation, Marketing, Sales, Value Delivery, Finance). Limit yourself to three to five KPIs per system; dig deeper only when needed.
- **Correlation and Causation**: Correlation means two measures move together; Causation is a complete, repeatable chain of cause and effect.
  - When to use: Any time you attribute a result to a change you made.
  - How: Remember correlation is "a hint," not proof. Isolate your change from other factors, adjust for known variables (seasonality, conventions) using historical data; the more you isolate, the higher your confidence the change caused the result.
- **Sampling**: Take a small random percentage of total output and use it as a proxy for the whole system.
  - When to use: The system is too large or scalable to measure every unit (millions of phones, transactions).
  - How: Pull a random subset (1 in 20), test it, raise/lower the sampling rate by how fast you must catch errors; watch for non-random samples that bias results (Manhattan vs. West Virginia incomes). Use the largest random sample you can.
- **Segmentation**: Split a data set into well-defined subgroups to add Context and reveal hidden relationships.
  - When to use: Aggregate numbers look good but you don't know *why* (87% order increase — from whom?).
  - How: Segment by Past Performance, Demographics, or Psychographics. "Never report a metric without segmenting it."

## Key Concepts
- **Garbage In, Garbage Out**: Useless input always yields useless output; data quality caps how well you can understand a system.
- **Analytical Honesty**: Measuring and analyzing data dispassionately, resisting the social pull to make things look better than they are.
- **Context**: Using related measurements to interpret data; aggregate numbers in isolation tell you almost nothing.
- **Ratio**: Comparing two measurements by dividing one by the other (closing ratio, ROI, return on promotion).
- **Mean, Median, Mode, and Midrange**: Four measures of typicality — average, middle value, most frequent value, and the halfway point between extremes.
- **Norms**: Historical measurements used as Context for current ones (e.g. comparing this year's Q4 to last year's Q4).
- **Proxy**: Measuring one thing by measuring a closely correlated stand-in (mouse position as a proxy for attention).
- **Humanization**: Using data to tell a Narrative about a real person's experience, often via personas.
- **Confidence Interval**: The probability an analysis is correct; larger samples raise it.

## Mental Models
- Use **a Median next to the Mean** when you suspect outliers ("Gates and Buffett Syndrome") are skewing the average.
- Use a **Proxy** when the thing you care about can't be measured directly — but only when it's highly correlated with the real subject.
- Use **Norms** when comparing present performance to the past, and rebuild them whenever measurement methods change.
- Use **Humanization** when raw numbers (an 8-minute hold time) hide how a real customer actually feels.

## Anti-patterns
- **Fixating on easy-to-measure proxies**: Lines of code or raw revenue are visible but misleading; rewarding them triggers Incentive-Caused Bias.
- **Chasing a single "magic number"**: Stripping Context blinds you to why a number changed or whether it's just noise.
- **Living a comfortable lie**: Refusing more accurate data because it makes you look worse compromises your ability to actually improve.

## Worked Example
A manager wants a KPI for a team of programmers and picks "lines of code" — easy to collect and visible. But a skilled programmer improves a product by deleting ten thousand lines, which now registers as a setback. Worse, paying by line count invites Incentive-Caused Bias, producing bloated, *War and Peace*-length code. Lines of code is a Proxy for productivity, but an *inverse* one, so it fails as a KPI. The fix: choose a KPI tied to actual Throughput or value delivered (features shipped, defects resolved, customer outcomes), and have a dispassionate third party audit the choice to preserve Analytical Honesty.

## Key Takeaways
1. Deconstruct first — break a system into subsystems within your Cognitive Scope before trying to measure or fix it.
2. You can't improve what you don't measure, but measuring too much is as paralyzing as measuring nothing; pick three to five KPIs.
3. Quality of input bounds quality of insight (Garbage In, Garbage Out) — and so does honesty about what the data says.
4. Never read a number in isolation; supply Context through Ratios, Norms, and Segmentation.
5. Correlation is only a hint; prove Causation by isolating your change from everything else.
6. Choose the right measure of typicality, and use Proxies only when tightly correlated with what you actually care about.

## Connects To
- **Ch 12 (Improving Systems)**: You can only intervene wisely after analysis reveals how the system works and where its KPIs stand — analysis is the precondition for improvement.
- **Cognitive Scope Limitation**: Deconstruction and the three-to-five KPI rule both exist to keep a system inside the seven-or-eight-variable ceiling of working memory.
- **Incentive-Caused Bias**: Explains why proxy-based KPIs corrupt behavior and why Analytical Honesty needs an outside auditor.
