# 2026 AI Governance Buyer Readiness Report

**Edition:** 2026 launch  
**Last updated:** 2 July 2026  
**Audience:** SaaS, HR tech, fintech, health tech, enterprise AI, legal, compliance, security, product, procurement, and revenue teams  
**Use:** Internal readiness planning, customer diligence preparation, vendor-risk review, board/leadership updates

---

## Important note

This report is informational research and implementation guidance only. It is not legal advice, does not create an attorney-client relationship, and does not determine your obligations under any law or contract. AI regulation changes quickly. Review jurisdiction-specific obligations with qualified counsel before relying on any regulatory interpretation or making compliance decisions.

---

## How to use this report

Fastest path:

1. Build an AI inventory.
2. Apply the risk-tiering framework.
3. Assign owners.
4. Review AI vendors and model providers.
5. Build a customer-facing evidence pack.
6. Run the 90-day readiness sprint.
7. Report KPIs to leadership.

If you have one hour, complete the executive readiness check and AI Inventory Starter Table. If you have one week, complete inventory, risk tiering, and vendor triage. If you have one quarter, run the full 90-day implementation checklist.

---

# 1. Executive briefing

AI governance has become an operating issue for mid-market technology companies. Pressure usually arrives through four channels:

- **Enterprise buyer diligence:** customers ask where AI is used, what data it touches, what vendors power it, and what human oversight exists.
- **Regulatory readiness:** teams need to track EU, U.S. state/local, sector, consumer-protection, employment, privacy, and contract obligations.
- **Vendor-risk management:** companies increasingly rely on AI features embedded in third-party products.
- **Internal adoption:** employees use generative AI and automation tools whether or not a formal program exists.

The goal is to answer five questions without scrambling:

1. What AI systems do we use or provide?
2. Which systems affect people, rights, employment, finance, health, safety, security, or legal obligations?
3. Who owns each system, vendor, policy, and escalation path?
4. What evidence can we provide to customers, auditors, leadership, or regulators?
5. What must we stop, fix, monitor, or document in the next 90 days?

## 10-question executive readiness check

| Question | Yes/No | Evidence location | Owner |
|---|---:|---|---|
| Do we have a current inventory of product, internal, and vendor AI systems? |  |  |  |
| Do we classify AI systems by risk level and business context? |  |  |  |
| Do we know which AI systems affect EU users, customers, employees, or outputs? |  |  |  |
| Do we have a policy for employee use of public AI tools and confidential data? |  |  |  |
| Do we review AI vendors before use or renewal? |  |  |  |
| Do we review high-impact AI use cases before launch? |  |  |  |
| Do sales/customer teams have approved AI diligence responses? |  |  |  |
| Do we have an AI incident escalation path? |  |  |  |
| Do we document human oversight, testing, monitoring, and limitations? |  |  |  |
| Does leadership receive recurring AI governance metrics? |  |  |  |

---

# 2. Regulatory readiness map

## EU AI Act timeline summary

The EU AI Act applies on a phased schedule:

- **2 February 2025:** Prohibited AI practices and AI-literacy obligations began applying.
- **2 August 2025:** General-purpose AI model obligations began applying.
- **2 August 2026:** Most remaining obligations, including many high-risk AI-system obligations, apply.
- **2 August 2027:** Obligations for certain high-risk AI systems covered by Annex I apply.

Reference points to review with counsel: Regulation (EU) 2024/1689, especially Articles 2, 4, 5, 6, 9-15, 16-27, 50, 53-55, 99, and 113. Certain prohibited-practice infringements can carry administrative fines up to €35 million or 7% of total worldwide annual turnover, with different maximums for other categories.

## Practical EU readiness table

| Area | Why it matters | Owner | Minimum artifact |
|---|---|---|---|
| AI literacy | Relevant staff need appropriate AI literacy. | HR + Legal + Product | Training log, policy acknowledgment |
| Prohibited practices | Certain uses are restricted or banned. | Legal + Product | Use-case review checklist, stop-use process |
| High-risk AI | Some systems require risk management, documentation, logging, transparency, human oversight, accuracy, robustness, and cybersecurity. | Legal + Product + Security | Risk classification memo, control map |
| General-purpose AI models | Downstream teams need supplier evidence and data-use clarity. | Vendor Management + Product | Model/vendor diligence file |
| Transparency | Some AI interactions or generated content may require disclosure. | Product + UX + Legal | Disclosure review log, UI copy |
| Monitoring/incidents | Material systems need monitoring and escalation. | Product + Security + Legal | AI incident runbook, monitoring records |

