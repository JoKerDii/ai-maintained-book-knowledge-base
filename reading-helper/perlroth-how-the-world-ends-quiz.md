# Quiz Book: *This Is How They Tell Me the World Ends* (Nicole Perlroth)

> **Source note:** This quiz reflects the skill's chapter notes (SKILL.md, glossary, patterns, cheatsheet and the 25 chapter files, Prologue + Ch 1-24), **not the book's own wording**. Figures are as recorded in those notes; where the notes disagree with themselves, the answer says so.

## How to use this quiz book
1. Work one section at a time (about 10 minutes each). Cover the answers (the lines starting **A:**) and answer aloud or on paper first.
2. Question types are marked: **[SA]** short answer, **[TF]** true/false, **[MC]** multiple choice, **[Explain]** explain in your own words, **[Scenario]** apply a concept to a situation.
3. Score yourself: full credit if you hit the core idea, half if you only recall the vocabulary. Re-read the matching chapter notes for anything under 70%.
4. Finish with the 20-question cumulative final exam at the end. Pair this file with `perlroth-how-the-world-ends-arguments-and-evidence.md`.

Section map: 1 (Prologue, Ch1) / 2 (Ch2-3) / 3 (Ch4-5) / 4 (Ch6-7) / 5 (Ch8-9) / 6 (Ch10-11) / 7 (Ch12-13) / 8 (Ch14-15) / 9 (Ch16-17) / 10 (Ch18) / 11 (Ch19) / 12 (Ch20) / 13 (Ch21-22) / 14 (Ch23) / 15 (Ch24) / Final exam.

---

## Section 1 - Prologue: Kyiv, and Ch 1: Closet of Secrets

**1. [SA]** Why do the notes call Ukraine the world's cyberwar "test kitchen"?
**A:** Russia rehearsed every tool there: 2014 election malware that would have declared a fringe candidate the winner, disinformation, media trapdoors, then the 2015 and 2016 grid attacks and NotPetya. Ukrainian experts called it "a cruel version of the scientific method": test a capability, demonstrate it, move on. When attacks on Ukraine slow, "that means they've moved on."

**2. [TF]** NotPetya was ordinary ransomware: victims who paid could recover their data.
**A:** False. It mimicked Petya ransomware but no payment could recover data; it was a state weapon built for mass destruction "wearing a criminal's mask" (ransomware as disguise).

**3. [MC]** Putin's two rules for hackers are: (a) no hacking inside Russia and do the Kremlin's favors when asked; (b) never touch banks and always pay taxes; (c) only attack NATO states; (d) always leave a signature.
**A:** (a). Otherwise hackers have full autonomy, "patriotic" hackers as artists.

**4. [SA]** Give the key NotPetya facts: date, timing hook, cost, and two vivid effects.
**A:** June 27, 2017, on Ukraine's Constitution Day (an anniversary message). Cost over $10 billion and climbing by 2019 (Merck and FedEx roughly $1 billion between them in this chapter's account). 80% of Ukraine's computers wiped; at Chernobyl 2,500 computers went dark in seven minutes and radiation monitors went offline so staff measured by hand. Patient Zero was a family-run tax-software company whose update mechanism was hijacked.

**5. [Explain]** What is the "vulnerability paradox"? Use the numbers.
**A:** The country with the greatest offensive cyber advantage is also the most vulnerable. Ukraine survived because it was not fully automated (no Internet of Things, hand-counted paper ballots); the US plugs in 127 devices a second and has built "the world's largest attack surface," while at the NSA offense outnumbers defense roughly 100 to 1. Connectivity is the exposure.

**6. [Explain]** How did analysts attribute the Ukraine grid attack despite routing through Singapore, the Netherlands and Romania and randomized code?
**A:** Attribution by resources, not traces: the sophistication and the absence of a profit motive pointed to a state. "Political hit jobs don't have business models," so no money means political.

**7. [SA]** In Ch 1, what four routes did the NSA use around encryption instead of breaking the math?
**A:** (1) Lobbying standards bodies via allies to adopt a flawed random-number formula, (2) paying RSA to make it the default, (3) CIA-planted backdoors on chip factory floors, (4) hacking Google and Yahoo servers before the data was encrypted. The algorithms "held up quite nicely"; attackers go through people, standards, supply chains and endpoints.

**8. [SA]** Define zero-day and say why it is called "God mode." Which Stuxnet and espionage uses does Ch 1 name?
**A:** A flaw with no existing patch; the vendor has had "zero days" to defend. Exploiting one is like holding a spare key to a locked building that works no matter how vigilant the administrator. Uses named: iPhone surveillance, sabotaging Iran's centrifuges (seven Windows and Siemens zero-days), stealing source code (one Microsoft zero-day). The Mariner 1 anecdote (a missing hyphen destroyed a $150M spacecraft) is the physical analogue of software flaws.

**9. [Scenario]** You run security at a utility in a country bordering one that is suffering repeated blackouts from a hostile neighbor. A colleague says "that's their problem." Which concept applies and what do you do?
**A:** The test-kitchen pattern / "a neighbor's cyberattacks are your rehearsal footage." Treat the neighbor's incidents as a preview, study them, and brief leadership; the prologue's anti-pattern is ignoring the neighbor's blackouts because the news cycle is elsewhere (Ferguson, ISIS, Sony in 2014).

**10. [Scenario]** A board member says "we encrypt everything with strong algorithms, so surveillance can't reach us." Which Ch 1 lesson answers this?
**A:** Encryption works; the NSA wins by subverting standards, vendors, supply chains and endpoints. Ask "who else has this, and where did it come from?" and note that shared technology means a backdoor into an adversary is a backdoor into you. Also: the Snowden trove showed a zero-day trade exists but not how it works, which is the book's quest.

---

## Section 2 - Ch 2: The Fucking Salmon, and Ch 3: The Cowboy

**1. [Explain]** What is "the fucking salmon" and why is it the book's shorthand?
**A:** At a 2013 Miami industrial-security dinner two Italian exploit sellers (Auriemma and Ferrante) deflected the question of whom they sell to and refuse to sell to ("talk about my salmon"). It stands for the trade's culture of silence: a non-answer about buyers is the answer, since a seller with limits would state them.

**2. [SA]** State Langner's mirror argument with numbers.
**A:** Stuxnet used seven zero-days to reach air-gapped centrifuge controllers and wreck roughly a fifth of Iran's centrifuges. The same techniques work on power, water and chemical plants, and the largest concentration of vulnerable industrial systems is in the United States. A weapon built for one target becomes a template for everyone.

**3. [SA]** Name at least four of Perlroth's research questions from Ch 2.
**A:** Who buys and who is refused; whether US agencies buy from foreign hackers with taxpayer money; how the government justifies undermining commercial technology its own citizens use; whether stockpiles are used, protected or leaking; what happens if they get out; who profits and who is trying to stop it. It took seven years to answer, by which time the NSA's tools had leaked and "the playing field was leveled."

**4. [TF]** John Watters, founder of the first public bounty business, had a deep computer-science background.
**A:** False. He was a Texas private-equity investor with no computer background who bought bankrupt iDefense for $10 (2002), put in $7M, and sold to Verisign for $40M in 2005.

**5. [MC]** What did Bill Gates's 2002 Trustworthy Computing memo do to the exploit market? (a) flooded it with bugs; (b) made Microsoft bugs rarer and far more valuable; (c) eliminated it; (d) moved it to Linux.
**A:** (b). Microsoft froze products, retrained about 10,000 developers, created a hacker hotline and Patch Tuesday; remote Windows exploits went from pennies to six or seven figures.

**6. [SA]** Give the iDefense price-erosion numbers.
**A:** Mystery government contractors offered $150,000 for bugs iDefense paid $400 for; within three years iDefense was priced out ($400 to $4,000 to $50,000 per bug). Rational hackers hoard when secret buyers pay more for silence than defenders pay for disclosure.

