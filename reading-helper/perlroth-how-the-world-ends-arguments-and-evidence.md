# This Is How They Tell Me the World Ends: Key Arguments, Stories & Evidence by Chapter
*Nicole Perlroth*

Each section covers a chapter or a group of closely related chapters and has: **Argument** (the claim), **Stories & evidence** (what the book uses to support it), **Key numbers**, and **So what** (the lesson). Built from the full text of the chapter files in the `perlroth-how-the-world-ends` skill, so it reflects that summary of the book (journalism reported through about 2020), not the book's own wording. Chapter numbering follows the skill (Prologue = Ch 0).

---

## The Big Arc in One Paragraph
The Prologue and Ch 1-2 open with Ukraine as Russia's test kitchen, the Snowden documents, and the secretive trade that supplies the NSA's tools. Ch 3-5 trace how a public bounty market for zero-days was outbid by secret government buyers. Ch 6-10 show why the NSA turned to offense (Gunman, Gosler, TAO, Stuxnet) and how contractors industrialized weaponization. Ch 11-13 follow the trade as it escaped US control into mercenary and spyware firms. Ch 14-16 describe the tech industry's defensive turn (Aurora, bounties, Project Zero, the crypto wars). Ch 17-20 show the market globalizing and the boomerang beginning: Iran, China, North Korea and Russia learn and strike, from the Ukraine blackout to the 2016 election. Ch 21-23 deliver the payoff: the Shadow Brokers leak EternalBlue, which powers WannaCry and NotPetya and then hits American towns, hospitals and nuclear plants. Ch 24 offers a remediation plan: build as if already broken, fix the human layer, and rebalance policy from hoarding to defense.

---

## Prologue, Ch 1, Ch 2: Kyiv; Closet of Secrets; The Fucking Salmon
**Argument:** The country with the greatest offensive cyber advantage is also the most vulnerable, and its advantage rests on a trade in zero-days that nobody will explain. Ukraine shows what is coming; the Snowden trove shows the NSA wins by going around encryption; the sellers' silence shows the market's structure.

**Stories & evidence**
- **Ukraine as test kitchen:** five years of Russian attacks (2014 election malware, disinformation, grid blackouts in 2015 and 2016) culminating in NotPetya on Constitution Day, June 27, 2017. Ukrainian experts called it a cruel version of the scientific method.
- **Attribution by resources:** the grid attack was routed through Singapore, the Netherlands and Romania and delivered in benign pieces, yet sophistication and no profit motive pointed to a state.
- **NotPetya as disguise:** it mimicked Petya ransomware, but no payment could recover data. It hit Merck, Pfizer, Maersk, FedEx, a Cadbury factory in Tasmania and Russia's own Rosneft and Evraz; Chernobyl's 2,500 computers went dark in seven minutes.
- **Ukraine's armor was backwardness:** no Internet of Things, paper ballots counted by hand; the US built the "world's largest attack surface."
- **The closet (Ch 1):** Perlroth worked the Snowden documents in a windowless Times storage closet in 2013. The NSA lobbied standards bodies for a flawed random-number formula, paid RSA to make it the default, had the CIA plant chip-factory backdoors, and hacked Google and Yahoo servers before encryption.
- **Hints of a market:** references to "commercial partners" implied a gray market of brokers and contractors; Mariner 1 (a missing hyphen destroyed a $150M spacecraft) and a $50 hotel-lock hack illustrate flaws everywhere.
- **The salmon dinner (Ch 2):** at a 2013 industrial-security dinner in Miami, Italian exploit sellers Luigi Auriemma and Donato Ferrante deflected the question of whom they sell to. Ralph Langner, who first attributed Stuxnet to the US and Israel, called them mercenaries.
- **Langner's mirror argument:** Stuxnet used seven zero-days to wreck roughly a fifth of Iran's centrifuges; the same techniques apply to US power, water and chemical plants.

**Key numbers:** NotPetya $10B+ (Merck and FedEx ~$1B each), 80% of Ukraine's computers wiped; 127 devices plugged in per second in the US; NSA offense roughly 100 to 1 over defense; seven zero-days in Stuxnet; seven years to answer the book's questions.

