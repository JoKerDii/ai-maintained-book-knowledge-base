# This Is How They Tell Me the World Ends Quiz Book
*This Is How They Tell Me the World Ends* by Nicole Perlroth

**How to use:** Cover the answers, answer from memory (out loud or in writing), then check. Anything you miss is a section to reread. The book has 25 short chapters (Prologue plus Ch 1-24), so they are grouped 2-3 per section, each with short-answer (SA), true/false (T/F), and multiple-choice (MC) questions. A cumulative 10-question final exam is at the end. Questions are built from the study notes on the book, so they reflect that summary, not the book's own wording.

---

## Section 1: Prologue, Ch 1, Ch 2 (Kyiv, Closet of Secrets, The Fucking Salmon)

**Q1 (SA).** Why does Perlroth call Ukraine a "test kitchen," and what does it mean when attacks on Ukraine slow down?
**A:** Russia used Ukraine to rehearse every tool (election malware, disinformation, media trapdoors, then grid attacks), a "cruel version of the scientific method": test a capability, demonstrate it, move on. When attacks slow, "that means they've moved on."

**Q2 (MC).** NotPetya is best described as:
a) a criminal ransomware gang's payday  b) a state weapon of mass destruction wearing ransomware's mask  c) a North Korean attack on Sony  d) a bug in Microsoft's update system
**A:** b. No payment could recover the data. It hit Merck, Pfizer, Maersk, FedEx and even Russia's own Rosneft and Evraz, with $10 billion+ in damage.

**Q3 (SA).** What is the "vulnerability paradox" from the Prologue?
**A:** Ukraine survived partly because it was not fully automated (no Internet of Things, paper ballots counted by hand), while the US plugs in 127 devices a second and has the world's largest attack surface. At the NSA, offense outnumbers defense roughly 100 to 1. Connectivity is the exposure.

**Q4 (T/F).** In Ch 1, Perlroth found that the NSA's main method was cracking encryption algorithms. **A:** False. The algorithms "held up quite nicely." The NSA routed around encryption: a flawed random-number standard, paying RSA to make it the default, chip-factory backdoors planted by the CIA, and hacking Google and Yahoo servers before data was encrypted.

**Q5 (SA).** Define a zero-day and say why exploiting one is "God mode."
**A:** A software or hardware flaw with no existing patch; the vendor has had "zero days" to defend. Exploiting one is like having a spare key to a locked building that works no matter how vigilant the administrator is.

**Q6 (MC).** In Ch 2, the Italian exploit sellers' deflection ("talk about my salmon") became shorthand for:
a) the trade's refusal to say whom it sells to and whom it won't  b) a food-safety scandal  c) Stuxnet's code name  d) a vendor ethics board
**A:** a. In the notes, a non-answer about buyers is the answer, since a seller with limits would state them.

**Q7 (SA).** What is "Langner's mirror argument"?
**A:** Stuxnet used seven zero-days to reach air-gapped centrifuge controllers and wreck roughly a fifth of Iran's centrifuges. The same techniques apply to power, water and chemical plants, and the largest concentration of vulnerable industrial systems is in the United States. A weapon built for one target becomes a template for everyone.

---

## Section 2: Ch 3, Ch 4, Ch 5 (The Cowboy, The First Broker, Zero-Day Charlie)

**Q1 (SA).** How did John Watters start the public zero-day market, and how much did he pay for the company?
**A:** In 2002 he bought bankrupt iDefense for $10 and let two young researchers pay hackers for bugs, the first open bounty program. He sold it to Verisign for $40M in 2005.

**Q2 (SA).** Why did Microsoft's Trustworthy Computing memo make zero-days more valuable?
**A:** Gates's 2002 memo froze products, retrained ~10,000 developers, created a hacker hotline and Patch Tuesday. Microsoft bugs became rarer, so a remote Windows exploit went from pennies to six or seven figures. Scarcity made them expensive.

**Q3 (MC).** Why did iDefense lose out within about three years?
a) hackers stopped finding bugs  b) secret government contractors paid far more for silence (e.g., $150,000 vs. $400)  c) Microsoft sued it  d) Verisign shut it down
**A:** b. Once secret buyers paid more for silence than defenders paid for disclosure, rational hackers hoarded.