## EU AI Act readiness checklist

### Scope and role

- [ ] Identify whether the company places AI systems on the EU market.
- [ ] Identify whether the company puts AI systems into service in the EU.
- [ ] Identify whether AI-system outputs are used in the EU.
- [ ] For each material system, classify possible role: provider, deployer, importer, distributor, product manufacturer, authorized representative, or other.
- [ ] Review role classification with counsel.

### Use-case classification

- [ ] Identify AI systems used in employment, worker management, education, credit, insurance, health, essential services, law enforcement, migration/asylum/border control, justice, democratic processes, biometric identification/categorization, emotion recognition, safety components, or regulated products.
- [ ] Flag any use case that may be prohibited or high-risk.
- [ ] Document the basis for each classification.
- [ ] Create an escalation path for uncertain classifications.

### Governance controls

- [ ] Adopt an AI acceptable-use policy.
- [ ] Create an AI use-case review process.
- [ ] Define human oversight requirements for high-impact workflows.
- [ ] Define testing, monitoring, and drift review expectations.
- [ ] Maintain logs and documentation for material systems.
- [ ] Create a customer/auditor evidence pack.

### Vendor/model management

- [ ] Identify model providers and embedded AI vendors.
- [ ] Collect vendor documentation, security summaries, subprocessors, data-use commitments, and model limitations.
- [ ] Confirm whether customer data is used for training or fine-tuning.
- [ ] Review contractual commitments and audit rights.
- [ ] Document fallback options for critical vendors.

---

# 3. U.S. AI governance watchlist

The United States remains fragmented across federal agency enforcement, state/local laws, privacy laws, consumer-protection expectations, employment rules, sector frameworks, and contracts.

| Area | Examples to monitor | Why it matters | Readiness action |
|---|---|---|---|
| Employment decision tools | NYC Local Law 144; state employment and anti-discrimination rules | Hiring, screening, ranking, and selection tools may require audit, notice, or bias review. | Inventory employment AI; collect audit and notice evidence. |
| High-risk/consequential decisions | Colorado AI Act implementation and related guidance | Developers/deployers of high-risk AI systems may face risk-management, documentation, and notice expectations. | Flag credit, education, employment, housing, insurance, legal, health, or essential-service workflows. |
| Consumer protection | FTC guidance/enforcement on AI claims, deception, unfairness | Unsupported AI claims and hidden limitations create risk. | Review marketing, sales decks, docs, and disclosures. |
| Privacy/data protection | State privacy laws; sensitive data and profiling provisions | AI often processes personal, sensitive, biometric, employee, or behavioral data. | Map data inputs/outputs, retention, rights, and opt-outs. |
| Sector rules | Finance, health, insurance, education, public sector procurement | Regulated sectors may impose validation, fairness, explainability, audit, and model-risk requirements. | Assign sector counsel/compliance owners. |
| Contracting | Enterprise AI addenda, security questionnaires, DPAs | Buyers increasingly impose AI governance commitments by contract. | Maintain approved responses and evidence pack. |

## U.S. readiness checklist

- [ ] Identify AI use cases affecting employment, credit, insurance, housing, education, health, legal access, essential services, safety, or consumer eligibility.
- [ ] Identify whether outputs make, recommend, rank, score, screen, prioritize, or deny decisions.
- [ ] Identify whether personal, sensitive, biometric, health, financial, children’s, employee, or regulated data is used.
- [ ] Identify whether the system is customer-facing, employee-facing, or internal-only.
- [ ] Identify states/cities where affected users, employees, applicants, customers, or consumers are located.
- [ ] Review applicable obligations with counsel.
- [ ] Maintain records showing testing, oversight, vendor review, notices, and escalation.

---

# 4. AI inventory template

## What to include

Include systems or tools that use machine learning, statistical models, generative AI, natural language processing, computer vision, speech recognition, recommendation/ranking, automated scoring, classification, prediction, or decision support.

Examples:

- Product AI features
- Internal copilots/chatbots
- Customer support automation
- Sales/marketing automation
- HR screening/workforce tools
- Fraud, risk, underwriting, identity, or scoring tools
- Analytics models used for prioritization
- Third-party SaaS with embedded AI
- Model APIs and foundation models
- Custom, fine-tuned, or retrieval-augmented systems

## AI Inventory Starter Table

Copy into a spreadsheet.