**So what:** Treat a neighbor's blackouts as rehearsal footage for your own. Use profit motive as the first attribution filter. Ask "who else has this, and where did it come from?" rather than "is the NSA spying?" And treat a seller's refusal to name buyers as the answer.

---

## Ch 3-5: The Cowboy; The First Broker; Zero-Day Charlie
**Argument:** The public bounty market (iDefense) and the vendors' hostility to researchers pushed hackers toward secret government buyers, who paid far more for silence. Secrecy is a precondition of a zero-day's value, so the trade resists exposure, and "No More Free Bugs" accelerated the shift.

**Stories & evidence**
- **John Watters and iDefense (Ch 3):** a Texas investor with no computer background bought bankrupt iDefense for $10 in 2002 and let two researchers pay hackers for bugs, the first open bounty program. Early hunters included Tamer Sahin ($75 = a month's rent) and Greg McManus, a New Zealand sheep farmer.
- **Vendor hostility:** Microsoft called disclosure "information anarchy"; Oracle's security chief called bounties immoral.
- **Trustworthy Computing:** Gates's 2002 memo (after Code Red, Melissa, ILOVEYOU, Nimda) froze products, retrained ~10,000 developers, and created Patch Tuesday. Microsoft bugs became scarce, hence valuable.
- **Priced out:** mystery contractors offered $150,000 for bugs iDefense paid $400 for; iDefense's per-bug price rose $400 to $4,000 to $50,000 and still lost. Watters sold to Verisign for $40M (2005) after putting in $7M.
- **Jimmy Sabien (Ch 4):** a pseudonymous Beltway broker explains access is king, agencies want the full kill chain, firmware persistence survives wipes, and agencies bought the same exploit two to four times (he once told four agencies to go to lunch together). The Grugq's Forbes interview posing with a bag of cash halved his business.
- **Cash-and-trust market:** hotel-room demos, Israeli middlemen with $500K in cash, Western Union; Watters's verdict was dark markets are inefficient and prices only climb.
- **Charlie Miller (Ch 5):** ex-NSA analyst sold a Linux zero-day for $50,000 after an $80,000 ask was accepted "too quickly" elsewhere and the exploit failed on the target variant. He defied four NSA officials who flew to St. Louis, and published the first public account of the government's prices ("The Legitimate Vulnerability Market," Carnegie Mellon talk with a redacted $50,000 check).
- **No More Free Bugs (March 2009):** after Google BCC'd Miller's boss over a free Android exploit, Miller, Dino Dai Zovi and Alexander Sotirov told hackers to stop reporting for free. The government men at the back did not clap: fewer patches, more sellers for them.

**Key numbers:** $10 purchase; $40M sale; $75 early bounty; $400 / $150,000 gap; ~$1M for ten exploits and ~$50K for a Windows bug in the mid-1990s; post-9/11 cyber spending up 50%+ in five years; over a hundred contractors, "probably only a dozen that know what they're doing"; $50,000 Linux exploit; prices cited 2006-07 ranged $60-250K.

**So what:** Whoever pays most for a bug decides whether it gets fixed. Punishing researchers is a subsidy to the underground. Government markets are cash-based, trust-based and inefficient, which drives prices up and leaves buyers unable to guarantee exclusivity.

---

## Ch 6-7: Project Gunman; The Godfather
**Argument:** The NSA's zero-day appetite is a reaction to a 1984 shock: an adversary can capture data before encryption touches it, and beyond a few thousand lines of code no one can guarantee a system is clean. That drove the pivot from passive interception to "hacking the endpoints."

**Stories & evidence**
- **Gunman (Ch 6):** Reagan-approved 1984 operation (Walter Deeley) to replace every piece of electrical equipment at the Moscow embassy and examine the old gear at Fort Meade. The NSA tagged 250 replacement typewriters, shipped under armed escort; the Soviets "coincidentally" disabled the elevator so ten tons went up by hand.
- **The search:** ten weeks on crypto gear and fax/teletypes found nothing. On July 23, 1984 one analyst noticed an extra coil in a Selectric power switch; X-ray revealed a magnetometer implant that converted keystroke mechanics into magnetic disturbances and radio-burst data.
- **Warning signs ignored:** an antenna in the embassy chimney; Soviets forbade their own staff from using electric typewriters for classified work.
- **Gosler (Ch 7):** Sandia scientist, founding director of the CIA's Clandestine Information Technology Office (1996). Chaperon studies (1985): subverters vs. evaluators; his implants (one used Zork text to leak secret variables) were never found by evaluators; in Chaperon 2 only Gosler found the new implant among ~100 engineers.
- **Complexity threshold:** Morris Sr. (1987) said total confidence at 10,000 lines or fewer, none above 100,000. Linux grew from 176K to 15M lines, F-35 8M, Vista 50M.
- **Historical warnings:** Thompson's "Reflections on Trusting Trust" (1984), Ware (1967) and Anderson (1972) reports.
- **Crypto AG and SIGINT Enabling:** vendors spiked or influenced so the US could read traffic; "complete enabling" of two VPN chip makers.
- **Adversary tiers I-VI:** V-VI spend years and billions inserting zero-days into the global supply chain.

**Key numbers:** 1976 first implant, found 1984 (eight years); 16 bugged typewriters (13 Moscow, 3 Leningrad); $5,000 bounty; 250 typewriters; Gosler implant under 3,000 lines; Sandia funding $500K (1990) to $50M (1995).

**So what:** Ask where data exists in the clear. Read an adversary's defensive habits as intelligence about their offense. Verification does not scale with code size, so design assuming implants exist, and red-team your own detection by planting implants and measuring whether evaluators find them. Every capability the US built to exploit endpoints can be built to exploit ours.

---

## Ch 8-9: The Omnivore; The Rubicon
**Argument:** After 9/11 the NSA industrialized hacking into near-indiscriminate global collection, creating a moral hazard (backdoors in shared technology are backdoors into America), and then Stuxnet crossed from espionage to physical destruction, proving a weapon built from zero-days cannot be kept in the box.

**Stories & evidence**
- **TAO and the ROC:** jeans-and-T-shirt hackers on 24/7 shifts at Fort Meade; recruits arrived by unmarked bus with red "uncleared" badges; ~$40K starting salary.
- **Genie and the assembly line:** ~85,000 implants by 2013; units for finding bugs, honing implants, reaching hard targets, and "fourth-party collection" piggybacking on others' hacks.
- **Operation Shotgiant:** NSA penetration of Huawei's HQ from 2007, used to reach Huawei's customers.
- **Weak controls:** a dozen LOVEINT cases were demoted, none prosecuted; FISA court approved 1,748 of 1,789 applications unchanged (2012); the 2008 Russian-seeded USB incident led the Pentagon to superglue USB ports.
- **Stuxnet (Ch 9):** Keith Alexander's "third option" for Bush. Joint operation Olympic Games (NSA, Unit 8200, CIA, Mossad, energy labs). The worm crossed the air gap via a human with a thumb drive, spread through a chain of seven zero-days with stolen Taiwanese certs, used Step 7's default password, and fired only on 164-centrifuge clusters.
- **The replay trick:** like looping security footage, it fed monitors normal readings for 13 days, then spun rotors to 1400 Hz and down to 2 Hz on a 27-day cycle.
- **Escape and exposure:** left Natanz in June 2010 (leading theory: an Israeli-added spreading mechanism; Biden: "Sonofabitch... they went too far"). Kaspersky, Symantec, Microsoft and Langner reverse-engineered it; Langner's TED talk named the US.
- **Hayden's frame:** "a whiff of August 1945."

**Key numbers:** ~85,000 implants (4x in five years, 3/4 in Iran, Russia, China, North Korea); 1,748 of 1,789 FISA approvals; 500 KB worm, 50x larger than anything seen, 100x the Apollo 11 code; ~2,000 of 8,700 centrifuges destroyed; ~10%/yr baseline failure; 164 centrifuges, 800-1100 Hz; declassification set for 2039.

**So what:** Every surveillance implant is an attack capability with a deferred payload. Depth (kernel, firmware) beats breadth. When you and your adversary run the same technology, every secret exploit is a liability you carry for them. Precision does not equal containment; using a novel weapon legitimizes it for everyone.

---

## Ch 10-11: The Factory; The Kurd
**Argument:** Offense-over-defense spending and contractor laundering created a private weaponization industry; then the trade escaped American control, as US-trained talent flowed to repressive governments and the US declined to regulate exports.

**Stories & evidence**
- **NOBUS:** keep exploits supposedly only the US can weaponize (Hayden's "four acres of supercomputers" test); collapsed from ~2012 as Russia and China caught up.
- **VRL (Ch 10):** five ex-TAO "Maryland Five" left in 2008 for autonomy, built Vulnerability Research Labs in Reston, kept secret 12 years; acquired by Computer Sciences Corp. in 2010. They commissioned foreign hackers (Argentina, Malaysia, Italy, Australia, France, Singapore), weaponized in fuzz farms, and delivered via "special contract vehicles." Perlroth's reporting hit walls (contracts booked as "$2.9M for computer peripheral equipment").
- **Turbine and the Spiegel catalog:** Turbine to manage millions of implants autonomously; catalog items such as Surlyspawn (keystrokes off air-gapped machines, the digital Gunman).
- **Burn economics:** multimillion-dollar zero-days are "virtually never deployed in anger."
- **Sinan Eren (Ch 11):** Kurdish hacktivist, Immunity Inc.'s second employee (founder Dave Aitel, whose refusal to name customers is another "fucking salmon"). He quit in 2009 after a Turkish general demanded personal training; his homemade ethic (cross-reference Amnesty reports, sell only to high-scoring governments) was individual and unenforceable.
- **Wassenaar:** surveillance tech added in 2012-13; US never adopted it.
- **Project Raven (Ch 11):** David Evenden went to Abu Dhabi in 2014 for 2-4x salary; the two folders (purple vs. black briefing); mission creep from ISIS to Qatar, FIFA, a London journalist (the Rori Donaghy email), and the US First Lady's staff in late 2015. He refused to move to Dark Matter and tipped the FBI.

**Key numbers:** $652M offense (2x defense) in 2013; $25.1M zero-day line (~625 zero-days/yr); Cyber Command $2.7B to $7B, staff 900 to 14,000; RAND: ~7-year average secrecy, ~25% found in 18 months; $1.7B pen-testing industry; ~400 victims of CyberPoint hacks; Wassenaar 1996.

**So what:** NOBUS is a wasting asset. The valuable work is reliable weaponization. Contractors let agencies buy where they legally can't, removing accountability. Self-regulation doesn't hold; offensive contracts drift from terrorists to whoever the client dictates. Two folders and a hidden job description are red flags.

---

## Ch 12-13: Dirty Business; Guns for Hire
**Argument:** In an opaque market, personal ethics and vendor ethics committees cannot survive money and middlemen. Spyware makers hand nation-state phone surveillance to any government with a seven-figure budget, and abuse follows.

**Stories & evidence**
- **Adriel Desautels (Ch 12):** Boston broker (Netragard; motto "We Protect You From People Like Us"). Origin sale: a $16,000 joke price for an MP3 zero-day. He accepted ~15% of offers, enforced exclusivity with 3x pay and NDAs, and cited "Bushido." Exclusivity eroded to "2-3 months, then non-exclusive."
- **The collapse:** his Adobe Flash zero-day went to Hacking Team via a trusted US buyer's "friendly" Italian client. On July 5, 2015 Phineas Fisher dumped 420 GB; Desautels found his exploit in spyware sold to Sudan, UAE, Saudi Arabia, Ethiopia and others and shut down his zero-day business.
- **Hacking Team:** customers included the FBI, DEA, CIA (via a front), Sudan ($1M), Saudi Arabia, Egypt, Russia, Morocco, Bahrain; it dropped Sudan and Russia only in 2014. Coverage of its abuses served as an advertisement to have-not governments.
- **NSO and Pegasus (Ch 13):** founded 2008 by Unit 8200 alumni Shalev Hulio and Omri Lavie; pivoted to surveillance after the FBI's 2011 "going dark" testimony; Francisco Partners bought control for ~$120M (2014). Zero-click, "room tap," and battery-conscious design.
- **Ahmed Mansoor:** the "million-dollar dissident," hit by Hacking Team, Gamma, then a three-zero-day Safari Pegasus chain; he forwarded the texts to Citizen Lab instead of clicking. Sentenced in 2018 to 10 years.
- **Mexico:** soda-tax advocates, anticorruption activists, lawyers for the 43 disappeared students, journalist Carmen Aristegui and her 16-year-old son; lures escalated to "your daughter was in an accident."

**Key numbers:** ~98.9% reliability and "clean fail"; Windows/Exchange remote $100K-$250K, urgent $500K-$1M; broker cut 3%-60%; 420 GB leak; Pegasus $500K install + $650K for 10 phones; ~1 billion users patched; 67 servers, 400+ targets, 45+ countries.

**So what:** Weaponized exploits are defined by silence (zero interaction, near-perfect reliability, clean failure). Exclusivity over copyable code is trust, not control. Do due diligence on the buyer; "we only sell to friendlies" dies at the first middleman. Once spyware ships, abuse is a matter of when. Independent watchdogs and a target who doesn't click are the real detection.

---

## Ch 14-16: Aurora; Bounty Hunters; Going Dark
**Argument:** Aurora and Snowden pushed the tech industry, not the government, to the front line of defense. Google named China, bounties and Project Zero tried to drain the exploit supply, and Silicon Valley turned on the NSA over Muscular and the FBI's backdoor demand.

**Stories & evidence**
- **Aurora (Ch 14):** China's 2009 breach (Legion Yankee) of Google via an IE zero-day on a Taiwan server delivered by a "Go Kill Yourself" chat link to Beijing staff. The goals were source code and dissidents' Gmail (the Five Poisons). The intern's "probably another intern" reflex nearly buried it; the Fog of Peace.
- **Response:** Adkins, Grosse, Marquis-Boire, Brin, and Mandiant; "Upchuck Hour"; 250 engineers sleeping on campus; machines confiscated, passwords reset, Google.cn redirected to Hong Kong, public naming on Jan 12, 2010. "Never again," then Dragonfly within a year.
- **Bounties (Ch 15):** Google's leet bounties ($1,337, $31,337), Facebook's no-cap approach, Microsoft's beta bounty through Moussouris' two-year data campaign (June 2013 pilot, first payout to a Google engineer, permanent in November). HackerOne (2014, Rice, Moussouris, the Three Dutchmen, $9M from Benchmark). Zerodium's price list from Chaouki Bekrar after Vupen lost its export license.
- **Pentagon and OPM:** Hack the Pentagon (2016, 1,400+ hackers; a Synack hacker breached classified networks in under 4 hours); the OPM breach (~1M+ federal employees' data, fingerprints) spurred action.
- **Muscular (Ch 16):** NSA-GCHQ interception of Google and Yahoo data-center links, with a smiley face on the slide; Google encrypted internal links.
- **Project Zero (Aug 2014):** Chris Evans's team found 1,600+ critical bugs; 90-day disclosure; Ian Beer neutered iOS exploits used against Uighurs.
- **Crypto wars:** PGP, Clipper Chip (1996), iPhone 6 encryption (2014), San Bernardino. Cook's refusal; the FBI paid $1.3M to an American hacker for a zero-day and dropped the case.

**Key numbers:** 2 billion lines of Google code (estimated); $100K no-questions signing bonuses; Google bounties $500 minimum, $1.5M for Android jailbreak by 2020; Zerodium $80K Chrome / $100K Android / $500K iPhone / $1M-$2.5M zero-click; Microsoft ~$250K bounty year one, 200K reports/year; 444,743 Yahoo address books in a day; $1.3M for the iPhone zero-day.

**So what:** You can't outbid governments; win on recognition, openness and intellectual challenge, and scope bounties to beta software. Name-and-shame deters silence and recruits talent. Covert interception damages trust more than compelled access. A backdoor for the good guys is a target for everyone. Principle erodes against market size.

---

## Ch 17-18: Cyber Gauchos; Perfect Storm
**Argument:** The market is now global and self-sustaining, and US offense taught every adversary: Iran, China and North Korea each learned and struck back where America was undefended.

**Stories & evidence**
- **Argentina (Ch 17):** "atado con alambre"; Cesar Cerrudo turning traffic lights on and off; Ekoparty with Zerodium as Platinum Sponsor; Core Security's Gera Richarte and Ivan Arce; Alfredo Ortega (the Cyber Gaucho) broke voting machines in under 20 minutes and refused to sell out of survival instinct.
- **Brokers and relationships:** Juliano Rizzo demoed a six-figure exploit onstage and foreign brokers swarmed afterward for his next one; a Gulf-state buyer closed a deal in a Palermo club.
- **Failed fix:** Dan Geer's buy-the-market idea (outbid everyone 10x, patch) was too late. Arce: "Do you perform an ethical analysis? Or do you weigh the bags?"
- **Flipped moral map:** older hackers lived through the Dirty War (30,000 desaparecidos); to Argentines the US looks different than "good Western governments."
- **Shamoon (Ch 18):** Aug 15, 2012, Iran wiped 30,000 Saudi Aramco computers, copied from US/Israeli code, then bank DDoS (BofA, JPMorgan, Citi, NYSE) with 70+ Gbps vs. banks' 40.
- **Failed infrastructure bill (2012):** McConnell: "if we were attacked, we would lose."
- **Bowman Dam (Aug 2013):** officials nearly retaliated against the wrong dam.
- **PLA Unit 61398:** traced by Mandiant and the NYT to a Shanghai tower; DOJ indicted five soldiers.
- **Sands (Feb 2014) and Sony (Dec 2014):** Iran and North Korea wiper-plus-doxxing playbooks, a model for 2016.
- **2015 deals:** Iran nuclear deal and Xi-Obama IP-theft agreement paused attacks.

**Key numbers:** Iran's cyber budget $76M to $1B+; the cost of ~3 F-35s; ~90% drop in Chinese industrial attacks for ~18 months; Sony: 70% of computers wiped; Aramco 30,000 computers; Bowman: 245-ft Oregon dam vs. 20-ft New York dam; Ali Abbasi hacked a grid controller onstage in 5 seconds.

**So what:** Sell-only-to-good-governments is a Western assumption. Stuxnet and Snowden were blueprints; deterrence fails because barriers are low and capability is buyable. Deploying a cyberweapon is free R&D for the target. Glass houses limit which norms the US can demand. Verify attribution before retaliating. Offense without hardened defense leaves the private sector holding the bag.

---

## Ch 19-20: The Grid; The Russians Are Coming
**Argument:** Russia pre-positioned in critical infrastructure and demonstrated it could turn off the lights; at home the US defense posture was thin and the VEP tilted toward hoarding while Russia ran an election-interference campaign built on America's own divisions.

**Stories & evidence**
- **Sandworm (Ch 19):** GRU Unit 74455, named by iSight's John Hultquist for Dune references. BlackEnergy began as a $40 DDoS tool; delivered in staged modules; KillDisk cleaned up. Targeted GE Cimplicity, Siemens and Advantech software.
- **Rehearsal in media companies:** Starlight and TRK; Starlight's lawyer clicked an Excel file in April and 200 machines were infected by October.
- **The December 23, 2015 blackout:** invisible cursor opened breakers at 30 substations; 230,000 without power for ~6 hours. Hultquist had told the Pentagon a month earlier, "they're going to turn off the lights."
- **Defensive collapse:** DHS's top four cyber officials resigned in four months of early 2013; a 2010 bipartisan letter warned of outages "for at least months to two years"; the grid bill was killed. Two decades of FUD trained people to tune out.
- **Printout defense and VEP (Ch 20):** the White House emergency plan was literally a printout; EternalBlue ("not dirty," WMD-class) was withheld about 7 years; Heartbleed's OpenSSL ran on one engineer on $2,000/year.
- **2016 interference:** IRA (Prigozhin; Heart of Texas vs. United Muslims of America staged standoffs; "Woke Blacks"); Fancy Bear phished Podesta (60,000 emails); Guccifer 2.0, DCLeaks and WikiLeaks laundered the loot; voter rolls probed in all 50 states, Arizona and Illinois breached, VR Systems hacked.
- **Response failure:** McConnell refused a bipartisan attribution statement; Obama's sanctions and 35 expelled diplomats were "barely a spanking"; NYT editors buried the DNC story.

**Key numbers:** 230,000 people, 30 substations, 6 hours; 198 critical-infrastructure incidents in 2012 (+52%); 1,000+ firms in 84 countries (Energetic Bear); EternalBlue 7 years; 126M Facebook users and 288M Twitter impressions; 60,000 Podesta emails.

**So what:** Control-system implants with "die/turnoff" targeting are land mines, not cameras. Adversaries rehearse on soft proxies. The VEP is structurally biased toward hoarding. Information warfare amplifies real divisions and aims at legitimacy and turnout. Partisan paralysis and symbolic sanctions don't deter.

---

## Ch 21-22: The Shadow Brokers; The Attacks
**Argument:** The nightmare of hoarding came true: someone stole the NSA's arsenal and dumped it, and within weeks EternalBlue powered two of history's most destructive attacks. Washington deflected responsibility.

**Stories & evidence**
- **The Shadow Brokers (Ch 21):** Aug 2016 auction of "Equation Group" tools (Kaspersky's name for TAO); 300 MB samples; Halloween "Trick or Treat?" dump; April 2017 password reveal and ~20 exploits including EternalBlue and DoublePulsar.
- **Jake Williams:** ex-TAO, recognized the tools as authentic and was outed with real NSA code words; felt his government didn't have his back.
- **Wrong suspects:** Hal Martin (a hoarder with 50 TB, not the leaker); Vault7 (CIA, Joshua Schulte) was separate; Israel showed the US that Kaspersky was pulling Top Secret files, "spies hacking spies hacking spies."
- **NOBUS exposed:** exploits hit Cisco and Fortinet firewalls anyone could have found. The NSA quietly tipped Microsoft a month before the dump (MS17-010, attribution blank).
- **False flags:** the mock-Russian broken English read like a native English speaker faking it.
- **WannaCry (Ch 22):** May 12, 2017, North Korea's Lazarus group; ~50 UK hospitals, Renault, Telefonica, FedEx; no working decryption; Marcus Hutchins triggered an ~$11 kill switch and was later arrested.
- **NotPetya:** GRU via Linkos Group's M.E.Doc ("Ukraine's TurboTax"), six weeks after breaching Linkos; EternalBlue + EternalRomance + MimiKatz; Maersk, Merck, FedEx/TNT, Mondelez, DLA Piper, Reckitt Benckiser, Cadbury Tasmania, Chernobyl, and Russia's Rosneft. Insurers invoked the war exemption.
- **Accountability dodge:** Bossert deflected on lost tools; a Bossert NotPetya op-ed blaming Russia was killed to avoid angering Putin. Brad Smith's "Digital Geneva Convention" speech (Nov 9, 2017), while Pentagon hackers planted logic bombs in the Russian grid.

**Key numbers:** up to 1M Bitcoin demanded; ~20 exploits in the final dump; 400,000 infections in two weeks; WannaCry 200,000+ orgs, 150 countries, 24 hours, under $200K collected, ~$11 kill switch; NotPetya $10B+; Hal Martin 50 TB.

**So what:** Losing working code is far worse than losing descriptions. A stockpile is a single point of catastrophic failure. A wormable leak arms every future attacker. Irreversible "ransomware" is a wiper in disguise. A patch existing is not protection. Accountability dodges and selective attribution undermine deterrence.

---

## Ch 23-24: The Backyard; Epilogue
**Argument:** The boomerang reached American towns, hospitals and nuclear plants, producing not a Cyber Pearl Harbor but "death by a thousand hacks." The remedy is to build assuming compromise, fix the human layer and foundations, and rebalance policy from offense to defense.

**Stories & evidence**
- **Eternal EternalBlue (Ch 23):** Allentown, a San Antonio jail and Baltimore ($18M). The NSA deflected with Rogers's Toyota-truck analogy (Microsoft's Burt: "It's already a bomb") and the "91% disclosed" statistic, meaningless without denominators.
- **NOBUS dead twice:** Legion Amber stole the NSA's tools about a year before the Shadow Brokers and used them against Five Eyes and for nuclear-propulsion tech; the Gulf (Crowdfense, $3M iPhone exploits; the Bezos WhatsApp hack; Khashoggi).
- **China:** a two-year Uighur watering-hole attack using 14 iOS zero-days (Project Zero's find); "best tools against their own people first."
- **Iran and Nitro Zeus:** US logic bombs in Iran's grid; 2,700 hits on Trump's 2020 campaign; escalation after the Suleimani strike.
- **Russia:** pax mafiosa (TrickBot, Evil Corp); inside Wolf Creek and Cooper nuclear plants; Petro Rabigh safety-lock attack ("All that's missing is some political motivation").
- **2020 election:** CISA's Krebs, Cyber Command's TrickBot/IRA takedowns, Microsoft's legal action, and Nakasone's "defend forward"; Election Day was "just another Tuesday on the internet," but the perception hack came from within.
- **Epilogue:** the internet built at a biker bar in 1976 (Dave Retz: "Everything is vulnerable"). Remedies: "move slowly and fix your shit," security from inception, "build it like it's broken" (Casey Ellis), CHERI, MFA, open-source census/bill of materials, offline elections, reinstating the cyber coordinator, VEP reform, red lines.

**Key numbers:** $18M Baltimore; 14 iOS zero-days over two years; $3M Crowdfense; 2,700 attacks on the 2020 campaign; 98% of attacks begin with phishing; 80-90% of modern software is open source; Windows zero-day ~$1M; 2018 elimination of the cyber coordinator.

**So what:** A leaked exploit persists wherever patching lags. Attacks on confidence are cheaper than attacks on votes. Paying ransoms funds the threat. Coordinated action (CISA, Cyber Command, companies) can blunt interference. Expiration dates, civilian VEP seats, DHS oversight, and using US buying power for patching terms are the policy fixes.

---

## Recurring Stories Across the Book
- **Stuxnet:** the espionage-to-attack line (Ch 2, 9), the blueprint (Ch 17), the plagiarized Shamoon (Ch 18), the lesson ignored at NotPetya (Ch 22).
- **EternalBlue:** hoarded ~7 years (Ch 20), dumped by the Shadow Brokers (Ch 21), WannaCry and NotPetya (Ch 22), Allentown and Baltimore (Ch 23).
- **Ukraine as test kitchen:** Prologue, the 2015 blackout (Ch 19), NotPetya (Ch 22); echoed by Xinjiang (Ch 23).
- **"The fucking salmon":** the Italians (Ch 2), Aitel (Ch 11), vendors' vagueness at NSO (Ch 13).
- **Gunman as origin story:** the NSA's pivot to offense (Ch 6-7), pre-encryption capture reappears in Muscular (Ch 16) and Pegasus (Ch 13); Aurora as Silicon Valley's Gunman (Ch 15).
- **Gosler's complexity problem:** reappears at Google scale (Ch 14) and in the open-source argument (Ch 20, 24).
- **Hacking Team and CyberPoint/Mansoor:** the same slide from "friendly" to abusive (Ch 11-13).
- **The 2016 playbook:** Sony as model (Ch 18), the IRA and Fancy Bear (Ch 20), the perception hack (Ch 23).
- **Moussouris and bounties:** the incentive model to scale (Ch 15, 24).
- **Heartbleed:** open-source security theater (Ch 20, 24).
- **Ralph Langner:** Cassandra of PLC sabotage and the first to name the US (Ch 2, 9).