**Q4 (SA).** In Ch 4, why does "Jimmy Sabien" say "access is king," and what did agencies actually want to buy?
**A:** Cyberweapons are useless without a way in. Agencies wanted the full stealthy kill chain (entry, beaconing, exfiltration, obfuscation, persistence). A reliable, invisible, persistent exploit, when all three appear together, is "ka-ching."

**Q5 (T/F).** Government agencies in the early market pooled purchases so they never paid twice for the same exploit. **A:** False. Agencies bought the same exploits two, three, four times because nothing is shared and each wants "the win" and the budget that follows.

**Q6 (SA).** What were a hacker's five options for a serious bug (Ch 5), and which one paid?
**A:** (1) Tell the vendor and risk threats or lawsuits; (2) keep and use it; (3) publish for credit and shame; (4) sell to a disclosure broker like iDefense for a few thousand; (5) sell to a government directly or via a broker for far more, with silence and no credit. Only option five paid.

**Q7 (MC).** "No More Free Bugs" (March 2009) is notable because:
a) vendors welcomed it  b) it pushed hackers away from vendors and toward buyers the government men at the back of the room were happy to see  c) it created HackerOne  d) it ended the underground market
**A:** b. Charlie Miller, Dino Dai Zovi and Alexander Sotirov launched it after Google tried to get Miller fired for reporting an Android bug for free. The government men didn't clap: fewer patches, more sellers for them.

---

## Section 3: Ch 6, Ch 7 (Project Gunman, The Godfather)

**Q1 (SA).** What did Project Gunman find, and what lesson did it teach?
**A:** In 1984 the NSA found Soviet magnetometer implants inside the US embassy's IBM Selectric typewriters, capturing keystrokes before encryption touched them. Lesson: encryption alone is never enough; ask where data exists in the clear.

**Q2 (SA).** Give the key numbers of the Selectric implants.
**A:** First implant traced to a 1976 shipment, found in 1984 (eight years undetected); 16 typewriters bugged (13 in Moscow, 3 in Leningrad); Deeley's internal bounty for finding it was $5,000.

**Q3 (T/F).** The Gunman team found the bug quickly because they started with the typewriters. **A:** False. They spent ten weeks on crypto gear because it was the "obvious" leak point; the typewriters were last. This is "searching where you expect the bug, not where it is."

**Q4 (MC).** The Soviets forbade their own staff from typing classified material on electric typewriters. The notes call this:
a) an unrelated policy  b) a tell the Americans ignored: if an adversary protects itself against a vector, assume they weaponized it  c) a Cold War myth  d) proof the typewriters were clean
**A:** b.

**Q5 (SA).** What is Robert Morris Sr.'s complexity confidence threshold, and how does Gosler's Chaperon implant illustrate it?
**A:** Total confidence in 10,000 lines of code or fewer, zero confidence above 100,000. Gosler's Chaperon implant hid undetected in under 3,000 lines. "Even if you found something, you could never be confident you found everything."

**Q6 (SA).** What is "Before Gunman / After Gunman" and the "Willie Sutton principle"?
**A:** BG/AG is Gosler's periodization: before Gunman the US was "in la-la land"; after, it broke into "anything with a pulse." Willie Sutton: go where the data is; passive collection dies when data moves to endpoints.

**Q7 (SA).** What was the SIGINT Enabling Project, and what was Crypto AG?
**A:** SIGINT Enabling: a Snowden-leaked 2013 budget line for covertly influencing commercial product designs so they are exploitable while appearing secure. Crypto AG: a Swiss encryption vendor whose machines were spiked so US decoders could read clients' traffic, the NSA's own "Gunman."

---

## Section 4: Ch 8, Ch 9 (The Omnivore, The Rubicon)

**Q1 (SA).** State the "intravenous principle."
**A:** Once the needle (implant) is in, the same access can replenish fluids or deliver a lethal dose. Reconnaissance implants are latent attack tools; ask what a payload swap would cost.

**Q2 (MC).** By 2013 the NSA's Genie program managed about:
a) 850 implants  b) 8,500 implants  c) 85,000 implants  d) 8.5 million implants
**A:** c. Up four times in five years, targeting routers, switches, firewalls and encryption devices.

