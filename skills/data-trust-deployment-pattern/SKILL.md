---
name: data-trust-deployment-pattern
description: Use when matching enterprise data sensitivity to AI deployment pattern, deciding whether a use case can run on consumer ChatGPT vs enterprise SaaS vs VPC vs air-gapped, suppressing shadow AI, or specifying the control stack required per data class. Phrases like "can we use ChatGPT for this?", "is this data safe for an enterprise SaaS LLM?", "what controls do we need for PII/PHI in this AI workflow?", "consumer-tier vs enterprise-tier tool — which one applies?", "shadow-AI is everywhere, how do we sanction tools?", "what deployment pattern fits regulated data?" all trigger this skill. Maps each data sensitivity class to one of five deployment tiers, names the minimum control stack per tier under NIST AI RMF / ISO 42001 / EU AI Act, and outputs a deployment-pattern verdict (Approved / Conditional / Blocked) with a control checklist and regulatory citations.
---

# Data-Trust Deployment Pattern

A four-dimension assignment of data sensitivity class to deployment pattern with explicit per-tier controls. Anchored to NIST AI RMF (GOVERN/MAP/MEASURE/MANAGE), ISO/IEC 42001, EU AI Act risk tiers, and IMDA Model AI Governance Framework + GenAI Companion.

Empirical anchor: BCG 88/25 — 88% of organizations use AI broadly, only 25% capture material value; the gap is largely a data-trust and deployment-pattern gap, not a model gap. MIT 95% — most enterprise GenAI pilots fail to reach production, and shadow-AI usage runs ~2x sanctioned usage in the surveyed cohort.

---

## Dimension 1: Data Sensitivity Classification

Core question: What class of data does this workflow actually touch — and which regulatory regime governs it?

Classify the data INPUT, the data IN-FLIGHT (prompt + retrieval), and the data OUTPUT separately. The most sensitive of the three sets the tier.

CLASS LADDER (assign one):
1. **PUBLIC** — already published; no confidentiality cost if exposed.
2. **INTERNAL** — non-public business data, low individual harm if leaked (org charts, internal docs, generic SOPs).
3. **CONFIDENTIAL** — commercially sensitive (M&A, pricing, source code, unreleased product, supplier contracts, legal privilege).
4. **REGULATED** — named regime applies. Identify which:
   - **PII** under GDPR (EEA), PDPA (SG), CCPA (CA)
   - **PHI** under HIPAA (US health) — requires BAA
   - **PCI-DSS** (cardholder data)
   - **MNPI** under MAS (SG financial), MiFID II (EU), SEC Reg FD (US)
   - **Student records** under FERPA (US education) / equivalent
   - **Cross-border transfer** triggers — GDPR Chapter V, China PIPL, India DPDP

DIAGNOSTIC QUESTIONS:
1. **What is the worst single record in the prompt?** (One PHI record drags the entire workflow into the regulated tier.)
2. **Does retrieval pull regulated data even when the user does not type it?** (RAG hit on a confidential index = confidential prompt.)
3. **Does the output get stored, indexed, or fed back as training data?** (Storage class follows the highest-class input.)
4. **Which jurisdiction's regulator can fine us for this dataset?** (Name the regulator, not the country.)

Output:
DATA CLASS | REGULATORY REGIME(S) | JURISDICTION + REGULATOR | CROSS-BORDER FLAG

---

## Dimension 2: Deployment-Pattern Map

Core question: Which of the five deployment tiers does this data class permit?

FIVE TIERS (least to most isolated):

- **T1 — Public consumer SaaS** (ChatGPT free/Plus, Gemini consumer, Claude.ai personal). Provider may train on input. No DPA. No tenant isolation.
- **T2 — Enterprise SaaS with DPA** (ChatGPT Enterprise/Team, Gemini for Workspace, Claude for Work, Copilot M365). Contractual no-train, signed DPA, SOC2/ISO 27001, regional residency options.
- **T3 — Private-tenant cloud / hyperscaler-hosted model** (Azure OpenAI, AWS Bedrock, Vertex AI, SageMaker). Model runs in tenant subscription; data stays in tenant; no provider training.
- **T4 — VPC self-host / dedicated** (Bedrock provisioned, Azure OpenAI PTU in private VNet, self-hosted Llama/Mistral/Qwen on tenant GPUs, NVIDIA NIM in customer VPC).
- **T5 — Air-gapped / on-prem** (no egress; on-prem GPU; sovereign cloud; classified networks; SCIF-equivalent).

