# Chapter 10: Visualizations That Really Work
*Scott Berinato*

## Core Idea
Don't start with chart-making rules — that's packing for a trip without knowing where you're going. Answer two strategic questions first (conceptual or data-driven? declaring or exploring?) and the right tools, skills, and chart type follow.

## Frameworks Introduced
- **The Two Questions**:
  1. **Is the information conceptual or data-driven?** — about the *information itself*, not the form you'll use. Conceptual: ideas, qualitative, goals are to simplify and teach ("here's how our organization is structured"). Data-driven: statistics, quantitative, goals are to inform and enlighten ("here are our revenues for the past two years"). Note the Gartner Hype Cycle uses a data-driven form (a line chart) with no actual data — it's a concept.
  2. **Am I declaring something or exploring something?** — Declarative: documenting and designing, affirming a statement to an audience in a formal setting. Exploratory: prototyping, iterating, interacting, automating — the audience is usually yourself or a small team.
- **The Four Types (the 2×2)**:

  | | **Conceptual** | **Data-driven** |
  |---|---|---|
  | **Declarative** | **Idea illustration** | **Everyday dataviz** |
  | **Exploratory** | **Idea generation** | **Visual discovery** |

  - **Idea illustration** — "the consultants' corner." Info type: process, framework. Setting: presentations, teaching. Primary skills: **design and editing**. Goals: learning, simplifying, explaining. Org charts, decision trees, cycle diagrams, this very 2×2. Because data's discipline and boundaries aren't built in, you must impose them; the useful skill is a text editor's — paring to the essence.
  - **Idea generation** — Info type: complex, undefined. Setting: working sessions, brainstorming, off-sites, early-phase innovation. Primary skills: **team-building and facilitation**. Goals: problem solving, discovery, innovation. Design and editing are *less* important here and sometimes counterproductive — when seeking breakthroughs, think in rapid sketches; refined designs slow you down. Jon Kolko: sketching is the effort to work through ambiguity and muddiness toward crispness.
  - **Visual discovery** — Info type: big, complex, dynamic data. Setting: working sessions, testing, analysis. Primary skills: **business intelligence, programming, paired analysis**. Splits in two:
    - *Visual confirmation* — answering "is what I suspect true?" or "what are other ways to depict this?" Manageable data, common chart types, rapid prototyping over design.
    - *Visual exploration* — no hypothesis; plot inclusively, combine data sets, load real-time data, add interactivity. Function trumps form. Suits specialized forms like force-directed diagrams for network clustering, or topographical plots. This is where you call in experts.
  - **Everyday dataviz** — Info type: simple, low volume. Setting: formal presentations. Primary skills: **design and storytelling**. Goals: affirming, setting context. Line charts, bars, pies, scatter plots — ideally one message, few variables.

## Key Concepts
- **Click and viz** — converting spreadsheet cells straight into a chart; it visualizes pieces of a spreadsheet, not an idea.
- **Visual grammar** — the rules (bar vs. line, color counts, key placement, zero baselines); useful but insufficient, and starting there forgoes strategy for execution.
- **Pyramid search** — the illustrated example technique: get information from experts in adjacent fields, who point you to top experts in theirs, who point you onward.
- **Declarative vs. exploratory purpose** — communicating information vs. figuring something out.
- **Duarte's reframe** — don't project that you're showing a chart; project that you're showing a reflection of human activity. Not "here are our Q3 financial results" but "here's where we missed our targets."
- **The joke test** — if an everyday dataviz can't speak for itself, it has failed, like a joke whose punch line has to be explained.

## Mental Models
- Use "the bigger and more complex the data, and the less you know going in, the more open-ended the work" to decide between confirmation and exploration.
- Think of chart discussion as a diagnostic: discussion about the *idea in the chart* is success; discussion about the *chart itself* is failure.
- When a chart takes more than a few seconds to digest, move it out of the presentation and onto paper or a personal screen for someone who isn't simultaneously listening to you.
- Treat busy charts as self-portraits: they say "look at all the data I have and the work I've done," which is never the audience's question.