**Q3 (SA).** What is the "moral hazard of shared technology"?
**A:** In the Cold War the US and USSR ran different tech. Now everyone runs the same Windows, Oracle, Gmail and iPhones, so weakening a target's stack weakens your own. "There are no patents on vulnerabilities."

**Q4 (SA).** What was Keith Alexander's "third option," and why was Stuxnet designed to look like accidents?
**A:** Between failed diplomacy and airstrikes (World War III), a deniable, gradual cyberattack. The worm accelerated the failure rate centrifuges already had (~10%/yr), so Iranian engineers blamed themselves.

**Q5 (SA).** List what Stuxnet's chain used and what made its targeting precise.
**A:** Seven zero-days (four Microsoft, three Siemens), including a .LNK USB jump, printer-spooler spread, stolen Taiwanese code-signing certs and a Siemens Step 7 default password. It fired only on PLCs controlling clusters of exactly 164 centrifuges at 800-1100 Hz, designed with NSA legal review.

**Q6 (T/F).** Because Stuxnet's payload was tightly targeted, it could not spread beyond Natanz. **A:** False. Precision does not equal containment: the constraint on what it damaged did not constrain where it spread. It escaped in June 2010, and Biden's reaction was "Sonofabitch... they went too far."

**Q7 (SA).** What was Stuxnet's outcome, and what broader precedent did it set?
**A:** About 2,000 of 8,700 centrifuges destroyed by early 2010. Using a novel weapon legitimized it for everyone and lowered the bar for attacking critical infrastructure; Hayden called it "a whiff of August 1945."

---

## Section 5: Ch 10, Ch 11 (The Factory, The Kurd)

**Q1 (SA).** What is NOBUS and when did it collapse?
**A:** "Nobody But Us": patch low-hanging fruit anyone could find, but keep exploits that supposedly only the US can weaponize. It collapsed from ~2012 as Russia and China honed the same router-hacking skills.

**Q2 (SA).** What is the "weaponization gap," and what did VRL sell?
**A:** Finding a bug is a pain, weaponizing it is a bigger pain, and making it 100% reliable is the biggest. VRL (five ex-TAO hackers, "Maryland Five," Reston) sold push-button exploits, using "fuzz farms" so exploits never crashed or tipped off targets.

**Q3 (MC).** Which describes the "contractor laundering layer"?
a) contractors cleaned up leaked code  b) contractors bought in shadier foreign markets agencies couldn't legally touch and delivered finished tools via special contract vehicles with no provenance questions  c) contractors audited the NSA  d) contractors sold only to allies
**A:** b.

**Q4 (SA).** Give three numbers showing the US tilt toward offense in Ch 10.
**A:** NSA breaking-and-entering budget of $652M in 2013, twice its network-defense budget; a new $25.1M zero-day procurement line (~625 zero-days/year); Cyber Command budget from $2.7B to $7B by 2012. RAND: average zero-day secret ~7 years but ~25% found within 18 months.

**Q5 (SA).** What was the Wassenaar Arrangement and what did the US do about it?
**A:** A 1996 nonbinding export-control regime; surveillance tech was added to its control list in 2012-13. The US, uniquely, never adopted the changes into law after objections from EFF, Google and the pen-testing industry.

**Q6 (SA).** What is the "purple briefing / black briefing" (two folders) red flag?
**A:** Contractor tradecraft: a memorized defensive cover story (purple) for outsiders and the real offensive job (black). Evenden's red flags: you aren't told the job before arriving, two folders on day one, and a lot of money overseas.

**Q7 (SA).** Trace the mission creep in Evenden's Project Raven work.
**A:** Track ISIS, then show Qatar funds the Muslim Brotherhood, then hack Qatar, then FIFA officials, then a template spearphish for a UAE dissident journalist (the "template" got sent), then in late 2015 the US First Lady's staff. CyberPoint's fingerprints were on hacks of ~400 people; contracts then moved to the Emirati LLC Dark Matter.

---

## Section 6: Ch 12, Ch 13 (Dirty Business, Guns for Hire)

**Q1 (SA).** What was Desautels' ethical model and why did it fail?
**A:** A reputation-driven broker who sold only to US entities and turned down ~85% of offers on gut instinct ("Bushido"). It failed because ethics don't survive an opaque market: sellers wriggled out of exclusivity, and one middleman defeated "US-only."

