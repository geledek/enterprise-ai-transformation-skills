# Air Canada Chatbot (Bereavement Fare)

**Year:** Deployed pre-2022 → tribunal ruling February 2024 → chatbot disabled
**Mode pitched:** Augment / deflect
**Outcome:** Failure — legal liability established; chatbot disabled on the affected pathway

## Story

Air Canada deployed a customer service chatbot on aircanada.com as a routine 24/7 self-service tool. The pitch was quiet and unambitious — no bold claims about replacing agents, simply cost reduction through deflection.

In November 2022, passenger Jake Moffatt asked the chatbot about bereavement fares after his grandmother's death. The chatbot stated he could book a flight at full price and apply for a bereavement refund within 90 days. He did so. Air Canada then refused the refund, pointing to its actual policy, which requires bereavement discounts to be applied before booking.

Moffatt took Air Canada to the British Columbia Civil Resolution Tribunal. Air Canada's defense — that the chatbot was "a separate legal entity responsible for its own actions" — was rejected. The tribunal ruled Air Canada must honor the policy its chatbot stated. Damages were small (CAD $812.02) but the precedent was significant: companies are legally accountable for their AI's statements. Air Canada disabled the chatbot shortly after.

## Diagnostic

**Q1 — Real Friction?** Mildly friction-first. Customers genuinely wanted faster answers to common policy questions. Pain was understated but real.

**Q2 — Right Solution Mode?** Officially Augment, operationally Replace on policy questions. The operational-mode check fails — when the bot stated a refund policy, no human reviewed the answer before the customer relied on it. Critical condition: bot must never state policy not in its source of truth. Not met.

**Q3 — Value Accumulates?** Productivity tool only. Tracked metrics (deflection rate, CSAT) did not include policy-statement-error rate, which was the metric that mattered legally.

**Verdict:** Partial Pass — concept fine, guardrails missing. The framework correctly flagged the operational mismatch.

**One change:** Constrain bot to retrieval-grounded answers from a versioned policy KB. Refuse confidently rather than improvise.

## Why it matters as a reference case

Air Canada is the canonical "operationally-Replace-while-officially-Augment" failure. The bot was pitched as a self-service convenience but was, in the moment of failure, the company speaking to the customer with no human between them. Use this case when a pitch describes "AI assistant" or "deflection bot" but the AI's outputs are statements the customer will rely on — that is Replace, regardless of the language in the deck.

It is also the canonical liability precedent. Companies own their chatbots' outputs. The "separate legal entity" defense does not work.

## Sources

- [Moffatt v. Air Canada, 2024 BCCRT 149](https://decisions.civilresolutionbc.ca/crt/sd/en/525448/1/document.do)
- [Washington Post, February 2024](https://www.washingtonpost.com/travel/2024/02/18/air-canada-airline-chatbot-ruling/)