| ID | System/tool | Internal/product/vendor | Business process | AI function | Users affected | Data inputs | Data outputs | Vendor/model | Owner | Region | Risk tier | Status | Evidence link |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AI-001 |  |  |  | Summarization/classification/scoring/generation/etc. |  |  |  |  |  |  |  | Proposed/Pilot/Live/Retired |  |

## Discovery process

### Ask function leads

- What tools use AI, automation, scoring, prediction, ranking, generation, or recommendation?
- Are AI features enabled by default in existing SaaS tools?
- Are employees using public AI tools for work?
- Are AI outputs used in customer, employee, applicant, consumer, or regulated workflows?
- Are any AI outputs relied on without human review?

### Review vendor and product records

- SaaS subscriptions and expenses
- Security/procurement intake records
- HR/recruiting tools
- Customer support and CRM tools
- Analytics/data platforms
- Cloud/model providers
- Product roadmap and feature flags
- Help-center pages and sales decks
- RFPs and security questionnaires

---

# 5. Risk-tiering framework

This framework helps triage effort. It is not a legal classification by itself.

| Tier | Label | Description | Default action |
|---|---|---|---|
| 0 | No AI/out of scope | No AI functionality or only deterministic rules. | Record as out of scope if needed. |
| 1 | Low-risk productivity | Internal productivity use, low sensitivity, no material effect on people or customer rights. | Allow with policy, training, and data guardrails. |
| 2 | Operational AI | Supports operations/customer workflows; humans review outputs; limited impact. | Inventory, vendor review, owner assignment, monitoring. |
| 3 | High-impact decision support | Informs, ranks, scores, recommends, screens, or influences outcomes affecting people, money, access, employment, health, legal rights, safety, or regulated services. | Legal review, risk assessment, human oversight, testing, notices, evidence pack. |
| 4 | Restricted/prohibited or potentially regulated high-risk | Potential prohibited practice, high-risk AI system, biometric/emotion/inference use, safety component, regulated product, or formal assessment concern. | Pause pending counsel review; executive approval required. |

## Tiering questions

For each system, ask:

1. Does it make, recommend, rank, score, screen, prioritize, deny, or materially influence a decision?
2. Is the decision related to employment, credit, lending, insurance, housing, education, health, essential services, legal access, public benefits, safety, fraud, identity, law enforcement, migration, or democratic processes?
3. Does it use sensitive, biometric, health, financial, children’s, employee, or confidential customer data?
4. Is it customer-facing or used in a customer deliverable?
5. Are users likely to rely on the output without meaningful review?
6. Could an error cause financial loss, denial of opportunity, reputational harm, safety harm, discrimination, privacy harm, legal exposure, or contract breach?
7. Is the vendor/model a black box with limited documentation?
8. Does it generate content that could be mistaken for human-created or authoritative output?
9. Does it operate in the EU or affect EU users/outputs?
10. Is it part of a regulated product or safety component?

## Risk assessment template

| Field | Response |
|---|---|
| AI system ID/name |  |
| Business owner / technical owner |  |
| Vendor/model |  |
| Use case and intended users |  |
| Affected persons/entities |  |
| Data inputs and outputs |  |
| Decision impact |  |
| Region/user location |  |
| Proposed risk tier |  |
| Reason for tier |  |
| Required controls |  |
| Human oversight method |  |
| Testing/validation performed |  |
| Known limitations |  |
| Monitoring plan |  |
| Incident escalation path |  |
| Legal/compliance review required? |  |
| Approval status and next review date |  |

---

# 6. Function-by-function owner map

| Function | Responsibilities | Evidence produced |
|---|---|---|
| Executive sponsor | Set risk appetite, approve Tier 3/4 use, unblock resources. | Charter, KPI review, approvals |
| Legal | Interpret obligations, review high-risk use, approve disclosures/contracts. | Review memos, clauses, watchlist |
| Compliance/GRC | Maintain controls and evidence. | Control map, policy attestations, audit files |
| Product | Identify product AI, document use, design controls/disclosures. | Product AI documentation, release checklist |
| Engineering/Data | Document models, testing, logs, monitoring, data pipelines. | System cards, test results, monitoring records |
| Security | Review vendor/security posture, access controls, incident response. | Security review, threat model, runbook |
| Privacy | Review data inputs, retention, rights, assessments. | Data maps, privacy assessments |
| Procurement | Review AI suppliers and renewals. | Vendor questionnaires, contracts, risk ratings |
| HR/People | Govern employee AI use and employment tools. | Training records, HR tool reviews |
| Revenue | Respond to buyer diligence; avoid unsupported claims. | AI FAQ, RFP responses, evidence pack |
| Marketing | Ensure AI claims are accurate/substantiated. | Claim review log |
| Support | Monitor AI-related customer issues. | Ticket tags, incident summaries |

