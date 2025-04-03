import os
from report import run_generation
import pandas as pd

# Reading the Excel file
sheet = pd.read_csv('RocketAnnual.csv')
sheet2 = pd.read_csv('ROEROA.csv')

earningcall= """
Rocket Lab USA, Inc. (NASDAQ:RKLB) Q3 2024 Earnings Conference Call November 12, 2024 5:00 PM ET

Company Participants

Murielle Baker - Senior Communications Manager
Peter Beck - Founder & CEO
Adam Spice - CFO

Conference Call Participants

Andres Sheppard - Cantor Fitzgerald
Edison Yu - Deutsche Bank
Matt Akers - Wells Fargo
Erik Rasmussen - Stifel
Suji Desilva - ROTH Capital
Andre Madrid - BTIG
Jason Gursky - Citi
Michael Leshock - KeyBanc Capital
Anthony Valentini - Goldman Sachs
Cai von Rumohr - TD Cowen

Operator

Thank you for standing by. My name is Bailey and I will be your conference operator today. At this time, I would like to Welcome everyone to the Rocket Lab Third Quarter 2024 Fiscal Results Update and Conference Call.

All lines have been placed on mute to prevent any background noise. After the speakers' remarks, there will be a question-and-answer session. [Operator Instructions]

I would now like to turn the call over to Mariel Baker, Senior Communications Manager at Rocket Lab. You may begin.

Murielle Baker

Thank you. Hello and welcome to today's conference call to discuss Rocket Lab’s Third Quarter 2024 Financial Results. Before we begin the call, I'd like to remind you that our remarks may contain forward-looking statements that relate to the future performance of the company and these statements are intended to qualify for the Safe Harbor protection from liability established by the Private Securities Litigation Reform Act.

Any Such statements are not guarantees of future performance and factors that could influence our results are highlighted in today's press release and others are contained in our filings with the Securities and Exchange Commission. Such statements are based upon information available to the company as of the day hereof and are subject to change for future developments. Except as required by law, the company does not undertake any obligation to update these statements.

Our remarks and press release today also contain non-GAAP financial measures within the meaning of Regulation G enacted by the SEC. Included in such release and our supplemental materials are reconciliations of these historical non-GAAP financial measures to the comparable financial measures calculated in accordance with GAAP. Now this call is also being webcast with a supporting presentation and a replay and copy of the presentation will be available on our website.

Our speakers today are Rocket Lab’s Founder and Chief Executive Officer, Sir Peter Beck, as well as Chief Financial Officer, Adam Spice. They will be discussing key business highlights, including updates on our launch and space systems programs. And we will discuss the financial highlights and outlook before we finish by taking questions.

So with that, let me turn the call over to Sir Peter.

Peter Beck

Thanks, Murielle, and thanks for everybody joining us today. Before we take you through the achievements of the quarter, I'd like to remind everybody what every launch, every development milestone, every spacecraft we build is working towards. Rocket Lab is an end-to-end space company. We provide the ride to space with our launch vehicles, and we build the spacecraft to do the work in orbit. This ultimately gives us the keys to space, unlocking the largest market of all space applications.

With Phase 1 and 2, the rockets in the spacecraft now well established. We're well positioned to create our own constellations to provide in-demand services and capabilities in space. In Q3, we strengthened this position with a few key achievements, including the signing of a multi-launch deal for Neutron with a commercial constellation operator. And we've been very considerate in the way that we've approached Neutron's first commercial contracts. And I look forward to sharing more on this later in the call.

On the small rocket front, we successfully launched multiple electron missions in Q3 and signed $55 million in new electron launch contracts, a testament to strong and growing demand for dedicated small launch and acknowledgement of electrons position. As for space systems, I'll be sharing updates on various programs, but one key call out is the Mars Sample Return Contract Study. Anybody who's familiar with Mars Sample Return understands NASA believes their current mission architecture is too costly, will take too long, so they've requested innovative new proposals to deliver samples sooner and bring the cost down.

We are delighted to be selected by NASA to put forward a study into how Rocket Lab would achieve this, and I'm very excited to share in more details about our proposal to support the mission today. And of course, to deliver space systems at scale, you need to be able to pump out constellations of spacecraft quickly and cost-effectively. I'm proud to share that our spacecraft production line in Long Beach is churning out spacecraft at a faster rate than ever, with builds underway for a backlog of more than 40 spacecraft. All of these achievements and capabilities feed into our final strategic pillar, being able to build and launch and operate our own constellations.

I'll [address it] (ph) right up front, which is that we're not ready to reveal details on what this constellation or application may be. But I think it's important to understand the strong foundation we've built up across launch and space systems to enable it in due course. Okay, excuse me. Onto some quick financial highlights for Q3. We delivered another really strong quarter with positive metrics across the business. The third quarter revenue topped out at $105 million, within $1 million of our record revenue achieved last quarter. That's a 55% revenue increase year-on-year, while our backlog has grown 80% year-on-year to set at $1.05 billion at the end of September.

I'll let Adam dig into the numbers properly, but I think it's important to note upfront that once again we're delivering on the old Rocket Lab adage and mantra of we do what we say we were going to do, across both engineering and technical achievements, but as well as financial goals. Okay, on to Electron updates. We've reached 12 missions for the year and counting, setting a new annual launch record for Electron. Only two rockets globally launched more than Electron, that's the Falcon 9 and the Chinese Long March, making Electron one of the most globally significant rockets flying today.

Launch cadence is one thing, but doing so in a financially sustainable way is quite another. We've sold 55 million in new Electron launch contracts in Q3, but what's really important to note about is the significant increase in average sales price. This is now 60% higher than when Electron first started flying. We've bought a service to market that works, that customers need, and we've proven we can scale. The cost just reflects how rare and sought after this capability is. Just to help visualize it, here's a snapshot of the global launch cadence this year across all vehicles. And you can see Electron is right up in the top ranking in Number 3 spot. Now onto Electron launches for the quarter. We had three missions for three separate commercial constellation operators during Q3. Each of the missions are part of multi-launch contracts with return customers. Electron provides a vital sought after service for small [satellite] (ph) constellation operators who want to be in control all of their orbits, launch schedule, and mission parameters in a way that's just not possible on large rides to your missions.

We had another quick turnaround between missions to launching electrons back to back from Launch Complex 1 within just eight days of each other. Speaking of fast turnarounds, after Q3, we completed another launch in record time. We launched a mission for a confidential constellation operator just 10 weeks after signing contract. This kind of speed is pretty well unheard of in the space industry. It's typical to take a year to go from contract to orbit. Of course, that causes bottlenecks and limited launch opportunities for satellite operators.

Electron has plugged this gap, getting a satellite operation on orbit faster, so they can test their technology sooner, begin generating revenue for constellations earlier, or collect urgent data from space on demand. I've discussed [at length] (ph) previously that launch is a lumpy business. It's common for customers to increase delays and new launch dates, causing “constant manifest shuffles”. This results in an ever-changing fluid launch schedule. But because we have a factory of rockets and three launch sites standing by to support. We can slot new customers in as these gaps open up quickly.

Now I'm sure the software team will laugh at me for this but in reference to ultimate flexibility it's a feature and not a bug of the Electron business model. Especially as we collect up to 90% of the contract value for every mission before launch day, with revenue recognised on launch. So if a launch slips a month here or there, the overall impact to the business is pretty well negligible. Right, moving on from small launch onto Neutron updates.

Okay, so we've signed a launch agreement with the Constellation operator, which encompasses two very early launches on Neutron. Thanks to our proven track record with Electron, the space industry has come to expect high-performing reliable launch vehicles from Rocket Lab. Because of this, we have worked with a lot of different customers for Neutron's first few missions, but we're in the fortunate position to be able to choose who flies first and have made a careful and considered strategic decisions around that.

We see this agreement as an important opportunity that signifies the beginning of a productive collaboration that could see Neutron deploy this particular customer's entire constellation. I'm confident in these two launches will be the first of many more to come from this particular customer. Now we've really been methodical about when we open the bookings on Neutron 2. It's all too common in the space industry for aspiring launch providers to sign non-binding agreements and sell missions that are lost to fund development.

We know that it's better to bring a real rocket to the market first and to command a premium price. As we draw closer to Neutron's debut next year, conversations with customers and demands for launch slots have started to mature. As everyone will expect, I'm very happy to say that the contract value, this particular contract value, [is in] (ph) family with our standard Neutron pricing for launches. One of the programs that Neutron has been ideally suited for from day one, was when we conceived the vehicle was the US's Space Force National Security Space Launch Program or NSSL. The Space Force recently opened up the RFPs for the program, Program Next Lane 1 on-ramp, which will see us compete to qualify for a share of up to $5.6 billion of national security launches.

There is an unnerving bottleneck in the medium launch market currently, creating a risk for National Security. Bringing new launch capability to NSSL, is critical to increasing the DoD's diversity of opportunities, assuring access to space for National Security, and with our proven track record, market-leading design and established infrastructure, Neutron is a pretty compelling choice. We're well past the design phase, now moving into Neutron's build and test campaigns. Keeping our schedule for the first launch next year, puts us inside the 2025 year-end time frame sought by the Space Forces for the next on-ramp.

We brought a new vehicle to market before with Electron, which is a reliably delivered national security payloads to orbit for several years. And with Electron, we reached 50 launches faster than any other commercially developed rocket in history. So we know how to do this and we know how to do this well. Government interest in Neutron's development is ramping up in other areas too. This quarter we're awarded an $8 million study contract with the US Air Force's research lab to showcase our digital engineering prowess with Archimedes. This contract has a tie-in with the NSSL program, as well where it includes the option to expand our digital engineering processes and further build the digital engineering framework for NSSL Phase 3 Lane 1 launch providers.

This contract is a bit of a win-win when it comes to defense industry partnerships. It not only allows the US Air Force to collaborate with industry leaders like the Archimedes team to help develop and modernize the US Air Force's engineering processes and capabilities, But it also supports smooth integration of Neutron into the NSSL program to more efficiently and quickly provide for some of the nation's most critical missions.

Elsewhere across the DoD, the USTRANSCOM has extended our 2022 research agreement that allows us to continue to explore point-to-point cargo delivery with Neutron. And we've recently received confirmation from the US Space Force's -- Space Systems Command that Neutron can now compete for missions under OSP-4, a near $1 billion indefinite delivery and definite quantity contract that were on ramp to a few years back.

All right, moving on now to Neutron's development progress and some of the technical milestones we've hit this quarter. We're well past the design phase now and deep into the qualification testing of our large-scale flight hardware. Starting with the reusable captive fairing for Neutron, or as we like to call it, the Hungry Hippo, these fairing halves remain attached to Neutron's first stage for the full flight, simply opening to release the payload and the second stage before closing back and returning back to Earth with the rest of Stage 1 ready for another flight.

These fairing halves will soon be going through their mechanical testing before assembly and integration onto the large-scale composite panels and the seven-metre-wide barrels that make up the first stage. Another big milestone was the recent successful test of the second stage. We conducted its first Wet Dress Rehearsal in a flight configuration, going through the pressures, mechanical loads, processes, and procedures that would be seen in flight operations. Part of the test campaign included onboard avionics, taking command and control of the stage and demonstrating pressurization, fill, drain, and [cold-float] (ph) operations. This has been one of the biggest integrated milestones yet, proving out not only the flight hardware, but also the supporting infrastructure to operate the vehicle.

We have flight hardware in production for all other Neutron composite structures, including the barrels and domes for the vehicles for a stage propellant tank. All of the internal propellant management devices, the avionics are on track for integration for Stage 1 tank before it goes through the same set of test -- and test campaign as the second stage has just done.

Now onto Archimedes. We've talked about it before, our approach before with Archimedes, and how we were strategic in taking our time to bring a flight-ready engine to the test stand. That means we could hit the ground running to qualify it rather than mess around with early prototypes needing lots of design tweaks and changes and manufacturing that would ultimately slow the program down. But seeing that strategy really pay-off in these past few months. Our engine test cadence in Mississippi has doubled over the quarter, and we've bought multiple engines to the test stand.

The thing to point out here, too, is the rocket engine program is never a one-and-done scenario. Archimedes engines will go through short burst tests, full duration hot fires and tweaks, all the way up to Neutron's first flight. So far, though, we have continued to see strong performance from the Archimedes, and we're able to iterate updates rapidly, which is really what we want to be in this point in time in the test campaign. All that to say is that the cornerstone of any rocket program depends on how quickly and reliably you can scale engine production in parallel.

I know I've said it before, but it bears repeating because building your first rocket engine is hard. Building it 10, 20, 50 times at that pace that can keep up with demand is even harder. With that in mind, we continue to scale production for Archimedes at the same time that we're testing it. We've got the assembly line in California humming with engines shipping out the door frequently to Mississippi, setting us up well to get into a good launch cadence with Neutron after first flight.

A rocket program is much more than just a vehicle, of course, and its engines. Launch infrastructure is a critical component and one of the pieces that we've had a bit of practice to, thanks to having stood up three pads on two hemispheres with electrons. Launch sites are a little bit like an iceberg. There's so much of the infrastructure that is underground or hidden in the development phase. With that now well established, we're starting to put the finishing touches on the above ground of the structure, including a massive 165-ton steel structure launch mount that will hold down mechanisms. It's from this structure that Neutron will lift off next year. The launch mount will be installed in LC3 in the coming few weeks. And from there, the focus will start to shift to Pad commissioning before Flight 1.

On the ground at launch complex 3, some really big long lead items have made their way to the Pad at Wallops Island, including two 90,000 gallon propellant tanks that were installed in Q3. Each of them is longer than one of our electron rockets, which really helps put into perspective the scale of the works that are happening at LC3. Just a few miles up the road from the launch pad, we've completed the construction of the assembly and integration and test building, where Neutron's vehicles will go through their final checks before they're taken to the launch pad.

Having this building only 3 miles from the launch pad is a real strategic advantage for us as we don't have to grapple with the slow and expensive complex logistics of transporting a hulking rocket across the country just to get to the launch pad. That wraps up the headline items on the launch front, so now moving into space systems. So one of NASA's flagship missions is the Mars Sample Return Program, which aims to bring scientifically selected samples from Mars -- back from Mars to Earth, for the first time in history. But NASA has said that their current architecture is too costly at $11 billion and too slow, with the samples not expected to be into the hands of scientists until 2040.

So the agency put out a call to industry for new proposals, and I'm proud to confirm we were selected to conduct the study. We're putting forward a highly compelling concept that will return Mars rocks faster and at a fraction of the cost -- of the current cost of the program. This mission is one of the biggest most ambitious projects NASA has ever undertaken. It will completely change the way that we think about our solar system, potentially answer whether life ever existed on Mars and help prepare for the first human explorers on the red planet.

While it might not be obvious at first glance, it's a mission that we're actually uniquely suited to. Now our fingerprints are already all over Mars. Our technology has been incorporated into missions like the Mars Insight Lander, the Ingenuity Helicopter, and even the cruise stage that brought Perseverance to Mars, enabling the very rovers that are collecting samples to be brought to -- samples brought to Earth under the Mars Sample return. From orbiters and rovers, landers, crew stages, we have experience in delivering mission success on the red planet.

Now everything we've put into place over the years, either through our own organic development or through acquisitions of some of the industry's leading technology suppliers, has been part of our methodical strategy to offer vertically integrated solutions for complex missions just like these. Mars Sample Return requires an immense depth of experience and capability, the very kind that our team and technologies have delivered on before. We have the expertise in building and launching small rockets from little planets. We have, the innovative Mars spacecraft. We have demonstrated re-entry capability. We've enabled rendezvous and proximity missions, where leaders in guidance, navigation control, and our flight software is already on Moon landers.

And we know how to manage large and complicated missions, including ones for NASA. We've shown time-and-time again that we're disruptors in the industry who are able to conduct missions beyond Earth's orbit on a rapidly fast development timelines. And whenever they can't do it, we can do it at a fraction of the traditional cost. We look forward to delivering this once again from Mars Sample Return should a proposal make it through the selection process later this year.

Now on to other updates across our Space Systems business. Before I dive into more specific mission updates, I want to provide a quick snapshot of just some of the various programs underway. This one is just a -- this is just the latest lineup of spacecraft we're building right now or have already completed, Like our 2 ESCAPADE spacecraft for Mars, two completely different constellation spacecraft, one for cell connectivity for MDA Globalstar, the other for National Security and the Space Development Agency, and other individual technology test missions ranging from connectivity in space to cryogenic fuel storage on orbit.

Beyond these missions and constellations, we continue to do strongly in our merchant space systems business with mega constellation contracts too. Some of you will remember me talking about scaling up our satellite facilities in California, as we bring on new and bigger spacecraft contracts. Well, part of the benefit for us taking over the previous Virgin Orbit building for pennies on the dollar for our new engine production site, was it allowed us to use that extra space in our headquarters to be converted to our satellite production facility. We're really starting to see that strategy pay dividends with production lines of our various spacecraft platforms now up and running.

Without -- or without a single shovel in the ground, we've avoided all the headaches of having to build new buildings and factories from scratch and save precious time and resource in a scaling strategy. And the beauty of having all those space systems products co-located in one building in one building, there are simple ease of integration for our teams. A technician can literally walk across the floor, hand over an avionics box to a spacecraft integration team as opposed to waiting for months for a supplier to produce it, ship it and then deliver it. It's really the true beauty of [vertical] (ph) integration for our business.

Now on to some more specific program updates under the Space Systems umbrella. And if I can stick with Mars for just -- the Mars thing for just a little bit longer, in Q3, we completed and delivered the two spacecraft for the ESCAPADE Science Mission to Mars for NASA. It was a really monumental feat in itself given the 3.5 year time span handed to us to deliver this mission. Unfortunately, however, outside our control, the rocket, the satellites we're launching on wasn't quite ready in time for that Mars transfer window. So the mission has been somewhat delayed. But the team is standing by and ready to support once the new launch date is set.

On to our $500 million prime contract with the Space Development Agency for their tranche to transport layer constellation. The team is hitting some great technical targets within the program. The preliminary design of the spacecraft complete, the work being pulled the work can begin pulling the hardware together in the clean rooms at headquarters. This progress puts us in a strong position for the upcoming, solicitation of 200 satellites under the Tranche 3 of the SDA's program, a procurement process expected to begin in 2025.

And finally, to wrap up, space systems and next two satellites for Varda Space Industries have been completed and are now ready for launch. Pioneer class space satellites host Varda's capsule and provide power, communications, propulsion, and altitude control for the mission. It's our first spacecraft for Varda to help bring the capsule back home from space, landing it in the Utah desert last year with our next spacecraft set to do the same thing again but this time over Australia where both missions are set to re-enter the Earth's atmosphere and land in southern Australia soon after launch next year. In the meantime, the team is already working on the fourth pioneer spacecraft for the same Varda mission.

And before I hand it over to Adam, I just wanted to wrap up with a couple of personnel changes at the board and executive level for this past quarter. So Mike Griffin has finished up on the Rocket Lab board after a four-year, ten-year serving the company. We're incredibly grateful for his experience and leadership helping guide Rocket Lab's growth from a private start-up to a global industry leader in launch and space systems and really want to thank him and wish him all the best, as he retires from Rocket Lab's board.

But as one chapter ends, another two begin at Rocket Lab across board and executive level. This quarter we welcomed Frank Klein to the team as our new Chief Operations Officer. Frank joins us with 30 years of international manufacturing experience and leadership in the Automotive Industry at Daimler, Mercedes-Benz, and most recently a prominent EV company. As a COO, Frank is leading our efforts to scale global manufacturing of our spacecraft, launch vehicles and spacecraft components. And it's great to have a seasoned and experienced leader like Frank bring his wealth of knowledge in lean manufacturing and scaling to Rocket Lab.

And Ken Possenriede also joined us on the Board of Directors this past quarter. He joins Rocket Lab after a 35-year career at Lockheed Martin in financial leadership positions, including serving as the Space Prime's Chief Financial Officer. Ken's deep aerospace and defence industry experience combined with his financial leadership adds to even more horsepower on an already impressive board lineup and it's fantastic to have him on board to help us shape the future.

So with that I'll hand it over to Adam now to provide further commentary and to discuss our financial highlights and outlook. Over to you Adam.

Adam Spice

Great. Thanks Pete. All right. Third quarter 2024 revenue was $105 million, which was at the high end of our prior guidance range and reflects significant year-on-year growth of 55%, driven by strong contribution from both business segments but led by space systems. Our launch services segment delivered revenue of $21 million in-line with our prior guidance. Our current backlog continues to support our 2024 target average revenue per launch of $7.5 million, with some quarterly variability tied to volume purchase commitments, launch location, and mission assurance requirements.

Our space system segment delivered $83.9 million in the quarter, near the high end of our prior guidance range of $79 million to $84 million, reflecting sequential growth of over 9%, driven primarily by a strong quarter from our space solar business. Now turning to gross margin. GAAP gross margin for the third quarter was 26.7% in-line with our prior guidance range of 25% to 27%. Non-GAAP gross margin for the third quarter was 31.3%, which was also in-line with our prior guidance range of 30% to 32%.

Relatedly, we ended Q3 with production related headcount of 964, up 50 from the prior quarter. Now turning to Backlog. We ended Q3 2024 with $1.05 billion of total backlog with launch backlog of $326 million and space systems backlog of $721 million. [We're over to] (ph) Q3 of last year, total backlog increased 80% or $465 million, primarily due to our $515 million contract awards about 18 spacecraft for the FDA, we won last year. Sequentially, there's a slight remixing of our backlog, as a result of particularly strong bookings in our launch segment.

We continue to cultivate a healthy pipeline including multi-launch deals and large satellite manufacturing contracts that can create lumpiness in our backlog growth given the size and complexities of these opportunities. We expect approximately 50% of current backlog to be recognized as revenues within 12 months.

Turning to operating expenses. GAAP operating expenses for the third quarter of 2024 were $79.9 million, up $9.5 million sequentially, which was at the low end of our guidance range of $80 million to $82 million. Non-GAAP operating expenses for the third quarter were $68.7 million, up $10.2 million sequentially, which was also at the low end of our guidance range of $69 million to $71 million. The sequential increases in both GAAP and non-GAAP operating expenses were primarily driven by continued growth in headcount and prototype spending to support our Neutron development program, related infrastructure IT support for Neutron, and our SDA satellite contract.

In R&D specifically, GAAP expenses were up $7.8 million quarter-on-quarter due to Neutron prototyping, materials, and headcount growth. Non-GAAP R&D expenses were up $8.1 million quarter-on-quarter, driven similarly to GAAP expenses. Q3 ending R&D headcount was 776, representing an increase of 103 from the prior quarter. In SG&A, GAAP expenses increased $1.7 million quarter-on-quarter, largely due to an increase in outside services related to legal and IT, With IT spend largely related to security and cyber requirements under our SDA contract, and legal spend driven by a range of corporate initiatives, including corporate development as we continue to look to scale the business organically and inorganically.

These legal and IT increases are paired with an increase in staff costs. Non-GAAP SG&A expenses increased $2.1 million, driven similarly to the GAAP SG&A expenses. Q3 ending SG&A headcount was 300, representing an increase of 27 from the prior quarter. In summary, total third quarter headcount was 2,040, up 180 heads from the prior quarter. Now moving to non-GAAP free cash flow and adjusted EBITDA.

With regards to cash, purchases of property, equipment, and capitalized software licenses was $11 million in the third quarter of 2024, a decrease of $4.3 million from the $15.3 million in the second quarter of 2024. We continue our investment in Neutron research, testing, and production infrastructure projects along with expansion of our satellite production and space solar solutions capacity and we do expect our capital expenditures to increase over the next few quarters.

Cash consumed from operations was $30.9 million in the third quarter of 2024 compared to $13 million in the second quarter of 2024. The sequential increase of $17.9 million was driven primarily by increased Neutron and Space Systems program spend and lumpiness in Space Systems Program milestone receipts, partially offset by improved launch contract cash collections.

Overall, non-GAAP free cash flow, defined as GAAP operating cash flow less purchases of property, equipment, and capitalized software in the third quarter of 2024 was a use of $41.9 million compared to $28.3 million in the second quarter of 2024. While we were doing better versus our targeted cash consumption run rate, we do expect to pick up in cash consumption in the next few quarters, owing to an increased expected increase in Neutron spending ahead of our mid-2025 launch and lumpiness in large space systems milestone payment collections.

The ending balance of cash, cash equivalents, restricted cash, and marketable securities was $508 million, as of the end of the third quarter of 2024. We exit Q3 in a strong position to execute on our organic expansion initiatives as well as inorganic options to further vertically integrate our supply chain with the critical capabilities and expand our addressable market consistent with what we've done successfully in the past. Adjusted EBITDA loss was $30.9 million in the third quarter of 2024 compared to a loss of $21.2 million in the second quarter of 2024.

The sequential increase of $9.7 million was primarily driven by increased spending related to Neutron development. With that, let's turn to our guidance for the fourth quarter of 2024. We expect revenue in the fourth quarter to range between $125 million and $135 million. This range reflects a step up in space systems and an increase in launch cadence consistent with our prior outlook. In the past, we've broken down guidance by launch and space system segments. However, we found it difficult at best to predict launch customer readiness within a quarter and believe that providing a single top-line guidance number is more appropriate at this time, given the resilience we've witnessed as a result of the expanded diversification of our business. That said, we'll continue to report actual revenues and related gross margins of launch and space systems as distinct segments.

We expect fourth quarter GAAP gross margin to range between 26% to 28% and non-GAAP gross margin to range between 32% to 34%. These forecasted GAAP and non-GAAP gross margins reflect improved mix within our space system segment, primarily within satellite manufacturing, as well as better overhead cost absorption in our launch business. We expect fourth quarter GAAP operating expenses to range between $84 million and $86 million and non-GAAP operating expenses to range between $75 million and $77 million.

The quarter-on-quarter increases are driven primarily by continued Neutron investment in the staff costs, prototyping and materials. We expect fourth quarter GAAP and non-GAAP net interest expense to be $1.5 million. And we expect fourth quarter adjusted EBITDA loss to range between $27 million and $29 million and basic shares outstanding to be approximately 501 million shares.

And with that we'll hand the call over the operator for questions.

Question-and-Answer Session

Operator

[Operator Instructions] Your first question comes from the line of Andres Sheppard with Cantor Fitzgerald. Your line is open.

Andres Sheppard

Hey, everyone. Good afternoon and congratulations on the quarter. Certainly a lot of developments, so well done. I guess first question, just on the Neutron, I just wanted to clarify. So it sounds like you're, the target for the first launch is unchanged for mid-2025, but the multi-launch agreement that you disclosed today, that's targeted for, I believe, to start in middle of 2026. So I guess A, just wanted to confirm that, and B, then if that's the case, why announced this contract today, just given where you still are on the Neutron development? Any color there would be helpful. Thank you.

Peter Beck

Yeah, hey, Andres. Happy to take that question. So I think we've been pretty clear about what we expect for Neutron's launch cadence to be. So obviously, one test flight in the following year three, and then five, and then continue to seven and beyond. And that's following pretty much the same scaling rate as we saw that we could do with Electron and quite frankly I mean if you look back through history, it's pretty difficult to see any examples of a scaling rate faster than that.

So that kind of backs into real available slots. So as we're talking to customers, obviously they want to know when is their launch slot because they have certain mission objectives from their end. Of course we want to know are their spacecraft going to be ready. I think we've talked about this in the past. So it's really just a careful marry up of various customer requirements and also the launch slots that we've made available to customers. And as we say on the call, we're very selective about those -- especially those early slots.

We need to make sure that we're there on time, we need to make sure that they're on time. So we're kind of easing into that kind of gently. With respect to announcing it now, I think it's fairly material that once we start signing a Neutron contract, I think it's been anticipated. So I think it was a material thing that we really would have to disclose.

Adam Spice

Yeah, and I would add to that, too, Andres, that we've talked about the fact that, as you start to approach Neutron readiness, you think about a timeframe of kind of 12 months, 18 months where you want to have your customer lined up because you got to -- again, have this whole synchronization to make sure that the rocket's ready. There's a long time between signing a contract usually and getting the actual payload integrated and launched. So I think the timing roughly worked out to that. And then I also think it's important that, what We've also said, and I think Pete's been very, very consistent in this, that we're not going to be selling heavily discounted Neutron launches just because it's a new vehicle.

We bring a lot of heritage to this market because of the 54 successful launches that we've had with Electron. And so it really did put us in a really good position to again not be out there kind of you know having to do heavily discounted launches just to gain credibility. So I think this was a definitely an important milestone for the company to reach and we're very happy to be able to announce that today.

Andres Sheppard

Thanks guys you know that that's super helpful I appreciate all that context. Maybe just a quick follow-up, if I may. Can you maybe just remind us, what are the outstanding maybe catalysts or milestones for the Neutron development that you think investors should be aware of. And additionally maybe if you can give us a little more granularity on the hot fire test and the production of the additional engines there. Thank you.

Peter Beck

Yeah, sure. Sure, Andres. The best way I like to explain it is, and we tried to do a little bit of that in this presentation, was you need to think of it as three kind of pillars. One you have launch infrastructure and that's actually where the majority of the capital flows into. And the things that everybody should be watching there is stuff being built. Quite simply, steel going in the ground, concrete being poured and things that look like a launch site. Now thankfully that's relatively easy to follow because it's sitting on the coast and it's relatively easy to get information on that. And of course, we provide good updates.

So as long as steel is being built and shipped and propellant lines are running and all the rest of it, then you can feel pretty good about that. And then the second pillar is kind of structures. So you've seen full Stage 2 tanks and flight configurations running during wet dresses, fairings, first stage tanks. So as long as you keep seeing all those large structures, I think you can see that we're on track. And they all come together relatively late in the piece for an end-to-end wet dress rehearsal.

And then with Archimedes, we're in a test and qualification campaign. So what we're doing with that engine is we're finding, it's called a run box basically, is we're finding all of the operational conditions of that engine and defining what they are.

So we have a desired run box and then we'll have an actual run box. And what we're looking to do is changing various intake pressures of the propellants and various operating points and really understanding the engine and what kind of idiosyncrasies that it may or may not have. So the Hot Fire campaign reached a really important milestone last quarter, where we put a production engine that was full of all production components, valves, hardware, software, and we took it to over 100% throttle level. So I think that was a really important milestone. Working from that, it's just all about accumulating test time, putting the engine into unknown conditions, and continue to evolve the engine and increase its performance over time.

And I sort of made comment in the script here that like an engine program, it's a long process. Yep, you can make fire and you can achieve kind of preliminary targets and milestones, but you're always looking to improve either manufacturing or performance or reliability of an engine over many, many years. So I think we're in a good spot, but those are the three things for folks to track.

Andres Sheppard

Wonderful. I really appreciate all that color. Congrats again on the quarter. I'll pass it on.

Peter Beck

Thanks, Andres.

Operator

Your next question comes from the line of Edison Yu with Deutsche Bank. Your line is open.

Edison Yu

Hey, thank you for taking our questions and also congrats. I know you're not saying too much on the Neutron award, but maybe I could kind of ask from a different perspective. Can you provide any context in terms of what you want relative to if the customer had already placed the launch with someone else and they switched you? Or do they have other kind of maybe like soft contracts out there with other launch providers? Just is this, I know you say you could launch a whole thing, just some context around currently what is the piece that you have?

Peter Beck

Yeah, I mean look, we probably can't say too much, but it's a customer that we know. And as I mentioned, we were very strategic, in especially these early launches, about who we want to almost essentially partner with on these early contracts. So look, I mean, it's not my business to get into their kind of business, but needless to say, we were happy with that particular customer, and it's a good customer for the stage and phase of the program.

Adam Spice

And Edison, maybe little more context to that. So as we've talked about in the past, there just are not that many companies in our space that have executed in a position to launch with a level of confidence. So you've got the added dynamic that there's a range of customers out there who, also have payloads that compete with some of the other launch providers. And at this point, we feel probably more comfortable launching with somebody they don't necessarily compete with. So, I think that plays into a lot of the discussions that we have. And I would say that the market remains pretty robust as far as demand is concerned.

When you look at the people that have capacity, a lot of that capacity has been spoken for. So really we think Neutron is coming to market at a great time where we're really filling a new need for incremental capacity, and we're doing it in a way that's really non-competitive and non-threatening with those customers. So just a lot of the stars are starting to align on that for us with regards to Neutron.

Edison Yu

Understood. Then a follow up question a bit longer term. Obviously you've got Frank on board now and he comes from the automotive industry. And curious if you can maybe dimension the kind of scale you're looking for. Obviously automotive is orders of magnitude higher scale than aerospace is frankly coming on Board to kind of take you to much, much higher level or more to kind of get the existing backlog up to speed?

Peter Beck

Yeah, look, a bit of both Edison and we have some components that are at low scale like Mars spacecraft and they're going to be produced at high scale and then we have other things like reaction wheels where we produce thousands and thousands a year of. But the one thing about production, and I can attest to this, is that it all looks the same whether you're building a car or a spacecraft or a rocket, the production fundamentals are always the same.

Now, of course, the numbers that roll-off the end of the production line differ, but all the manufacturing techniques and good practices remain the same. And we've done a great job here, and the team's done an amazing job here at Scaling. But as we look to move even further up that curve, bringing someone on with just such deep experience, not just within production and production scaling but within operations. It was just kind of the right time for the company to create that position.

Edison Yu

Fantastic. Thank you.

Operator

And your next question comes from the line of Matt Akers with Wells Fargo. Your line is open.

Matt Akers

Yeah, hey guys. Good afternoon. Thanks for the question. I wanted to ask about space services. You guys kind of teed that on Slide 4. Just curious. I know you don't want to reveal what that could look like yet but just curious what kind of time frame you had in mind. It seems like you know kind of the Phase 1 and 2 are in pretty good shape so I guess – if you move to phase 3, I mean do we need to get Neutron sort of at a higher production cadence? Are there maybe more parts of the portfolio to fill in? Just curious how you think of kind of the timing there.

Peter Beck

Yeah, thanks Matt. So look, everything is irrelevant without a reusable high cadence launch. So Neutron is really the key to unlocking that. And if you look at Starlink, it's a good example, it's a great spacecraft, but actually the thing that has really made that possible is a high cadence, low cost launch. And that in turn is made possible by a reusable launch vehicle. So until Neutron is flying at some level of cadence, it's kind of academic to talk about deploying constellations.

Matt Akers

Yeah, got it. Okay. And just curious on this Neutron deal or maybe just Neutron in general, thoughts on kind of what the progress payment maybe looks like on that? Just curious, I guess one, if there's maybe some lumpiness in cash flow around that just because those are pretty big dollar items and also just how we should think about kind of the advanced payments versus kind of working capital aspect as that program ramps up.

Adam Spice

Yeah, I can take that one, Pete. So each, we have a fairly standard launch services agreement that we've obviously used many times with Electron and we're leveraging most of that forward on Neutron. And you're right that building this Neutron vehicles, it will be a challenging working capital cycle, at least initially, particularly when you think about the context here of reusability, right? So I think, we've never said that we plan to basically have a fully reusable vehicle for the first launch.

So as we kind of work our way towards full reusability, you know, we'll be getting more kind of benefits from a working capital perspective as we do that. But you know, the first few launches here are certainly going to be, you know, cash consuming. So you can think about the structure. Most of these LSAs have a deposit, and then there's milestone payments. And if you look at our Electron business, typically we've collected about 60% of the contract value by the time we actually start building the rocket. This might be a little bit different because, you know, it's the -- we're at the very early stages of kind of coming transitioning from R&D into production, but you can think of Neutron. Well, it should look very, very, very similar to what we've kind of disclosed and kind of producing our results, as we have with Electron.

So I did nothing too unusual with this one is just yeah -- it's the first few rockets out of the chute, so kind of we got to go through that transition period. And as we experience also on Electron, the Electron you know came out initially with not kind of target margins obviously but as we kind of build towards that, I think that there's a combination of the fact that we'll be collecting payments against milestones in the contracts, but also getting production efficiencies and ultimately reusability, which is a real key to kind of getting Neutron to its target model, which we think will look very similar to the long-term model for Electron. So hopefully that gives you a little bit of context.

Matt Akers

Yeah, that's very helpful. Thank you.

Operator

Your next question comes from the line of Erik Rasmussen with Stiefel. Your line is open.

Erik Rasmussen

Yeah, thanks for taking the questions. And congrats on the progress with Neutron. Maybe just on that subject, Neutron, I know it's not a lot you want to really share at this time, but are you replacing anyone or are you being brought on to sort of, you know, as another alternative just because of, like Adam you said, there's a number of medium rockets that are in the market or that will be potentially in the market in the coming years but is this just sort of you think a hedge because you guys are a lot closer than some others?

Peter Beck

Yeah, I think with respect to kind of commercial contracts and in some cases, definitely replacing. I would say that Erik in the NSSL world, it's bringing on new providers. I think if you look at the last NSSL Lane 1 Phase 3 award, 100% of that award went to one particular launch provider because there was nobody else. So in some cases, it's replacing and in some cases it's just being brought on as a new alternative.

Erik Rasmussen

Okay, and then you stated that the ASPs, you're going to be pretty firm on pricing. Is that the $50 million to $55 million that you initially talked about, and that's sort of where things have settled maybe for these two dedicated missions, and it says you're starting in mid-2026. Would both of those potentially happen in 2026, or how should we think about sort of timing, assuming you do meet the mid-2025 for your first test launch?

Peter Beck

Yeah, I mean the launch pricing as we pointed out is, you know, that was a really important thing for us and I think -- as I've said, I've made, well I kind of [had to] (ph) -- but with Electron it took us years to flush out bad kind of contracts with respect to ASP. So no, this contract is in line with our previously discussed ASP for Neutron. And then we're selling real slots with real launch windows. So we kind of, you know, somewhat at the bequest of the customer. So, you know, so the 2026 timeframes for those launches, are the customers, you know, driven requests.

Erik Rasmussen

Got it. Then maybe just staying with launch. You sitting at 12 launches year-to-date, you previously gave a range of 15 to 18. You have another 1 slotted in the coming weeks, the earliest. You would need sort of four in this quarter to get to the bottom of that range but do you still feel like that's a viable range for you the 15 to 18 where we sit today I appreciate you not giving specific guidance on that but I just want to get a sense of your confidence level on that prior guidance of 15 to 18.

Peter Beck

Well I mean if you recall at the start of the year, we thought we were going to do 22. So I'm always a little bit gun shy on this these days. But no, I think we've got certainly a very busy fourth quarter. And at this stage, the customers are looking good. So I think, we'll be within that range.

Erik Rasmussen

Okay. And then just -- on the NSSL, I just want to clarify the RFPs opened up pretty recently within the last two weeks. Does that mean you'll be available for this particular one or it's the next cycle because of the timeframe of Neutron at the earliest of mid-2025?

Peter Beck

Yeah, the way it works is that you have to demonstrate you can launch in 2025 to be on-ramped, and then once you're on-ramped, then you'll bid for various task orders. So there'll be, you know, this kind of, the task order is separate from the on-ramp and those task orders, you know, are released at the times that NSSL or the Space Force decides to.

Adam Spice

I think, Erik, I think what we're saying that, even though we'll be on ramping in 2025, we wouldn't be awarded any contracts for launch in 2025. And right now we're planning one test launch in 2025. We're talking about three launches in 2026, and then we've talked about five launches in 2027. And given kind of the discussion that we've had, you know, previously about this, the first customer for Neutron that we announced today, that's obviously consuming some of that capacity in 2026. So the most likely scenario is that could you see something in 2026 for NSSL? You know, it's a possibility, but it's probably not the most likely scenario. That probably looks more like it, you know, at 2027, but never seen ever.

Erik Rasmussen

Right. Okay, great. And then just one last thing on the backlog of clarification. The $326 million for launch, Does that include this latest award win for the two for Neutron?

Peter Beck

No, it does not, because that was a Q3 ending, and this contract was signed post the end of Q3.

Erik Rasmussen

Great. Okay. I’ll get back in the queue.

Peter Beck

It will show up in our Q4 backlog.

Erik Rasmussen

Great. Thank you.

Operator

Your next question comes from the line of Suji Desilva with ROTH Capital. Your line is open.

Suji Desilva

Hi, Pete. Hi, Adam. Congrats on the progress and the Neutron success here. The gross margin improvement here, Adam, is that the relative contribution between launch and space systems sequentially in 3Q and 4Q relatively even? And can you give an update on the solar gross margin improvement? Is there tailwinds still there?

Adam Spice

So the gross margin percentages are actually pretty close across. I mean, they're pretty consistent across launch and space systems right now. That's the function of kind of again, where we are in the margin improvement path for the launch part of the business and then just kind of where we are a mix within space systems. So you know -- if you look at the mix of our business being roughly 70% space systems, you know 30% launch, I mean, I think kind of gives you it's all proportional. So you just take the percentage of the business times the same rough margin calculation and just apply it.

Suji Desilva

Okay and then on solar, Adam is that remain a tailwind?

Adam Spice

So solar is -- solar has actually been progressing. It's a little bit slower than we thought. We talked about that on some prior calls where we expected to be at target margins within – which was -- we said about 30% non-GAAP gross margins of that business within two years of the acquisition. So we acquired that business in early 2022. So we're a bit behind, but we're making steady progress. So I would say when we look at our backlog for that business, we're really not booking. I can't remember the last time, maybe Pete can correct that, I can't remember the last time that we've actually booked business lower than our target gross margin. So it's all about kind of replacing, flushing out some of that older, in fact, there's really just one bad contract in the mix that we inherited.

Unfortunately, it was a large part of the -- I think it was almost $100 million of the $150 million backlog at deal close that came along that was basically essentially zero margin. So as we build the new business that target margins are better, that's starting to flow through now. We're seeing that come through in a little bit more profound way. And so I think that -- I think we all have actually probably more conviction now about getting to that 30% better target gross margin for that business. It's just taken us a little bit longer.

And so I think, you know, it's also not too dissimilar to our launch business where it's a very kind of fixed cost oriented business. So when you have a good quarter where you're shipping a lot more product, you get the benefit of that overhead absorption. And so as we mentioned earlier, and we mentioned in our prepared remarks, the solar business is particularly strong in Q3.

Suji Desilva

Okay, great. And then my other questions on the launch business, I understand that Neutron is going to add to the backlog this quarter but Electron growing $55 million. I'm just wondering what that, how that comparison to the last few quarters. Is that kind of in a range or is it accelerating and what the drivers if it is accelerating are? Is it ASP trending up or any color there be helpful?

Peter Beck

Yeah, I have a [crack at] (ph).

Adam Spice

Yeah, go ahead, Pete.

Peter Beck

I have a crack and maybe add a bit more color as well. So launch is lumpy, like actually launching the rockets is lumpy, so is the contracts. And we can go a quarter without signing anything. So as far as historical kind of lookbacks, I mean, certainly this has been a good call for Electron, but it tends to be pretty lumpy throughout.

Adam Spice

Yeah, and if you look at – certainly we book more launches. And again, as Pete said, it's lumpy because we're chasing bigger multi-launch agreements. But also the ASP has been very supportive. So I mentioned earlier that the average selling price for 2024 for Electron works out to be about $7.5 million per launch. And we've also talked on previous calls that our total backlog for Electron is priced at around $8.2 million ASP.

So we're actually doing, we're doing better on booking at higher prices. So that we're having a beneficial ASP mix effect. And that's obviously helping contribute to the backlog growth, but also to what we believe is kind of a nice steady progress towards our target margins for that electron business.

Suji Desilva

Okay. Very helpful. Thanks, guys.

Operator

Your next question comes from the line of Andre Madrid with BTIG. Your line is open.

Andre Madrid

Adam, Peter, thanks for the time. I know we kind of danced around it, but I wanted to just ask more specifically, how much was total Neutron development cost in 3Q? I know previously you said about [$160 million] (ph) for the year or about $40 million a quarter. And also like, is that kind of still an appropriate target looking all in?

Adam Spice

Yeah, I'm scrolling up the number right now. Yeah, no, this in Q3, it was a total -- well, you have to split out between the different elements, but if you look at total net spend for Neutron across OpEx and CapEx, it was just a hair under $44 million.

Andre Madrid

Got it, Got it. Okay. And I think --.

Adam Spice

And that's going to, you know that's going to step up as kind of, as we continue to kind of get towards the first launch. So that's why this first launch of Neutron is so important for us, because that really has such a tremendous impact on the P&L, right? Where we have all of this cost right now just hitting R&D. Once you get past that first test launch and you carry the first paying customer, everything flips over. You've got now R&D associated with it, cost of sales and so forth. So it's a super important thing for us to get that first launch off because it kind of caps that initial spend because you'll have minimum viable product both in the rocket and on the infrastructure side of the house.

And so I think probably along with that, we still feel very, very comfortable that we're within our target original budget for Neutron. And if you think about, we talked, this is going back when we came public, three years ago now, a little over three years ago, we said it was going to take roughly three, four years and cost $250 million to $300 million. And we put that in pretty stark contrast to what some other kind of medium and larger launch vehicles have cost in the many, many billions of dollars and taken the better part of a decade to get to first launch. So we feel like we're on track and we're going to set a new benchmark for capital efficiency and timing of getting a new launch vehicle to the pad.

Andre Madrid

Got it, got it. And if I could squeeze in one more, could you maybe highlight backlog at some of the non-photon space systems businesses like PSC, Sinclair? I mean, how is expansion and acquiring more business progressed at that line of business?

Peter Beck

Yeah, those businesses continue to grow at a pretty healthy clip. If you look at our target growth for the components business within space systems is around 20%. And we feel very comfortable. We've been delivering better than that, considerably better than some parts of our business. I would say that of our components businesses, Sinclair's probably had experienced the most recent growth. And that's driven by, you know, the mega constellation reaction wheel contract that we've talked about in the past that has been starting to shift. But we've seen strength across all of that. If you take it -- in aggregate, we kind of look at it across all of it. And when you look at our merchant business or the components business, there's really two pieces to that. There's the merchant components that we sell into other spacecraft manufacturers. And then there's the integrated or vertically integrated supply element where we're now supplying our own feed, if you will, into these spacecraft manufacturing projects that we've won, like SDA and like the MDA Global Star.

So it's really, it kind of, the growth is fueled not only by overall macro growth in the broader merchant market, but also from our own internal consumption as well. So we feel really good about, continuing a 20% CAGR for that business. I think some will be stronger than others, right? Like this year, I said, we're having more strength in Sinclair and that probably continues through next year. And then, as we look forward into 2025 and 2026, based on a lot of these big programs, you know, we're going to have very good years for our solar too, because, you know, we're dedicating a significant amount of our capacity to internal programs.

And overall, you know, it's actually has a very healthy kind of roadmap, I would say, for gross margin as well. If you look at the components or subsystems business, that's kind of already in the -- I call low to mid 40s, non-GAAP gross margin. And we think there's some upside to that. And then there's just the kind of a little bit of the offset where you have these bigger program gross margin models that are kind of more towards call it 30%. So you've got that blending effect there. But we feel really good about, you know, all the elements of that subsystem business.

Andre Madrid

And since you brought it up, what's the mix between what goes in-house for components versus what's delivered as a merchant supplier? And do you guys have a target mix for first-base systems, I guess?

Peter Beck

Yeah, that's a good question. I don't have that data at the tip of my fingers and I don't really want to try to guess on that. I mean, I think for some of the businesses we have a little bit more visibility. So I'd say for example, I think in our solar business, I think our internal capacity consumption right now is probably only about 10%. So 90% is going out to the merchant market to a lot of the people that sell into the national security market for these exquisite systems.

When you look at the separation systems business, for example, we sell much more externally than we consume internally, just the fact because, it's one of those predominant separation systems that flies on basically all rockets. So really, there really is a mix. But that's a good question. We can certainly follow up offline and see if we can get you more kind of concrete answer to that.

Andre Madrid

Yeah, definitely. I would appreciate that. Adam, thanks so much for the call. I really appreciate it.

Adam Spice

Sure.

Operator

Next question comes from Jason Gursky with Citi. Your line is open.

Jason Gursky

Hey, good afternoon everybody. Pete, I want to -- have you just walk us all through, if you don't mind one more time, why it is that we have to do one, three, and five. And if there isn't an opportunity to go a little faster here, you suggest that, you know, history would suggest with others you got to do it that way, but why is that the case? And Adam, you talked about throwing CapEx. There's some more CapEx coming into the mix here. Is this something we can throw some capital at and speed things up a bit?

Peter Beck

Jason, you asked the question that Adam asked me every day. And there's some things and you can throw as much capital as you want but until you fly you can only learn a certain number of things. And look, [135] (ph) is a pretty good scaling rate at best. And fundamentally you fly your first rocket and you'll do the best job that you think you can. There's a whole lot of stuff you can test on the ground, and then there's a whole lot of stuff you can't test on the ground. And it's just, well obviously, forward build is many of the components that we think in many of the systems and structures as we can. But you can find yourself just in a dead end pretty quickly. But it also just takes time to scale the production line.

And we've tried to front end it as loaded as best we can with the engine production line. Generally the engines are the longest pole in the tent from a production perspective. So we've really leaned into that so hopefully we can do better. But it just takes time to put one on the pad and commission it and learn it and learn from it and then roll those iterations into the next vehicle. And we're flying customers payloads so everything has to be very methodically thought through and every change is well qualified to reach that cadence.

I guess it might be a slightly different story if you had no customers and you just threw everything at it and had a different risk posture. But we're looking to get into commercial operations as quickly as we can. So when you're flying a customer, you can't just kind of be fast and loose. You have to be very methodical in any of the changes that you roll in. So we just don't want to be unrealistic with what's being -- what can tangibly be delivered.

Adam Spice

Jason, I'll be asking Pete that question every day going forward as well.

Jason Gursky

Yeah, if you can do it on my behalf, I appreciate that. And then, Pete, look, 1, 3, and 5, okay, so we've got 6 launches, one's a test. But as you look at the pipeline, I mean, over that time period, if you had more capacity, is there more demand out there? I just want to -- maybe strip out the national security launch just on the commercial side of things. I'm just trying to get a better gauge of supply and demand equilibrium.

Peter Beck

Yeah, well, I mean, that's the fundamental reason why you're asking this question, Adam asked this question, everybody asks this question, is how can we scale faster? And indeed customers. But the worst thing you can do is promise a customer that you're going to be able to provide a whole bunch of launch. They make a big commitment to you and then you don't deliver because that plays a [big part in their] (ph) business. So that's not good for their business or long term relationships or quite frankly, our reputation.

So of -- all the things we worry about, I think we've said before, demand is not one of them. We worry more about how fast can we scale the Neutron rather than other customers there to fly on it for sure. Right.

Jason Gursky

Okay, then last one is for me. I'm just kind of curious. We've got a new administration coming to town. Let's see here. I guess what policy statements have you heard to date that, you know, either have you encouraged or are giving you a little bit of pause. And what would you suggest we hear on the outside, kind of pay attention to here as this transition happens? What are you going to be looking for and looking to hear from the new administration?

Peter Beck

Yeah, it's a really good question. So I think what I take out of it is that I don't think there's ever been such a focus on space from any administration, perhaps back in the Apollo era but I mean it's very clear that this administration has a very strong focus on space which is good and when Space wins, Rocket Lab wins. Also, we see a very strong focus on national security which is obviously a core part of our business. But I guess probably the thing I'm most excited about is there's a real focus on moving away from the kind of slow government contracting and really focusing on commercial providing much more of the traditional space in government services which is really when you think about it there are only a few companies that are really well positioned to take advantage of those commercial opportunities and us being one of them.

So, you know, I look out on the new administration with quite a bullish outlook given those kind of three things.

Jason Gursky

Right. Okay, great. I'll pass the line. Appreciate it.

Operator

And your next question comes from the line of Michael Leshock with KeyBanc Capital Markets. Your line is open.

Michael Leshock

Hey, thank you. I wanted to ask on space systems. You've talked about both organic and inorganic ways to scale the business. We're just hoping for an update there on the M&A pipeline, whether you see any new opportunities. And then secondly, you also have those organic initiatives like additional clean room capacity that you already have the footprint for. I'm just wondering if you could provide some more details there and how much is left to go on those initiatives. Thanks.

Peter Beck

I can take a swing at this Adam and maybe you can follow it up. On the organic stuff, we always have a number of new products and things in development. Some of those are spin-offs from some of the programs that we're developing. Some of them are just areas that we think there's a market opportunity for and the way we kind of talk about those is obviously you've seen in the past product releases from us.

So that will – when we have something that we think is ready, then we'll release it. And I think we have a pretty strong reputation that we release it when it's done. We don't kind of talk about it until really it's done. And you saw that with even reaction wheels or something like the haste missions, you know, we announced a haste mission and then a number of weeks later we launched one. So that's kind of the way we roll with organic product development. And then inorganic, you know, we always maintain a pretty healthy pipeline and maybe, Adam, you can provide a bit more comment on that.

Adam Spice

Yeah, I'd say on the corporate development front, we continue to look at a lot of assets out there. I think that one thing is we're very selective, right. I think if you look at the assets that we've acquired in the past, the team is always at the center of it. If you look at the fact that you pick any one of the deals, they've always been leading products in their area. You pick from solar where they've had a single failure on orbit to bring new kind of innovative capabilities to the market through the software capabilities for command and control software for ASI and separation systems from TSC and so forth.

So it's really, I would say we continue to look at things and we've largely gotten the bus, the satellite bus into the point where we have most of the capabilities there that we think that we need to be kind of that -- to fulfill the end-to-end requirements there. There's still a few little things here and there that we're working on. And we're actually trying to address those, and some of those organically as well, not just inorganically, but probably the biggest missing piece to space systems from that's going to be filled likely through inorganic is going to be on the payload side.

So we really kind of stop at the payload right now. And certainly as we've talked many, many times about our grander ambitions of having our own applications on orbit, that's going to be benefited by having our own internal capabilities around the payload side of the system. So, you know, there is, fortunately for us, there's actually quite a few assets out there that are quite interesting that are kind of, I'd say poised to be part of a much bigger, you know, consolidated platform like we're building. So I think there is ample opportunities there, but we're very disciplined. It's got to be the right team. It's got to be the right time. It's got to be the right price. And so far we haven't gotten those three stars to align, but I'm pretty confident that we'll get some of those stars to align in the not too distant future.

And I think that will also provide a bit of a bread-crumbing for folks to understand a little bit more specifically which applications we're targeting because a lot of the payload is obviously very specific to the application. And so having kind of some insight into kind of the capabilities that we'd be acquiring would kind of give you some ideas about where we're going from an applications perspective, which I know everyone's chomping at the bit to try to understand better.

Michael Leshock

Okay, great. I appreciate all that detail. I'll leave it there. Thanks, guys.

Operator

Your next question comes from the line of Anthony Valentini with Goldman Sachs. Your line is open.

Anthony Valentini

Hey, guys, thanks for taking my question. You got Anthony on for [NOAA] (ph) tonight. Sorry to beat this point to death here, but it's been pretty well publicized at this point that Amazon's Kuiper has to get over a thousand satellites into orbit, you know, I think by mid-2026. And they have orders with some of your competitors for launch vehicles that either have not launched yet or in very limited cadence.

So I guess my question is, you know, do you guys stand to benefit from that between now and 2026 where you guys can get, you know, a piece of that pie or is it, you know, to what Peter was talking to in an earlier answer, it's just not possible given capacity and how many slots you guys have available?

Peter Beck

Well, I'll put it this way, as we said, Anthony, demand is not something that we worry about and that kind of falls into that category.

Anthony Valentini

Okay, that's helpful. And then, Adam, for you, is the systems segment profitable today?

Adam Spice

Well, you know, we only report our segments down to the gross margin line, and that's because we have a lot of shared resources across the different areas of development and production, so forth, and also we have one key decision maker, which is Pete, who kind of provides the overall kind of investment decisions or mandates across both businesses. So we -- I would say from a technical accounting perspective, we can't say that the space systems businesses is profitable on that level. But we can tell you is that when we look at kind of anecdotally across each of the lines of business, it would be safe to say that the vast majority, if not all, of the cash consuming nature of this business is coming from Neutron.

Right, so I think that's again that's one of the most important things about getting Neutron to minimum viable product in the first launch up. Things will become a lot more clear at that point as in and actually at some level doesn't really matter because then the overall profitability of the company starts to shine through. So, again, I would say that we can't say technically that space systems is profitable because we just don't account for the business at that level right now. That could change in the future, but that's not the current kind of approach we take to it.

Anthony Valentini

Okay. Yeah, that makes a ton of sense. Last one for me here. I just want to confirm the test flight on Neutron in 2025. That’s no revenue. Right.

Adam Spice

Correct. Yeah. There won't be any revenue associated with that launch. But we are working on things that would allow us to have probably some contra revenue, sorry, contra R&D associated with that. So looking to do some creative things there where we can kind of buy down our cost of that test launch. And so that's something that we're working pretty hard towards and hopefully we can get some of that to come into focus.

Anthony Valentini

Awesome. Thank you guys so much. Appreciate the time.

Operator

Your next question comes from the line of Cai von Rumohr with TD Cowen. Your line is open.

Cai von Rumohr

Super, thanks so much. So Adam, your ASPs for Electron have gone down sequentially for three straight quarters and yet your gross margin has improved. Now I know that costs are kind of specific to each mission, but what does that tell us about the underlying core profitability of Electron?

Adam Spice

Yeah, it's really a function of, so when you talk about ASP, the ASP is a function of customer timing, right? And so we have some customers that sign up for many launches and as a result of signing up for these bulk buys, they naturally get a lower price. And we get the benefit of having actually better margins on a lot of those flights, because a lot of the work doesn't have to get redone. All the GNC work that you have to do for each individual flight you don't have to redo that. You get maybe the benefit of having payload adapter plates that are common, you know, across multiple launch deals.

So a lot of what you're seeing, the ASP is again just a function of timing aware that customer [launch plan] (ph) is that we're again we're very comfortable with the number that we set for the year at $7.5 million being the average. And of course, like -- I mentioned before, our total backlog is priced at $8.2 million per electron. So that kind of shows you where it's going. And then the reason why the gross margin has gone up, despite having the optics on the ASP, is because we've been getting production efficiencies, right? So as we've gotten better at building these electrons the cost is coming down, which is helpful for us. So even as ASP may go down, gross margins go up. I think that's kind of the most salient points of kind of the gross margin trend analysis.

Cai von Rumohr

Got it. And the second one is, you started the year, Peter, you mentioned that 22 launches sort of scheduled or targeted and we're going to probably end up at 15 to 18. Have you ever thought, I mean, and one of the big problems is that you commit to a certain price and the customer commits to a certain date, but it's not a hard date. Have you ever thought of a kind of pricing so that if the customer misses, the price goes up? And I know that you have other competitors, but Certainly if you could get your number of launches up, you've made a big point of how high the fixed launch costs are. Is there any thought of kind of getting that volume -- thinking of ways, creative ways of getting that volume up?

Peter Beck

Yeah, I mean, some launch contracts have provisions for penalties. But I mean, if a customer has had a failure of something in a TVAC and then you start loading penalties on them, you know, it's not great for long term relationships. And I think the learning is here for us and I think for everybody as well is that the service that we provide is a bespoke, dedicated service for customers to launch. And they pay the premium for that. You compare an Electron to a Rideshare, it's many, many times higher. So that's what they're paying the premium for.

I guess the point that we try and make is that once a customer goes into backlog and we start collecting the cash from that customer, these customers never go away. They just sort of shift around. It's just a peculiarity of the way that revenue is recognized on launch. So no, I think We continue to play launch whack a mole and wherever possible, like you see, we did in the last quarter, we'll take quick turns business and fill some gaps. But it's kind of really the reality of the service that we provide.

Cai von Rumohr

Terrific. Thank you so much.

Operator

And there are no further questions at this time. I will turn the call back over to Peter Beck for closing remarks.

Peter Beck

Great, and thanks very much for everybody sticking around for the questions as well. Much appreciated. But before we close out today, I just wanted to draw your attention to some of the up and coming conferences we'll be attending. We'll look forward to sharing more exciting news and updates with you there. But that wraps up today's call, and thanks everybody for sticking around and listening to all the progress that's been made. The team is certainly very proud of this quarter and what we've achieved this year. So thanks very much.

Operator

This does conclude today's conference. You may now disconnect.

Read more current RKLB 
View all 

ChatGPT said:
ChatGPT
Rocket Lab USA, Inc. Q3 2024 Earnings Call Highlights (November 12, 2024)
Key Participants:
Management: Peter Beck (Founder & CEO), Adam Spice (CFO), Murielle Baker (Senior Communications Manager)
Analysts: Representatives from major firms like Deutsche Bank, Wells Fargo, Goldman Sachs, Citi, and others.
Quarterly Highlights:
Financial Overview:
Revenue: $105M (+55% YoY), just shy of record $106M last quarter.
Backlog: $1.05B (+80% YoY), split across launch ($326M) and space systems ($721M).
Gross Margins:
GAAP: 26.7%
Non-GAAP: 31.3%
Operating Expenses: $79.9M GAAP ($68.7M non-GAAP).
Cash Position: $508M in cash and equivalents.
Operational Achievements:
Launch Cadence:

12 missions year-to-date, setting an annual record for Electron.
Secured $55M in new Electron launch contracts during Q3.
Increased Electron’s average sales price by 60% since inception.
Continued high demand for Electron in small satellite markets.
Neutron Development:

Signed a multi-launch agreement with a commercial operator.
On track for its first launch by mid-2025, followed by 3 launches in 2026 and 5 in 2027.
Secured $8M Air Force study contract tied to Neutron's digital engineering and integration for the NSSL program.
Space Systems Progress:

Strengthened manufacturing capabilities, particularly in spacecraft production with over 40 spacecraft in backlog.
Advanced projects like Mars Sample Return studies for NASA, demonstrating cost and timeline efficiencies.
Strategic and Program Updates:
Electron Performance:

Positioned as a leading small-launch vehicle globally, ranking third by total missions behind SpaceX Falcon 9 and China's Long March.
Quick-turn launch capability demonstrated with a record 10-week contract-to-launch turnaround.
Neutron Rocket:

Designed for reusable medium-lift operations.
Target ASP: $50M-$55M per launch.
Integrated production lines in California and critical infrastructure nearing completion at Wallops Island.
Space Systems Expansion:

Key contracts include Mars ESCAPADE, SDA satellites, and Varda spacecraft.
Integrated vertical capabilities (e.g., solar panels, reaction wheels) enabling cost savings and production efficiencies.
Prepared for large-scale programs like Tranche 3 SDA satellites.
Guidance and Outlook:
Q4 Revenue Forecast: $125M-$135M.
Gross Margins: 26%-28% (GAAP), 32%-34% (non-GAAP).
Ongoing Investment: Focused on scaling Neutron, space systems production, and infrastructure to meet rising demand.
Leadership Changes:
Welcomed Frank Klein as COO to scale production and Ken Possenriede to the Board, leveraging experience in aerospace and defense sectors.
Key Takeaways:
Rocket Lab achieved solid growth in Q3, led by its space systems business and strong demand for launch services. The Neutron rocket development is progressing as planned, set to unlock larger markets with reusable medium-lift capabilities. Strategic positioning in both commercial and national security sectors places Rocket Lab in a strong competitive position moving forward.






You said:
Delete all mark ie ( ) "" .
Rocket Lab USA, Inc. (NASDAQ:RKLB) Q3 2024 Earnings Conference Call November 12, 2024 5:00 PM ET

Company Participants

Murielle Baker - Senior Communications Manager
Peter Beck - Founder & CEO
Adam Spice - CFO

Conference Call Participants

Andres Sheppard - Cantor Fitzgerald
Edison Yu - Deutsche Bank
Matt Akers - Wells Fargo
Erik Rasmussen - Stifel
Suji Desilva - ROTH Capital
Andre Madrid - BTIG
Jason Gursky - Citi
Michael Leshock - KeyBanc Capital
Anthony Valentini - Goldman Sachs
Cai von Rumohr - TD Cowen

Operator

Thank you for standing by. My name is Bailey and I will be your conference operator today. At this time, I would like to Welcome everyone to the Rocket Lab Third Quarter 2024 Fiscal Results Update and Conference Call.

All lines have been placed on mute to prevent any background noise. After the speakers' remarks, there will be a question-and-answer session. [Operator Instructions]

I would now like to turn the call over to Mariel Baker, Senior Communications Manager at Rocket Lab. You may begin.

Murielle Baker

Thank you. Hello and welcome to today's conference call to discuss Rocket Lab’s Third Quarter 2024 Financial Results. Before we begin the call, I'd like to remind you that our remarks may contain forward-looking statements that relate to the future performance of the company and these statements are intended to qualify for the Safe Harbor protection from liability established by the Private Securities Litigation Reform Act.

Any Such statements are not guarantees of future performance and factors that could influence our results are highlighted in today's press release and others are contained in our filings with the Securities and Exchange Commission. Such statements are based upon information available to the company as of the day hereof and are subject to change for future developments. Except as required by law, the company does not undertake any obligation to update these statements.

Our remarks and press release today also contain non-GAAP financial measures within the meaning of Regulation G enacted by the SEC. Included in such release and our supplemental materials are reconciliations of these historical non-GAAP financial measures to the comparable financial measures calculated in accordance with GAAP. Now this call is also being webcast with a supporting presentation and a replay and copy of the presentation will be available on our website.

Our speakers today are Rocket Lab’s Founder and Chief Executive Officer, Sir Peter Beck, as well as Chief Financial Officer, Adam Spice. They will be discussing key business highlights, including updates on our launch and space systems programs. And we will discuss the financial highlights and outlook before we finish by taking questions.

So with that, let me turn the call over to Sir Peter.

Peter Beck

Thanks, Murielle, and thanks for everybody joining us today. Before we take you through the achievements of the quarter, I'd like to remind everybody what every launch, every development milestone, every spacecraft we build is working towards. Rocket Lab is an end-to-end space company. We provide the ride to space with our launch vehicles, and we build the spacecraft to do the work in orbit. This ultimately gives us the keys to space, unlocking the largest market of all space applications.

With Phase 1 and 2, the rockets in the spacecraft now well established. We're well positioned to create our own constellations to provide in-demand services and capabilities in space. In Q3, we strengthened this position with a few key achievements, including the signing of a multi-launch deal for Neutron with a commercial constellation operator. And we've been very considerate in the way that we've approached Neutron's first commercial contracts. And I look forward to sharing more on this later in the call.

On the small rocket front, we successfully launched multiple electron missions in Q3 and signed $55 million in new electron launch contracts, a testament to strong and growing demand for dedicated small launch and acknowledgement of electrons position. As for space systems, I'll be sharing updates on various programs, but one key call out is the Mars Sample Return Contract Study. Anybody who's familiar with Mars Sample Return understands NASA believes their current mission architecture is too costly, will take too long, so they've requested innovative new proposals to deliver samples sooner and bring the cost down.

We are delighted to be selected by NASA to put forward a study into how Rocket Lab would achieve this, and I'm very excited to share in more details about our proposal to support the mission today. And of course, to deliver space systems at scale, you need to be able to pump out constellations of spacecraft quickly and cost-effectively. I'm proud to share that our spacecraft production line in Long Beach is churning out spacecraft at a faster rate than ever, with builds underway for a backlog of more than 40 spacecraft. All of these achievements and capabilities feed into our final strategic pillar, being able to build and launch and operate our own constellations.

I'll [address it] (ph) right up front, which is that we're not ready to reveal details on what this constellation or application may be. But I think it's important to understand the strong foundation we've built up across launch and space systems to enable it in due course. Okay, excuse me. Onto some quick financial highlights for Q3. We delivered another really strong quarter with positive metrics across the business. The third quarter revenue topped out at $105 million, within $1 million of our record revenue achieved last quarter. That's a 55% revenue increase year-on-year, while our backlog has grown 80% year-on-year to set at $1.05 billion at the end of September.

I'll let Adam dig into the numbers properly, but I think it's important to note upfront that once again we're delivering on the old Rocket Lab adage and mantra of we do what we say we were going to do, across both engineering and technical achievements, but as well as financial goals. Okay, on to Electron updates. We've reached 12 missions for the year and counting, setting a new annual launch record for Electron. Only two rockets globally launched more than Electron, that's the Falcon 9 and the Chinese Long March, making Electron one of the most globally significant rockets flying today.

Launch cadence is one thing, but doing so in a financially sustainable way is quite another. We've sold 55 million in new Electron launch contracts in Q3, but what's really important to note about is the significant increase in average sales price. This is now 60% higher than when Electron first started flying. We've bought a service to market that works, that customers need, and we've proven we can scale. The cost just reflects how rare and sought after this capability is. Just to help visualize it, here's a snapshot of the global launch cadence this year across all vehicles. And you can see Electron is right up in the top ranking in Number 3 spot. Now onto Electron launches for the quarter. We had three missions for three separate commercial constellation operators during Q3. Each of the missions are part of multi-launch contracts with return customers. Electron provides a vital sought after service for small [satellite] (ph) constellation operators who want to be in control all of their orbits, launch schedule, and mission parameters in a way that's just not possible on large rides to your missions.

We had another quick turnaround between missions to launching electrons back to back from Launch Complex 1 within just eight days of each other. Speaking of fast turnarounds, after Q3, we completed another launch in record time. We launched a mission for a confidential constellation operator just 10 weeks after signing contract. This kind of speed is pretty well unheard of in the space industry. It's typical to take a year to go from contract to orbit. Of course, that causes bottlenecks and limited launch opportunities for satellite operators.

Electron has plugged this gap, getting a satellite operation on orbit faster, so they can test their technology sooner, begin generating revenue for constellations earlier, or collect urgent data from space on demand. I've discussed [at length] (ph) previously that launch is a lumpy business. It's common for customers to increase delays and new launch dates, causing “constant manifest shuffles”. This results in an ever-changing fluid launch schedule. But because we have a factory of rockets and three launch sites standing by to support. We can slot new customers in as these gaps open up quickly.

Now I'm sure the software team will laugh at me for this but in reference to ultimate flexibility it's a feature and not a bug of the Electron business model. Especially as we collect up to 90% of the contract value for every mission before launch day, with revenue recognised on launch. So if a launch slips a month here or there, the overall impact to the business is pretty well negligible. Right, moving on from small launch onto Neutron updates.

Okay, so we've signed a launch agreement with the Constellation operator, which encompasses two very early launches on Neutron. Thanks to our proven track record with Electron, the space industry has come to expect high-performing reliable launch vehicles from Rocket Lab. Because of this, we have worked with a lot of different customers for Neutron's first few missions, but we're in the fortunate position to be able to choose who flies first and have made a careful and considered strategic decisions around that.

We see this agreement as an important opportunity that signifies the beginning of a productive collaboration that could see Neutron deploy this particular customer's entire constellation. I'm confident in these two launches will be the first of many more to come from this particular customer. Now we've really been methodical about when we open the bookings on Neutron 2. It's all too common in the space industry for aspiring launch providers to sign non-binding agreements and sell missions that are lost to fund development.

We know that it's better to bring a real rocket to the market first and to command a premium price. As we draw closer to Neutron's debut next year, conversations with customers and demands for launch slots have started to mature. As everyone will expect, I'm very happy to say that the contract value, this particular contract value, [is in] (ph) family with our standard Neutron pricing for launches. One of the programs that Neutron has been ideally suited for from day one, was when we conceived the vehicle was the US's Space Force National Security Space Launch Program or NSSL. The Space Force recently opened up the RFPs for the program, Program Next Lane 1 on-ramp, which will see us compete to qualify for a share of up to $5.6 billion of national security launches.

There is an unnerving bottleneck in the medium launch market currently, creating a risk for National Security. Bringing new launch capability to NSSL, is critical to increasing the DoD's diversity of opportunities, assuring access to space for National Security, and with our proven track record, market-leading design and established infrastructure, Neutron is a pretty compelling choice. We're well past the design phase, now moving into Neutron's build and test campaigns. Keeping our schedule for the first launch next year, puts us inside the 2025 year-end time frame sought by the Space Forces for the next on-ramp.

We brought a new vehicle to market before with Electron, which is a reliably delivered national security payloads to orbit for several years. And with Electron, we reached 50 launches faster than any other commercially developed rocket in history. So we know how to do this and we know how to do this well. Government interest in Neutron's development is ramping up in other areas too. This quarter we're awarded an $8 million study contract with the US Air Force's research lab to showcase our digital engineering prowess with Archimedes. This contract has a tie-in with the NSSL program, as well where it includes the option to expand our digital engineering processes and further build the digital engineering framework for NSSL Phase 3 Lane 1 launch providers.

This contract is a bit of a win-win when it comes to defense industry partnerships. It not only allows the US Air Force to collaborate with industry leaders like the Archimedes team to help develop and modernize the US Air Force's engineering processes and capabilities, But it also supports smooth integration of Neutron into the NSSL program to more efficiently and quickly provide for some of the nation's most critical missions.

Elsewhere across the DoD, the USTRANSCOM has extended our 2022 research agreement that allows us to continue to explore point-to-point cargo delivery with Neutron. And we've recently received confirmation from the US Space Force's -- Space Systems Command that Neutron can now compete for missions under OSP-4, a near $1 billion indefinite delivery and definite quantity contract that were on ramp to a few years back.

All right, moving on now to Neutron's development progress and some of the technical milestones we've hit this quarter. We're well past the design phase now and deep into the qualification testing of our large-scale flight hardware. Starting with the reusable captive fairing for Neutron, or as we like to call it, the Hungry Hippo, these fairing halves remain attached to Neutron's first stage for the full flight, simply opening to release the payload and the second stage before closing back and returning back to Earth with the rest of Stage 1 ready for another flight.

These fairing halves will soon be going through their mechanical testing before assembly and integration onto the large-scale composite panels and the seven-metre-wide barrels that make up the first stage. Another big milestone was the recent successful test of the second stage. We conducted its first Wet Dress Rehearsal in a flight configuration, going through the pressures, mechanical loads, processes, and procedures that would be seen in flight operations. Part of the test campaign included onboard avionics, taking command and control of the stage and demonstrating pressurization, fill, drain, and [cold-float] (ph) operations. This has been one of the biggest integrated milestones yet, proving out not only the flight hardware, but also the supporting infrastructure to operate the vehicle.

We have flight hardware in production for all other Neutron composite structures, including the barrels and domes for the vehicles for a stage propellant tank. All of the internal propellant management devices, the avionics are on track for integration for Stage 1 tank before it goes through the same set of test -- and test campaign as the second stage has just done.

Now onto Archimedes. We've talked about it before, our approach before with Archimedes, and how we were strategic in taking our time to bring a flight-ready engine to the test stand. That means we could hit the ground running to qualify it rather than mess around with early prototypes needing lots of design tweaks and changes and manufacturing that would ultimately slow the program down. But seeing that strategy really pay-off in these past few months. Our engine test cadence in Mississippi has doubled over the quarter, and we've bought multiple engines to the test stand.

The thing to point out here, too, is the rocket engine program is never a one-and-done scenario. Archimedes engines will go through short burst tests, full duration hot fires and tweaks, all the way up to Neutron's first flight. So far, though, we have continued to see strong performance from the Archimedes, and we're able to iterate updates rapidly, which is really what we want to be in this point in time in the test campaign. All that to say is that the cornerstone of any rocket program depends on how quickly and reliably you can scale engine production in parallel.

I know I've said it before, but it bears repeating because building your first rocket engine is hard. Building it 10, 20, 50 times at that pace that can keep up with demand is even harder. With that in mind, we continue to scale production for Archimedes at the same time that we're testing it. We've got the assembly line in California humming with engines shipping out the door frequently to Mississippi, setting us up well to get into a good launch cadence with Neutron after first flight.

A rocket program is much more than just a vehicle, of course, and its engines. Launch infrastructure is a critical component and one of the pieces that we've had a bit of practice to, thanks to having stood up three pads on two hemispheres with electrons. Launch sites are a little bit like an iceberg. There's so much of the infrastructure that is underground or hidden in the development phase. With that now well established, we're starting to put the finishing touches on the above ground of the structure, including a massive 165-ton steel structure launch mount that will hold down mechanisms. It's from this structure that Neutron will lift off next year. The launch mount will be installed in LC3 in the coming few weeks. And from there, the focus will start to shift to Pad commissioning before Flight 1.

On the ground at launch complex 3, some really big long lead items have made their way to the Pad at Wallops Island, including two 90,000 gallon propellant tanks that were installed in Q3. Each of them is longer than one of our electron rockets, which really helps put into perspective the scale of the works that are happening at LC3. Just a few miles up the road from the launch pad, we've completed the construction of the assembly and integration and test building, where Neutron's vehicles will go through their final checks before they're taken to the launch pad.

Having this building only 3 miles from the launch pad is a real strategic advantage for us as we don't have to grapple with the slow and expensive complex logistics of transporting a hulking rocket across the country just to get to the launch pad. That wraps up the headline items on the launch front, so now moving into space systems. So one of NASA's flagship missions is the Mars Sample Return Program, which aims to bring scientifically selected samples from Mars -- back from Mars to Earth, for the first time in history. But NASA has said that their current architecture is too costly at $11 billion and too slow, with the samples not expected to be into the hands of scientists until 2040.

So the agency put out a call to industry for new proposals, and I'm proud to confirm we were selected to conduct the study. We're putting forward a highly compelling concept that will return Mars rocks faster and at a fraction of the cost -- of the current cost of the program. This mission is one of the biggest most ambitious projects NASA has ever undertaken. It will completely change the way that we think about our solar system, potentially answer whether life ever existed on Mars and help prepare for the first human explorers on the red planet.

While it might not be obvious at first glance, it's a mission that we're actually uniquely suited to. Now our fingerprints are already all over Mars. Our technology has been incorporated into missions like the Mars Insight Lander, the Ingenuity Helicopter, and even the cruise stage that brought Perseverance to Mars, enabling the very rovers that are collecting samples to be brought to -- samples brought to Earth under the Mars Sample return. From orbiters and rovers, landers, crew stages, we have experience in delivering mission success on the red planet.

Now everything we've put into place over the years, either through our own organic development or through acquisitions of some of the industry's leading technology suppliers, has been part of our methodical strategy to offer vertically integrated solutions for complex missions just like these. Mars Sample Return requires an immense depth of experience and capability, the very kind that our team and technologies have delivered on before. We have the expertise in building and launching small rockets from little planets. We have, the innovative Mars spacecraft. We have demonstrated re-entry capability. We've enabled rendezvous and proximity missions, where leaders in guidance, navigation control, and our flight software is already on Moon landers.

And we know how to manage large and complicated missions, including ones for NASA. We've shown time-and-time again that we're disruptors in the industry who are able to conduct missions beyond Earth's orbit on a rapidly fast development timelines. And whenever they can't do it, we can do it at a fraction of the traditional cost. We look forward to delivering this once again from Mars Sample Return should a proposal make it through the selection process later this year.

Now on to other updates across our Space Systems business. Before I dive into more specific mission updates, I want to provide a quick snapshot of just some of the various programs underway. This one is just a -- this is just the latest lineup of spacecraft we're building right now or have already completed, Like our 2 ESCAPADE spacecraft for Mars, two completely different constellation spacecraft, one for cell connectivity for MDA Globalstar, the other for National Security and the Space Development Agency, and other individual technology test missions ranging from connectivity in space to cryogenic fuel storage on orbit.

Beyond these missions and constellations, we continue to do strongly in our merchant space systems business with mega constellation contracts too. Some of you will remember me talking about scaling up our satellite facilities in California, as we bring on new and bigger spacecraft contracts. Well, part of the benefit for us taking over the previous Virgin Orbit building for pennies on the dollar for our new engine production site, was it allowed us to use that extra space in our headquarters to be converted to our satellite production facility. We're really starting to see that strategy pay dividends with production lines of our various spacecraft platforms now up and running.

Without -- or without a single shovel in the ground, we've avoided all the headaches of having to build new buildings and factories from scratch and save precious time and resource in a scaling strategy. And the beauty of having all those space systems products co-located in one building in one building, there are simple ease of integration for our teams. A technician can literally walk across the floor, hand over an avionics box to a spacecraft integration team as opposed to waiting for months for a supplier to produce it, ship it and then deliver it. It's really the true beauty of [vertical] (ph) integration for our business.

Now on to some more specific program updates under the Space Systems umbrella. And if I can stick with Mars for just -- the Mars thing for just a little bit longer, in Q3, we completed and delivered the two spacecraft for the ESCAPADE Science Mission to Mars for NASA. It was a really monumental feat in itself given the 3.5 year time span handed to us to deliver this mission. Unfortunately, however, outside our control, the rocket, the satellites we're launching on wasn't quite ready in time for that Mars transfer window. So the mission has been somewhat delayed. But the team is standing by and ready to support once the new launch date is set.

On to our $500 million prime contract with the Space Development Agency for their tranche to transport layer constellation. The team is hitting some great technical targets within the program. The preliminary design of the spacecraft complete, the work being pulled the work can begin pulling the hardware together in the clean rooms at headquarters. This progress puts us in a strong position for the upcoming, solicitation of 200 satellites under the Tranche 3 of the SDA's program, a procurement process expected to begin in 2025.

And finally, to wrap up, space systems and next two satellites for Varda Space Industries have been completed and are now ready for launch. Pioneer class space satellites host Varda's capsule and provide power, communications, propulsion, and altitude control for the mission. It's our first spacecraft for Varda to help bring the capsule back home from space, landing it in the Utah desert last year with our next spacecraft set to do the same thing again but this time over Australia where both missions are set to re-enter the Earth's atmosphere and land in southern Australia soon after launch next year. In the meantime, the team is already working on the fourth pioneer spacecraft for the same Varda mission.

And before I hand it over to Adam, I just wanted to wrap up with a couple of personnel changes at the board and executive level for this past quarter. So Mike Griffin has finished up on the Rocket Lab board after a four-year, ten-year serving the company. We're incredibly grateful for his experience and leadership helping guide Rocket Lab's growth from a private start-up to a global industry leader in launch and space systems and really want to thank him and wish him all the best, as he retires from Rocket Lab's board.

But as one chapter ends, another two begin at Rocket Lab across board and executive level. This quarter we welcomed Frank Klein to the team as our new Chief Operations Officer. Frank joins us with 30 years of international manufacturing experience and leadership in the Automotive Industry at Daimler, Mercedes-Benz, and most recently a prominent EV company. As a COO, Frank is leading our efforts to scale global manufacturing of our spacecraft, launch vehicles and spacecraft components. And it's great to have a seasoned and experienced leader like Frank bring his wealth of knowledge in lean manufacturing and scaling to Rocket Lab.

And Ken Possenriede also joined us on the Board of Directors this past quarter. He joins Rocket Lab after a 35-year career at Lockheed Martin in financial leadership positions, including serving as the Space Prime's Chief Financial Officer. Ken's deep aerospace and defence industry experience combined with his financial leadership adds to even more horsepower on an already impressive board lineup and it's fantastic to have him on board to help us shape the future.

So with that I'll hand it over to Adam now to provide further commentary and to discuss our financial highlights and outlook. Over to you Adam.

Adam Spice

Great. Thanks Pete. All right. Third quarter 2024 revenue was $105 million, which was at the high end of our prior guidance range and reflects significant year-on-year growth of 55%, driven by strong contribution from both business segments but led by space systems. Our launch services segment delivered revenue of $21 million in-line with our prior guidance. Our current backlog continues to support our 2024 target average revenue per launch of $7.5 million, with some quarterly variability tied to volume purchase commitments, launch location, and mission assurance requirements.

Our space system segment delivered $83.9 million in the quarter, near the high end of our prior guidance range of $79 million to $84 million, reflecting sequential growth of over 9%, driven primarily by a strong quarter from our space solar business. Now turning to gross margin. GAAP gross margin for the third quarter was 26.7% in-line with our prior guidance range of 25% to 27%. Non-GAAP gross margin for the third quarter was 31.3%, which was also in-line with our prior guidance range of 30% to 32%.

Relatedly, we ended Q3 with production related headcount of 964, up 50 from the prior quarter. Now turning to Backlog. We ended Q3 2024 with $1.05 billion of total backlog with launch backlog of $326 million and space systems backlog of $721 million. [We're over to] (ph) Q3 of last year, total backlog increased 80% or $465 million, primarily due to our $515 million contract awards about 18 spacecraft for the FDA, we won last year. Sequentially, there's a slight remixing of our backlog, as a result of particularly strong bookings in our launch segment.

We continue to cultivate a healthy pipeline including multi-launch deals and large satellite manufacturing contracts that can create lumpiness in our backlog growth given the size and complexities of these opportunities. We expect approximately 50% of current backlog to be recognized as revenues within 12 months.

Turning to operating expenses. GAAP operating expenses for the third quarter of 2024 were $79.9 million, up $9.5 million sequentially, which was at the low end of our guidance range of $80 million to $82 million. Non-GAAP operating expenses for the third quarter were $68.7 million, up $10.2 million sequentially, which was also at the low end of our guidance range of $69 million to $71 million. The sequential increases in both GAAP and non-GAAP operating expenses were primarily driven by continued growth in headcount and prototype spending to support our Neutron development program, related infrastructure IT support for Neutron, and our SDA satellite contract.

In R&D specifically, GAAP expenses were up $7.8 million quarter-on-quarter due to Neutron prototyping, materials, and headcount growth. Non-GAAP R&D expenses were up $8.1 million quarter-on-quarter, driven similarly to GAAP expenses. Q3 ending R&D headcount was 776, representing an increase of 103 from the prior quarter. In SG&A, GAAP expenses increased $1.7 million quarter-on-quarter, largely due to an increase in outside services related to legal and IT, With IT spend largely related to security and cyber requirements under our SDA contract, and legal spend driven by a range of corporate initiatives, including corporate development as we continue to look to scale the business organically and inorganically.

These legal and IT increases are paired with an increase in staff costs. Non-GAAP SG&A expenses increased $2.1 million, driven similarly to the GAAP SG&A expenses. Q3 ending SG&A headcount was 300, representing an increase of 27 from the prior quarter. In summary, total third quarter headcount was 2,040, up 180 heads from the prior quarter. Now moving to non-GAAP free cash flow and adjusted EBITDA.

With regards to cash, purchases of property, equipment, and capitalized software licenses was $11 million in the third quarter of 2024, a decrease of $4.3 million from the $15.3 million in the second quarter of 2024. We continue our investment in Neutron research, testing, and production infrastructure projects along with expansion of our satellite production and space solar solutions capacity and we do expect our capital expenditures to increase over the next few quarters.

Cash consumed from operations was $30.9 million in the third quarter of 2024 compared to $13 million in the second quarter of 2024. The sequential increase of $17.9 million was driven primarily by increased Neutron and Space Systems program spend and lumpiness in Space Systems Program milestone receipts, partially offset by improved launch contract cash collections.

Overall, non-GAAP free cash flow, defined as GAAP operating cash flow less purchases of property, equipment, and capitalized software in the third quarter of 2024 was a use of $41.9 million compared to $28.3 million in the second quarter of 2024. While we were doing better versus our targeted cash consumption run rate, we do expect to pick up in cash consumption in the next few quarters, owing to an increased expected increase in Neutron spending ahead of our mid-2025 launch and lumpiness in large space systems milestone payment collections.

The ending balance of cash, cash equivalents, restricted cash, and marketable securities was $508 million, as of the end of the third quarter of 2024. We exit Q3 in a strong position to execute on our organic expansion initiatives as well as inorganic options to further vertically integrate our supply chain with the critical capabilities and expand our addressable market consistent with what we've done successfully in the past. Adjusted EBITDA loss was $30.9 million in the third quarter of 2024 compared to a loss of $21.2 million in the second quarter of 2024.

The sequential increase of $9.7 million was primarily driven by increased spending related to Neutron development. With that, let's turn to our guidance for the fourth quarter of 2024. We expect revenue in the fourth quarter to range between $125 million and $135 million. This range reflects a step up in space systems and an increase in launch cadence consistent with our prior outlook. In the past, we've broken down guidance by launch and space system segments. However, we found it difficult at best to predict launch customer readiness within a quarter and believe that providing a single top-line guidance number is more appropriate at this time, given the resilience we've witnessed as a result of the expanded diversification of our business. That said, we'll continue to report actual revenues and related gross margins of launch and space systems as distinct segments.

We expect fourth quarter GAAP gross margin to range between 26% to 28% and non-GAAP gross margin to range between 32% to 34%. These forecasted GAAP and non-GAAP gross margins reflect improved mix within our space system segment, primarily within satellite manufacturing, as well as better overhead cost absorption in our launch business. We expect fourth quarter GAAP operating expenses to range between $84 million and $86 million and non-GAAP operating expenses to range between $75 million and $77 million.

The quarter-on-quarter increases are driven primarily by continued Neutron investment in the staff costs, prototyping and materials. We expect fourth quarter GAAP and non-GAAP net interest expense to be $1.5 million. And we expect fourth quarter adjusted EBITDA loss to range between $27 million and $29 million and basic shares outstanding to be approximately 501 million shares.

And with that we'll hand the call over the operator for questions.

Question-and-Answer Session

Operator

[Operator Instructions] Your first question comes from the line of Andres Sheppard with Cantor Fitzgerald. Your line is open.

Andres Sheppard

Hey, everyone. Good afternoon and congratulations on the quarter. Certainly a lot of developments, so well done. I guess first question, just on the Neutron, I just wanted to clarify. So it sounds like you're, the target for the first launch is unchanged for mid-2025, but the multi-launch agreement that you disclosed today, that's targeted for, I believe, to start in middle of 2026. So I guess A, just wanted to confirm that, and B, then if that's the case, why announced this contract today, just given where you still are on the Neutron development? Any color there would be helpful. Thank you.

Peter Beck

Yeah, hey, Andres. Happy to take that question. So I think we've been pretty clear about what we expect for Neutron's launch cadence to be. So obviously, one test flight in the following year three, and then five, and then continue to seven and beyond. And that's following pretty much the same scaling rate as we saw that we could do with Electron and quite frankly I mean if you look back through history, it's pretty difficult to see any examples of a scaling rate faster than that.

So that kind of backs into real available slots. So as we're talking to customers, obviously they want to know when is their launch slot because they have certain mission objectives from their end. Of course we want to know are their spacecraft going to be ready. I think we've talked about this in the past. So it's really just a careful marry up of various customer requirements and also the launch slots that we've made available to customers. And as we say on the call, we're very selective about those -- especially those early slots.

We need to make sure that we're there on time, we need to make sure that they're on time. So we're kind of easing into that kind of gently. With respect to announcing it now, I think it's fairly material that once we start signing a Neutron contract, I think it's been anticipated. So I think it was a material thing that we really would have to disclose.

Adam Spice

Yeah, and I would add to that, too, Andres, that we've talked about the fact that, as you start to approach Neutron readiness, you think about a timeframe of kind of 12 months, 18 months where you want to have your customer lined up because you got to -- again, have this whole synchronization to make sure that the rocket's ready. There's a long time between signing a contract usually and getting the actual payload integrated and launched. So I think the timing roughly worked out to that. And then I also think it's important that, what We've also said, and I think Pete's been very, very consistent in this, that we're not going to be selling heavily discounted Neutron launches just because it's a new vehicle.

We bring a lot of heritage to this market because of the 54 successful launches that we've had with Electron. And so it really did put us in a really good position to again not be out there kind of you know having to do heavily discounted launches just to gain credibility. So I think this was a definitely an important milestone for the company to reach and we're very happy to be able to announce that today.

Andres Sheppard

Thanks guys you know that that's super helpful I appreciate all that context. Maybe just a quick follow-up, if I may. Can you maybe just remind us, what are the outstanding maybe catalysts or milestones for the Neutron development that you think investors should be aware of. And additionally maybe if you can give us a little more granularity on the hot fire test and the production of the additional engines there. Thank you.

Peter Beck

Yeah, sure. Sure, Andres. The best way I like to explain it is, and we tried to do a little bit of that in this presentation, was you need to think of it as three kind of pillars. One you have launch infrastructure and that's actually where the majority of the capital flows into. And the things that everybody should be watching there is stuff being built. Quite simply, steel going in the ground, concrete being poured and things that look like a launch site. Now thankfully that's relatively easy to follow because it's sitting on the coast and it's relatively easy to get information on that. And of course, we provide good updates.

So as long as steel is being built and shipped and propellant lines are running and all the rest of it, then you can feel pretty good about that. And then the second pillar is kind of structures. So you've seen full Stage 2 tanks and flight configurations running during wet dresses, fairings, first stage tanks. So as long as you keep seeing all those large structures, I think you can see that we're on track. And they all come together relatively late in the piece for an end-to-end wet dress rehearsal.

And then with Archimedes, we're in a test and qualification campaign. So what we're doing with that engine is we're finding, it's called a run box basically, is we're finding all of the operational conditions of that engine and defining what they are.

So we have a desired run box and then we'll have an actual run box. And what we're looking to do is changing various intake pressures of the propellants and various operating points and really understanding the engine and what kind of idiosyncrasies that it may or may not have. So the Hot Fire campaign reached a really important milestone last quarter, where we put a production engine that was full of all production components, valves, hardware, software, and we took it to over 100% throttle level. So I think that was a really important milestone. Working from that, it's just all about accumulating test time, putting the engine into unknown conditions, and continue to evolve the engine and increase its performance over time.

And I sort of made comment in the script here that like an engine program, it's a long process. Yep, you can make fire and you can achieve kind of preliminary targets and milestones, but you're always looking to improve either manufacturing or performance or reliability of an engine over many, many years. So I think we're in a good spot, but those are the three things for folks to track.

Andres Sheppard

Wonderful. I really appreciate all that color. Congrats again on the quarter. I'll pass it on.

Peter Beck

Thanks, Andres.

Operator

Your next question comes from the line of Edison Yu with Deutsche Bank. Your line is open.

Edison Yu

Hey, thank you for taking our questions and also congrats. I know you're not saying too much on the Neutron award, but maybe I could kind of ask from a different perspective. Can you provide any context in terms of what you want relative to if the customer had already placed the launch with someone else and they switched you? Or do they have other kind of maybe like soft contracts out there with other launch providers? Just is this, I know you say you could launch a whole thing, just some context around currently what is the piece that you have?

Peter Beck

Yeah, I mean look, we probably can't say too much, but it's a customer that we know. And as I mentioned, we were very strategic, in especially these early launches, about who we want to almost essentially partner with on these early contracts. So look, I mean, it's not my business to get into their kind of business, but needless to say, we were happy with that particular customer, and it's a good customer for the stage and phase of the program.

Adam Spice

And Edison, maybe little more context to that. So as we've talked about in the past, there just are not that many companies in our space that have executed in a position to launch with a level of confidence. So you've got the added dynamic that there's a range of customers out there who, also have payloads that compete with some of the other launch providers. And at this point, we feel probably more comfortable launching with somebody they don't necessarily compete with. So, I think that plays into a lot of the discussions that we have. And I would say that the market remains pretty robust as far as demand is concerned.

When you look at the people that have capacity, a lot of that capacity has been spoken for. So really we think Neutron is coming to market at a great time where we're really filling a new need for incremental capacity, and we're doing it in a way that's really non-competitive and non-threatening with those customers. So just a lot of the stars are starting to align on that for us with regards to Neutron.

Edison Yu

Understood. Then a follow up question a bit longer term. Obviously you've got Frank on board now and he comes from the automotive industry. And curious if you can maybe dimension the kind of scale you're looking for. Obviously automotive is orders of magnitude higher scale than aerospace is frankly coming on Board to kind of take you to much, much higher level or more to kind of get the existing backlog up to speed?

Peter Beck

Yeah, look, a bit of both Edison and we have some components that are at low scale like Mars spacecraft and they're going to be produced at high scale and then we have other things like reaction wheels where we produce thousands and thousands a year of. But the one thing about production, and I can attest to this, is that it all looks the same whether you're building a car or a spacecraft or a rocket, the production fundamentals are always the same.

Now, of course, the numbers that roll-off the end of the production line differ, but all the manufacturing techniques and good practices remain the same. And we've done a great job here, and the team's done an amazing job here at Scaling. But as we look to move even further up that curve, bringing someone on with just such deep experience, not just within production and production scaling but within operations. It was just kind of the right time for the company to create that position.

Edison Yu

Fantastic. Thank you.

Operator

And your next question comes from the line of Matt Akers with Wells Fargo. Your line is open.

Matt Akers

Yeah, hey guys. Good afternoon. Thanks for the question. I wanted to ask about space services. You guys kind of teed that on Slide 4. Just curious. I know you don't want to reveal what that could look like yet but just curious what kind of time frame you had in mind. It seems like you know kind of the Phase 1 and 2 are in pretty good shape so I guess – if you move to phase 3, I mean do we need to get Neutron sort of at a higher production cadence? Are there maybe more parts of the portfolio to fill in? Just curious how you think of kind of the timing there.

Peter Beck

Yeah, thanks Matt. So look, everything is irrelevant without a reusable high cadence launch. So Neutron is really the key to unlocking that. And if you look at Starlink, it's a good example, it's a great spacecraft, but actually the thing that has really made that possible is a high cadence, low cost launch. And that in turn is made possible by a reusable launch vehicle. So until Neutron is flying at some level of cadence, it's kind of academic to talk about deploying constellations.

Matt Akers

Yeah, got it. Okay. And just curious on this Neutron deal or maybe just Neutron in general, thoughts on kind of what the progress payment maybe looks like on that? Just curious, I guess one, if there's maybe some lumpiness in cash flow around that just because those are pretty big dollar items and also just how we should think about kind of the advanced payments versus kind of working capital aspect as that program ramps up.

Adam Spice

Yeah, I can take that one, Pete. So each, we have a fairly standard launch services agreement that we've obviously used many times with Electron and we're leveraging most of that forward on Neutron. And you're right that building this Neutron vehicles, it will be a challenging working capital cycle, at least initially, particularly when you think about the context here of reusability, right? So I think, we've never said that we plan to basically have a fully reusable vehicle for the first launch.

So as we kind of work our way towards full reusability, you know, we'll be getting more kind of benefits from a working capital perspective as we do that. But you know, the first few launches here are certainly going to be, you know, cash consuming. So you can think about the structure. Most of these LSAs have a deposit, and then there's milestone payments. And if you look at our Electron business, typically we've collected about 60% of the contract value by the time we actually start building the rocket. This might be a little bit different because, you know, it's the -- we're at the very early stages of kind of coming transitioning from R&D into production, but you can think of Neutron. Well, it should look very, very, very similar to what we've kind of disclosed and kind of producing our results, as we have with Electron.

So I did nothing too unusual with this one is just yeah -- it's the first few rockets out of the chute, so kind of we got to go through that transition period. And as we experience also on Electron, the Electron you know came out initially with not kind of target margins obviously but as we kind of build towards that, I think that there's a combination of the fact that we'll be collecting payments against milestones in the contracts, but also getting production efficiencies and ultimately reusability, which is a real key to kind of getting Neutron to its target model, which we think will look very similar to the long-term model for Electron. So hopefully that gives you a little bit of context.

Matt Akers

Yeah, that's very helpful. Thank you.

Operator

Your next question comes from the line of Erik Rasmussen with Stiefel. Your line is open.

Erik Rasmussen

Yeah, thanks for taking the questions. And congrats on the progress with Neutron. Maybe just on that subject, Neutron, I know it's not a lot you want to really share at this time, but are you replacing anyone or are you being brought on to sort of, you know, as another alternative just because of, like Adam you said, there's a number of medium rockets that are in the market or that will be potentially in the market in the coming years but is this just sort of you think a hedge because you guys are a lot closer than some others?

Peter Beck

Yeah, I think with respect to kind of commercial contracts and in some cases, definitely replacing. I would say that Erik in the NSSL world, it's bringing on new providers. I think if you look at the last NSSL Lane 1 Phase 3 award, 100% of that award went to one particular launch provider because there was nobody else. So in some cases, it's replacing and in some cases it's just being brought on as a new alternative.

Erik Rasmussen

Okay, and then you stated that the ASPs, you're going to be pretty firm on pricing. Is that the $50 million to $55 million that you initially talked about, and that's sort of where things have settled maybe for these two dedicated missions, and it says you're starting in mid-2026. Would both of those potentially happen in 2026, or how should we think about sort of timing, assuming you do meet the mid-2025 for your first test launch?

Peter Beck

Yeah, I mean the launch pricing as we pointed out is, you know, that was a really important thing for us and I think -- as I've said, I've made, well I kind of [had to] (ph) -- but with Electron it took us years to flush out bad kind of contracts with respect to ASP. So no, this contract is in line with our previously discussed ASP for Neutron. And then we're selling real slots with real launch windows. So we kind of, you know, somewhat at the bequest of the customer. So, you know, so the 2026 timeframes for those launches, are the customers, you know, driven requests.

Erik Rasmussen

Got it. Then maybe just staying with launch. You sitting at 12 launches year-to-date, you previously gave a range of 15 to 18. You have another 1 slotted in the coming weeks, the earliest. You would need sort of four in this quarter to get to the bottom of that range but do you still feel like that's a viable range for you the 15 to 18 where we sit today I appreciate you not giving specific guidance on that but I just want to get a sense of your confidence level on that prior guidance of 15 to 18.

Peter Beck

Well I mean if you recall at the start of the year, we thought we were going to do 22. So I'm always a little bit gun shy on this these days. But no, I think we've got certainly a very busy fourth quarter. And at this stage, the customers are looking good. So I think, we'll be within that range.

Erik Rasmussen

Okay. And then just -- on the NSSL, I just want to clarify the RFPs opened up pretty recently within the last two weeks. Does that mean you'll be available for this particular one or it's the next cycle because of the timeframe of Neutron at the earliest of mid-2025?

Peter Beck

Yeah, the way it works is that you have to demonstrate you can launch in 2025 to be on-ramped, and then once you're on-ramped, then you'll bid for various task orders. So there'll be, you know, this kind of, the task order is separate from the on-ramp and those task orders, you know, are released at the times that NSSL or the Space Force decides to.

Adam Spice

I think, Erik, I think what we're saying that, even though we'll be on ramping in 2025, we wouldn't be awarded any contracts for launch in 2025. And right now we're planning one test launch in 2025. We're talking about three launches in 2026, and then we've talked about five launches in 2027. And given kind of the discussion that we've had, you know, previously about this, the first customer for Neutron that we announced today, that's obviously consuming some of that capacity in 2026. So the most likely scenario is that could you see something in 2026 for NSSL? You know, it's a possibility, but it's probably not the most likely scenario. That probably looks more like it, you know, at 2027, but never seen ever.

Erik Rasmussen

Right. Okay, great. And then just one last thing on the backlog of clarification. The $326 million for launch, Does that include this latest award win for the two for Neutron?

Peter Beck

No, it does not, because that was a Q3 ending, and this contract was signed post the end of Q3.

Erik Rasmussen

Great. Okay. I’ll get back in the queue.

Peter Beck

It will show up in our Q4 backlog.

Erik Rasmussen

Great. Thank you.

Operator

Your next question comes from the line of Suji Desilva with ROTH Capital. Your line is open.

Suji Desilva

Hi, Pete. Hi, Adam. Congrats on the progress and the Neutron success here. The gross margin improvement here, Adam, is that the relative contribution between launch and space systems sequentially in 3Q and 4Q relatively even? And can you give an update on the solar gross margin improvement? Is there tailwinds still there?

Adam Spice

So the gross margin percentages are actually pretty close across. I mean, they're pretty consistent across launch and space systems right now. That's the function of kind of again, where we are in the margin improvement path for the launch part of the business and then just kind of where we are a mix within space systems. So you know -- if you look at the mix of our business being roughly 70% space systems, you know 30% launch, I mean, I think kind of gives you it's all proportional. So you just take the percentage of the business times the same rough margin calculation and just apply it.

Suji Desilva

Okay and then on solar, Adam is that remain a tailwind?

Adam Spice

So solar is -- solar has actually been progressing. It's a little bit slower than we thought. We talked about that on some prior calls where we expected to be at target margins within – which was -- we said about 30% non-GAAP gross margins of that business within two years of the acquisition. So we acquired that business in early 2022. So we're a bit behind, but we're making steady progress. So I would say when we look at our backlog for that business, we're really not booking. I can't remember the last time, maybe Pete can correct that, I can't remember the last time that we've actually booked business lower than our target gross margin. So it's all about kind of replacing, flushing out some of that older, in fact, there's really just one bad contract in the mix that we inherited.

Unfortunately, it was a large part of the -- I think it was almost $100 million of the $150 million backlog at deal close that came along that was basically essentially zero margin. So as we build the new business that target margins are better, that's starting to flow through now. We're seeing that come through in a little bit more profound way. And so I think that -- I think we all have actually probably more conviction now about getting to that 30% better target gross margin for that business. It's just taken us a little bit longer.

And so I think, you know, it's also not too dissimilar to our launch business where it's a very kind of fixed cost oriented business. So when you have a good quarter where you're shipping a lot more product, you get the benefit of that overhead absorption. And so as we mentioned earlier, and we mentioned in our prepared remarks, the solar business is particularly strong in Q3.

Suji Desilva

Okay, great. And then my other questions on the launch business, I understand that Neutron is going to add to the backlog this quarter but Electron growing $55 million. I'm just wondering what that, how that comparison to the last few quarters. Is that kind of in a range or is it accelerating and what the drivers if it is accelerating are? Is it ASP trending up or any color there be helpful?

Peter Beck

Yeah, I have a [crack at] (ph).

Adam Spice

Yeah, go ahead, Pete.

Peter Beck

I have a crack and maybe add a bit more color as well. So launch is lumpy, like actually launching the rockets is lumpy, so is the contracts. And we can go a quarter without signing anything. So as far as historical kind of lookbacks, I mean, certainly this has been a good call for Electron, but it tends to be pretty lumpy throughout.

Adam Spice

Yeah, and if you look at – certainly we book more launches. And again, as Pete said, it's lumpy because we're chasing bigger multi-launch agreements. But also the ASP has been very supportive. So I mentioned earlier that the average selling price for 2024 for Electron works out to be about $7.5 million per launch. And we've also talked on previous calls that our total backlog for Electron is priced at around $8.2 million ASP.

So we're actually doing, we're doing better on booking at higher prices. So that we're having a beneficial ASP mix effect. And that's obviously helping contribute to the backlog growth, but also to what we believe is kind of a nice steady progress towards our target margins for that electron business.

Suji Desilva

Okay. Very helpful. Thanks, guys.

Operator

Your next question comes from the line of Andre Madrid with BTIG. Your line is open.

Andre Madrid

Adam, Peter, thanks for the time. I know we kind of danced around it, but I wanted to just ask more specifically, how much was total Neutron development cost in 3Q? I know previously you said about [$160 million] (ph) for the year or about $40 million a quarter. And also like, is that kind of still an appropriate target looking all in?

Adam Spice

Yeah, I'm scrolling up the number right now. Yeah, no, this in Q3, it was a total -- well, you have to split out between the different elements, but if you look at total net spend for Neutron across OpEx and CapEx, it was just a hair under $44 million.

Andre Madrid

Got it, Got it. Okay. And I think --.

Adam Spice

And that's going to, you know that's going to step up as kind of, as we continue to kind of get towards the first launch. So that's why this first launch of Neutron is so important for us, because that really has such a tremendous impact on the P&L, right? Where we have all of this cost right now just hitting R&D. Once you get past that first test launch and you carry the first paying customer, everything flips over. You've got now R&D associated with it, cost of sales and so forth. So it's a super important thing for us to get that first launch off because it kind of caps that initial spend because you'll have minimum viable product both in the rocket and on the infrastructure side of the house.

And so I think probably along with that, we still feel very, very comfortable that we're within our target original budget for Neutron. And if you think about, we talked, this is going back when we came public, three years ago now, a little over three years ago, we said it was going to take roughly three, four years and cost $250 million to $300 million. And we put that in pretty stark contrast to what some other kind of medium and larger launch vehicles have cost in the many, many billions of dollars and taken the better part of a decade to get to first launch. So we feel like we're on track and we're going to set a new benchmark for capital efficiency and timing of getting a new launch vehicle to the pad.

Andre Madrid

Got it, got it. And if I could squeeze in one more, could you maybe highlight backlog at some of the non-photon space systems businesses like PSC, Sinclair? I mean, how is expansion and acquiring more business progressed at that line of business?

Peter Beck

Yeah, those businesses continue to grow at a pretty healthy clip. If you look at our target growth for the components business within space systems is around 20%. And we feel very comfortable. We've been delivering better than that, considerably better than some parts of our business. I would say that of our components businesses, Sinclair's probably had experienced the most recent growth. And that's driven by, you know, the mega constellation reaction wheel contract that we've talked about in the past that has been starting to shift. But we've seen strength across all of that. If you take it -- in aggregate, we kind of look at it across all of it. And when you look at our merchant business or the components business, there's really two pieces to that. There's the merchant components that we sell into other spacecraft manufacturers. And then there's the integrated or vertically integrated supply element where we're now supplying our own feed, if you will, into these spacecraft manufacturing projects that we've won, like SDA and like the MDA Global Star.

So it's really, it kind of, the growth is fueled not only by overall macro growth in the broader merchant market, but also from our own internal consumption as well. So we feel really good about, continuing a 20% CAGR for that business. I think some will be stronger than others, right? Like this year, I said, we're having more strength in Sinclair and that probably continues through next year. And then, as we look forward into 2025 and 2026, based on a lot of these big programs, you know, we're going to have very good years for our solar too, because, you know, we're dedicating a significant amount of our capacity to internal programs.

And overall, you know, it's actually has a very healthy kind of roadmap, I would say, for gross margin as well. If you look at the components or subsystems business, that's kind of already in the -- I call low to mid 40s, non-GAAP gross margin. And we think there's some upside to that. And then there's just the kind of a little bit of the offset where you have these bigger program gross margin models that are kind of more towards call it 30%. So you've got that blending effect there. But we feel really good about, you know, all the elements of that subsystem business.

Andre Madrid

And since you brought it up, what's the mix between what goes in-house for components versus what's delivered as a merchant supplier? And do you guys have a target mix for first-base systems, I guess?

Peter Beck

Yeah, that's a good question. I don't have that data at the tip of my fingers and I don't really want to try to guess on that. I mean, I think for some of the businesses we have a little bit more visibility. So I'd say for example, I think in our solar business, I think our internal capacity consumption right now is probably only about 10%. So 90% is going out to the merchant market to a lot of the people that sell into the national security market for these exquisite systems.

When you look at the separation systems business, for example, we sell much more externally than we consume internally, just the fact because, it's one of those predominant separation systems that flies on basically all rockets. So really, there really is a mix. But that's a good question. We can certainly follow up offline and see if we can get you more kind of concrete answer to that.

Andre Madrid

Yeah, definitely. I would appreciate that. Adam, thanks so much for the call. I really appreciate it.

Adam Spice

Sure.

Operator

Next question comes from Jason Gursky with Citi. Your line is open.

Jason Gursky

Hey, good afternoon everybody. Pete, I want to -- have you just walk us all through, if you don't mind one more time, why it is that we have to do one, three, and five. And if there isn't an opportunity to go a little faster here, you suggest that, you know, history would suggest with others you got to do it that way, but why is that the case? And Adam, you talked about throwing CapEx. There's some more CapEx coming into the mix here. Is this something we can throw some capital at and speed things up a bit?

Peter Beck

Jason, you asked the question that Adam asked me every day. And there's some things and you can throw as much capital as you want but until you fly you can only learn a certain number of things. And look, [135] (ph) is a pretty good scaling rate at best. And fundamentally you fly your first rocket and you'll do the best job that you think you can. There's a whole lot of stuff you can test on the ground, and then there's a whole lot of stuff you can't test on the ground. And it's just, well obviously, forward build is many of the components that we think in many of the systems and structures as we can. But you can find yourself just in a dead end pretty quickly. But it also just takes time to scale the production line.

And we've tried to front end it as loaded as best we can with the engine production line. Generally the engines are the longest pole in the tent from a production perspective. So we've really leaned into that so hopefully we can do better. But it just takes time to put one on the pad and commission it and learn it and learn from it and then roll those iterations into the next vehicle. And we're flying customers payloads so everything has to be very methodically thought through and every change is well qualified to reach that cadence.

I guess it might be a slightly different story if you had no customers and you just threw everything at it and had a different risk posture. But we're looking to get into commercial operations as quickly as we can. So when you're flying a customer, you can't just kind of be fast and loose. You have to be very methodical in any of the changes that you roll in. So we just don't want to be unrealistic with what's being -- what can tangibly be delivered.

Adam Spice

Jason, I'll be asking Pete that question every day going forward as well.

Jason Gursky

Yeah, if you can do it on my behalf, I appreciate that. And then, Pete, look, 1, 3, and 5, okay, so we've got 6 launches, one's a test. But as you look at the pipeline, I mean, over that time period, if you had more capacity, is there more demand out there? I just want to -- maybe strip out the national security launch just on the commercial side of things. I'm just trying to get a better gauge of supply and demand equilibrium.

Peter Beck

Yeah, well, I mean, that's the fundamental reason why you're asking this question, Adam asked this question, everybody asks this question, is how can we scale faster? And indeed customers. But the worst thing you can do is promise a customer that you're going to be able to provide a whole bunch of launch. They make a big commitment to you and then you don't deliver because that plays a [big part in their] (ph) business. So that's not good for their business or long term relationships or quite frankly, our reputation.

So of -- all the things we worry about, I think we've said before, demand is not one of them. We worry more about how fast can we scale the Neutron rather than other customers there to fly on it for sure. Right.

Jason Gursky

Okay, then last one is for me. I'm just kind of curious. We've got a new administration coming to town. Let's see here. I guess what policy statements have you heard to date that, you know, either have you encouraged or are giving you a little bit of pause. And what would you suggest we hear on the outside, kind of pay attention to here as this transition happens? What are you going to be looking for and looking to hear from the new administration?

Peter Beck

Yeah, it's a really good question. So I think what I take out of it is that I don't think there's ever been such a focus on space from any administration, perhaps back in the Apollo era but I mean it's very clear that this administration has a very strong focus on space which is good and when Space wins, Rocket Lab wins. Also, we see a very strong focus on national security which is obviously a core part of our business. But I guess probably the thing I'm most excited about is there's a real focus on moving away from the kind of slow government contracting and really focusing on commercial providing much more of the traditional space in government services which is really when you think about it there are only a few companies that are really well positioned to take advantage of those commercial opportunities and us being one of them.

So, you know, I look out on the new administration with quite a bullish outlook given those kind of three things.

Jason Gursky

Right. Okay, great. I'll pass the line. Appreciate it.

Operator

And your next question comes from the line of Michael Leshock with KeyBanc Capital Markets. Your line is open.

Michael Leshock

Hey, thank you. I wanted to ask on space systems. You've talked about both organic and inorganic ways to scale the business. We're just hoping for an update there on the M&A pipeline, whether you see any new opportunities. And then secondly, you also have those organic initiatives like additional clean room capacity that you already have the footprint for. I'm just wondering if you could provide some more details there and how much is left to go on those initiatives. Thanks.

Peter Beck

I can take a swing at this Adam and maybe you can follow it up. On the organic stuff, we always have a number of new products and things in development. Some of those are spin-offs from some of the programs that we're developing. Some of them are just areas that we think there's a market opportunity for and the way we kind of talk about those is obviously you've seen in the past product releases from us.

So that will – when we have something that we think is ready, then we'll release it. And I think we have a pretty strong reputation that we release it when it's done. We don't kind of talk about it until really it's done. And you saw that with even reaction wheels or something like the haste missions, you know, we announced a haste mission and then a number of weeks later we launched one. So that's kind of the way we roll with organic product development. And then inorganic, you know, we always maintain a pretty healthy pipeline and maybe, Adam, you can provide a bit more comment on that.

Adam Spice

Yeah, I'd say on the corporate development front, we continue to look at a lot of assets out there. I think that one thing is we're very selective, right. I think if you look at the assets that we've acquired in the past, the team is always at the center of it. If you look at the fact that you pick any one of the deals, they've always been leading products in their area. You pick from solar where they've had a single failure on orbit to bring new kind of innovative capabilities to the market through the software capabilities for command and control software for ASI and separation systems from TSC and so forth.

So it's really, I would say we continue to look at things and we've largely gotten the bus, the satellite bus into the point where we have most of the capabilities there that we think that we need to be kind of that -- to fulfill the end-to-end requirements there. There's still a few little things here and there that we're working on. And we're actually trying to address those, and some of those organically as well, not just inorganically, but probably the biggest missing piece to space systems from that's going to be filled likely through inorganic is going to be on the payload side.

So we really kind of stop at the payload right now. And certainly as we've talked many, many times about our grander ambitions of having our own applications on orbit, that's going to be benefited by having our own internal capabilities around the payload side of the system. So, you know, there is, fortunately for us, there's actually quite a few assets out there that are quite interesting that are kind of, I'd say poised to be part of a much bigger, you know, consolidated platform like we're building. So I think there is ample opportunities there, but we're very disciplined. It's got to be the right team. It's got to be the right time. It's got to be the right price. And so far we haven't gotten those three stars to align, but I'm pretty confident that we'll get some of those stars to align in the not too distant future.

And I think that will also provide a bit of a bread-crumbing for folks to understand a little bit more specifically which applications we're targeting because a lot of the payload is obviously very specific to the application. And so having kind of some insight into kind of the capabilities that we'd be acquiring would kind of give you some ideas about where we're going from an applications perspective, which I know everyone's chomping at the bit to try to understand better.

Michael Leshock

Okay, great. I appreciate all that detail. I'll leave it there. Thanks, guys.

Operator

Your next question comes from the line of Anthony Valentini with Goldman Sachs. Your line is open.

Anthony Valentini

Hey, guys, thanks for taking my question. You got Anthony on for [NOAA] (ph) tonight. Sorry to beat this point to death here, but it's been pretty well publicized at this point that Amazon's Kuiper has to get over a thousand satellites into orbit, you know, I think by mid-2026. And they have orders with some of your competitors for launch vehicles that either have not launched yet or in very limited cadence.

So I guess my question is, you know, do you guys stand to benefit from that between now and 2026 where you guys can get, you know, a piece of that pie or is it, you know, to what Peter was talking to in an earlier answer, it's just not possible given capacity and how many slots you guys have available?

Peter Beck

Well, I'll put it this way, as we said, Anthony, demand is not something that we worry about and that kind of falls into that category.

Anthony Valentini

Okay, that's helpful. And then, Adam, for you, is the systems segment profitable today?

Adam Spice

Well, you know, we only report our segments down to the gross margin line, and that's because we have a lot of shared resources across the different areas of development and production, so forth, and also we have one key decision maker, which is Pete, who kind of provides the overall kind of investment decisions or mandates across both businesses. So we -- I would say from a technical accounting perspective, we can't say that the space systems businesses is profitable on that level. But we can tell you is that when we look at kind of anecdotally across each of the lines of business, it would be safe to say that the vast majority, if not all, of the cash consuming nature of this business is coming from Neutron.

Right, so I think that's again that's one of the most important things about getting Neutron to minimum viable product in the first launch up. Things will become a lot more clear at that point as in and actually at some level doesn't really matter because then the overall profitability of the company starts to shine through. So, again, I would say that we can't say technically that space systems is profitable because we just don't account for the business at that level right now. That could change in the future, but that's not the current kind of approach we take to it.

Anthony Valentini

Okay. Yeah, that makes a ton of sense. Last one for me here. I just want to confirm the test flight on Neutron in 2025. That’s no revenue. Right.

Adam Spice

Correct. Yeah. There won't be any revenue associated with that launch. But we are working on things that would allow us to have probably some contra revenue, sorry, contra R&D associated with that. So looking to do some creative things there where we can kind of buy down our cost of that test launch. And so that's something that we're working pretty hard towards and hopefully we can get some of that to come into focus.

Anthony Valentini

Awesome. Thank you guys so much. Appreciate the time.

Operator

Your next question comes from the line of Cai von Rumohr with TD Cowen. Your line is open.

Cai von Rumohr

Super, thanks so much. So Adam, your ASPs for Electron have gone down sequentially for three straight quarters and yet your gross margin has improved. Now I know that costs are kind of specific to each mission, but what does that tell us about the underlying core profitability of Electron?

Adam Spice

Yeah, it's really a function of, so when you talk about ASP, the ASP is a function of customer timing, right? And so we have some customers that sign up for many launches and as a result of signing up for these bulk buys, they naturally get a lower price. And we get the benefit of having actually better margins on a lot of those flights, because a lot of the work doesn't have to get redone. All the GNC work that you have to do for each individual flight you don't have to redo that. You get maybe the benefit of having payload adapter plates that are common, you know, across multiple launch deals.

So a lot of what you're seeing, the ASP is again just a function of timing aware that customer [launch plan] (ph) is that we're again we're very comfortable with the number that we set for the year at $7.5 million being the average. And of course, like -- I mentioned before, our total backlog is priced at $8.2 million per electron. So that kind of shows you where it's going. And then the reason why the gross margin has gone up, despite having the optics on the ASP, is because we've been getting production efficiencies, right? So as we've gotten better at building these electrons the cost is coming down, which is helpful for us. So even as ASP may go down, gross margins go up. I think that's kind of the most salient points of kind of the gross margin trend analysis.

Cai von Rumohr

Got it. And the second one is, you started the year, Peter, you mentioned that 22 launches sort of scheduled or targeted and we're going to probably end up at 15 to 18. Have you ever thought, I mean, and one of the big problems is that you commit to a certain price and the customer commits to a certain date, but it's not a hard date. Have you ever thought of a kind of pricing so that if the customer misses, the price goes up? And I know that you have other competitors, but Certainly if you could get your number of launches up, you've made a big point of how high the fixed launch costs are. Is there any thought of kind of getting that volume -- thinking of ways, creative ways of getting that volume up?

Peter Beck

Yeah, I mean, some launch contracts have provisions for penalties. But I mean, if a customer has had a failure of something in a TVAC and then you start loading penalties on them, you know, it's not great for long term relationships. And I think the learning is here for us and I think for everybody as well is that the service that we provide is a bespoke, dedicated service for customers to launch. And they pay the premium for that. You compare an Electron to a Rideshare, it's many, many times higher. So that's what they're paying the premium for.

I guess the point that we try and make is that once a customer goes into backlog and we start collecting the cash from that customer, these customers never go away. They just sort of shift around. It's just a peculiarity of the way that revenue is recognized on launch. So no, I think We continue to play launch whack a mole and wherever possible, like you see, we did in the last quarter, we'll take quick turns business and fill some gaps. But it's kind of really the reality of the service that we provide.

Cai von Rumohr

Terrific. Thank you so much.

Operator

And there are no further questions at this time. I will turn the call back over to Peter Beck for closing remarks.

Peter Beck

Great, and thanks very much for everybody sticking around for the questions as well. Much appreciated. But before we close out today, I just wanted to draw your attention to some of the up and coming conferences we'll be attending. We'll look forward to sharing more exciting news and updates with you there. But that wraps up today's call, and thanks everybody for sticking around and listening to all the progress that's been made. The team is certainly very proud of this quarter and what we've achieved this year. So thanks very much.

Operator

This does conclude today's conference. You may now disconnect."""