**Q2 (SA).** What did the Hacking Team breach (July 5, 2015) reveal?
**A:** Phineas Fisher dumped 420 GB of contracts, source code and email. Hacking Team sold Remote Control System to the FBI, DEA, CIA (via a front) and to Sudan ($1M), Saudi Arabia, Egypt, Russia, Morocco, Bahrain, Ethiopia and others, despite denials and a supposed human-rights veto board. Desautels' Flash zero-day was baked into it; he shut down his zero-day business.

**Q3 (T/F).** Perlroth's exposes of Hacking Team shrank the market by shaming buyers. **A:** False. They showed have-not governments what they were missing: "no intelligence agency on the planet was going to miss out." Sunlight doesn't always disinfect this market.

**Q4 (MC).** An "ideal state" broker-grade exploit needs:
a) a phishing email and a user click  b) zero target interaction, about 98.9% reliability, and a "clean fail"  c) a public CVE number  d) a vendor patch
**A:** b.

**Q5 (SA).** What is "zero-click," and why does it matter for NSO's Pegasus?
**A:** Infection with no target interaction ("over the air stealth installation"). It removes the one defense users had (don't click). Pegasus also detects battery drain, shuts down and waits for WiFi to exfiltrate.

**Q6 (SA).** How was Pegasus first caught in the wild?
**A:** In August 2016 Ahmed Mansoor got suspicious texts and forwarded them to Citizen Lab's Bill Marczak instead of clicking. Marczak found a chain of three Apple zero-days with files naming "Pegasus" and "NSO." Lookout helped; Apple patched for ~1 billion users. Pegasus was traced to 67 servers, 400+ targets, operators in 45+ countries.

**Q7 (SA).** What does the "AK-47 defense" and the Mexico case tell you about vendor ethics committees?
**A:** "When you're selling AK-47s, you can't control how they'll be used once they leave the loading docks." NSO had never been denied an export license; in Mexico Pegasus hit soda-tax advocates, anticorruption activists, lawyers for the 43 disappeared students and journalist Carmen Aristegui and her 16-year-old son. Ethics committees were marketing, not safeguards.

---

## Section 7: Ch 14, Ch 15, Ch 16 (Aurora, Bounty Hunters, Going Dark)

**Q1 (SA).** What is the "Fog of Peace" and how did it matter in Operation Aurora?
**A:** Grosse's inversion of the fog of war: so many benign alarms that a real nation-state attack hides in them, and the bias is toward the innocent explanation ("probably another intern"). At Google, the intern's first instinct nearly buried the fastest attack the company had seen.

**Q2 (SA).** What did China want in Aurora, and what was Google's response?
**A:** Google's source code (permanent access) and dissidents' Gmail accounts (the Five Poisons). Google confiscated machines, reset every password, redirected Google.cn to Hong Kong, and on Jan 12, 2010 became the first US company to publicly name China. Motto: "Never again."

**Q3 (T/F).** Google's stand against China proved lasting: the company never reconsidered the Chinese market. **A:** False. Within a year executives pushed re-entry; later came Dragonfly (secret censored search) and a Beijing AI lab. Principle eroded against market size.

**Q4 (SA).** What are Moussouris' three hacker motivations, and how did Microsoft apply them?
**A:** Compensation, recognition, and "intellectual happiness." If you can't win on money, win on the other two. Microsoft scoped its bounty to beta IE/Windows (June 2013 pilot, permanent that November) so defense didn't bid against government offense.

**Q5 (MC).** Zerodium's published price list included:
a) $80K Chrome, $100K Android, $500K iPhone, up to $1M-$2.5M for zero-click/remote jailbreaks  b) $5 per bug  c) a flat $10,000 rate  d) no published prices
**A:** a. Google's own leet-themed bounties started at $1,337 and reached $1.5M for a full Android remote jailbreak by 2020.

**Q6 (SA).** What was Muscular, and why did the smiley face matter?
**A:** An NSA-GCHQ man-in-the-middle on Google and Yahoo internal data-center links (444,743 Yahoo address books grabbed in one day). A hand-drawn smiley face on the slide turned an ambiguous diagram into a declaration of war; intent, not just capability, escalates.