## RACI starter

Use R = Responsible, A = Accountable, C = Consulted, I = Informed.

| Activity | Exec | Legal | Compliance | Product | Eng/Data | Security | Privacy | Procurement | HR | Revenue |
|---|---|---|---|---|---|---|---|---|---|---|
| Maintain AI inventory | I | C | A/R | R | R | C | C | C | C | I |
| Risk-tier use cases | A | R | R | R | C | C | C | C | C | I |
| Approve Tier 3/4 launch | A | R | R | R | C | C | C | I | C | I |
| Review AI vendors | I | C | C | C | C | R | C | A/R | C | I |
| Maintain evidence pack | I | C | A/R | C | C | C | C | C | I | R |
| Handle AI incident | A | R | R | C | R | R | C | C | C | C |
| Approve AI marketing claims | I | R | C | C | C | I | C | I | I | A/R |
| Train employees | I | C | R | I | I | C | C | I | A/R | I |

---

# 7. Vendor and model-risk diligence templates

## Vendor AI intake form

| Field | Response |
|---|---|
| Vendor/product |  |
| Business owner / procurement owner |  |
| Security reviewer |  |
| Data categories processed |  |
| Personal/sensitive/customer/employee data involved? |  |
| AI function provided |  |
| Model/provider used, if known |  |
| Customer data used for training? |  |
| Opt-out available? |  |
| Human oversight available? |  |
| Output relied on for decisions? |  |
| Regions/users affected |  |
| Proposed risk tier |  |
| Required legal/privacy/security review |  |
| Contract terms reviewed |  |
| Approval decision |  |
| Renewal review date |  |

## 40 vendor diligence questions

### AI functionality

1. What AI/ML/automated decisioning features are included?
2. Which features are optional, configurable, or enabled by default?
3. What is the intended use of each AI feature?
4. What uses are prohibited or discouraged?
5. Does the product make decisions, recommendations, rankings, predictions, classifications, scores, or generated content?
6. Can customers disable or limit AI features?

### Model and data practices

7. What model providers or foundation models are used?
8. Are models proprietary, third-party, open-source, or customer-specific?
9. Is customer data used to train, fine-tune, improve, evaluate, or benchmark models?
10. Where is the data-use commitment documented?
11. Are prompts, outputs, embeddings, logs, or feedback retained?
12. What are retention periods?
13. Can customers opt out of training, human review, or model improvement?
14. Is data segregated by tenant/customer?
15. Are subprocessors/model providers listed and updated?

### Security and privacy

16. What controls protect prompts, outputs, embeddings, and logs?
17. Is data encrypted in transit and at rest?
18. What access controls limit vendor personnel access?
19. Are AI features covered by SOC 2, ISO 27001, HITRUST, PCI, or other reports?
20. How are prompt injection, data leakage, vulnerabilities, and abuse monitored?
21. Does the vendor support deletion, export, retention controls, and audit logs?
22. Does the vendor process sensitive, biometric, health, financial, children’s, or employee data?

### Testing and limitations

23. What testing has been performed for accuracy, robustness, hallucination, bias, safety, and misuse?
24. Are test results or summaries available?
25. What known limitations should customers understand?
26. Does performance vary by language, region, demographic group, data type, or use context?
27. How does the vendor monitor drift or degradation?
28. How often are models updated, and how are customers notified?

### Human oversight and compliance

29. Can humans review, override, reject, or correct outputs?
30. Are confidence scores, reasons, citations, or source references provided?
31. Are users warned that outputs may be incomplete or inaccurate?
32. Does the vendor provide documentation for audits or regulator inquiries?
33. Does the vendor map its product to the EU AI Act or other AI regulations?
34. How does the vendor classify its role?
35. Does the vendor support notices, disclosures, audits, or impact assessments?
36. Will the vendor notify customers of material model, subprocessor, or data-use changes?
37. Does the vendor agree not to use customer data for model training without written permission?
38. Does the vendor provide indemnities, warranties, audit rights, or cooperation obligations?
39. Does the vendor have an AI incident notification process?
40. How does the vendor handle harmful, discriminatory, unlawful, or inaccurate outputs?

## Vendor decision matrix

