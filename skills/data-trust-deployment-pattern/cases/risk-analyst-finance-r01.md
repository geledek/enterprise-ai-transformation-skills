---
title: "r01 — Credit Memo Assistant on MNPI: Singapore Mid-Tier Finance"
type: skill-case
skill: data-trust-deployment-pattern
participant: r01
sector: financial-services
jurisdiction: SG (MAS-regulated, PDPA, cross-border restrictions)
date: 2026-06-11
verdict: Conditional (Azure OpenAI SG-tenant recommended; ChatGPT Enterprise conditional; consumer ChatGPT BLOCKED)
---

> One-line summary: A MAS-regulated risk analyst wants to draft credit memos with three years of internal credit committee minutes — material non-public information (MNPI) plus customer PII. The deployment pattern that survives MAS Notice 655 + PDPA cross-border rules is a private-tenant Azure OpenAI deployment in Singapore region with customer-managed keys, not the consumer ChatGPT she's already pasting redacted minutes into.

# r01 — Credit Memo Assistant on MNPI: Singapore Mid-Tier Finance

## Persona / Setup

**Participant:** r01, Risk Analyst, mid-tier corporate lending firm headquartered in Singapore (~S$4B AUM, ~180 staff, MAS-licensed under the Banking Act / Finance Companies Act).

**Survey response (quoted):**
> "Effective AI use using proprietary data to improve productivity while retaining confidentiality. Right now I'm spending 6–8 hours per credit memo and most of that is restating committee minutes into the standard template. I tried ChatGPT but compliance shut it down."

**The job-to-be-done.** Draft first-pass credit memos for the Credit Committee. Inputs: last 3 years of credit committee minutes (~2,400 documents), client financials, RM call notes, and external rating reports. Output: a ~12-page memo in the firm's standard template with risk rating, exposure summary, covenant proposal, and dissent log.

**The data she wants to feed the model:**
- Credit committee minutes (MNPI on listed and unlisted obligors, names of directors discussed, dissent attribution by committee member)
- Customer financials (private companies, including beneficial owner data — PDPA personal data)
- RM call notes (often contain individual borrower personal circumstances — PDPA + potentially "sensitive" under PDPA Advisory Guidelines)
- Internal risk ratings and watchlist status

**What she's currently considering** (from intake call):
1. ChatGPT Enterprise (US-hosted, SOC 2, no training on her data per Enterprise terms)
2. Azure OpenAI Service in the Singapore region with private endpoint
3. A self-hosted Llama 3 70B deployment in their existing AWS VPC (Singapore region)

**What she's actually doing today.** Pasting redacted minutes into consumer ChatGPT on her personal laptop "because IT blocks it on the work machine." This is the shadow-AI problem we have to solve in parallel with the main verdict.

**Compliance context:**
- MAS Notice 655 (Cyber Hygiene) + MAS Technology Risk Management Guidelines (Jun 2021 update)
- MAS Guidelines on Outsourcing (cloud as outsourcing — Annex 2 cloud-specific obligations)
- MAS FEAT Principles (Fairness, Ethics, Accountability, Transparency, 2018)
- MAS / IMDA Veritas Phase 2 toolkit (FEAT assessment methodology)
- PDPA (2012, 2020 amendments — mandatory data breach notification, 30-day window if ≥500 individuals or significant harm)
- PDPC Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (Mar 2024)
- IMDA Model AI Governance Framework for Generative AI (May 2024)
- Cross-border transfer: PDPA s.26 + Transfer Limitation Obligation — receiving jurisdiction must offer "comparable" protection or contractual safeguards (SCCs/BCRs equivalent)

## Applying the Data-Trust Deployment-Pattern Skill

We work the four dimensions in order, then synthesize.

### Dimension 1 — Data Sensitivity Classification

Walk every input through the classification ladder: public / internal / confidential / regulated.