**Q7 (SA).** Describe the San Bernardino outcome and Project Zero's doctrine.
**A:** The FBI sought an order forcing Apple to write backdoored software; Cook refused ("the equivalent of cancer"). A week before trial the DOJ dropped the case after buying a zero-day for $1.3M. Project Zero (Aug 2014) attacks the whole ecosystem and publishes bugs after a 90-day vendor deadline, trading patch-lag risk for long-term hardening.

---

## Section 8: Ch 17, Ch 18 (Cyber Gauchos, Perfect Storm)

**Q1 (SA).** What does "atado con alambre" explain about Argentine hackers?
**A:** "Held together with wire": MacGyver resourcefulness born of scarcity. The "embargo on cool shit" forces reverse-engineering to the metal, producing deep exploitation skill, while US engineers "skim the surface."

**Q2 (MC).** Ivan Arce's summary of selling to buyers outside the West: "A guy from the NSA and a guy from Iran show up with big bags of cash..."
a) "...you call the police."  b) "...do you perform an ethical analysis? Or do you weigh the bags?"  c) "...you sell to neither."  d) "...you auction publicly."
**A:** b.

**Q3 (SA).** Why do brokers approach a hacker after he burns an exploit onstage?
**A:** They are buying the researcher's relationship and future work "for a rainy day," not the burned exploit.

**Q4 (SA).** Why did Alfredo Ortega, the Cyber Gaucho, refuse to sell?
**A:** Not from morals ("I don't think spying is bad") but survival: "It's like being a physicist in the 1930s with the atomic bomb. You'd get killed."

**Q5 (SA).** What is the plagiarized-weapon boomerang?
**A:** Shamoon (Aug 2012) wiped 30,000 Saudi Aramco computers and was essentially copied from the US/Israeli code used months earlier on Iran's oil networks. Using a cyberweapon teaches the target to rebuild it cheaply.

**Q6 (SA).** What did the Bowman Dam scare teach?
**A:** "The first assessment is almost always wrong." Officials nearly retaliated believing Iran was in a 245-ft Oregon dam; it was a 20-ft New York flood-control dam with its sluice gates disconnected for maintenance.

**Q7 (T/F).** The "glass houses" problem meant the US could demand a ban on all government hacking. **A:** False. The NSA does exactly that, so the US could only draw the line at commercial IP theft (the 2015 Xi-Obama deal, followed by a ~90% drop in Chinese industrial attacks for ~18 months).

---

## Section 9: Ch 19, Ch 20 (The Grid, The Russians Are Coming)

**Q1 (SA).** What is the tell that an intrusion is pre-positioning for attack rather than espionage?
**A:** It targets control systems with "die"/"turnoff" commands. Hultquist: the Russians were "not there to collect intelligence on the price of gas."

**Q2 (SA).** Describe the December 23, 2015 Ukraine blackout.
**A:** Sandworm (GRU Unit 74455) hijacked SCADA, an invisible cursor opened breakers at 30 substations, changed the operator's password, killed emergency phone lines and backup power. 230,000 people were in the dark for about 6 hours: a message, "We can torch you."

**Q3 (MC).** Sandworm's BlackEnergy evolved from:
a) a $40 DDoS tool (Cr4sh)  b) Stuxnet source code  c) a Chinese Aurora payload  d) Hacking Team's toolkit
**A:** a. It was delivered in harmless-looking modules over months, only becoming a weapon once assembled.

**Q4 (SA).** State the VEP and why it tilts toward hoarding.
**A:** The Vulnerabilities Equities Process weighs keeping vs. disclosing a zero-day (widespread technology favors disclosure). With vast offense budgets it "always weighs more heavily on hoarding." EternalBlue was withheld about 7 years, a decision Daniel came to regret.

**Q5 (SA).** What did Heartbleed show?
**A:** That open-source ubiquity is not open-source security: OpenSSL secured millions of systems but was maintained by one engineer on $2,000/year.

**Q6 (SA).** What was the Russian aim in 2016, and how did the IRA operate?
**A:** Not necessarily a Trump win but bruising Clinton and casting doubt on legitimacy. The Internet Research Agency amplified real divisions (Heart of Texas vs. United Muslims of America, "Woke Blacks"), reaching 126M Facebook users and 288M Twitter impressions.