| Area | Green | Yellow | Red | Notes |
|---|---|---|---|---|
| Data use | No training on customer data; clear retention | Limited/unclear retention; opt-out needed | Training on customer data by default |  |
| Security | Strong assurance and controls | Partial evidence | No meaningful security evidence |  |
| Transparency | Clear model/vendor docs | Some gaps | Refuses basic documentation |  |
| High-impact use | Not consequential | Decision support with review | Automates high-impact decisions without controls |  |
| Contract terms | Commitments documented | Negotiation needed | Rejects core protections |  |
| Monitoring/support | Incident and change notices | Informal support | No escalation process |  |

Decision: approve / approve with conditions / pilot only / reject or pause.

---

# 8. Customer-facing evidence pack

Create a folder with:

1. AI Governance Overview
2. Customer-safe AI Inventory Summary
3. AI Acceptable Use Policy or summary
4. Product AI Documentation
5. Vendor/Model List
6. Data Use Statement
7. Security Controls Summary
8. Privacy Controls Summary
9. Testing/Monitoring Summary
10. AI Incident Escalation Process
11. AI Governance Contacts

## AI Governance Overview template

> **Company AI Governance Overview**  
> Last updated: [date]
>
> [Company] maintains an AI governance process designed to inventory AI systems, classify AI-related risk, review vendors and model providers, define human oversight for material use cases, and maintain evidence for customer diligence. AI use cases are reviewed based on business context, affected users, data sensitivity, decision impact, geography, vendor/model dependency, and potential legal or contractual obligations.
>
> Material AI systems are assigned business and technical owners. Higher-impact use cases are escalated for legal, privacy, security, and executive review as appropriate. [Company] maintains policies for employee AI use, confidential data handling, vendor review, security controls, and incident escalation.
>
> This overview is provided for customer diligence purposes and does not amend the parties’ agreement unless expressly incorporated by written contract.

## Data use statement options

### No training on customer data

> [Company] does not use customer content submitted to [product/service] to train or fine-tune third-party foundation models unless expressly agreed in writing. Customer content may be processed to provide the contracted service, maintain security, troubleshoot issues, and improve product functionality as described in the applicable agreement and documentation.

### Limited product improvement use

> [Company] may use limited service data to improve product performance as described in the applicable agreement and privacy documentation. [Company] does not use customer confidential content to train third-party foundation models without appropriate authorization. Customers may contact [contact] for configuration options and data-use details.

### Customer-controlled model integration

> [Company] supports customer-configured AI/model integrations. Where customers connect their own model provider or account, processing by that model provider is governed by the customer’s agreement with that provider. [Company] provides configuration controls and documentation to support customer review.

## Customer AI questionnaire answer bank

| Buyer question | Draft response |
|---|---|
| Do you use AI in your product? | Yes. [Company] uses AI for [summarization/classification/recommendation/etc.] in [feature/workflow]. The intended use is [description]. |
| Is AI optional? | [Yes/No/Partially]. Customers can [enable/disable/configure] AI features through [admin setting/support request/contract configuration]. |
| What model providers do you use? | [Company] uses [vendor/model] for [purpose]. Vendor/subprocessor details are available at [link]. |
| Do you train models on customer data? | [Company] [does/does not] use customer data for model training or fine-tuning. Details are documented in [DPA/privacy notice/product docs]. |
| Are humans involved in reviewing AI outputs? | [Describe human oversight, customer controls, review workflows, warnings, or required approvals]. |
| Can AI outputs make automated decisions? | [Describe whether outputs are advisory, whether decisions require human review, and any prohibited use]. |
| How do you test AI outputs? | [Company] performs [testing/QA/monitoring/red-team/manual review] for [accuracy, reliability, bias, safety, security, limitations]. |
| How do you handle inaccurate or harmful outputs? | Customers can report issues through [support channel]. [Company] triages AI-related issues under [incident/support process]. |
| Do you have an AI policy? | Yes. [Company] maintains internal AI acceptable-use and governance procedures covering approved tools, confidential data, vendor review, and escalation. |
| Are AI features covered by security controls? | Yes. AI systems are reviewed under [Company]’s security, access control, logging, vendor-risk, and incident response processes as applicable. |

---

# 9. 90-day implementation checklist

## Days 1-15: Baseline and ownership

- [ ] Name executive sponsor.
- [ ] Approve AI governance charter.
- [ ] Define risk appetite and escalation criteria.
- [ ] Create initial regulatory watchlist.
- [ ] Draft/update AI acceptable-use policy.
- [ ] Identify product AI features and model/vendor dependencies.
- [ ] Pull list of AI vendors and SaaS tools with AI features.
- [ ] Collect recent AI diligence questions from prospects/customers.