| Data element | Class | Regime | Notes |
|---|---|---|---|
| Credit committee minutes | **Regulated — MNPI** | SFA Part XII (insider trading), MAS market-conduct expectations | Discussions of listed obligors are MNPI; dissent attribution is reputationally sensitive |
| Beneficial-owner data | **Regulated — PII** | PDPA + AML/CFT (MAS Notice 626) | Names, NRIC/passport fragments, addresses |
| RM call notes | **Regulated — PII (sensitive-adjacent)** | PDPA — health/financial-distress mentions trigger Advisory Guidelines | Often contain "borrower's wife is undergoing chemo, requesting standstill" — sensitive |
| Internal risk ratings | **Confidential** | Contractual + MNPI-adjacent | Could move market if leaked for listed obligors |
| Standard memo template | **Internal** | None | Format only |
| External rating-agency reports | **Confidential (licensed)** | Vendor licence terms (Moody's/S&P) | Most licences prohibit ingestion into third-party AI training |

**Classification verdict for the corpus as a whole:** **Regulated.** The dataset is dominated by MNPI and PDPA personal data. The whole pipeline must be designed to the regulated tier — you cannot "average down" by counting the template pages.

### Dimension 2 — Deployment-Pattern Map

Five-tier map, with the sensitivity class that each tier can lawfully and prudently host:

| Tier | Pattern | Highest sensitivity class permitted | r01 candidates |
|---|---|---|---|
| T1 | Public consumer SaaS (consumer ChatGPT, Gemini free, Claude.ai free) | Public only | **Consumer ChatGPT — BLOCKED** |
| T2 | Enterprise SaaS w/ DPA (ChatGPT Enterprise, Claude for Work, Gemini for Workspace) | Internal, Confidential (case-by-case for Regulated with strong controls) | **ChatGPT Enterprise — conditional** |
| T3 | Private-tenant cloud (Azure OpenAI, Bedrock, Vertex with regional pinning + CMK + private endpoint) | Regulated (with control stack) | **Azure OpenAI SG — recommended** |
| T4 | VPC self-host (Llama / Mistral / Qwen on the firm's own cloud account, no model-vendor data path) | Regulated (highest) | **VPC Llama — viable but high TCO** |
| T5 | Air-gapped on-prem | Regulated + sovereign / state-secret | Not required here |

**Why T1 is BLOCKED.** Consumer ChatGPT (a) trains on inputs by default unless the user toggles it off and the toggle is per-session brittle, (b) has no DPA the firm has signed, (c) routes to US infrastructure with no contractual cross-border safeguard the firm has executed, (d) cannot satisfy MAS outsourcing-as-cloud requirements because there is no outsourcing agreement, exit plan, or audit right. Pasting redacted minutes does not cure the breach — re-identification risk on a 2,400-document corpus is non-trivial, and the act of transfer itself is a PDPA s.26 issue.

**Why T2 is conditional.** ChatGPT Enterprise has a signed DPA, SOC 2 Type 2, and contractual no-training. But:
- Default residency is US. OpenAI's data-residency-in-region offering (announced Feb 2024, expanded through 2025) covers some APAC regions but Singapore residency for ChatGPT Enterprise specifically requires confirmation per workspace — not a default.
- Sub-processor list includes Microsoft Azure (US) and others — the firm's MAS outsourcing register must be updated and each sub-processor risk-assessed.
- For MNPI, the audit-right and incident-notification clauses in the standard ChatGPT Enterprise DPA are weaker than what Azure OpenAI offers under the Microsoft Online Services DPA + Financial Services Amendment.

**Why T3 is the recommended landing zone.** Azure OpenAI in the Singapore region (Southeast Asia) gives:
- Data residency in SG (the model-serving and content filtering happen in-region; abuse-monitoring data path can be opted out via the Limited Access Modified Abuse Monitoring program for eligible regulated customers)
- Customer-managed keys (CMK) via Azure Key Vault
- Private endpoint / VNet integration — no public ingress
- Microsoft's Financial Services Compliance Program + the MAS-specific compliance addendum
- The vendor is already on the firm's MAS outsourcing register for M365 and Azure infra — material risk assessment is incremental, not greenfield

**Why T4 is viable but not chosen.** Self-hosting Llama 3 70B in their AWS SG VPC eliminates the model-vendor data path entirely. But: the firm has no MLOps team, no eval harness, no red-team capability, and the latency/quality gap on long-context credit-memo drafting is meaningful. TCO for a usable deployment (2× p4d or equivalent + ops) is ~S$40–60k/month before headcount. T3 gets to value in 6–10 weeks; T4 in 6–9 months.

### Dimension 3 — Control Stack Selection

The minimum control set for the chosen tier (T3, Azure OpenAI SG-region) — mapped to NIST AI RMF MEASURE / MANAGE functions and IMDA Model AI Governance Framework for Generative AI.

#### 3.1 Logging
- All prompts + completions logged to a customer-owned Azure Log Analytics workspace in SG region, retained 7 years (MAS record-keeping)
- Per-user attribution via Entra ID (no shared service principals for end-user calls)
- Immutable storage (WORM) for the audit log container
- NIST AI RMF: MEASURE 2.7 (model performance + provenance), MANAGE 4.1 (incident response readiness)

#### 3.2 DLP (egress + ingress)
- Microsoft Purview DLP policies on the gateway: block egress of NRIC patterns, account numbers, SWIFT codes, and a bespoke "MNPI marker" regex that the credit-ops team maintains (e.g., the watchlist-ticker syntax)
- Ingress DLP on prompts: same policies, applied before the prompt hits the model, with a "review queue" rather than hard-block for borderline cases (the analyst is allowed to override with a reason code that is logged)
- IMDA GenAI Companion: aligns with "Data" pillar — provenance + DLP

#### 3.3 Redaction
- Pre-prompt Presidio-based redaction pipeline running in-VNet: replaces NRIC, names of natural persons, phone numbers with stable pseudonyms before the prompt is sent. Pseudonym map is held in a separate SG-region Key Vault and never sent to the model.
- Post-completion re-identification step (optional, for the analyst's eyes only) reverses the pseudonyms client-side.
- Critical: this is **defence in depth**, not a substitute for tier choice. Redaction does not move MNPI down a tier — committee deliberation is MNPI even with names redacted.

#### 3.4 Access Scope
- RBAC at the index level: only the credit-risk team's Entra group can query the credit-memo index. Other AI use cases (HR, marketing, legal) live in separate indexes with separate keys.
- Conditional Access: device compliance + Singapore IP range + MFA. No personal-laptop access.
- Just-in-time elevation for the index admin role (PIM).
- NIST AI RMF: MANAGE 2.3 (access control on AI system components).

#### 3.5 Retention
- Prompts and completions: 7 years (MAS s.199 record-keeping equivalent for risk-management records).
- Vector embeddings of source minutes: tied to the source document's existing retention schedule (committee minutes are 10-year retained). Re-indexing on document destruction.
- Abuse-monitoring data on the Microsoft side: opt out of human review via Limited Access Modified Abuse Monitoring program, document the approval letter in the MAS outsourcing file.

#### 3.6 Cross-Border
- Primary inference path: stays in SG region. Document this in the PDPA Transfer Impact Assessment.
- Failover: explicitly disabled (no automatic failover to a non-SG region). If SG region is down, the service is down — the firm prefers degraded availability over silent cross-border transfer.
- Sub-processors: full list reviewed against MAS Outsourcing Guidelines Annex 2; any US-located sub-processor (e.g., for telemetry) must have a documented PDPA-comparable safeguard (Microsoft's EU SCCs + supplemental measures, accepted by PDPC in prior guidance, applied here by analogy).
- PDPC Advisory Guidelines on AI (Mar 2024): document the lawful basis for using personal data — "legitimate interests" exception with the prescribed assessment, since consent from every borrower is impractical.

#### 3.7 Model + Output Controls (additive, IMDA GenAI Companion)
- Content filters at Azure OpenAI default + custom blocklist for known dissent-attribution phrases.
- Grounding: retrieval-augmented generation against the curated minutes index only — no open-web tools.
- Human-in-the-loop: the model produces a draft; the analyst signs off; the Credit Committee chair approves. The model output is never the system of record.
- Eval harness: 50 historical memos, blind-graded by two senior risk officers monthly, tracking factual accuracy, completeness against template, and any hallucinated obligor facts. Threshold: <2% factual error rate to remain in production.
- IMDA GenAI Companion pillars touched: Accountability, Data, Trusted Development, Incident Reporting, Testing & Assurance.

### Dimension 4 — Shadow-AI Suppression

The hardest part of this engagement. r01 is already pasting redacted minutes into consumer ChatGPT on her personal laptop. If we ship the Azure OpenAI deployment without solving the shadow-AI problem, we'll have two systems and the leak surface will grow.

#### 4.1 Sanctioned-Tool Catalogue
Publish a one-page internal catalogue:
- **Approved for MNPI/PII work:** Azure OpenAI SG (credit-memo assistant), M365 Copilot (general productivity, with the firm's existing tenant controls)
- **Approved for internal/confidential, not MNPI:** ChatGPT Enterprise (the firm holds a small seat count for non-credit teams)
- **Blocked:** consumer ChatGPT, Claude.ai (consumer), Gemini consumer, Perplexity consumer, any AI feature in browser extensions

#### 4.2 Conditional-Access Policy
- Entra Conditional Access blocks `chat.openai.com`, `claude.ai`, `gemini.google.com` (consumer) on managed devices.
- Defender for Cloud Apps (MCAS) blocks the same domains on unmanaged devices that touch corporate data.
- Network egress logs reviewed weekly for new shadow-AI domains; the catalogue updates monthly.

#### 4.3 Enterprise vs Consumer Mapping (the explainer page that goes to staff)
| If you want to… | Use this | Not this |
|---|---|---|
| Draft a credit memo from minutes | Credit Memo Assistant (Azure OpenAI SG) | Anything else |
| Summarize a public news article | M365 Copilot or ChatGPT Enterprise | Consumer ChatGPT |
| Translate a Mandarin contract clause | M365 Copilot | Google Translate web |
| Generate Python for a one-off analysis | M365 Copilot in VS Code | Copy-pasting code with client data into consumer tools |

#### 4.4 Amnesty + Replacement
- 30-day amnesty: anyone admits prior shadow-AI use, no disciplinary action, in exchange for full disclosure of what data was sent and a pseudonym-rotation exercise on any affected clients.
- Replace before you block: the credit-memo assistant must be live before consumer ChatGPT is hard-blocked, otherwise users will route around the block (mobile hotspot, personal phone). r01 specifically named this as her risk: "if you block ChatGPT before giving me something else, I'll just do the memos by hand and miss deadlines."

## Synthesis

> **DEPLOYMENT PATTERN VERDICT: CONDITIONAL — Approved on T3 (Azure OpenAI, Singapore region) with the control stack below. ChatGPT Enterprise (T2) is conditional fallback only for non-MNPI workloads. Consumer ChatGPT (T1) is BLOCKED.**
>
> **CONTROL STACK (required, all of):**
> - Azure OpenAI deployed in Southeast Asia (Singapore) region with private endpoint and customer-managed keys via Azure Key Vault (SG)
> - Limited Access Modified Abuse Monitoring approval on file (no human review of prompts/completions by Microsoft)
> - Pre-prompt Presidio redaction (NRIC, names, account numbers) with pseudonym map held client-side in SG Key Vault
> - Microsoft Purview DLP on ingress and egress with bespoke MNPI-marker policy
> - Per-user Entra ID attribution; RBAC scoped to the credit-risk Entra group; PIM for admin
> - Conditional Access: managed device + SG IP + MFA
> - 7-year immutable audit log in SG Log Analytics
> - RAG-only grounding (no open-web tools); content filters + custom blocklist
> - Human-in-the-loop sign-off; model output never system of record
> - Monthly eval against 50 historical memos; <2% factual-error threshold
> - Shadow-AI suppression: sanctioned catalogue + Conditional Access block on consumer AI domains, sequenced after the assistant goes live
>
> **REGULATORY CITATIONS:**
> - MAS Notice 655 (Cyber Hygiene) — controls 4.1, 4.4
> - MAS Technology Risk Management Guidelines (Jun 2021) — sections on cloud, third-party risk, audit logging
> - MAS Guidelines on Outsourcing — cloud as outsourcing; Annex 2 cloud-specific obligations; outsourcing register update required
> - MAS FEAT Principles (2018) + Veritas Phase 2 toolkit — fairness/ethics/accountability/transparency assessment for the credit-memo use case
> - SFA Part XII — insider-trading boundary on MNPI handling
> - PDPA s.26 + Transfer Limitation Obligation — cross-border safeguards documented in TIA
> - PDPA Mandatory Data Breach Notification — incident-response runbook tied to 30-day / ≥500-individual threshold
> - PDPC Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (Mar 2024) — lawful-basis assessment, "legitimate interests" exception applied
> - IMDA Model AI Governance Framework (2nd ed., 2020) + Model AI Governance Framework for Generative AI (May 2024) — pillars on Accountability, Data, Trusted Development, Incident Reporting, Testing & Assurance
> - NIST AI RMF 1.0 — MEASURE 2.7, MANAGE 2.3, MANAGE 4.1
>
> **CONDITIONS for status to remain Approved:**
> 1. Quarterly review by the firm's Outsourcing Committee
> 2. Annual independent assurance over the control stack (SOC 2 of the firm's wrapper services, not just Microsoft's)
> 3. Eval-harness factual-error rate stays under 2%; if breached, service is paused until re-baselined
> 4. Any sub-processor change by Microsoft triggers a 30-day re-assessment under MAS outsourcing notification expectations

## Why This Matters

The intuitive answer to r01's problem is "use ChatGPT Enterprise, it has a DPA." That answer is wrong in this jurisdiction for this data, and getting it wrong is the difference between a productivity win and a MAS Section 55 inspection finding. The skill forces the analyst to separate three things that get conflated in vendor pitches: data residency (where the bytes sit), processing locus (where inference runs), and contractual safeguard (what the DPA actually obliges). ChatGPT Enterprise has the third in good shape and the first two in negotiated shape; Azure OpenAI in SG has all three by default plus the firm's existing MAS-outsourcing paperwork covers most of the lift.

The shadow-AI dimension is what most playbooks skip and what bites every regulated firm. r01's behaviour — pasting redacted minutes into consumer ChatGPT on a personal laptop — is rational from her seat: she has a deadline and no sanctioned tool. Blocking without replacing converts a documented, auditable shadow-AI flow into a more clandestine one. The sequencing in the verdict (build the assistant, then amnesty, then block) is the only sequence that actually reduces leak surface; any other order grows it.

Finally, this case demonstrates why the four-dimension structure earns its keep over an ad-hoc "is this safe?" review. Dim 1 forces an honest read of the corpus (MNPI dominates, you don't get to average down). Dim 2 forces a tier choice before vendor selection (T3, then pick among T3 vendors — not "ChatGPT vs Azure" framed as peers when they're different tiers). Dim 3 makes the controls comprehensive instead of cherry-picked. Dim 4 closes the human-behaviour loop. The verdict at the end is short because the work was done in the dimensions.

## Sources

- Monetary Authority of Singapore, Notice 655 — Cyber Hygiene. https://www.mas.gov.sg/regulation/notices/notice-655
- MAS, Technology Risk Management Guidelines (Jun 2021). https://www.mas.gov.sg/regulation/guidelines/technology-risk-management-guidelines
- MAS, Guidelines on Outsourcing (incl. Annex 2 — Cloud). https://www.mas.gov.sg/regulation/guidelines/guidelines-on-outsourcing
- MAS, FEAT Principles (2018). https://www.mas.gov.sg/publications/monographs-or-information-paper/2018/FEAT
- MAS / Veritas Consortium, Veritas Phase 2 Whitepaper + Toolkit. https://www.mas.gov.sg/news/media-releases/2022/mas-led-industry-consortium-publishes-assessment-methodologies-for-responsible-use-of-ai-by-financial-institutions
- Personal Data Protection Act 2012 (rev 2020), Singapore. https://sso.agc.gov.sg/Act/PDPA2012
- PDPC, Advisory Guidelines on Use of Personal Data in AI Recommendation and Decision Systems (1 Mar 2024). https://www.pdpc.gov.sg/guidelines-and-consultation/2024/02/advisory-guidelines-on-use-of-personal-data-in-ai-recommendation-and-decision-systems
- IMDA, Model AI Governance Framework for Generative AI (May 2024). https://aiverifyfoundation.sg/resources/
- IMDA / AI Verify Foundation, Model AI Governance Framework (2nd ed., 2020). https://www.pdpc.gov.sg/help-and-resources/2020/01/model-ai-governance-framework
- NIST, AI Risk Management Framework 1.0 (Jan 2023). https://www.nist.gov/itl/ai-risk-management-framework
- Microsoft, Azure OpenAI Service — Data, privacy, and security. https://learn.microsoft.com/azure/ai-services/openai/concepts/data-privacy
- Microsoft, Limited Access Features — Azure OpenAI (Modified Abuse Monitoring). https://learn.microsoft.com/azure/ai-services/openai/concepts/abuse-monitoring
- OpenAI, Enterprise Privacy & Data Processing Addendum. https://openai.com/enterprise-privacy
- Securities and Futures Act 2001, Part XII (Market Conduct), Singapore. https://sso.agc.gov.sg/Act/SFA2001
- Microsoft, Purview Data Loss Prevention overview. https://learn.microsoft.com/purview/dlp-learn-about-dlp
- Microsoft Presidio (PII detection / anonymization). https://microsoft.github.io/presidio/
