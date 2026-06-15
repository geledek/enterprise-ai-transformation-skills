# NYC "MyCity" Business Chatbot

**Year:** Launched October 2023 → illegal-advice exposé March 2024 → remained live in beta
**Mode pitched:** Augment (regulatory navigation)
**Outcome:** Failure — bot found giving illegal advice; remained online with disclaimers

## Story

In October 2023, New York City Mayor Eric Adams launched the MyCity Chatbot, built on Microsoft Azure, framed as "a one-stop shop for accessing trusted information from more than 2,000 NYC business web pages." The pitch was friction-first in framing: small business owners struggle to navigate city regulation, and the bot would help them.

In March 2024, a joint investigation by The Markup and The City found the chatbot was telling business owners they could legally do things that were not legal — fire workers for reporting harassment, take tip jars from employees, serve cheese a rat had nibbled, refuse to accept Section 8 housing vouchers. The investigation reproduced the failures across multiple sessions.

Mayor Adams defended keeping the bot live, noting it was in beta and that public feedback was how it would improve. The bot remained online with added disclaimers. The episode became a recurring reference point in regulatory and academic discussions of public-sector AI deployment.

## Diagnostic

**Q1 — Real Friction?** Friction-first in framing, tech-first in execution. Small business regulation is genuinely opaque, but the solution chosen — an LLM paraphrasing 2,000 web pages — was a tech-led answer to a problem better solved by retrieval and citation.

**Q2 — Right Solution Mode?** Replace dressed as Augment. The operational-mode check fails — when the bot stated a regulatory position, no human reviewed it before the small business owner acted. Critical condition: bot must never state legal or regulatory positions outside its source of truth. Not met.

**Q3 — Value Accumulates?** Productivity tool at best. Tracked metrics (query volume, satisfaction) did not include legal-accuracy of responses. Blast radius is severe — the city government issuing wrong legal advice has political and regulatory consequences beyond the individual business owner harmed.

**Verdict:** Fail. Should have been a retrieval system that returned links and quoted excerpts, never a paraphraser.

**One change:** Bot returns links to source pages with quoted excerpts only. Never paraphrases regulation in its own voice.

## Why it matters as a reference case

NYC MyCity is the canonical "government issues wrong advice via LLM" failure. The blast radius is unique to public-sector deployments — the entity making the statement is the same entity enforcing the law. Use this case for any pitch where AI is asked to interpret regulation, policy, or law for an external audience that will rely on it.

It is also a clean example of a tech-first solution in friction-first clothing. The pain was real; the chosen solution was not the right tool.

## Sources

- [The Markup / The City, March 2024](https://themarkup.org/news/2024/03/29/nycs-ai-chatbot-tells-businesses-to-break-the-law)
- [AP News coverage](https://apnews.com/article/new-york-city-chatbot-misinformation-6ebc71db5b770b9969c906a7ee4fae21)