## Anti-patterns
- **Starting with rules instead of purpose**: execution without strategy.
- **Decorating conceptual diagrams**: 3-D sandstone pyramids, color gradients, and drop shadows distract from the idea, and arrows that don't actually show the mechanism explain nothing; placing "experts" and "top experts" on the same plane destroys the very hierarchy the visual exists to convey.
- **Polishing during idea generation**: editing is the opposite of what breakthroughs need.
- **Including everything you know in a declarative chart**: two decades of historical context when the point is the last few years.
- **Presenting an exploratory visualization to a general audience**: Tesla's four-tire scatter plot is clear to its intended audience and inscrutable to everyone else — translate before presenting to executives.

## Worked Example
**The HR VP's health care chart (everyday dataviz).** She needs to tell the executive committee that growth in health care costs has slowed significantly, creating room to invest in additional services. She finds an online report, downloads the linked government data, clicks Excel's line chart option, and has a viz in seconds. Because it's for a presentation, she asks a designer colleague to add detail from the data set for a more comprehensive view — producing a well-designed, accurate chart covering two decades. It's the wrong chart. The committee doesn't need twenty years of context to decide about benefits investments; the point is that cost increases have slowed over the past few years, and that point isn't clearly communicated. The fix is subtractive: a single clean chart showing just the recent slowdown, so the trend lands without her saying a word — a foundation for her recommendation rather than a display of effort. Berinato's note: that simplicity takes discipline *and courage*.

**The mobile-vs-desktop hypothesis (visual confirmation).** A marketing manager suspects that at certain times of day more customers shop his site on mobile than on desktop, and his marketing programs aren't built for it. He loads data into Datawrapper. Attempt 1: a bar chart — he can't tell anything. He isn't designing, he's prototyping, so he moves fast. Attempt 2: a line chart — now he's seeing something, but three variables still obscure the mobile-versus-desktop comparison. Attempt 3: two variables. Attempt 4: he zooms in, and the hypothesis is confirmed. Each iteration is evaluated against the same original question.

**Tesla tire pressure (visual exploration).** Data scientist Anmol Garg built an interactive scatter plot of all four tires' pressure over time from the company's vast sensor data — creating the visualization *first*, then discovering uses: checking whether tires leave the factory properly inflated, how often customers reinflate, how long they take to respond to a low-pressure alert, leak rates, and predictive modeling of when a tire will go flat. His constraint: with terabytes of data, "you can't find anything looking at spreadsheets and querying databases. It has to be visual." For executive presentations, he translates these sessions into simple charts.

**Pyramid search (idea illustration).** The good version maps industries near-to-far on one axis and expertise low-to-high on the other, uses pyramid shapes to convey the rarity of top experts, and puts "climbing" and "pyramids" in the title so the idea lands immediately — with no literal 3-D decoration.

**The upmarket strategy whiteboard (idea generation).** A marketing team off-site spends an hour producing several competing approaches on a whiteboard, erasing nothing, until one gains traction because it best captures the key point: get fewer customers to spend much more. That sketch later becomes a formally designed idea illustration.

## Key Takeaways
1. Answer the two questions before opening any tool; they determine your resources, skills, and format.
2. Match skills to quadrant — editing and design for illustration, facilitation for generation, programming and BI for discovery, design plus storytelling for everyday charts.
3. In exploratory work, iterate fast and ignore aesthetics; in declarative work, aesthetics are the job.
4. Give a declarative chart one message and few variables, and cut anything that doesn't serve it.
5. Translate exploratory visuals into simple charts before showing them to executives.
6. Never adorn a conceptual diagram; metaphor invites decoration, and decoration obscures the logic.
7. Judge a chart by whether it moves people to see something they couldn't before — visualization is the process, not the outcome.

## Connects To
- **Ch 1 (Killer Presentation)**: Anderson's rules for slides — show images only when they carry meaning — are everyday dataviz discipline.
- **Ch 11 (Structure Your Presentation Like a Story)**: Duarte's reframe ("here's where we missed our targets") is a story move applied to a chart.
- **Ch 5 (Necessary Art of Persuasion)**: numbers alone don't persuade; the chart must carry an idea, not a spreadsheet.
- **Ch 7 (Get the Boss to Buy In)**: knowing which data forms your leaders trust is normative knowledge.
- **External — Tufte's data-ink ratio**: the subtractive discipline behind the VP's cleaner chart.