**Q7 (T/F).** Podesta's email theft required a sophisticated zero-day. **A:** False. Fancy Bear phished him with a fake Google password alert; an aide's "legitimate/illegitimate" typo ("This is a legitimate email") helped hand over 60,000 emails.

---

## Section 10: Ch 21, Ch 22 (The Shadow Brokers, The Attacks)

**Q1 (SA).** Why is "capabilities vs. descriptions" the key distinction between Snowden and the Shadow Brokers?
**A:** Snowden leaked descriptions of programs; the Shadow Brokers leaked working exploit code ("the keys to the kingdom"). Losing the weapon is far worse than losing the manual.

**Q2 (SA).** Why did the leak expose NOBUS as false?
**A:** Many exploits hit bugs anyone could find in Cisco, Fortinet and other firewalls securing American networks, yet the NSA held them for years instead of disclosing.

**Q3 (MC).** The NSA tipped Microsoft to patch EternalBlue (MS17-010):
a) years earlier  b) a month before the April 2017 dump, with attribution left blank  c) after WannaCry  d) never
**A:** b. Infections hit 400,000 machines within two weeks of the dump.

**Q4 (SA).** Compare WannaCry and NotPetya.
**A:** WannaCry (May 12, 2017): North Korea's Lazarus group, 200,000+ orgs in 150 countries in 24 hours, ~50 UK hospitals hit, botched (under $200K collected), stopped by an ~$11 kill switch (Marcus Hutchins). NotPetya (June 2017): Russia's GRU wiper, via M.E.Doc supply chain, EternalBlue + EternalRomance + MimiKatz, $10B+ damage.

**Q5 (T/F).** NotPetya was confined to Ukraine because it was delivered through a Ukrainian tax program. **A:** False. "The internet has no borders": any company with even one Ukraine-connected machine was hit (Maersk, Merck, FedEx, Mondelez, Chernobyl's monitors, Russia's Rosneft). Insurers invoked the war exemption.

**Q6 (SA).** What does "patch exists does not equal patched" mean?
**A:** A patch (MS17-010, March 2017) doesn't protect legacy systems: critical infrastructure runs Windows XP, patches need approval and rare maintenance windows, and automated patching is a "no-no."

**Q7 (SA).** What was the U.S. official line after WannaCry, and what did Brad Smith propose?
**A:** Bossert: the tools were ours but we're not responsible for how others use them, while quickly naming North Korea (and a NotPetya op-ed blaming Russia was killed). Smith proposed a "Digital Geneva Convention": no peacetime attacks on civilians, hospitals, the grid or elections, no IP theft, mutual response. Ironically, as he spoke, Pentagon hackers were planting logic bombs in the Russian grid.

---

## Section 11: Ch 23, Ch 24 (The Backyard, Epilogue)

**Q1 (SA).** What does "Eternal is the perfect name" mean?
**A:** A leaked exploit persists wherever patching lags, which is most civic infrastructure. EternalBlue hit Allentown, a San Antonio jail and Baltimore ($18M cleanup) even though it was long patched.

**Q2 (SA).** Explain "NOBUS is dead twice over."
**A:** Adversaries independently steal your tools (Legion Amber, a Chinese group that took the NSA's exploits ~a year before the Shadow Brokers) and buy equivalent capability (the Gulf, e.g., Crowdfense at $3M for iPhone exploits).

**Q3 (MC).** The "perception hack" is:
a) altering vote totals  b) small, amplifiable attacks that erode confidence in election legitimacy  c) a phishing technique  d) a type of ransomware
**A:** b. Cheaper and more corrosive than altering votes; the gravest 2020 interference came from within.

**Q4 (SA).** What did the nuclear-plant intrusions show?
**A:** Russia inside Wolf Creek (Kansas) and Cooper (Nebraska), mapping for a future attack; at Saudi Arabia's Petro Rabigh an attack switched off safety locks, the last step before an explosion.

**Q5 (SA).** What is Perlroth's bottom-line verdict on the "Cyber Pearl Harbor"?
**A:** Not a single unseen event but a decade-long, normalized plague: "death by a thousand hacks."