**7. [Explain]** What was the "bounty insight" of Endler and James, and what is proof-of-concept leverage?
**A:** Vendors lived off hackers' free labor via BugTraq and threatened them with lawsuits, so white hats had every incentive to go black. Paying gives clients early warning plus workarounds and a unique product. A working proof-of-concept forced vendors who dismissed a bug as minor to patch on the customer's timetable, shifting power from vendor to finder.

**8. [SA]** What were D5, "fire your customers upward," and Watters's refusal about the gray market?
**A:** D5 = the Pentagon's offensive-cyber purposes: deny, degrade, disrupt, deceive, destroy (why zero-days are hoarded). Fire upward = double the subscription ($18K to $38K), drop non-payers, win them back at multiples ($25K to $1.5M for one agency). Watters refused to withhold bugs from customers to sell to contractors because that would be conspiring against his customers.

**9. [Scenario]** A software vendor's counsel wants to threaten the researcher who reported a flaw. What does Ch 3 predict and which anti-pattern is this?
**A:** "Suing the people who find your flaws." Microsoft once called disclosure "information anarchy" and the Def Con message was "give us your bugs first or get sued"; hostility pushed finders toward buyers who pay for silence. Better: a defined, paid reporting channel.

**10. [Scenario]** A Gulf-state reseller pitches your sales team on a "zero-day ethics board" and refuses to say which governments are excluded. Which Ch 2/3 ideas apply?
**A:** The salmon rule (a non-answer is the answer) and "governments are clients, not regulators": no one in a secret market has an incentive to disclose, so the only containment is publicity. Also remember Watters's lesson that the market you open does not stay yours.

---

## Section 3 - Ch 4: The First Broker, and Ch 5: Zero-Day Charlie

**1. [Explain]** Why is secrecy a precondition of a zero-day's value, and what happened to the Grugq?
**A:** A disclosed bug is named, scored, databased and patched, so access dies; government buyers pay for silence. The Grugq's Forbes interview (posing with a bag of cash) halved his business overnight: talking to media is a broker's fastest route to bankruptcy.