## Days 16-30: Inventory and triage

- [ ] Complete AI Inventory Starter Table.
- [ ] Assign owner for every AI system.
- [ ] Apply preliminary risk tier to every system.
- [ ] Flag Tier 3 and Tier 4 systems.
- [ ] Pause new high-impact AI launches until review is complete.
- [ ] Identify customer-facing AI claims needing review.
- [ ] Identify missing vendor/model documentation.

## Days 31-45: Controls and documentation

- [ ] Complete risk assessments for Tier 3 and Tier 4 systems.
- [ ] Review high-impact use cases with counsel.
- [ ] Define human oversight requirements.
- [ ] Document testing and monitoring expectations.
- [ ] Create AI incident escalation path.
- [ ] Update procurement intake to include AI questions.
- [ ] Update security review to include prompts, outputs, embeddings, logs, and model providers.

## Days 46-60: Vendor and contract readiness

- [ ] Send diligence questions to critical AI vendors.
- [ ] Confirm whether customer data is used for training/fine-tuning/model improvement.
- [ ] Review subprocessors, security posture, retention, and incident processes.
- [ ] Negotiate or document data-use restrictions where needed.
- [ ] Decide: approve, approve with conditions, pilot only, reject/pause.
- [ ] Create renewal review calendar for AI vendors.

## Days 61-75: Buyer evidence pack

- [ ] Build customer-facing evidence folder.
- [ ] Draft approved AI questionnaire responses.
- [ ] Review responses with legal, security, product, and revenue.
- [ ] Create customer-safe AI governance overview.
- [ ] Review public AI claims in website, sales decks, help docs, and release notes.
- [ ] Train sales/customer success on approved language and escalation.

## Days 76-90: Leadership reporting and operating rhythm

- [ ] Finalize AI governance RACI.
- [ ] Create monthly AI review meeting.
- [ ] Create KPI dashboard.
- [ ] Present leadership/board update.
- [ ] Close or assign remediation items.
- [ ] Set quarterly review schedule.
- [ ] Define process for new AI use-case intake.

## 90-day success criteria

- Current AI inventory
- Risk tier assigned to each system
- Named owners
- Review process for high-impact AI
- Vendor diligence process
- AI acceptable-use policy
- AI incident escalation path
- Customer evidence pack
- Leadership KPI dashboard

---

# 10. Scripts and email templates

## Internal AI inventory request

Subject: Action needed: AI systems and tools inventory

Hi team,

We are creating a company-wide inventory of AI systems and AI-enabled tools so we can respond accurately to customer diligence, vendor-risk reviews, and evolving AI governance requirements.

Please send the following by [date]:

1. Any product feature, internal tool, vendor system, workflow, or pilot that uses AI, machine learning, automated scoring, recommendation, ranking, classification, summarization, generation, or prediction.
2. The business owner and technical owner.
3. The data used by the system.
4. Whether the output affects customers, employees, applicants, consumers, or regulated workflows.
5. Any vendor/model provider involved.

If you are unsure whether something counts, include it. We will triage centrally.

Thanks,  
[Name]

## Manager script: why this matters

> We are not trying to slow down useful AI adoption. We are making sure we can answer basic questions from customers, auditors, leadership, and regulators. If a tool uses AI to generate, rank, score, classify, summarize, recommend, or automate something, we need to know it exists, who owns it, what data it uses, and whether it affects people or regulated workflows. Low-risk productivity use should be simple. High-impact use needs more review.

## Employee AI acceptable-use announcement

Subject: Updated guidance for using AI tools at work

Hi team,

We are updating our AI-use guidance to support safe and productive adoption. Effective [date]:

- Do not enter confidential customer data, regulated personal data, credentials, source code, trade secrets, or non-public company information into unapproved public AI tools.
- Use approved AI tools for approved purposes only.
- Review AI outputs before relying on them, sending them externally, or using them in customer deliverables.
- Do not use AI outputs as the sole basis for employment, credit, access, eligibility, health, legal, safety, or other high-impact decisions without approved review.
- Report inaccurate, harmful, unexpected, or suspected data-leaking AI outputs to [channel/contact].
- Submit new AI tools or use cases through [intake process].

Thanks,  
[Name]

## Vendor diligence email

Subject: AI functionality and data-use diligence request

Hi [Vendor],

As part of our AI governance and vendor-risk process, we are reviewing AI-enabled functionality in products we use. Please provide responses or documentation for:

1. AI/ML features included in [product].
2. Model providers or foundation models used.
3. Whether our data, prompts, outputs, logs, embeddings, or feedback are used for training, fine-tuning, evaluation, benchmarking, or product improvement.
4. Retention periods for prompts, outputs, logs, embeddings, and derived data.
5. Security controls for AI-related data.
6. Subprocessors/model providers involved.
7. Testing for accuracy, robustness, bias, safety, and misuse.
8. Human oversight, explainability, audit log, and configuration options.
9. Incident notification and material model-change notification processes.
10. Contractual documentation for the above commitments.

Thanks,  
[Name]

## Customer AI governance response

Subject: AI governance information for [Customer]

Hi [Customer],

Thank you for the AI governance questions. We maintain an AI governance process covering AI inventory, risk classification, vendor/model review, human oversight for material use cases, security/privacy review, and incident escalation.

For [product/service], AI is used for [brief description]. [Company] [does/does not] use customer content to train or fine-tune third-party foundation models unless expressly agreed in writing. AI-related systems are reviewed under our security and privacy processes, and material vendors are assessed through our vendor-risk process.

Attached/linked are the current materials we can share:

- AI Governance Overview
- Product AI Documentation
- Data Use Statement
- Vendor/Subprocessor Information
- Security and Privacy Documentation
- AI Incident Escalation Summary

Best,  
[Name]

## High-risk escalation script

> This use case may affect [employment/credit/health/access/safety/legal rights/customer obligations] or may involve regulated/sensitive data. We should not launch or expand it until legal, privacy, security, and product owners complete a risk assessment. The next step is to document intended use, affected users, data inputs, output role in the decision, human oversight, vendor/model details, testing evidence, and fallback process. Once we have that, leadership can decide whether to approve, approve with conditions, pilot only, or pause.

## Sales script: “Are you AI compliant?”

> AI compliance depends on the specific use case, jurisdiction, contract, and role of each party, so we avoid blanket claims. What we can say is that we maintain an AI governance process covering inventory, risk classification, vendor/model review, security and privacy controls, human oversight for material use cases, and incident escalation. For this product, we can provide documentation on how AI is used, what data is processed, whether customer data is used for training, and what controls are in place.

---

# 11. Board-level KPI template

| KPI | Current | Prior | Target | Owner | Notes |
|---|---:|---:|---:|---|---|
| AI systems inventoried |  |  | 100% known systems | Compliance/Product |  |
| Systems with assigned owner |  |  | 100% | Compliance |  |
| Tier 3/4 systems identified |  |  | Track | Legal/Product |  |
| Tier 3/4 systems reviewed |  |  | 100% before launch | Legal |  |
| Critical AI vendors reviewed |  |  | 100% | Procurement/Security |  |
| Vendors with confirmed data-training terms |  |  | 100% critical vendors | Legal/Procurement |  |
| Customer AI questionnaires received |  |  | Track trend | Revenue |  |
| Avg. AI diligence response time |  |  | [target] days | Revenue/Compliance |  |
| AI-related incidents/issues |  |  | 0 severe unresolved | Security/Product |  |
| Employees trained on AI policy |  |  | 95%+ | HR/Compliance |  |
| Public AI claims reviewed |  |  | 100% material claims | Marketing/Legal |  |

## Board update outline

**AI governance update — [Month/Quarter]**

1. **Executive summary:** status green/yellow/red; main risk; progress; decision needed.
2. **Inventory:** total systems; Tier 1/2/3/4 count; unclassified count.
3. **Regulatory and buyer readiness:** EU AI Act readiness; U.S. watchlist; customer evidence pack; vendor review.
4. **Key risks:** risk, impact, likelihood, owner, mitigation, due date.
5. **Metrics:** top KPIs from dashboard.
6. **Decisions requested:** resources, policy approval, high-risk use approval/pause, remediation priorities.

---

# 12. Readiness scorecard

Score each 0-3:

- **0 = Not started**
- **1 = Draft/in progress**
- **2 = Implemented for some systems/functions**
- **3 = Implemented, evidenced, recurring**