PERMISSION MATRIX (minimum tier required):

| Data Class | Min. Tier | Notes |
|---|---|---|
| Public | T1 | T1 acceptable; T2 preferred for auditability |
| Internal | T2 | Block T1 if logging or compliance asks for audit trail |
| Confidential | T3 | T2 only with explicit legal/IP review and no-train DPA |
| Regulated PII (GDPR/PDPA) | T3 | T2 acceptable IF residency + DPA + DPIA done |
| Regulated PHI (HIPAA) | T3 with BAA | T2 only if BAA signed; otherwise T4 |
| Regulated MNPI / privileged | T4 | Bank/legal default; T5 if regulator requires no egress |
| Sovereign / classified | T5 | Air-gapped only |

EU AI Act overlay: if the use case is high-risk (Annex III) or GPAI with systemic risk, the deployment pattern must support Art. 12 logging, Art. 14 human oversight, and Art. 26 deployer obligations regardless of tier.

Output:
ASSIGNED TIER | TIER JUSTIFICATION | EU AI ACT RISK TIER | EXCEPTIONS REQUESTED

---

## Dimension 3: Control-Stack Selection

Core question: What is the minimum control set this tier requires under NIST AI RMF MEASURE/MANAGE and ISO 42001?

CONTROL STACK (per tier — minimums, not maximums):

LOGGING + AUDIT:
- T1: not acceptable for audited workflows.
- T2: tenant-side prompt/response log retained per record schedule; admin console export.
- T3-T5: full prompt/response/tool-call/identity log; immutable store; SIEM integration.

DLP + REDACTION (pre-prompt):
- T2+: regex + ML DLP on egress; redact PII/PHI/PCI before send; block clipboard-class secrets.
- T3+: policy engine inline (Presidio, Nightfall, Microsoft Purview, Cloudflare AI Gateway).

ACCESS SCOPE:
- Role-based access on the model endpoint AND on retrieval indexes.
- ABAC on RAG corpora — user can only retrieve documents they could already read.
- Per-agent identity (machine identity, not shared API key).

RETENTION:
- T1: assume indefinite retention by provider — disqualifying for anything beyond Public.
- T2: zero-day or per-DPA; verify in admin settings.
- T3-T5: tenant-controlled; tied to record retention schedule.

CROSS-BORDER:
- Pin region. GDPR: EU residency or SCCs + TIA. PDPA: SG residency or transfer impact assessment. China PIPL: in-country processing for personal info.

NIST AI RMF MAPPING:
- GOVERN 1.1 — policies for data class + deployment tier mapping documented.
- MAP 4 — data and model risks identified pre-deployment.
- MEASURE 2.7 — privacy risk measured; MEASURE 2.10 — security risk measured.
- MANAGE 2.4 — documented "off" path; MANAGE 4.1 — incident response.

ISO 42001 mapping: Annex A controls A.6 (data), A.7 (resources), A.8 (impact). IMDA GenAI Companion: provenance, data quality, third-party assessment.

*Consult `nist-rmf-functions.md` for the four-function mapping and `pwc-20-item-checklist.md` for the deployer checklist items.*

Output:
LOGGING SPEC | DLP/REDACTION SPEC | ACCESS + RETENTION SPEC | CROSS-BORDER POSTURE | NIST/ISO/IMDA CITATIONS

---

## Dimension 4: Shadow-AI Suppression

Core question: How do we kill the consumer-tier-tool-on-corporate-data flow without killing AI adoption?

SANCTIONED-TOOL CATALOGUE:
- Publish a one-page list: for each common task (summarize, draft, code, analyze image), name the sanctioned T2/T3 tool and the data class it covers.
- Map every consumer-tier tool to its enterprise twin: ChatGPT free → ChatGPT Enterprise; Gemini consumer → Gemini for Workspace; Claude.ai → Claude for Work; Copilot consumer → Copilot M365.

