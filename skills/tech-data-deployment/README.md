# Data-Trust Deployment Pattern

A four-dimension assignment of data sensitivity to one of five deployment tiers, with the minimum control stack and a deployment-pattern verdict.

## What it does

1. Classifies data sensitivity across input, in-flight, and output (Public / Internal / Confidential / Regulated) and names the regulator.
2. Maps the class to one of five deployment tiers (T1 consumer SaaS through T5 air-gapped) using a permission matrix.
3. Specifies the minimum control stack — logging, DLP/redaction, access scope, retention, cross-border posture — keyed to NIST AI RMF, ISO/IEC 42001, IMDA GenAI Companion, EU AI Act.
4. Builds the shadow-AI suppression plan: sanctioned-tool catalogue, conditional-access policy, BYOAI boundary, measurement.
5. Issues an Approved / Conditional / Blocked verdict with regulatory citations and a sanctioned-tool replacement when a consumer-tier tool was requested.

## When to use it

Triggers on phrases like "can we use ChatGPT for this?", "is this data safe for an enterprise SaaS LLM?", "what controls do we need for PII/PHI in this AI workflow?", "consumer-tier vs enterprise-tier — which one applies?", "shadow AI is everywhere, how do we sanction tools?", "what deployment pattern fits regulated data?". Use when matching data sensitivity to deployment pattern, suppressing shadow AI, or specifying the per-tier control stack before a CISO/DPO sign-off.

## What it outputs

- Data class with regulatory regime, jurisdiction + named regulator, cross-border flag
- Assigned tier (T1-T5) with one-line justification and EU AI Act risk-tier overlay
- Minimum control stack: logging, DLP/redaction, access + retention, cross-border posture, with NIST/ISO/IMDA citations
- Shadow-AI plan: sanctioned-tool catalogue, conditional-access posture, shadow-AI rate target, seat-utilization target
- Deployment verdict (Approved / Conditional / Blocked) with critical-blocker checks
- Sanctioned-tool replacement path when a consumer-tier tool was requested

## Example

**Scenario:** Dr. Annie Tay, CIO of HealWell Group (4 hospitals + 11 specialist clinics, ~3,400 beds, Singapore-licensed under PHMC Act / forthcoming HCSA), is sponsoring a clinical-documentation assistant that drafts discharge summaries from de-identified inpatient progress notes. The clinical informatics lead has shortlisted ChatGPT Enterprise, Azure OpenAI in the Singapore region, and an on-prem Llama 3 70B. The CMIO is already running consumer ChatGPT on a "test" account with redacted notes pasted in. Annie needs a verdict before Friday's steering meeting.

**User prompt:**

> Can we run a clinical documentation AI on de-identified inpatient notes? I have three options on the table — ChatGPT Enterprise, Azure OpenAI Singapore region, on-prem Llama. Which deployment pattern is permissible under HSA + PDPA, what controls do we need, and how do I shut down the consumer ChatGPT thing the CMIO is doing on the side? Need this for Friday's steering committee.

**Skill output (excerpt):**

```
DATA CLASS: Regulated — PHI (sensitive sub-class)
REGIME: PDPA + PDPC AI Advisory Guidelines (Mar 2024); HSA / MOH PHMC / HCSA;
        IMDA GenAI Companion (May 2024)
REGULATOR: PDPC + MOH/HSA (Singapore)
CROSS-BORDER FLAG: YES — any non-SG inference path triggers PDPA s.26

DEPLOYMENT TIER MAP
| Tier | Pattern                      | Candidate                  | Disposition         |
|------|------------------------------|----------------------------|---------------------|
| T1   | Consumer SaaS                | CMIO consumer ChatGPT      | BLOCKED             |
| T2   | Enterprise SaaS w/ DPA       | ChatGPT Enterprise         | Conditional (non-PHI only) |
| T3   | Private-tenant cloud         | Azure OpenAI SG            | RECOMMENDED         |
| T4   | VPC self-host                | On-prem Llama 70B          | Viable, defer 12mo  |
| T5   | Air-gapped                   | n/a                        | Not required        |

CONTROL CHECKLIST (T3)
[x] Logging — Azure Log Analytics SG, WORM, 10-yr, Entra-attributed
[x] DLP — Purview ingress/egress + bespoke NRIC/MRN/Singpass policy
[x] Redaction — Presidio + medical-NER pseudonymization in-VNet
[x] Access — RBAC + ABAC on indexes; Conditional Access (managed + SG IP + MFA)
[x] Retention — 10-yr aligned to PHMC R25; failover disabled
[x] Cross-border — SG region pinned; PDPA s.26 TIA on file
[x] HITL — clinician sign-off in Epic; model is decision-support only
[x] Shadow-AI — sanctioned catalogue + Entra CA block on consumer AI domains

SHADOW-AI PLAN
- Sequenced: assistant live (W4) → 30-day amnesty → consumer-domain block (W6)
- Target shadow rate <2% by month 4 (current ~9% from egress logs)
- Seat utilization >70% of eligible clinicians within 90 days

VERDICT: CONDITIONAL APPROVED — T3 (Azure OpenAI SG) for discharge-summary
         T2 ChatGPT Enterprise Conditional for non-PHI workflows only
         T1 consumer ChatGPT BLOCKED
CITATIONS: PDPA s.26; PDPC AI Advisory (Mar 2024); MOH PHMC + Mar 2024 AI circular;
           IMDA GenAI Companion (May 2024); NIST AI RMF GOVERN 1.1 / MAP 4 /
           MEASURE 2.7-2.10-2.11 / MANAGE 2.4-4.1; ISO/IEC 42001 A.6/A.7/A.8;
           EU AI Act Art. 4/12/14/26 (by analogy)
```

**How to read this output:**

- Look at the verdict line and the assigned tier first — if Blocked, stop and read the critical-blocker reasons before debating controls.
- The tier map is the load-bearing artifact: it forces residency, processing locus, and contractual safeguard to be separated rather than conflated as a vendor pitch would.
- The control checklist is a minimum, not a maximum — every unticked box is a condition that must be closed before go-live.
- The shadow-AI sequencing rule (assistant live → amnesty → block) is non-negotiable; reversing it converts a documented exposure into a clandestine one.
- Push back if the regulator named in Dimension 1 does not match where the bytes actually land in Dimension 2, or if Regulated data is being argued onto T1/T2 without DPA + residency + DPIA evidence.

## Sources used

- `nist-rmf-functions.md` — GOVERN / MAP / MEASURE / MANAGE; MEASURE 2.7 privacy, 2.10 security; MANAGE 2.4 off-path
- `eu-ai-act-essentials.md` — Art. 4 literacy, Art. 12 logging, Art. 14 oversight, Art. 26 deployer obligations, risk tiers
- `imda-4-dimensions-agentic.md` — technical controls dimension; GenAI Companion provenance + data quality
- `isg-data-foundation.md` — data-foundation prerequisites that make any deployment tier viable
- `ai-stack-layers.md` — where logging, DLP, retrieval, and identity controls sit in the stack
- `pwc-20-item-checklist.md` — deployer-side control checklist items aligned to this skill's output

Reference files are bundled with this skill — Claude resolves them by filename regardless of install layout (single-skill or plugin).

## Effectiveness

Effectiveness test (2026-06-12): scored 25/25 (Grade B, +5 lift over the strongest baseline of vanilla LLM and kb-ask retrieval). 3-judge unanimous verdict.

See `docs/effectiveness/2026-06-12-skill-effectiveness-report.md` for methodology and the full grade card.