| Capability | Score | Evidence | Owner | Next action |
|---|---:|---|---|---|
| AI inventory exists and is current |  |  |  |  |
| AI systems have named owners |  |  |  |  |
| Risk-tiering process exists |  |  |  |  |
| High-impact use cases receive legal/privacy/security review |  |  |  |  |
| Vendor AI diligence process exists |  |  |  |  |
| Customer data-training terms are documented |  |  |  |  |
| AI acceptable-use policy exists |  |  |  |  |
| Employees receive AI usage training |  |  |  |  |
| Product AI documentation exists |  |  |  |  |
| Human oversight is documented |  |  |  |  |
| Testing/monitoring evidence exists |  |  |  |  |
| AI incident escalation path exists |  |  |  |  |
| Customer AI evidence pack exists |  |  |  |  |
| Sales has approved AI questionnaire responses |  |  |  |  |
| Leadership receives AI governance KPIs |  |  |  |  |

## Score interpretation

- **0-12:** Reactive. Start with inventory, ownership, and triage.
- **13-25:** Emerging. Core process exists but evidence is incomplete.
- **26-37:** Operational. Most buyer diligence can be handled with moderate follow-up.
- **38-45:** Mature. Governance is documented, evidenced, and recurring.

---

# 13. Appendix: operating templates

## AI governance charter

> [Company]’s AI governance program exists to support responsible, secure, compliant, and commercially trustworthy use of AI. The program maintains an inventory of AI systems, classifies use cases by risk, reviews vendors and model providers, defines human oversight and testing expectations for material systems, maintains customer and auditor evidence, and escalates high-impact or uncertain use cases for review.
>
> The program applies to product AI, internal AI tools, employee use of AI, vendor-provided AI functionality, and experimental AI pilots. Business owners remain accountable for their use cases. Legal, privacy, security, product, engineering, procurement, HR, and revenue teams provide review and controls based on risk.

## New AI use-case intake form

| Field | Response |
|---|---|
| Requester/department |  |
| Proposed tool/system |  |
| Vendor/model |  |
| Business purpose |  |
| Internal/product/customer-facing |  |
| Users affected |  |
| Data inputs and outputs |  |
| Personal/sensitive/confidential data involved |  |
| Does output influence a decision? |  |
| Decision type |  |
| Human review process |  |
| Region/user location |  |
| Expected launch date |  |
| Proposed risk tier |  |
| Reviews required |  |
| Approval decision |  |

## AI incident intake form

| Field | Response |
|---|---|
| Date/time discovered |  |
| Reporter |  |
| System/tool |  |
| Business owner |  |
| Description of issue |  |
| Affected users/customers |  |
| Data involved |  |
| Output involved |  |
| Potential harm |  |
| Severity | Low / Medium / High / Critical |
| Immediate containment |  |
| Customer notification needed? |  |
| Legal/privacy/security review needed? |  |
| Root cause |  |
| Corrective action |  |
| Closure date |  |

## Public AI claims review checklist

- [ ] Claim is accurate and not exaggerated.
- [ ] Claim can be substantiated.
- [ ] Claim does not imply guaranteed accuracy, fairness, security, compliance, or legal sufficiency unless approved.
- [ ] Limitations are disclosed where needed.
- [ ] Customer data-use statements match contracts and product behavior.
- [ ] Human oversight claims match actual workflow.
- [ ] Security/privacy claims match current controls.
- [ ] Legal has reviewed high-risk or regulated claims.

## AI acceptable-use policy outline

1. Purpose and scope
2. Approved AI tools
3. Prohibited or restricted data inputs
4. Human review expectations
5. High-impact decision restrictions
6. Customer deliverable rules
7. Code/security rules
8. Vendor/tool approval process
9. Incident and error reporting
10. Training and acknowledgment
11. Enforcement and exceptions

## Minimal operating cadence

| Cadence | Meeting/action | Participants | Output |
|---|---|---|---|
| Weekly during first 90 days | Inventory/remediation standup | Compliance, legal, product, security, procurement | Updated inventory and blockers |
| Monthly | AI governance review | Cross-functional owners | New use cases, vendor issues, incidents, diligence |
| Quarterly | Leadership update | Exec sponsor + program owner | KPI dashboard, decisions, roadmap |
| Procurement intake | AI vendor review | Procurement, security, privacy, legal | Vendor approval decision |
| Product launch | AI release review | Product, engineering, legal, security, privacy | Launch approval and documentation |
| Incident | AI incident review | Security, legal, product, support, privacy | Containment, notification, corrective action |

---

## Final implementation reminder

A useful AI governance program is not a binder. It is a living operating rhythm:

- Inventory what exists.
- Classify what matters.
- Assign owners.
- Review vendors.
- Document controls.
- Prepare evidence.
- Escalate uncertainty.
- Revisit quarterly.

Start with visibility. Then build the control layer around the systems that create the highest regulatory, customer, contractual, and human-impact risk.