**2. [SA]** What does "access is king" mean and what is the "trifecta"?
**A:** Cyberweapons are useless without a way in, so contractors sold access (reconnaissance on the target's environment, then a clean beachhead). Agencies wanted the full kill chain (entry, beaconing to command-and-control, exfiltration, obfuscation). The trifecta is reliability, invisibility, persistence; when all three appear, "ka-ching."

**3. [SA]** Why do agencies buy the same exploit multiple times, and what did "Sabien" do about it?
**A:** Nothing is shared; each agency wants "the win" and the budget that follows. Sabien once told four agencies to go to lunch together. NDAs and classification produce duplication and waste.

**4. [SA]** Recall the early price structure (mid-1990s) and the trust chain.
**A:** About $1M from an agency for a set of ten exploits; about $50K for a Windows bug, double for an obscure adversary system, about $150K for deep persistent access. Suppliers: post-Soviet Eastern Europeans and Israelis (Unit 8200 veterans). Deals were hotel-room demos, cash via Israeli middlemen ($500K), Western Union, no payment if unreliable, and no way to know if a bug was resold to your enemies.

**5. [TF]** Firmware persistence means a reinstall of the operating system cures the infection.
**A:** False. Exploits close to the hardware (e.g., a video memory card) survive wipes and reinstalls; the only cure is the dumpster.

**6. [SA]** Miller's "five options" for a serious bug: list them and say which paid.
**A:** (1) Tell the vendor and risk threats or lawsuits; (2) keep it and use it; (3) publish for credit and shame; (4) sell to a disclosure broker like iDefense for a few thousand; (5) sell to a government directly or via a broker for far more, with silence and no credit. Only option five paid.

**7. [Explain]** What negotiation lessons come from Miller's first sale?
**A:** One agency offered $10,000; another accepted an $80,000 ask "too quickly" (he'd underpriced); the exploit failed on the target's Linux variant so the price fell to $50,000 with a two-year silence license; he never learned the target. Quick acceptance of your price is evidence you asked too little.

**8. [Explain]** What was "No More Free Bugs" (March 2009), what triggered it, and why didn't the government men clap?
**A:** After Google BCC'd Miller's boss to try to get him fired over a free Android exploit report, Miller, Dino Dai Zovi and Alexander Sotirov told hackers to stop reporting for free. It pushed hackers away from vendors and toward the underground, meaning fewer patches and more sellers, which is what government buyers wanted. One NSA veteran worried about whom foreign hackers would sell to instead.

**9. [Scenario]** You found a critical bug in a popular browser in your spare time and the vendor has no bounty. Using Miller's framework, what are your realistic outcomes and risks?
**A:** Predict where it goes by asking "which of the five options pays?" Only selling pays; reporting free risks threats and bad treatment; selling means you may never know the end user and the exploit can return. Vendor hostility is a subsidy to the underground market.

**10. [Scenario]** You lead procurement at an intelligence contractor and a seller offers an "exclusive" exploit. What does Ch 4/5 warn?
**A:** Assuming a bought exploit is exclusive is an anti-pattern; there is no way to know if it was resold. Miller's white paper also notes buyers can't guarantee exclusivity or advertise needs, and a patch during weeks-long vetting can zero the value.

---

## Section 4 - Ch 6: Project Gunman, and Ch 7: The Godfather

**1. [Explain]** What is the central lesson of Project Gunman?
**A:** The most valuable interception point is upstream of encryption (keystrokes, sensors, plaintext links). Encryption alone is never enough; ask "where does the data exist in the clear?" The NSA later used the same idea on Google/Yahoo links and smartphones.

**2. [SA]** Recall the Gunman numbers and dates.
**A:** Reagan-approved 1984 operation, six months, "VRK" (very restricted knowledge). 250 replacement typewriters prepared (only 50 obtainable at first). First implant traced to a 1976 shipment, so about eight years undetected; 16 bugged typewriters found (13 in Moscow, 3 in Leningrad), 5+ variants. Found July 23, 1984. Deeley's internal bounty: $5,000. Earlier "The Thing"/"Golden Mouth" Great Seal bug ran 1945-52.

**3. [MC]** Where did Deeley's team look first? (a) typewriters; (b) crypto gear; (c) the chimney; (d) the elevator.
**A:** (b), for about ten weeks, because it was the "obvious" leak point. The typewriters were last. The chimney antenna was a missed near-miss.

**4. [SA]** What was the Soviet "tell" the Americans ignored?
**A:** Soviets forbade their own staff from typing classified material on electric typewriters and used tamperproof containers. If an adversary protects itself unusually against a vector, assume they have weaponized it.

**5. [Explain]** Explain Before Gunman / After Gunman (BG/AG) and the Ware and Anderson reports.
**A:** Gosler's periodization: BG the US was "in la-la land"; AG it was breaking into "anything with a pulse." The Ware Report (1967) and Anderson Report (1972) had already concluded technology could not provide a secure system in an open environment and that trapdoors are inevitable wherever operating systems accept updates; nobody acted.

**6. [SA]** State Robert Morris Sr.'s confidence thresholds and the code-size examples.
**A:** Total confidence in 10,000 lines of code or fewer, zero confidence above 100,000. Gosler's Chaperon implant hid undetected in under 3,000 lines. Linux grew 176K to 15M lines; F-35 8M; Vista 50M. Verification does not scale with code size.

**7. [Explain]** Describe the Chaperon studies and what they teach about evaluation.
**A:** Sandia split staff into subverters and evaluators (1985). Gosler planted a cheap implant (Zork text leaking secret variables) and a deep one; evaluators failed on both over months, and explaining the second took three eight-hour whiteboard sessions. In Chaperon 2 only Gosler of about 100 engineers found the new implant. Measure detection rate, not just presence of bugs.

**8. [SA]** Give the adversary Tier model and the Willie Sutton principle.
**A:** Tiers I-II buy click-and-shoot exploits; III-IV train hackers and hire contractors; V-VI spend years and billions on zero-days and supply-chain insertion, VI at push-button scale (Russia, China, US). Willie Sutton: go where the data is; passive collection dies when data moves to endpoints.

**9. [SA]** What was CITO's doctrine, and what are Crypto AG and the SIGINT Enabling Project?
**A:** Recruit people (sysadmins, fiber techs, couriers, even the janitor) because humans hold combinations, passwords and manuals. Crypto AG: Swiss encryption vendor whose machines were spiked so US decoders could read Iran, Iraq and Libya traffic. SIGINT Enabling: Snowden-leaked 2013 budget line for covertly influencing commercial product designs, claiming "complete enabling" of two leading VPN chip makers.

**10. [Scenario]** A manager must buy hardware for a sensitive environment. Apply Gunman's supply-chain lessons.
**A:** Use tamper-evident bags, anti-tamper sensors wired to a guard post, X-ray before and after transit, chain of custody with armed escort, and treat insider/shipping/maintenance as insertion points. Also: if a leak persists after clearing people, "assume the machine is the mole."

**11. [Scenario]** A vendor says its 5-million-line product has been "fully audited and verified clean." How does Ch 7 respond?
**A:** Beyond a few thousand lines no one can guarantee a system is implant-free: "even if you found something, you could never be confident you found everything." Treat vendor assurances as claims, not proofs, and design assuming implants exist beyond small trusted kernels.

---

## Section 5 - Ch 8: The Omnivore, and Ch 9: The Rubicon

**1. [Explain]** What is the intravenous principle?
**A:** Once the needle (implant) is in, the same access can replenish fluids or deliver a lethal dose: reconnaissance implants are latent attack tools. Ask what a payload swap would cost; if trivial, treat the implant as a weapon.

**2. [SA]** Describe the "race to the bare metal" and the TAO assembly line.
**A:** Target progression: terrorist channels, operating systems, browsers and apps, kernel-level exploits. Deeper (kernel, firmware, hardware) means longer dwell time and patching helps less. TAO divides labor: bug-finding/exploit writing; implants and payloads; hard-to-reach targets (hack the mistress or maid); the Transgression Branch for "fourth-party collection"; front-company infrastructure.

**3. [SA]** Recall the Ch 8 numbers: Genie, FISA, LOVEINT, starting pay.
**A:** Genie managed about 85,000 implants by 2013 (up 4x in five years). FISA court approved 1,748 of 1,789 applications unchanged in 2012. LOVEINT: a dozen employees caught spying on exes; demoted, clearances stripped, none prosecuted. Starting salary about $40K. The 2008 USB incident led the Pentagon to superglue USB ports.

**4. [Explain]** Why is shared technology a moral hazard? Quote the line.
**A:** In the Cold War the US spied on Soviet tech; now everyone runs the same Windows, Oracle, Gmail and iPhones, so weakening a target's stack weakens your own. "There are no patents on vulnerabilities." Secrecy only deferred the reckoning.

**5. [TF]** Genie's automation was a good safeguard because it removed human error.
**A:** False (anti-pattern). It eliminated the pause where someone might ask "should we?" Build the moral pause back in deliberately.

**6. [SA]** What was Keith Alexander's "third option" and why was Stuxnet "sabotage-as-accident"?
**A:** Between failed diplomacy and airstrikes (World War III), a cyberattack that mimics natural accidents. The worm accelerated centrifuge failure rates already around 10% a year, so Iranian engineers blamed themselves.

**7. [SA]** Outline the seven-zero-day chain and targeting limits.
**A:** Four Microsoft plus three Siemens exploits: .LNK USB jump (no click), printer-spooler spread, two Windows privilege exploits, stolen Taiwanese code-signing certs, Siemens Step 7 default password, PLC payload. Fired only on PLCs controlling clusters of exactly 164 centrifuges running 800-1100 Hz (designed with NSA legal review). One spread mechanism was documented in Hakin9, so not truly a zero-day.

**8. [SA]** What did the worm do at the end, and what were the results?
**A:** After 13 days feeding normal readings (the "Mission Impossible replay"), it spun rotors to 1400 Hz for 15 minutes and down to 2 Hz for 50 minutes on a 27-day cycle. About 2,000 of 8,700 centrifuges destroyed by early 2010; Iranians turned on each other. It was 500 KB, fifty times larger than anything seen before.

**9. [Explain]** What happened in June 2010 and what lessons about containment follow?
**A:** The worm escaped Natanz; the leading theory blames an Israeli-added spreading mechanism (Biden: "Sonofabitch... they went too far"); Obama chose to accelerate. Precision does not equal containment; the constraint on what it damages did not constrain where it spreads; the air gap was bridged by a human with a USB stick. Langner's TED talk named the US.

**10. [Scenario]** Your team proposes a "surveillance-only" implant in a competitor-country router. Which Ch 8 concepts do you apply?
**A:** Intravenous principle (a payload swap makes it a weapon), moral hazard (the same router model runs in US hospitals and utilities), and the mirror rule (any accusation you level at an adversary is probably true in reverse).

**11. [Scenario]** You design a targeted payload for a sensitive operation. Lawyers approved a narrow target. What does Stuxnet say you still must do?
**A:** Design containment separately from targeting: plan for escape ("never contemplated what would happen if it ever seeped through the air gap"), expect it to be studied, copied and turned back, and recognize that using a novel weapon legitimizes it for everyone.

---

## Section 6 - Ch 10: The Factory, and Ch 11: The Kurd

**1. [Explain]** What is NOBUS and why did it fail?
**A:** "Nobody But Us": patch low-hanging fruit, hoard exploits supposedly only the US can weaponize (Hayden's "four acres of supercomputers" test). It collapsed from about 2012 as Russia and China honed the same skills; exclusivity arguments expire as adversaries catch up.

**2. [SA]** What is the weaponization gap and what did VRL sell?
**A:** Finding a bug is a pain, weaponizing it a bigger pain, making it 100% reliable the biggest. VRL ran fuzz farms (tens of thousands of VMs) to guarantee no crash or tip-off and delivered push-button tools. Exploit development time went from hours to weeks to months.

**3. [SA]** Give the budget numbers: Cyber Command, offense vs defense, zero-day procurement line.
**A:** Cyber Command created June 2009; budget tripled $2.7B to $7B by 2012; staff 900 to 4,000 to 14,000 (2020). Offense (breaking and entering) $652M in 2013, twice the network-defense budget. New $25.1M procurement line, about 625 zero-days a year. (The Prologue says offense outnumbers defense "roughly 100 to 1" at the NSA without saying what is counted, while Ch 10 gives 2:1 for budget; the notes do not reconcile them, so do not conflate them.)

**4. [SA]** Who were the "Maryland Five" and what is Turbine?
**A:** Five ex-TAO hackers who left in 2008 for autonomy, built VRL in Reston, stayed secret 12 years, acquired by Computer Sciences Corp. in 2010. Turbine: NSA robot for "industrial-scale exploitation," autonomously managing millions of implants; the NSA could man only about 1/8 of its implants by hand.

**5. [Explain]** How did contractors "launder" provenance, and what was the RAND finding?
**A:** VRL bought in shadier markets agencies couldn't touch (hackers in Argentina, Malaysia, Italy, Australia, France, Singapore) and delivered finished tools through "special contract vehicles" (e.g., "$2.9M for computer peripheral equipment"). RAND: average zero-day secret about 7 years, about 25% found within 18 months (earlier studies about 10 months). Ch 24 uses "about a year" for the same study; the notes conflict.

**6. [SA]** What is "we don't sell weapons, we sell information" and what is the Wassenaar situation?
**A:** The industry's self-exemption (exploits as code, speech, math). Wassenaar (1996) is a nonbinding export regime; surveillance tech was added 2012-13 after Perlroth/Citizen Lab reporting, but the US never adopted the changes after EFF, Google and the $1.7B pen-testing industry objected.

**7. [Explain]** What was Eren's "upper-right-quadrant ethic" and why did it fail?
**A:** Cross-reference Amnesty reports and sell only to governments scoring high on democratic norms and press rights. It was individual, unenforceable and erodes as paychecks grow; "there weren't always good answers." Eren quit Immunity in 2009 after a Turkish general demanded personal training.

**8. [SA]** What are "purple" and "black" briefings and Evenden's red flags?
**A:** Purple = memorized defensive cover story for reporters; black = the real offensive job. Red flags: won't tell you the job before you arrive; two folders on day one; lots of money overseas.

**9. [SA]** Trace the Project Raven mission creep.
**A:** Track ISIS, then prove Qatar funds the Muslim Brotherhood, hack Qatar, hack FIFA officials, template spearphish for a UAE dissident journalist (Donaghy, sent; about 400 victims), then the US First Lady's staff (late 2015). The State Department letter was real but dated 2011; data destruction promises weren't kept; contracts moved to Dark Matter with no State cover, and Evenden refused and tipped the FBI.

**10. [Scenario]** A recruiter offers triple pay for an overseas "network defense" role and won't describe the job until you arrive. What do you do?
**A:** Two-folders heuristic: those are the red flags; walk away or demand the real job in writing. Boiling-frog logic: incremental asks produce complicity.

**11. [Scenario]** Your firm wants to "self-regulate" exploit sales with an internal ethics code. Critique using Ch 10-11.
**A:** Self-certified ethics substitute for law and bend to money; the US built demand then declined to regulate supply. NOBUS-style exclusivity thinking fails too. Lacking enforcement, expect capability to flow to the highest bidder.

---

## Section 7 - Ch 12: Dirty Business, and Ch 13: Guns for Hire

**1. [SA]** Who was Desautels and how did he operate?
**A:** Boston broker/Netragard (alias Cyanide, then "Simon Smith"); motto "We Protect You From People Like Us." Sold only to US entities, accepted about 15% of offers via a "sniff test," paid 3x for exclusivity with NDAs backed by implicit threats. His first sale: a $16,000 joke price for an MP3 zero-day.

**2. [SA]** What defines an "ideal state" broker-grade exploit?
**A:** Zero target interaction, about 98.9% reliability, and a "clean fail" (no crash, no alert).

**3. [SA]** Give the pricing ladder and broker cuts.
**A:** Routers/USB low five figures; PDF/Safari/Firefox/Word/Excel; Windows/Exchange remote $100K-$250K; urgent needs $500K-$1M. Broker cut 3% for a quick match up to 60% to source, vet and test.

**4. [Explain]** How did Desautels's ethics collapse?
**A:** Developers threatened to quit unless exclusivity ended; buyers accepted "exclusive for 2-3 months, then nonexclusive"; a trusted US buyer wanted to resell to a "friendly" Italian client; Desautels brokered an Adobe Flash zero-day to Hacking Team. After the July 2015 leak he found it in spyware sold to Sudan, the UAE, Saudi Arabia, Ethiopia; he shut the business. Bushido: "More like Bullshit."

**5. [SA]** What was the Hacking Team breach?
**A:** July 5, 2015, Phineas Fisher dumped 420 GB (contracts, invoices, source code, five years of email). Clients included FBI, DEA, CIA (via an Annapolis front), Sudan ($1M), Saudi Arabia, Egypt, Russia, Morocco, Bahrain, Ethiopia, the 'Stans; near-deals with Belarus and a Bangladeshi death squad; despite CEO Vincenzetti's denials and a "human-rights veto board." It dropped Sudan and Russia only in 2014.

**6. [Explain]** Why can coverage of the trade backfire?
**A:** "Coverage as advertisement": Perlroth's own Hacking Team exposes showed have-not governments what they lacked. The market is a ratchet: exposure expands demand, not shrinks supply (also Comey's admission about FBI-Apple).

**7. [SA]** What made NSO's Pegasus distinctive, and what did it cost?
**A:** Zero-click "over the air stealth installation," room tap (mic + camera), battery-conscious design that waits for WiFi. Pricing: $500K install + $650K for 10 phones; +100 targets $800K; scaling down to +10 for $150K; about double Hacking Team. NSO: founded 2008 by Unit 8200 alumni Hulio and Lavie; controlling stake to Francisco Partners for about $120M (2014).

**8. [Explain]** How did NSO sidestep the crypto wars?
**A:** Hack the endpoint: capture data on the phone before and after encryption, solving "going dark" (FBI's Caproni, 2011) without any backdoor mandate. The pivot to surveillance followed that testimony.

**9. [Explain]** Tell the Mansoor story and its lessons.
**A:** UAE activist Ahmed Mansoor (Egret) received torture-details texts in August 2016, forwarded them to Citizen Lab's Bill Marczak instead of clicking; a chain of three Apple zero-days (Safari) naming "Pegasus" and "NSO" hundreds of times; Lookout helped; Apple patched for about 1 billion users. Sentenced 2018 to 10 years. Reach: 67 servers, 400+ targets, operators in 45+ countries. A target who didn't click plus independent watchdogs is the real detection mechanism.

**10. [Scenario]** A spyware vendor says its "ethics committee" and government approvals ensure only terrorism cases. What do you tell your board?
**A:** Marketing, not safeguards: NSO had never been denied an export license and targets included soda-tax advocates, Aristegui and her 16-year-old son. The AK-47 defense (Mahaffey): you can't control use past the loading dock.

**11. [Scenario]** You are asked to broker one "exception" sale to a friendly European firm. What does Ch 12 warn?
**A:** One middleman defeats "U.S.-only." Do due diligence on the buyer and end use; exclusivity over copyable code is a rental resting on trust. "Nobody in this trade ever seemed to take a stance until it was too late."

---

## Section 8 - Ch 14: Aurora, and Ch 15: Bounty Hunters

**1. [Explain]** What is the Fog of Peace?
**A:** Grosse's inversion of the fog of war: so many benign alarms that a real nation-state attack hides in the noise; bias toward the innocent explanation ("probably another intern") is the vulnerability. Echoes the Pearl Harbor radar blip.

**2. [SA]** Why did China want Google's source code, and what was the scale problem?
**A:** Passwords change but a backdoor in Gmail's source gives permanent access. Verifying about 2 billion lines is Gosler's Sandia problem at planetary scale: "the only certainty was uncertainty."

**3. [SA]** Walk through the Aurora facts.
**A:** Legion Yankee (PLA-linked): IE zero-day hosted in Taiwan, delivered via a "Go Kill Yourself" chat link clicked by Beijing staff; goals included dissidents' Gmail (the Five Poisons: prodemocracy activists, Tibetans, Uighurs, pro-independence Taiwanese, Falun Gong). 250 engineers on campus, Mandiant ("don't wear suits"), "Upchuck Hour." Google confiscated machines, reset all passwords, moved Google.cn to Hong Kong and disclosed Jan 12, 2010, the first US company to name China. Motto "Never again."

**4. [Explain]** What is "name and shame" and what did it buy?
**A:** Breaking the industry norm of silence (the "two kinds of companies" line: those who know they've been hacked by China and those who don't know yet). Adkins: telling the world "ended up being the best recruiting strategy."

**5. [TF]** The notes say Google's principled stand against China lasted permanently.
**A:** False. Within a year execs pushed reentry; later Dragonfly (secret censored search), a Beijing AI lab, Project Maven, etc. Corporate principle has a short memory when the largest market is at stake.

**6. [SA]** What are Moussouris's three hacker motivations and the beta-software trick?
**A:** Compensation, recognition, and "the pursuit of intellectual happiness." Pay for bugs in beta/preview software governments don't yet care about so defense doesn't bid against offense.

**7. [SA]** Give the bounty/market numbers.
**A:** Google: min $500, $1,337 (leet), $31,337, up to $60K for Chrome, $1.5M for a full Android remote jailbreak by 2020. Zerodium: $80K Chrome, $100K Android, $500K iPhone, $1M-$2.5M for zero-click iMessage/WhatsApp. A Chrome bug earns about 3x more on the government market. Facebook $1.5M to 330 researchers by 2013. Microsoft: about $250K in year one; 200K reports a year.

**8. [Explain]** Tell Moussouris's campaign at Microsoft.
**A:** Reports dried up (2011); no budget; two years of data showed worst drop for IE; game theory to avoid perverse incentives; beta IE/Windows scope $500-$100K; one-month pilot June 2013 (timed with the Prism leak; first payout to a Google engineer); permanent program that November.

**9. [SA]** What is HackerOne and Hack the Pentagon?
**A:** Founded 2014 by Alex Rice, Moussouris and the three Dutchmen; $9M from Benchmark. Hack the Pentagon (2016, Ash Carter): 1,400+ hackers, a Synack hacker breached classified networks in under 4 hours, later $34M funded. OPM breach (2015, ~1M+ federal employees' data) spurred action.

**10. [Scenario]** Your small company can't pay market rates for bugs. How do you attract researchers?
**A:** Compete on recognition and openness (public credit, no lawsuits, a working reporting channel) and intellectual challenge; scope to pre-release software; mandate 2FA internally. Avoid the Microsoft "dead disclosure link" ("calling 911 and getting a full voicemail").

**11. [Scenario]** Your SOC sees a flood of benign alerts and one odd blip. Which concept applies?
**A:** Fog of Peace: triage against the innocent-explanation bias, escalate the anomaly (an intern's first instinct nearly buried the fastest attack Google had seen), and adopt "shepherds of their safety" thinking.

---

## Section 9 - Ch 16: Going Dark, and Ch 17: Cyber Gauchos

**1. [Explain]** Distinguish upstream from downstream collection.
**A:** Downstream = Prism-style court orders for customer data from companies. Upstream = tapping undersea cables and hacking data-center links (Muscular) without the companies' knowledge. The Prism slides misleadingly implied direct server access; companies had never heard the name.

**2. [SA]** What was Muscular and what number illustrates it?
**A:** An NSA-GCHQ man-in-the-middle on Google and Yahoo internal links; in one day it grabbed 444,743 Yahoo address books plus Hotmail, Facebook and Gmail data. Google's front-end servers held data unencrypted internally until Snowden.

**3. [Explain]** Why does the smiley face matter?
**A:** The gratuitous "gotcha" emoji converted an ambiguous diagram into a declaration of war. Perceived intent, not just capability, drives the target's response.

**4. [SA]** What is "encrypt the last chink" and what did Google do?
**A:** Encrypt the unencrypted seam between your own systems: Google adopted Perfect Forward Secrecy between data centers and laid its own subsea cable. Grosse: "Signals intercept is totally off the table."

**5. [SA]** Describe Project Zero.
**A:** Launched August 2014 (Lake Tahoe) under Chris Evans with Hawkes, Ormandy, Geohot, Beer, Lokihardt. Attacks the whole ecosystem, publishes bugs after a 90-day vendor deadline, found 1,600+ critical bugs. Break one link in a jailbreak chain and spies are set back months or years. Trade-off: patch-lag exploitation after publication.

**6. [SA]** Give the crypto-war lineage.
**A:** Zimmermann's PGP (1990s), Clinton's Clipper Chip (backed down 1996), Zfone (2011), iPhone 6 full-device encryption (Sept 2014; Apple holds no keys; 10 wrong tries wipes the phone).

**7. [Explain]** Recount San Bernardino and the outcome.
**A:** FBI picked Farook's county-owned, un-backed-up iPhone as a perfect precedent and sought a court order for "Government OS." Cook's 1,100-word letter refused ("the equivalent of cancer"), citing OPM as proof the government can't safeguard a key. A week before trial DOJ dropped the case after buying a zero-day for $1.3M from an American hacker (not Cellebrite). Comey conceded litigation "stimulated a marketplace."

**8. [SA]** What are Argentina's "atado con alambre" and the "depth-erosion thesis"?
**A:** "Held together with wire": scarcity (an "embargo on cool shit") forces reverse-engineering to the metal. US engineers now "skim the surface" and lose kernel/firmware depth; ICPC wins shifted to Russia, Poland, China, Iran; post-Snowden NSA departures.

**9. [Explain]** Evaluate Dan Geer's buy-the-market plan and Arce's quote.
**A:** Geer: outbid everyone 10x, use the bug, patch it. Perlroth, standing in Buenos Aires: too late. Arce: "A guy from the NSA and a guy from Iran show up with big bags of cash. Do you perform an ethical analysis? Or do you weigh the bags?"

**10. [SA]** Who are Cerrudo, Ortega (the Gaucho), and Core Security's founders, and why does Ortega refuse to sell?
**A:** Cerrudo: demoed turning traffic lights on/off from a laptop ("dumb cities were smart, smart cities were dumb"). Core Security: Richarte and Arce (Impact/Implant; NASA a customer; 9/11 erased $1M in contracts). Ortega broke Argentine voting machines in under 20 minutes and refuses from survival: "like being a physicist in the 1930s with the atomic bomb."

**11. [Scenario]** Your CEO wants to ship a lawful-access backdoor "only the good guys can use." Respond with Ch 16.
**A:** A backdoor for one government becomes a target for all and a precedent for Beijing, Moscow and Riyadh; the government that can't protect OPM can't protect the key. Also, endpoint attackers bypass the crypto wars anyway.

**12. [Scenario]** A conference organizer asks whether to let an exploit broker sponsor a hacking con in Latin America. What does Ch 17 say about who is in the room?
**A:** Brokers approach hackers after they burn an exploit onstage, buying the relationship and future work; Zerodium was Platinum Sponsor of Ekoparty. The "sell only to good Western governments" ethic lands as absurd where the US is remembered for Kissinger and the junta.

---

## Section 10 - Ch 18: Perfect Storm

**1. [Explain]** Explain the plagiarized-weapon boomerang.
**A:** Shamoon (August 15, 2012) was essentially copied from the US/Israeli code used months earlier on Iran's oil networks; using a weapon teaches the target to rebuild it. It wiped 30,000 Saudi Aramco computers on the "Night of Power" and left a burning-flag image; it failed to cross into production systems.

**2. [SA]** What are the asymmetric-retaliation numbers?
**A:** For about the cost of three F-35s Iran built a cyber army, budget $76M to $1B+ after Stuxnet.

**3. [Explain]** What is the glass-houses problem?
**A:** The US couldn't demand a ban on hacking government agencies (OPM) because the NSA does it; it could only draw the line at commercial IP theft. A state bans what it doesn't do.

**4. [SA]** Recount Bowman Dam and the lesson.
**A:** Officials nearly retaliated believing Iran was in a 245-foot Oregon dam; it was a 20-foot New York flood-control dam with sluice gates disconnected for maintenance. "The first assessment is almost always wrong."

**5. [SA]** Describe the 2012 infrastructure bill failure and the bank attacks.
**A:** McConnell: "if we were attacked, we would lose." Chamber of Commerce lobbyists turned mandatory standards voluntary; even those were filibustered. Iran's bank DDoS hit BofA, JPMorgan, Citi, NYSE and about four dozen banks with 70+ Gbps against banks' 40 Gbps, the longest-running cyberattack in internet history; DHS was "toothless."

**6. [SA]** Who was Ali Abbasi, and what did the China files show?
**A:** Young Iranian hacker funded by China's 863 program who hacked a power-grid controller onstage in 5 seconds. Perlroth, Barboza, Sanger and Mandiant traced thousands of attacks to PLA Unit 61398's 12-story Shanghai tower; DOJ indicted five soldiers (symbolic).

**7. [SA]** Sands and Sony: what happened?
**A:** Feb 2014: Iran wiped Adelson's casinos ("Don't let your tongue cut your throat"). Dec 2014: North Korea ("Guardians of Peace") wiped about 70% of Sony's computers over The Interview and dumped emails, a playbook for the later election hack.

**8. [Explain]** What did the 2015 deals show?
**A:** The Iran nuclear deal halted destructive attacks; the Xi-Obama commercial-IP agreement brought about a 90% drop in Chinese industrial attacks for about 18 months until Trump's trade war and stealthier attacks. Restraint evaporates when the deal does.

**9. [Scenario]** At 3 a.m. your CISO says "it's definitely Iran." Leadership wants to hit back. What principle applies?
**A:** Verify attribution before retaliating; the first assessment is usually wrong (Bowman). Also glass houses: be sure you could accept the norm you invoke.

**10. [Scenario]** The board wants an aggressive offensive program but defers hardening. Which quote and lesson fit?
**A:** Panetta: "If we are going to be aggressive... we have to be damn well prepared when these attacks come our way." Aggressive offense without hardened defense leaves private firms and citizens holding the bag (DHS could advise but not defend or compensate).

---

## Section 11 - Ch 19: The Grid

**1. [Explain]** How can you tell pre-positioning from espionage?
**A:** Espionage collects intelligence; Russia's Trojanized industrial-control updates reached dams, nuclear plants, pipelines and the grid, "not there to collect intelligence on the price of gas" (Hultquist). Targeting control systems with "die"/"turnoff" commands means attack preparation. Implants in control systems are land mines, not cameras.

**2. [SA]** State the key facts of the December 2015 blackout.
**A:** December 23, 2015: Sandworm (GRU Unit 74455) hijacked SCADA at Prykarpattyaoblenergo and two other utilities; an invisible cursor opened 30 substations' breakers, changed the operator's password, killed emergency phone lines and backup power; 230,000 people lost power for about 6 hours. The message: "We can torch you."

**3. [Explain]** What is the staged-assembly implant?
**A:** BlackEnergy arrived one harmless-looking module at a time across months; only assembled did it become a weapon, defeating signature detection. BlackEnergy began as Cr4sh's $40 DDoS tool; KillDisk wipes and cleans up; targets included GE Cimplicity, Siemens, Advantech.

**4. [SA]** How did Ukraine function as a testing ground?
**A:** Attackers tried different techniques on media companies (Starlight, TRK), a dry run three months before the grid. Starlight's lawyer clicked an Excel file in April (Patient Zero); by October 200 machines were infected. Hultquist told the Pentagon a month before: "they're going to turn off the lights."

**5. [Explain]** Why is the grid attack called MAD for the internet era?
**A:** Russia embedded in the US grid as it moved "little green men" into Crimea, signaling that any US retaliation would be answered in kind. The attack was a message, not permanent damage.

**6. [SA]** Recount DHS's collapse and grid weaknesses.
**A:** In four months of early 2013 DHS's top four cyber officials resigned; NSF scholarship recipients chose NSA over DHS; 198 critical-infrastructure incidents in 2012 (+52%). The grid: local distributors regulated state-by-state, no federal standards, legacy software built "for access, not security." A 2010 bipartisan letter warned of outages "for at least months to two years"; McCain led lobbyist-backed opposition that killed the bill.

**7. [SA]** What are Energetic Bear and "left of boom"?
**A:** CrowdStrike's name for the earlier (2010+) Russian grid campaign: watering-hole and man-in-the-middle attacks on 1,000+ firms in 84 countries. Left of boom: Watters's iSight doctrine of tracking bomb-makers before the attack lands.

**8. [TF]** The notes say Russia never wanted a cyberweapons treaty.
**A:** False. Russia pushed, and was rebuffed on, a cyberweapons treaty after Stuxnet (partly because Kaspersky contests showed how trivially Russian substations fall). The US waved it off as a ploy, an anti-pattern.

**9. [Scenario]** You find malware in your plant's control network that does nothing yet. Management says "no data was stolen, so no harm." Reply.
**A:** Presence signals intent to detonate; treat as red alert. Also expect staged modules, and that the adversary may be rehearsing on you or a softer proxy.

**10. [Scenario]** Your firm's vendor marketing is full of alarmist cyber warnings and staff ignore them. Which concept explains and what is the risk?
**A:** FUD fatigue: two decades of "blood sport" marketing trained people to tune out real warnings, which is itself a vulnerability.

---

## Section 12 - Ch 20: The Russians Are Coming

**1. [Explain]** What is the Vulnerabilities Equities Process and why does it tilt?
**A:** The formal weighing of keeping vs disclosing a zero-day: widespread technology favors disclosure, adversary-only use favors withholding, with periodic review. With vast offense budgets it "always weighs more heavily on hoarding"; "there's blood left on the table" (Daniel).

**2. [SA]** What happened with EternalBlue under the VEP?
**A:** NSA SMB exploit, nicknamed "EternalBluescreen" while being perfected; "not dirty" (minimal logging); "we knew it could be a weapon of mass destruction." Withheld 7 years and never seriously considered for disclosure; Daniel came to regret it.

**3. [TF]** Heartbleed shows open-source code is well-audited because of "many eyeballs."
**A:** False. OpenSSL secured millions of systems but was maintained by one engineer on $2,000 a year. Ubiquity is not security.

**4. [SA]** What was the printout defense?
**A:** The White House cyber emergency plan was literally a printout ("Hour 0... Notify... may take days or weeks"), no real-time attack map.

**5. [SA]** Describe the IRA and its reach.
**A:** Prigozhin's St. Petersburg troll farm; 2014 recon (Krylova, Bogacheva) of nine "purple states"; Heart of Texas vs United Muslims of America (staged real standoffs); Black Lives Matter/"Woke Blacks" voter-suppression pages; reached 126M Facebook users and 288M Twitter impressions.

**6. [Explain]** Explain the DNC/Podesta operation chain.
**A:** Cozy Bear (SVR) and Fancy Bear (GRU) both inside the DNC; Fancy Bear phished Podesta with a fake Google alert, an aide's "This is a legitimate email" typo (for illegitimate) yielding 60,000 emails. Laundered via Guccifer 2.0 (Cyrillic metadata, "Iron Felix," Google-Translate Romanian), DCLeaks and WikiLeaks, timed pre-convention and pre-election.

**7. [Explain]** What was the objective, and what did Russia probe in election infrastructure?
**A:** Chaos and legitimacy, bruising Clinton and doubt over the election, not necessarily a Trump win; disenfranchising voters in blue counties of purple states beats hacking machines. Russia scanned voter rolls in all 50 states, breached Arizona and Illinois, and hacked VR Systems (e-pollbooks).

**8. [SA]** How did the US respond?
**A:** McConnell refused a bipartisan attribution statement; Trump amplified WikiLeaks ("400-pound hacker"); Obama's December sanctions and 35 expelled "diplomats" were "barely a spanking." NYT editors buried the DNC story: "cyberattacks had become the overplayed soundtrack of our lives."

**9. [Scenario]** Your agency debates holding a wormable exploit in widely used software "for operations." Apply the VEP.
**A:** Score prevalence, reliance, severity; widely deployed plus wormable means disclose now. Note the structural hoarding bias and the shared-technology dilemma: "You can no longer cut a hole in something without poking a hole in security for everyone" (Daniel).

**10. [Scenario]** A local election office asks where to spend a small security budget. What do Ch 20 and 24 point to?
**A:** Protect voter-registration data (even if public), keep paper trails, never go online, and prepare for perception attacks on legitimacy, not just vote counts.

---

## Section 13 - Ch 21: The Shadow Brokers, and Ch 22: The Attacks

**1. [Explain]** Why is "capabilities vs descriptions" the key to ranking the Shadow Brokers breach?
**A:** Snowden leaked descriptions; the Shadow Brokers leaked the working exploit code ("the keys to the kingdom"). Losing the weapon is far worse than losing the manual.

**2. [SA]** Give the Shadow Brokers timeline.
**A:** Aug 2016 auction (@shadowbrokerss; Equation Group tools; samples of 300 MB; demand up to 1M Bitcoin); Halloween "Trick or Treat?" decoy-server map; direct sales; "going dark"; April 2017 password reveal and a dump of about 20 exploits including EternalBlue and DoublePulsar. Infections hit 400,000 machines within two weeks.

**3. [SA]** Who were Jake Williams, Hal Martin and Vault7?
**A:** Williams: ex-TAO (2008-2013) outed by the Shadow Brokers with true code words (OddJob, CCI, Q Group); felt his government didn't "have his back." Martin: contractor with 50 TB of stolen data, a hoarder not the leaker. Vault7: separate CIA tool leak (Schulte, mistrial on leak charge).

**4. [Explain]** Why is NOBUS exposed as false by this leak?
**A:** The tools hit bugs anyone could find in Cisco, Fortinet and other firewalls securing American networks, yet were held for years. Cisco zero-days were worth five figures each on the market; the dump caused hundreds of millions in damage.

**5. [SA]** Why is attribution ambiguous (false-flag problem, Kaspersky angle)?
**A:** The mock-Russian broken English read like a native English speaker faking Russian. Israeli intelligence had hacked Kaspersky and showed Kaspersky antivirus pulling Top Secret files; an NSA employee's home PC may have been the vector.

**6. [SA]** Recall WannaCry facts.
**A:** May 12, 2017, North Korea's Lazarus group; 200,000 orgs in 150 countries in 24 hours; about 50 UK hospitals, Renault, Telefonica, FedEx; no working decryption, under $200K collected; a kill switch triggered by 22-year-old Marcus Hutchins for about $11 (later arrested by US feds).

**7. [SA]** Recall NotPetya mechanics and fallout.
**A:** GRU; Constitution Day; M.E.Doc (Linkos Group = Patient Zero) six weeks after the breach; EternalBlue + EternalRomance + MimiKatz. Hit Merck, Maersk, FedEx/TNT, Mondelez, DLA Piper, Reckitt Benckiser, Cadbury Tasmania, Chernobyl monitors, and Russia's Rosneft. $10B+; insurers invoked the war exemption against Merck and Mondelez. (Cheatsheet says Merck + Mondelez >$1B; Prologue says Merck and FedEx about $1B; treat "over $1B for the largest victims" as the safe claim.)

**8. [Explain]** What was the "patch exists is not patched" point and the Toyota-style deflection?
**A:** MS17-010 (March 2017) existed but critical infrastructure runs legacy XP, patches need approval and rare maintenance windows. The US line (Bossert) stressed adversary use, not agency custody. Selective attribution: North Korea named fast; Bossert's NotPetya op-ed blaming Russia was killed.

**9. [Scenario]** A hospital CIO says "a patch is out, so we're covered." What do you say?
**A:** A patch's existence is not protection; legacy and maintenance realities leave exposure for years (WannaCry on XP). Prioritize patch and isolation plans, and MFA.

**10. [Scenario]** You receive a "ransomware" incident where decryption can never work. How do you read it?
**A:** Irreversible encryption signals a wiper in disguise (NotPetya). Read the intent, not the ransom note; escalate as a possible state operation.

**11. [Explain]** What did Brad Smith propose, and what was the irony?
**A:** A Digital Geneva Convention: no peacetime attacks on civilians, hospitals, the grid, elections; no IP theft; mutual response. As he spoke (Nov 9, 2017), Pentagon hackers were planting logic bombs in the Russian grid.

---

## Section 14 - Ch 23: The Backyard

**1. [Explain]** What is the Toyota-truck defense and Microsoft's rebuttal?
**A:** Rogers: if someone welds a bomb to a Toyota and drives into a crowd, is that Toyota's responsibility? Burt: the analogy presupposes exploits have any benefit to society; "It's already a bomb."

**2. [SA]** Why is "Eternal is the perfect name"?
**A:** Leaked exploits remain features of attacks long after patches because towns run legacy software. Allentown, a San Antonio jail and Baltimore ($18M cleanup) were hit; the NSA deflected via wordsmithing (Joyce) and the meaningless "91% disclosed" statistic.

**3. [SA]** What was Legion Amber?
**A:** Chinese contractor group that stole the NSA's exploits off its own systems about a year before the Shadow Brokers leaked them, used them against Five Eyes and to steal nuclear-propulsion technology: another death of NOBUS.

**4. [SA]** Describe the Uighur watering-hole attack.
**A:** 14 iOS zero-days hidden in plain sight for two years (Project Zero's find), plus parallel Android/Tibetan campaigns; capabilities worth $2M+ used broadly. "The Chinese use their best tools against their own people first" (Lewis): Xinjiang is China's test kitchen.

**5. [SA]** Describe the Iran and Gulf escalations.
**A:** After the nuclear-deal withdrawal: 2,700 hits on Trump's 2020 campaign and a Proud Boys voter-intimidation spoof; the US's own Nitro Zeus logic bombs in Iran's grid; escalation after the Suleimani strike. Gulf: Crowdfense outbidding at $3M; Twitter's Saudi-spy engineers; the Bezos WhatsApp hack; Khashoggi.

**6. [Explain]** What is the perception hack and what is pax mafiosa?
**A:** Perception hack: small amplifiable attacks (battleground states) that can be spun as proof the election is "rigged"; damage is confidence. Pax mafiosa: Russian criminals (TrickBot, Evil Corp whose leader "was FSB") treated as national assets in exchange for untouchable status.

**7. [SA]** Describe the 2020 defense.
**A:** Nakasone's "defend forward"; Cyber Command disrupted TrickBot and the IRA; Microsoft's TrickBot legal action; CISA (Krebs, "rumor control"); fast Iran attribution. Election Day was "just another Tuesday on the internet." The gravest interference came from within: "our candidate is chaos."

**8. [SA]** What were the nuclear-plant findings?
**A:** Russia inside Wolf Creek (Kansas) and Cooper (Nebraska) nuclear plants, mapping for a future attack; the Petro Rabigh (Saudi) attack switched off safety locks, the last step before an explosion. "All that's missing is some political motivation" (Chien).

**9. [Scenario]** A city council asks whether to pay a ransomware demand because it's cheaper than rebuilding. Respond with Ch 23.
**A:** Paying funds the criminal ecosystem (anti-pattern); with pax mafiosa the gangs may be state-protected. Invest in patching legacy systems and backups; Baltimore's $18M cleanup shows the cost of neglect.

**10. [Scenario]** A politician claims the upcoming election is "rigged" after a minor hack. Which concept applies?
**A:** The perception hack and "delegitimizing your own election": the most effective interference may come from inside; focus on communicating verified facts (CISA rumor control) and paper trails.

---

## Section 15 - Ch 24: Epilogue

**1. [SA]** What is the internet's "original sin"?
**A:** Built at a biker bar in 1976 (SRI's first internetworked message from a bread truck) with zero thought to security; Dave Retz: "Everything can be intercepted... everything is vulnerable." SRI's radios had bled into SFO's air-traffic radar in 1974.

**2. [Explain]** What is "Move slowly and fix your shit" and "Build it like it's broken"?
**A:** The graffiti rebuttal to "move fast and break things": markets reward first-to-market over secure-to-market. Casey Ellis: assume compromise and compartmentalize crown jewels (Apple's sandboxing).

**3. [SA]** Give the open-source and hardware recommendations.
**A:** 80-90% of modern software is open source; Linux Foundation/Harvard census, bounties, a cybersecurity bill of materials, developer certification ("driver's license for programmers"), MFA for maintainers. CHERI (DARPA/SRI/Cambridge) adds "contamination chambers"; Arm, Microsoft, Google exploring.

**4. [SA]** What is the human-layer advice and numbers?
**A:** 98% of attacks start with phishing; password spraying is "insanely effective"; turn on MFA now; patch promptly (peak exploitation is the day a patch drops); cyber and media literacy in schools.

**5. [SA]** Policy recommendations?
**A:** Reinstate the national cybersecurity coordinator (eliminated 2018); mandate basic critical-infrastructure standards (no expired software, pen tests, no default passwords, MFA, air-gapping); Norway/Japan models; VEP reform (civilian seats such as HHS and Transportation, DHS oversight with IG/PCLOB audits, expiration dates, credit for disclosures like GCHQ's BlueKeep, close NDA loophole, PATCH Act).

**6. [Explain]** Zero-day expiration dates: what's the reasoning and the data conflict?
**A:** Ch 24 says the average zero-day lives about a year (RAND) so withholding deadlines should be shorter; holding EternalBlue 5+ years was indefensible. Ch 10 and the cheatsheet record the RAND average as about 7 years with about 25% found in 18 months (earlier studies about 10 months). The notes do not reconcile these; the recommendation stands either way because even 18 months is short.

**7. [SA]** What does "Spend for the common good" mean?
**A:** As the biggest buyer the US could require exclusive rights and patching from any broker it buys from and refuse vendors who sell to human-rights abusers.

**8. [TF]** The epilogue argues for a full Digital Geneva Convention as the only workable step.
**A:** False. It proposes red lines (hospitals, elections, airplanes, nuclear facilities) even short of a full treaty.

**9. [Scenario]** You are CTO of a regional utility with a flat network and a firewall moat. What does the epilogue say to do?
**A:** Assume compromise: compartmentalize crown jewels, security engineers at design time, replace expired software, no default passwords, MFA, air-gapping, pen tests. "It's nearly impossible to think of a company or agency that has not been hacked."

**10. [Scenario]** A state legislator proposes online voting for convenience. Answer.
**A:** "Lunacy": no online voting platform has survived expert hacking; keep elections offline, protect registration databases, keep paper trails.

---

## FINAL CUMULATIVE EXAM (20 questions)

**1. [SA]** State the book's central thesis in two sentences.
**A:** The US spawned and bankrolls the global zero-day market, built the world's most powerful cyber arsenal, then found it could neither keep its weapons secret nor defend its home front because everyone runs the same technology. Hoarding boomeranged (EternalBlue to WannaCry and NotPetya); the danger is "death by a thousand hacks," not one Cyber Pearl Harbor.

**2. [Explain]** Why do the notes say "access is king; weaponization is the moat"?
**A:** Finding bugs is easy, but reliable, silent, clean-fail exploits are what command premium prices (Ch 4, 10, 12). VRL's push-button tools made turnkey exploits worth multiples of raw bugs.

**3. [Synthesis]** Connect the offense-defense price gap to Moussouris's bounty design and Project Zero.
**A:** Governments pay far more (a Chrome bug about 3x), so defense can't win on money (Ch 3, 5, 15). Bounties compete on recognition and intellectual happiness and scope to beta software; Project Zero raises the cost of zero-days by publishing after 90 days. Both try to put points on the defensive board ("462-452, all offense and no defense").

**4. [Synthesis]** Trace the single chain: Gunman, endpoint attacks, Pegasus.
**A:** Gunman (Ch 6) taught pre-encryption capture; the NSA reused it on Google/Yahoo links (Ch 16); NSO hacked the phone endpoint (Ch 13) and sidestepped the crypto wars. Encryption alone never suffices.

**5. [Synthesis]** How do Stuxnet, Shamoon and Sony illustrate "using a weapon teaches the target to rebuild it"?
**A:** Stuxnet's logic was copied into Shamoon (30,000 Aramco machines), which fed Iran's bank DDoS and the Sands/Sony wiper playbook; publication of Stuxnet and Snowden globalized capability (Ch 9, 17, 18).

**6. [SA]** List the evidence that NOBUS is dead.
**A:** Russia and China honed router-hacking skills from about 2012 (Ch 10); Legion Amber stole the exploits (Ch 23); the Gulf (Crowdfense at $3M) buys equivalents (Ch 23); the Shadow Brokers leaked firewall bugs anyone could have found (Ch 21).

**7. [Scenario]** A cabinet official asks whether to hoard a newly acquired wormable bug for a future operation. Give a Perlroth-style answer using at least three chapters.
**A:** Score prevalence, reliance, severity (Ch 20, 24); EternalBlue was held 7 years and then powered WannaCry/NotPetya (Ch 21-22) and hit Baltimore and Allentown (Ch 23). Stockpiles are a single point of catastrophic failure; set expiration dates and civilian VEP seats.

**8. [SA]** Give five numbers about Stuxnet and NotPetya.
**A:** Stuxnet: 7 zero-days, 500 KB, 164 centrifuges, about 2,000 of 8,700 destroyed, 13-day observation. NotPetya: $10B+, June 2017, 80% of Ukraine's computers wiped (any five).

**9. [Explain]** What is the intravenous principle and which two chapters prove it?
**A:** Every espionage implant is a latent weapon (Ch 8). Proof: Stuxnet moved from reconnaissance to destruction (Ch 9) and Sandworm's implants in control systems (Ch 19).

**10. [Synthesis]** Compare the test-kitchen patterns: Ukraine for Russia and Xinjiang for China.
**A:** Both rehearse on a soft target before the main one (Ch 0, 19, 23). Lewis: the Chinese "use their best tools against their own people first because that's who they're most afraid of."

**11. [TF]** Per the notes, most attacks begin with zero-days. 
**A:** False. 98% start with phishing/credential theft; MFA, long unique passwords and fast patching are highest ROI (Ch 15, 24, cheatsheet).

**12. [Explain]** Why is attribution called spoofable? Give three examples.
**A:** False flags are standard: Shadow Brokers' mock-Russian English, Guccifer 2.0's Google-Translate Romanian, Aurora routed through universities and Tencent/Sina; the Bowman Dam misidentification shows first assessments are usually wrong.

**13. [Synthesis]** Why does exposure fail to shrink the exploit market?
**A:** Hacking Team coverage advertised the capability (Ch 12); FBI-Apple "stimulated a marketplace" (Ch 16); NSO coverage likewise (Ch 13). Exposure inflates demand among have-nots.

**14. [Scenario]** You are a CISO told "our vendor's code is audited, our crypto is strong, our perimeter is hardened." Name three questions from different chapters.
**A:** Where does data exist in the clear (Ch 6)? Can anyone verify a codebase this large (Ch 7, 14)? What if we're already compromised (Ch 24, "build it like it's broken")? Also: is the benign-alert flood hiding the real attack (Fog of Peace)?

**15. [Synthesis]** How does the self-regulation failure appear in Eren, Desautels and NSO?
**A:** Personal codes (upper-right quadrant, Bushido, ethics committees) bend to money and middlemen; one reseller defeats "U.S.-only"; vendors can't claw back tools (Ch 11, 12, 13).

**16. [SA]** What are the "Five Poisons" and who used them to define targets?
**A:** CCP priority targets: prodemocracy activists, Tibetans, Uighurs, pro-independence Taiwanese, Falun Gong. Aurora targeted dissidents' Gmail; Uighurs later hit by 14 iOS zero-days (Ch 14, 23).

**17. [Explain]** Why did the Google principle erode, and why does it matter for a company facing a nation-state?
**A:** Within a year execs pushed reentry into China; later Dragonfly and Maven. Defending against a nation-state requires becoming an intelligence organization (poaching NSA hackers, $100K signing bonuses), and principle has a short memory against the largest market (Ch 14).

**18. [Synthesis]** Compare how the 2016 and 2020 election threats evolved.
**A:** 2016: IRA built fake communities, hack-and-leak via Guccifer/WikiLeaks, 126M Facebook users, voter-roll probing (Ch 20). 2020: amplification of home-grown content ("our candidate is chaos"), the perception hack, defend-forward and CISA defense; the gravest interference from within (Ch 23).

**19. [Scenario]** Design a 6-point national remediation memo based on the epilogue.
**A:** Code (security from inception, funded open source), architecture (sandboxing, CHERI), humans (MFA, fast patching, literacy), elections (offline, paper, protect registration data), policy (coordinator, infrastructure standards, VEP reform with PATCH Act), market (buy with conditions, red lines).

**20. [Explain]** What does the closing line "It wasn't Ukraine. It was us." mean, and what is Perlroth's "left of boom" role for the book?
**A:** The test kitchen was never the endgame; the NSA's leaked arsenal and America's connected, undefended home front were the target and the bill (Prologue, Ch 22-23). The book is her own left-of-boom effort: solve the problem before the explosion (Ch 24).

---
*End of quiz. Score yourself: 18-20 on the final exam means you can apply the book; below 14, re-read the Part 3 key learnings in the companion file.*