if __name__ == '__main__':
    stock = "NASDAQ:RKLB"

    conversation = [
    {
        "role": "user",
        "content": f"Update news of {stock} with {earningcall} with {sheet} and {sheet2} summary in terms of its asset structure and financial health?"
    },
    {
        "role": "assistant",
        "content": f"Financial Overview:\nRevenue: $105M (+55% YoY), just shy of record $106M last quarter.\nBacklog: $1.05B (+80% YoY), split across launch ($326M) and space systems ($721M).\nGross Margins:\nOperating Expenses: $79.9M GAAP ($68.7M non-GAAP).\nCash Position: $508M in cash and equivalents.\nOperational Achievements:\nStrategic and Program Updates:\nSummary in this quarter."
    },    
    {
        "role": "user",
        "content": f"What is the financial quality of {stock} with {sheet} and {sheet2} summary in terms of its asset structure and financial health?"
    },
    {
        "role": "assistant",
        "content": f"### Financial Quality Analysis for {stock}\n\n#### Asset Structure Analysis\n\n1. **Current vs. Non-Current Assets**\n   - **Current Assets Dominance**: If {stock} has a higher proportion of current assets, the focus should be on liquidity analysis. These assets include cash, accounts receivable, and inventory. The liquidity ratios should reflect the company's ability to cover its short-term liabilities comfortably."
    },
    {
        "role": "assistant",
        "content": f"   - **Non-Current Assets Dominance**: A higher share of non-current assets, such as property, plant, and equipment, requires analyzing how effectively these assets generate revenue (e.g., ROA analysis).\n\n2. **Detailed Asset Analysis**\n   - **Composition of Current Assets**: Current assets should primarily consist of cash, trade receivables, and inventory. If there are significant 'other' current assets, this could signal liquidity concerns."
    },
    {
        "role": "assistant",
        "content": f"   - **Accounts Receivable**: If accounts receivable growth significantly outpaces sales growth, there could be issues with collection or potentially inflated revenue.\n   - **Inventory Levels**: If inventory growth exceeds COGS growth, it could indicate obsolescence or inefficiencies in inventory management."
    },
    {
        "role": "assistant",
        "content": f"   - **Intangible Assets**: Large intangible assets compared to total assets might imply expensive acquisitions, raising concerns about the sustainability of return on assets (ROA).\n   - **Fixed Assets vs. Revenue Growth**: An increase in property, plant, and equipment should ideally be accompanied by an increase in revenue, indicating effective use of investment for growth."
    },
    {
        "role": "assistant",
        "content": f"#### Debt Structure Analysis\n\n1. **Debt-Asset Alignment**\n   - **Matching Debt to Asset Structure**:\n     - If {stock} has significant current assets, it should rely more on short-term liabilities. Conversely, if non-current assets are prominent, long-term debt is more appropriate."
    },
    {
        "role": "assistant",
        "content": f"     - If the company has a high proportion of non-current assets but mostly short-term debt, this could indicate improper financing and future liquidity problems.\n   - **Debt Growth vs. Equity Growth**: If debt is growing faster than equity, this could signal an over-reliance on debt and potential solvency issues in the future."
    },
    {
        "role": "assistant",
        "content": f"2. **Debt Ratios**\n   - **Debt-to-Equity Ratio**: A high debt-to-equity ratio (>1.5) may suggest aggressive borrowing, which could be risky if the company’s earnings do not grow proportionally."
    },
    {
        "role": "assistant",
        "content": f"#### Equity Analysis\n\n1. **Accumulated Losses**: If {stock} has significant accumulated losses compared to its registered capital, this indicates prolonged periods of unprofitability in the past.\n2. **Quasi-Debt Instruments**: A large amount of quasi-debt, or hybrid instruments considered as equity, should be analyzed carefully. These are, in reality, debt and could distort the company's leverage."
    },
    {
        "role": "assistant",
        "content": f"#### Conclusion\n{stock} demonstrates [strong/moderate/weak] financial health based on its asset structure, debt management, and overall equity composition. Further monitoring of debt trends and asset utilization will be crucial."
    },
        {
            "role": "user",
            "content": "How does {stock}’s profit and loss statement look, and are there any concerns regarding revenue and profitability?"
        },
        {
            "role": "assistant",
            "content": "### Profit and Loss Statement Analysis for {stock}\n\n#### Revenue and Profitability Overview\n\n1. **Revenue and Net Profit Trends**\n   - **Continuous Growth**: Revenue and net profit should show consistent growth over the past several years. A steady increase in gross profit margin, EBIT margin, and net profit margin is indicative of effective cost control and strong pricing power.\n   - **Concerns with Declining Margins**:\n     - **Gross Margin Decline**: Could indicate rising input costs, unoptimized production, or price competition.\n     - **EBIT Margin Decline**: Suggests increased operating costs or reduced pricing power.\n\n2. **Detailed Profit Analysis**\n   - **Gross Profit Margin Consistency**: A stable gross margin over multiple years suggests effective cost management.\n   - **Selling Expenses**: Should ideally grow proportionally with revenue, indicating efficient use of marketing and sales investments.\n   - **Administrative Expenses**: Similar to selling expenses, growth should align with revenue increases.\n   - **Financial Costs**: If financial costs exceed 50% of EBIT, this may indicate over-leverage or a company in the initial phases of a high-cost expansion.\n\n#### Red Flags to Watch For\n\n1. **Decreased Gross Profit Margin**: Could indicate the following problems:\n   - **Cost Volatility**: Rising material costs affecting profitability.\n   - **Underutilization of Production**: Not operating at full capacity.\n   - **Intense Competition**: Price wars or excessive promotions may erode margins.\n\n2. **Increased Inventory and Receivables**: Growth in inventory and accounts receivable beyond revenue growth could indicate inefficiencies in production or collection, respectively.\n\n#### Conclusion\nThe profit and loss analysis suggests that {stock} is [effectively managing/struggling with] its revenue and cost structure. The company’s profitability is [stable/improving/deteriorating], and specific issues such as [increasing financial costs/declining gross margin] should be monitored."
        },
        {
            "role": "user",
            "content": "How does {stock}’s cash flow statement reflect its operational efficiency, and are there any cash flow concerns?"
        },
        {
            "role": "assistant",
            "content": "### Cash Flow Analysis for {stock}\n\n#### Cash Flow from Operations\n1. **Positive Operating Cash Flow**: A positive cash flow from operations suggests that {stock} is generating sufficient cash from its core business activities. This cash can be used for further investment or debt repayment.\n2. **Operating Cash Flow vs. Net Profit**:\n   - **Warning Sign**: If operating cash flow is consistently lower than net profit, this may indicate issues like inflated revenue, increased receivables, or excessive inventory.\n\n#### Cash Flow from Investing Activities\n1. **Investment in Fixed Assets**: Significant investments in fixed assets (like property and equipment) should align with revenue growth to demonstrate effective capacity expansion.\n2. **Red Flag**: If the cash outflow for investments far exceeds depreciation, it could mean over-investment or inefficiencies in capital allocation.\n\n#### Cash Flow from Financing Activities\n1. **Debt Repayment vs. New Borrowings**: Understanding how much cash is going towards debt repayment versus new debt taken can reveal if {stock} is managing its leverage effectively.\n\n#### Key Concerns to Watch For\n- **Negative Operating Cash Flow**: Indicates potential trouble in generating cash from core business, which might lead to reliance on external funding.\n- **Mismatch with Profitability**: A mismatch between cash flow and profitability is an early sign of financial manipulation or inefficiencies.\n\n#### Conclusion\n{stock} has [strong/weak] cash flows, with operational cash flow that is [in line with/exceeding/lagging behind] net profit. Cash flow from investing shows [strategic growth/excessive expansion], and financing activities indicate [appropriate debt management/rising leverage concerns]."
        },
        {
            "role": "user",
            "content": "What are {stock}’s key financial ratios, and how do they indicate the company’s business performance?"
        },
        {
            "role": "assistant",
            "content": "### Financial Ratio Analysis for {stock}\n\n#### Key Ratios for Evaluation\n\n1. **Return on Equity (ROE)**\n   - **Target**: ROE > 5% and consistent.\n   - **Interpretation**: Indicates how well {stock} generates returns on shareholders' equity. A consistent ROE suggests good profitability.\n\n2. **Return on Assets (ROA)**\n   - **Target**: ROA > 5% and consistent.\n   - **Interpretation**: Indicates how efficiently {stock} utilizes its assets to generate profits.\n   - **Concern**: A declining ROA suggests that new investments may not be yielding sufficient returns.\n\n3. **Debt-to-Equity Ratio**\n   - **Target**: < 1.5 for financial stability.\n   - **Red Flag**: If coupled with negative operating cash flows, high debt could signal repayment issues.\n\n4. **Asset Turnover Ratio**\n   - **Analysis**: A declining asset turnover ratio could mean that investments in new assets are not yet producing corresponding revenue growth.\n\n5. **Cash Conversion Cycle**\n   - **Cycle Length**: If the cycle exceeds 75 days, {stock} may require significant working capital, indicating potential liquidity issues.\n\n6. **Working Capital Efficiency**\n   - **Receivables and Inventory Turnover**: Increased days to collect receivables or sell inventory could indicate inefficiencies or liquidity problems.\n\n#### Conclusion\nThe key ratios suggest that {stock} has [strong/moderate/weak] business performance, with specific strengths in [ROE/ROA] and concerns regarding [debt levels/asset turnover]. Monitoring these ratios over time can provide insights into operational efficiency and financial health."
        },
        {
            "role": "user",
            "content": "What is {stock}’s growth potential compared to its industry and market, and how sustainable is it?"
        },
        {
            "role": "assistant",
            "content": "### Growth Potential Analysis for {stock}\n\n#### Industry Context\n1. **Industry Growth Rate**: {stock} operates in an industry that is [growing/stagnating/declining]. Understanding whether {stock}'s growth aligns with the industry can help gauge its market position.\n2. **Company Growth Relative to Industry**\n   - If {stock} grows faster than the industry, it could mean strong market share gains, but growth may slow in the future.\n   - If it grows slower, it may be losing ground to competitors.\n\n#### Financial Indicators of Growth\n1. **Investment in Growth**: Continuous increases in assets such as new facilities or equipment indicate expansion.\n2. **Revenue Growth Consistency**: Revenue growth in line with asset growth implies efficient use of investments to drive growth.\n3. **Stable Margins**: Consistent net profit margins suggest effective internal cost controls during growth phases.\n\n#### Red Flags to Watch For\n1. **Declining ROA**: Indicates that investments are not generating proportionate returns.\n2. **Reduced Asset Turnover**: A decreasing ratio might signal inefficiencies in the utilization of newly acquired assets.\n3. **Net Profit Margin Decline**: Growing expenses that are not matched by revenue increases could indicate a strain from attempting to expand too quickly.\n\n#### Conclusion\n{stock} shows [strong/moderate/limited] growth potential compared to its industry. The company’s recent investments and market positioning indicate [sustainable growth/a need for better efficiency/a risk of declining returns]."
        },
        {
            "role": "user",
            "content": "Is {stock} overvalued or undervalued based on its P/E ratio and other valuation metrics?"
        },
        {
            "role": "assistant",
            "content": "### Valuation Analysis for {stock} with {sheet2} \n\n#### Price-to-Earnings (P/E) Ratio\n1. **Current P/E**: {stock} currently has a P/E ratio of X, compared to the industry average of Y.\n   - **Above 20**: Suggests high market expectations for growth, which could be due to anticipated new products, innovations, or market expansions.\n   - **Below 20**: Could indicate undervaluation or market concerns about growth prospects.\n\n2. **Other Valuation Metrics**\n   - **PEG Ratio**: Evaluates growth-adjusted valuation. A PEG below 1 suggests undervaluation, while above 1 might imply overvaluation.\n   - **Price-to-Book (P/B) Ratio**: Helps assess if the stock price is justified by its book value. A high P/B ratio might indicate overvaluation.\n\n#### Market Sentiment and Concerns\n1. **One-Time Earnings Boost**: If recent profits are due to one-off events (e.g., asset sales or exchange gains), the current valuation might not reflect sustainable earnings.\n2. **Volatility in Earnings**: A fluctuating earnings history could lead to a higher risk perception, thereby impacting valuation.\n\n#### Conclusion\nBased on its P/E ratio and other metrics, {stock} appears to be [overvalued/undervalued/fairly valued]. Market optimism (or pessimism) seems to be driven by [recent developments, industry trends, competitive advantages, or risks]. Investors should consider both growth potential and the consistency of earnings when evaluating {stock}’s valuation."
        },
    ]

    title_dict = {
        "title": f"Comprehensive Stock Analysis Report for {stock}",
        "sub_title": "Evaluating Financial Quality, Profitability, Cash Flow, Growth Potential, and Valuation"
    }

    
    run_generation(
        conversation=conversation,
        title_dict=title_dict,
        user_name="Dhouchdhanin Lee",
        llm=os.getenv('LLM', 'gpt'),
        apply_section_dedup=True
    )
