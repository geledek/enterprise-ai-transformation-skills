# McDonald's + IBM Drive-Thru Voice AI

**Year:** 2021 pilot → 2022–2023 expansion to 100+ US locations → June 2024 cancellation
**Mode pitched:** Replace (Automated Order Taker)
**Outcome:** Failure — partnership ended after viral public failures

## Story

McDonald's and IBM partnered to deploy "Automated Order Taker" voice AI at drive-thrus, framed as freeing crew for higher-value tasks and improving order accuracy. McDonald's CEO Chris Kempczinski had earlier described voice AI as a path to "much simpler" operations. The system was rolled out to over 100 US locations through 2022 and 2023.

In late 2023 and early 2024, viral TikTok videos showed runaway orders — including hundreds of unrequested McNuggets added to a single order, bacon added to ice cream, and large amounts of extra items appearing on screens. The failures were filmed inside customers' cars and spread faster than McDonald's could respond.

In June 2024, McDonald's ended the IBM partnership. The company stated it would continue to "explore voice ordering more broadly" with other partners — not abandoning the concept, but acknowledging this specific deployment had failed.

## Diagnostic

**Q1 — Real Friction?** Tech-first with a friction veneer. Drive-thru wage cost and order-accuracy issues are real, but the pitch jumped to AI as the solution rather than scoping the underlying constraints (accents, ambient noise, menu variability).

**Q2 — Right Solution Mode?** Replace, in practice. Crew were technically present as backstop, but the operational-mode check fails — when the speaker delivers a wrong order to a customer's car window, no human stood between the AI and the consequence. Critical condition: order accuracy at or above human baseline across accents, ambient noise, and menu edge cases. Not met.

**Q3 — Value Accumulates?** Could have been an improving solution if McDonald's owned the audio data flywheel — but IBM owned the stack, so the data asset accumulated outside McDonald's. Tracked metrics (orders processed, throughput) did not include viral-incident rate, which is what actually killed the program.

**Verdict:** Fail. Should have been Augment — suggestion shown to crew member who confirms — until accuracy threshold met.

**One change:** Run as crew-assist for 12 months before any customer-facing deployment. Never bypass crew confirmation.

## Why it matters as a reference case

McDonald's is the canonical "blast-radius" failure. Every customer with a phone is a QA tester broadcasting to a global audience. Use this case when a new pitch puts AI output directly in front of the public with a forgiving error tolerance assumption — the public is not forgiving, and failures travel.

## Sources

- [Restaurant Business Magazine — McDonald's ends drive-thru AI test](https://www.restaurantbusinessonline.com/technology/mcdonalds-ends-its-drive-thru-ai-test-ibm)
- [CNBC, June 2024](https://www.cnbc.com/2024/06/17/mcdonalds-ends-ai-drive-thru-partnership-with-ibm.html)