CONDITIONAL-ACCESS POLICY:
- Identity-provider rules (Entra, Okta) that block consumer-tier domains from corporate identity.
- Browser/endpoint DLP that blocks paste of classified strings to consumer-tier URLs.
- Network egress policy: log + alert on traffic to consumer AI endpoints from managed devices.

BRING-YOUR-OWN-AI BOUNDARY:
- Personal-device + personal-account use of T1 tools is permitted ONLY for Public-class tasks.
- Any work data on a personal-device T1 tool = policy violation; route to sanctioned T2 instead.

MEASUREMENT:
- Track shadow-AI rate (consumer endpoint hits / total AI endpoint hits) monthly.
- Track sanctioned-tool seat utilization — low utilization is a UX/training problem, not a policy win.

DIAGNOSTIC QUESTIONS:
1. **Which sanctioned tool replaces ChatGPT for our top 5 user tasks?** (If unanswered, shadow AI is rational.)
2. **Is the enterprise-tier license actually deployed to the people who would otherwise use the consumer tier?** (License hoarding by IT = shadow AI guaranteed.)
3. **Do users know the data-class rules in plain English?** (One page or it does not exist.)

Output:
SANCTIONED CATALOGUE STATUS | CONDITIONAL-ACCESS POSTURE | SHADOW-AI RATE | SEAT UTILIZATION

---

## Synthesis: Deployment Pattern Verdict

Consolidate Dimensions 1–4. Write for the deployment decision-maker (CISO + business owner + DPO).

DEPLOYMENT VERDICT: [Approved / Conditional / Blocked]

- **Approved** — data class fits assigned tier; full control stack present; sanctioned-tool path exists.
- **Conditional** — fits tier but one or more controls (DLP, residency, BAA, DPIA, logging) are missing; list the conditions and the owner.
- **Blocked** — data class above tier ceiling (e.g., PHI proposed on T1 or T2 without BAA); MNPI on shared-tenant T2; cross-border transfer without legal basis.

DELIVER:
1. One-line verdict.
2. Assigned tier (T1–T5) with one-line justification.
3. Control checklist — tick/cross against logging, DLP, access, retention, cross-border.
4. Regulatory citations triggered (e.g., "EU AI Act Art. 26 deployer obligations; GDPR Art. 28 processor; HIPAA BAA required; MAS TRM Guidelines §6").
5. Sanctioned-tool replacement if user requested a consumer-tier tool.

CRITICAL BLOCKERS (any one = Blocked):
- Regulated data proposed on T1.
- PHI on T2 without signed BAA.
- MNPI / privileged data on shared-tenant T2 without legal sign-off.
- Cross-border transfer with no SCC / adequacy / PIPL basis.
- No prompt/response logging on a workflow that produces customer-facing or regulated output.

*Consult `eu-ai-act-essentials.md` (Art. 4, 12, 14, 26), `imda-4-dimensions-agentic.md` (technical controls), `isg-data-foundation.md` (data foundation prerequisites), and `ai-stack-layers.md` (where in the stack each control sits).*

Output:
VERDICT | ASSIGNED TIER | CONTROL CHECKLIST | REGULATORY CITATIONS | SANCTIONED-TOOL ROUTE

---

## References

- `nist-rmf-functions.md` — GOVERN / MAP / MEASURE / MANAGE; MEASURE 2.7 privacy, 2.10 security; MANAGE 2.4 off-path.
- `eu-ai-act-essentials.md` — Art. 4 literacy; Art. 12 logging; Art. 14 oversight; Art. 26 deployer obligations; risk tiers.
- `imda-4-dimensions-agentic.md` — technical controls dimension; GenAI Companion provenance + data quality.
- `isg-data-foundation.md` — data-foundation prerequisites that make any deployment tier viable.
- `ai-stack-layers.md` — where logging, DLP, retrieval, and identity controls sit in the stack.
- `pwc-20-item-checklist.md` — deployer-side control checklist items aligned to this skill's output.

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).