**Q6 (SA).** Give four elements of the epilogue's remediation plan.
**A:** Examples: "move slowly and fix your shit" and security from inception; "build it like it's broken" (compartmentalize crown jewels, Apple sandboxing); CHERI chip redesign; MFA and fast patching (98% of attacks start with phishing); keep elections offline with paper trails and protect voter rolls; reinstate the cybersecurity coordinator and mandate critical-infrastructure standards.

**Q7 (SA).** How should the VEP be reformed?
**A:** Add civilian agencies (HHS, Transportation); move oversight from NSA to DHS with IG/PCLOB audits; set expiration dates; take credit for disclosures (GCHQ's BlueKeep); close the NDA loophole for purchased zero-days; pass the stalled PATCH Act. Also use US buying power to demand exclusivity plus patching, and set red lines (hospitals, elections, planes, nuclear plants).

---

## Cumulative Final Exam (10 Questions)

**Q1 (SA).** State the book's central thesis in two sentences.
**A:** The US spawned and bankrolls the global zero-day market and built the most powerful cyber arsenal, but because the world runs the same technology it could neither keep those weapons secret nor defend its home front. Hoarding boomeranged (EternalBlue into WannaCry, NotPetya and attacks on US towns, hospitals, the grid and nuclear plants): "It wasn't Ukraine. It was us."

**Q2 (SA).** Why does defense lose the bidding war for bugs, and what is the counter-strategy?
**A:** Governments pay far more to keep holes open than vendors pay to close them (a Chrome bug earns ~3x more on the government market; iPhone jailbreaks reach $2-2.5M). Compete on recognition, openness and intellectual challenge, and scope bounties to beta software (Google, Microsoft, HackerOne, Project Zero).

**Q3 (MC).** Which pair best illustrates "pre-encryption capture / hack the endpoint"?
a) Gunman typewriters and NSO's Pegasus  b) Stuxnet and Shamoon  c) iDefense and Zerodium  d) Aurora and OPM
**A:** a (also Muscular). Encryption is beaten where the data sits in the clear.

**Q4 (SA).** Name three boomerang examples where using or building a weapon came back on the US or its allies.
**A:** Stuxnet escaped and inspired Shamoon (copied code); the Shadow Brokers dump of EternalBlue powered WannaCry and NotPetya; Legion Amber stole NSA exploits; Snowden and Stuxnet were blueprints that globalized capability.

**Q5 (SA).** What is the intravenous principle and which two chapters' stories show it?
**A:** Every espionage implant is a latent weapon since the payload can be swapped from surveillance to destruction. Ch 8 (Genie's ~85,000 implants) and Ch 9 (Stuxnet crossing from espionage to attack); also Ch 19's Sandworm pre-positioning.

**Q6 (T/F).** Vendor ethics boards, export approvals and "no-trace" branding are reliable safeguards in the spyware trade. **A:** False. They are marketing, not safeguards (Hacking Team's veto board, NSO never denied a license). The only question that matters is who the end user is and whom you won't sell to; a non-answer ("the fucking salmon") is the answer.

**Q7 (SA).** Why is attribution risky, and what examples does the book give?
**A:** It is spoofable and the first assessment is usually wrong: Bowman Dam near-retaliation, the Shadow Brokers' mock-Russian English, Guccifer 2.0's Cyrillic metadata and Google-Translate Romanian, NotPetya disguised as ransomware.

**Q8 (MC).** According to the book, what share of attacks start with phishing or stolen credentials rather than zero-days, and what is the top defense?
a) 10%, firewalls  b) 50%, antivirus  c) 98%, multifactor authentication plus long unique passwords and fast patching  d) 98%, air gaps only
**A:** c.

**Q9 (SA).** What do Ukraine (Russia's test kitchen) and Xinjiang (China) have in common, and why does it matter?
**A:** Adversaries rehearse their best tools on a soft proxy (their own people or a neighbor) before turning them on the West: "the Chinese use their best tools against their own people first... Then they turn those tools on us." Watch the testing ground.

**Q10 (SA).** If you were advising the NSA on a newly found wormable bug in a widely used Microsoft protocol, what would the book tell you to do and why?
**A:** Disclose it now. Score prevalence x reliance x severity; wormable plus widely deployed is a disclose-now case. NOBUS is dead (others will find or steal it), holding EternalBlue about 7 years was indefensible by the VEP's own criteria, and a stockpile is a single point of catastrophic failure.
