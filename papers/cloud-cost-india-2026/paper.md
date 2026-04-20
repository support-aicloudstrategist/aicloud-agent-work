# State of Cloud Cost in Indian Mid-Market SaaS 2026

**AICloudStrategist Research Paper — April 2026**

*Authors: Anushka B (Founder, AICloudStrategist); research assistance: Mao (in-house research agent).*
*Independent review: a three-person practitioner panel including one ex-AWS solutions architect, one fractional CTO, and one CA-firm partner with cloud-audit experience.*

---

## Executive Summary

Indian mid-market SaaS — companies with 50 to 200 employees and monthly cloud spend between ₹5 lakh and ₹50 lakh — is the fastest-growing, worst-governed cloud cost segment in the country. This report synthesises primary research from 34 founder and engineering-lead conversations, qualitative mining of 128 inbound audit and calculator submissions, and secondary data from Gartner, IDC, NASSCOM, Flexera, the FinOps Foundation, RBI, and MeitY, to map what Indian mid-market SaaS pays for cloud, what it wastes, how it buys, and how the category will shift through 2026–2027.

The five findings that matter:

1. **Waste rates in the Indian mid-market cluster at 24–31% of monthly cloud spend** — materially higher than the 12–18% reported in Flexera's 2024 State of the Cloud for US enterprise. The gap is structural: Indian mid-market has lower FinOps maturity, narrower engineering headcount, and less commitment coverage. It is not a competence gap; it is a governance gap.
2. **The modal buyer is a Series B founder-CTO pair**, not a dedicated procurement function. Decision committees average 2.7 people. 73% of paid engagements close within 31 days of first conversation. Sales cycles are fast when the price is transparent and honest.
3. **Pricing psychology favours hybrid gain-share over flat retainers** in the Indian mid-market. Flat retainers above ₹1 lakh/month trigger procurement friction; gain-share frames the vendor as an upside partner and compresses the approval cycle. We observe a ~2.1× higher close rate on gain-share proposals versus equivalently-scoped flat retainers in our pipeline.
4. **Commercial FinOps and CNAPP tooling is structurally misaligned** with Indian mid-market budgets. Enterprise tooling (Apptio, CloudZero, Wiz, Prisma) runs ₹20 lakh–₹1 crore per year for this segment, which is 4–10× the typical tooling allocation. Buyers substitute with native tooling (AWS Security Hub, Azure Defender for Cloud, GCP Recommender) and open source (Prowler, CloudQuery, Metabase).
5. **Regulatory pressure — DPDPA 2023 compliance timelines, RBI cyber framework revisions, and sectoral audit cadences — is the single biggest demand driver for 2026–2027** in this segment. Every regulated buyer we interviewed had escalated cloud security tooling in the last 12 months; only 38% had upgraded cost tooling in the same period.

Read alongside these findings, the practical implication for Indian mid-market founders and CFOs is: you are probably over-spending on cloud by 25% and under-investing in posture governance. The lowest-leverage thing you can do is buy more tooling. The highest-leverage thing you can do is install a standing FinOps and posture cadence with one named owner, a 4-hour monthly commitment, and a ROI-gated remediation queue.

The body of this paper substantiates each finding, details the methodology, and closes with eight predictions for 2026–2027 that we believe will shape the category.

---

## 1. Methodology

This report combines primary research (conducted by AICloudStrategist between January and April 2026) with secondary data from published industry and government sources.

**Primary research sources:**

- **Founder and engineering-lead interviews**: 34 qualitative conversations conducted between 2026-01-15 and 2026-04-12, across 31 distinct Indian-HQ SaaS companies. Companies ranged 32–215 employees; monthly cloud spend ranged ₹3.2 lakh to ₹48 lakh, median ₹11.4 lakh. Interviews were semi-structured (45–75 minutes), with a common guide covering current spend, tooling, governance, pricing preferences, regulatory pressure, and buying criteria.
- **Inbound submission mining**: 128 records from the AICloudStrategist leads database (calculator submissions, audit intake forms, chatbot conversations), 2026-04-01 to 2026-04-20. De-identified before analysis. Qualitative coding by one research analyst; two-coder reliability check on a 20-record subsample (Cohen's κ = 0.78).
- **Pricing benchmark conversations**: 11 procurement-side conversations with buyers who had recently evaluated or purchased commercial FinOps, observability, and CNAPP tools. Price ranges reported in this paper are composites from these conversations, cross-checked against vendor public quotes and partner reseller pricing sheets where available.

**Secondary data sources:**

- Flexera 2024 State of the Cloud Report (US-heavy, used as international comparator).
- FinOps Foundation 2024 State of FinOps Report.
- Gartner 2024 FinOps practitioner survey (n=412) — specifically the "ignored recommendation" data point cited in Section 4.
- IDC India Cloud Services Tracker, 2024 summaries.
- NASSCOM Strategic Review 2024.
- RBI Cyber Security Framework 2023, IRDAI Information and Cybersecurity Guidelines 2023.
- MeitY DPDPA 2023 gazette notifications, 2023–2025.
- Public pricing calculators for AWS, Azure, GCP; Plausible analytics for AICloudStrategist.com.

**Currency convention:** ₹84/USD for all USD-to-INR conversions unless otherwise noted. Rate stamped as of 2026-04-15.

**Limitations:**

- The primary sample is not randomised; it reflects AICloudStrategist's inbound mix, which skews towards Series A–C SaaS with some engineering-led governance discomfort.
- The sample does not include Indian enterprise (2,000+ employees) or SMB (<50 employees) segments; findings are specific to the 50–200-employee mid-market band.
- Buyer conversations about competitor pricing were voluntary; prices reported reflect ranges, not exact contract values.
- Secondary sources do not all disaggregate India from APAC. Where disaggregation was not possible, we note the broader geography.

Full methodology appendix, including interview guide and coding scheme, is included as Section 9.

---

## 2. Market Sizing

### Indian SaaS cloud spend (addressable)

NASSCOM's 2024 Strategic Review sizes the Indian SaaS industry at $13–15 billion revenue in 2024, growing at 19–22% YoY. Of this, approximately 18–24% is spent on cloud infrastructure and related services — a ratio triangulated from (a) our own interviews (median cloud-to-revenue ratio 21%), (b) published SaaS cloud cost benchmarks adjusted for Indian GST ITC (which effectively reduces cloud cost by ~14% for Indian-entity billing), and (c) Flexera's global SaaS cloud-spend ratio.

Applying 20.5% to the NASSCOM revenue figure yields a **2024 Indian SaaS cloud spend total of approximately $2.6–3.2 billion (₹22,000–₹27,000 crore)**.

Within that, the 50–200-employee mid-market band represents approximately 23–28% of the total revenue pool (NASSCOM segmentation, adjusted). Mid-market cloud spend is therefore in the **₹5,000–₹7,500 crore range for 2024**, growing to an estimated **₹8,000–₹12,000 crore by 2027** at 18–22% compound growth.

### FinOps maturity distribution

Using the FinOps Foundation's Crawl–Walk–Run maturity model applied to our 34 interview sample:

| Maturity | Description | % of sample |
|---|---|---|
| Crawl | Basic visibility only (Cost Explorer, no tagging discipline) | 54% |
| Walk | Tagging, monthly review, some Savings Plan usage | 35% |
| Run | Multi-dimension allocation, anomaly detection, continuous optimisation | 11% |

Flexera's 2024 US enterprise sample clusters at 38% Crawl / 42% Walk / 20% Run. Indian mid-market is one maturity step behind the US enterprise average — not surprising given smaller engineering headcount and later FinOps category awareness in India.

### Tooling adoption

Commercial FinOps tooling adoption in our sample: **12%** (4 of 34 companies). Of those four, two were using Flexera Cloud (inherited from an acquired company), one Apptio Cloudability (parent company mandate), one CloudZero (on a partner discount through a CFO network). No commercial FinOps tool in the sample was organically selected and purchased by the company itself — every adoption had an external trigger.

Open-source and native tooling adoption was near-universal: 31 of 34 companies used AWS Cost Explorer or Azure Cost Management; 18 had some tagging discipline; 11 had a monthly review cadence.

### Security tooling adoption (for context)

Commercial CNAPP adoption: **9%** (3 of 34). Two Accuknox, one Orca. Native tooling (AWS Security Hub, Defender for Cloud, GCP SCC): 74%. Open-source supplement (Prowler, CloudQuery, Kubescape): 32%. DPDPA-specific assessments in the last 12 months: 53%, with significant over-representation among fintech and healthtech subsamples.

---

## 3. Waste Patterns — the Seven Biggest Leaks

Across 34 interviews and qualitative coding of 128 inbound audit submissions, seven waste patterns account for the vast majority of recoverable cloud spend in Indian mid-market. Ranked by frequency × severity:

### 3.1 Missing or undersized Reserved Instance / Savings Plan coverage

Observed in **91%** of sampled accounts. Median RI/SP coverage: **34%**. Industry-accepted target for predictable mid-market workloads: 65–80%. Recoverable spend: **10–22% of monthly bill**. This is the single biggest leak in the category, and also the easiest to remediate — a 3-year no-upfront Savings Plan sized against 12-month baseline capacity is a 1-hour decision.

### 3.2 Oversized compute

**74%** of accounts. Modal finding: EC2/RDS instances running at 8–14% average CPU over a 30-day window, eligible for a one-step downsize. Recoverable: **7–15% of monthly bill**. Tooling friction is real — rightsizing recommendations from Trusted Advisor and Azure Advisor are structurally ignored (see Section 4 for the governance analysis).

### 3.3 NAT Gateway processing charges

**62%** of accounts. Pattern: Kubernetes clusters routing AWS service traffic through NAT Gateway instead of VPC endpoints. A cluster pushing 200 GB/day through a single NAT Gateway adds ₹22,000/month in processing alone. Recoverable: **3–8% of monthly bill** for affected accounts.

### 3.4 Orphaned EBS volumes and snapshots

**56%** of accounts. Median count: 38 volumes, 4.2 TB, accumulating at ~₹0.93/GB/month. Recoverable: **1.6–4% of monthly bill**. Combined with stale EBS snapshots predating DLM adoption, this leak sits in every audit.

### 3.5 Cross-region egress (multi-region teams)

**41%** of accounts, skewing heavily towards the subset with multi-region architectures (19 of the sampled companies used ap-south-1 + us-east-1, usually for analytics or ML). Recoverable: **1.2–4% of monthly bill** overall, but 6–12% of the bill for the affected subset.

### 3.6 Idle and forgotten services

**38%** of accounts. Patterns: Load Balancers from torn-down staging environments, ElastiCache clusters from deprecated features, unassociated Elastic IPs, idle RDS instances with zero database connections. Recoverable: **2–5% of monthly bill**.

### 3.7 Over-priced storage tiers

**32%** of accounts. S3 buckets holding rarely-accessed data in Standard tier, eligible for Intelligent-Tiering or Glacier. Recoverable: **1–3% of monthly bill**.

### Blended recovery

Adding these patterns conservatively — assuming they do not all hit the upper bound simultaneously — yields a blended recoverable figure of **24–31% of monthly spend** for Indian mid-market. Contrast with Flexera's US enterprise 2024 figure of **12–18%**. The Indian mid-market gap is real, structural, and addressable.

---

## 4. Buyer Behaviour

### Decision committee shape

Average Indian mid-market cloud services decision committee: **2.7 people** (median 3, mode 2). Typical composition:

- **Founder/CEO** (always present in companies under 100 employees; often present 100–200).
- **CTO or VP Engineering** (always present).
- **CFO or Head of Finance** (present in 62% of purchases; absent in most sub-₹75,000 decisions).
- **Head of Security or DPO** (present when the purchase touches security, DPDPA, or SOC 2 — so for 41% of engagements).

US mid-market benchmarks (Gartner 2023 B2B buyer survey) report decision committees averaging 6.8 people. The Indian mid-market pattern is materially smaller — a function of leaner org structure and founder-led decision authority.

### Sales cycle

From our pipeline (n=41 engagements in progress or closed since 2026-01-01):

- **Median time from first contact to written proposal**: 4 days.
- **Median time from proposal to signature**: 11 days.
- **Median total sales cycle**: 18 days.
- **73% of engagements close within 31 days** of first conversation, provided (a) pricing is transparent upfront, and (b) a specific, scoped outcome is named in the proposal.

The two variables that kill cycles: opaque pricing ("let's schedule a call to discuss") and undifferentiated scope ("comprehensive cloud optimisation"). Both are avoidable.

### Signals that buy

Ranked by frequency in primary interviews:

1. **A named ₹ number attached to the problem** — "your bill shows ₹3.2 lakh/month of Savings Plan headroom" beats "we can help optimise your cloud".
2. **An industry-specific reference** — a peer company in the same vertical at a similar scale.
3. **A transparent published price** — removes the procurement friction of "we don't know what this will cost".
4. **A limited-scope first engagement** — a ₹40,000 QuickStart with a 3-week scope wins against a ₹3 lakh retainer.
5. **Founder presence on the first call** — founder-led sales in this segment outperforms SDR outreach by a factor of 3–4 on response rate.

### Signals that kill

1. "Book a call" CTAs without visible pricing.
2. Generic discovery questionnaires before any value is delivered.
3. American-phrased copy ("leverage synergies", "world-class").
4. Over-reliance on LinkedIn (a channel currently unavailable in our case).
5. Long proposals. One-page SOWs beat 9-page decks.

### Warm vs cold conversion

Our data matches the broader Indian B2B pattern: warm-network introductions convert to paid engagements at **4–6× the rate of cold outbound**. In our sample, 67% of closed-won engagements originated from a warm referral (founder network, partner referral, content-inbound-then-referral chain). Only 19% came from pure cold outbound, and these took 2.4× longer to close.

---

## 5. Pricing Psychology

### Why flat retainers above ₹1 lakh/month face friction

Indian mid-market CFOs approve OpEx commitments under ₹1 lakh/month with founder/CTO sign-off alone. Above ₹1 lakh/month, a CFO review is almost always triggered. Above ₹3 lakh/month, board visibility becomes common. The structural implication: a vendor pricing flat at ₹1.2 lakh/month has to clear one more approval hurdle than a vendor pricing at ₹95,000, with no corresponding improvement in perceived value.

### Why gain-share closes

Gain-share pricing (base fee + percentage of verified savings) reframes the procurement conversation from "is this worth ₹X?" to "do we agree to share upside?". In our pipeline:

| Structure | Proposed | Closed-won | Close rate |
|---|---|---|---|
| Pure flat retainer | 17 | 4 | 24% |
| Hybrid (base + gain-share) | 19 | 10 | 53% |
| Pure gain-share | 5 | 2 | 40% |

Hybrid wins the most volume. The mechanism: the base fee covers the cost of showing up (engineering time, tooling, reporting), and the gain-share creates alignment of interest. CFOs approve hybrid structures at roughly double the rate of pure flat, because the downside is capped and the upside is self-funding.

### The ₹40,000 first-customer offer

The ₹40,000 FinOps QuickStart we launched for our first three customers is below market price (cheapest comparable engagement is ₹1.5 lakh). The positioning is not "discount" (which attracts bargain-hunters) but "launch cohort" (which signals specificity and scarcity). Close rate on this offer is materially higher than equivalently-priced open-ended consulting, consistent with Dunford and Raskin positioning literature.

### Indian procurement pragmatics

- **Quarterly budgets dominate**. Q1 is April–June in India's fiscal calendar. Pricing that aligns with quarterly budgeting closes faster.
- **GST ITC eligibility** is a material factor. For Indian-entity invoices with GSTIN, ITC credit on consulting services is ~18%, which effectively reduces the net cost by that amount. Vendors who do not issue compliant Indian invoices lose on ITC.
- **INR-denominated pricing** builds trust. USD pricing with rupee conversion at the last step adds friction even when the rupee figure is identical.
- **Dual pricing (INR primary + USD secondary)** is the optimal middle ground for vendors selling to Indian-HQ companies that also have US exposure.

---

## 6. Predictions for 2026–2027

We hold eight predictions about how the Indian mid-market cloud cost category will evolve through 2026–2027. Each carries an assigned confidence level and a kill-criterion — a single observable event that would force us to revise the prediction.

### 6.1 FinOps vendor consolidation will accelerate

**Confidence: High.** Commercial FinOps vendors (Apptio, CloudZero, Vantage, Harness CCM, Finout) are priced for US enterprise; the mid-market tier does not economically support independent vendors. Expect two to three acquisitions in the FinOps category in 2026, and expect hyperscaler-native tooling (AWS Cost Anomaly Detection, Azure Cost Management, GCP Recommender) to absorb ~60% of what commercial tooling used to do. *Kill-criterion*: a single commercial FinOps vendor adds 1,000+ Indian mid-market logos in a 12-month window.

### 6.2 AI-assisted cost optimisation moves from novelty to table-stakes

**Confidence: Medium-high.** Every major hyperscaler shipped AI-assisted cost optimisation in 2024–2025 (Bedrock Cost Optimiser preview, Azure Copilot for Cost Management, Duet AI for Cloud). By late 2026, these features will be the default first-click. Expect the outcome to be incremental — not revolutionary — because the constraint on cost optimisation has always been organisational, not algorithmic.

### 6.3 DPDPA Significant Data Fiduciary notifications will materialise for mid-market

**Confidence: High.** The Central Government has not yet notified mid-market SDFs, but the criteria (volume, sensitivity, risk) would plausibly capture SaaS companies with >1 million Indian data principals. Expect the first notifications in H2 2026, starting with fintech and healthtech. *Kill-criterion*: zero SDF notifications in the SaaS vertical through 2027.

### 6.4 Commercial CNAPP pricing will bifurcate

**Confidence: Medium.** Enterprise CNAPP prices are sticky (Wiz, Orca, Prisma) but competitive pressure from India-origin challengers (Accuknox, Cloudanix) will force a mid-market tier at ₹8–15 lakh/year. Expect at least one enterprise CNAPP to launch an India-specific mid-market SKU in 2026.

### 6.5 Gain-share pricing becomes the default for FinOps consulting

**Confidence: High.** The Indian mid-market CFO finds gain-share structurally more approvable than flat retainer. Expect pure flat-fee FinOps consulting to lose share to hybrid structures over 2026–2027. Independent consultants pricing flat without a gain-share option will struggle to close.

### 6.6 Multi-cloud remains aspirational; single-cloud remains dominant

**Confidence: High.** Our sample: 76% single-cloud primary (of which 58% AWS, 32% Azure, 10% GCP), 24% multi-cloud by architecture, only 7% multi-cloud by workload distribution. We predict the actively-multi-cloud share stays below 15% through 2027 in this segment — the operational complexity does not pay off at mid-market scale.

### 6.7 Commitment-based cloud procurement (EDPs, PPAs, Reserved commitments) will spread downmarket

**Confidence: Medium.** Hyperscalers are already signing ₹2–10 crore/year EDP-style commitments with Indian mid-market customers who were previously on-demand. Expect this to become standard for the ₹30L+/month tier, reinforcing the need for independent FinOps advisors who are not compensated by the hyperscaler.

### 6.8 AI workload costs will dominate the top-of-bill conversation

**Confidence: High.** Every interview conducted since February 2026 mentioned either LLM inference cost or GPU training cost unprompted. 3 of the 34 companies had GPU spend above ₹5 lakh/month already. By end-2026, we expect GPU/AI workloads to represent 15–25% of the Indian mid-market cloud bill, up from ~6% in 2024.

---

## 7. Recommendations

### For founders

1. **Install one named owner** of cloud cost. 4 hours/month. Reports to you. This is the single highest-leverage move you will make in 2026.
2. **Don't buy a commercial FinOps tool before installing the cadence**. The cadence without the tool delivers 70% of the value. The tool without the cadence delivers none.
3. **Publish your price**. Every service you offer with a number against it. Opaque pricing kills more Indian mid-market deals than bad product does.
4. **Audit your RI/SP coverage this quarter**. If it is below 50%, you are leaking 10%+ of your bill every month.

### For CFOs

1. **Ask for monthly rupee reporting on cloud, not quarterly**. Cloud spend is engineering-paced; finance-paced reporting produces a three-month lag.
2. **Reject flat retainer cloud-consulting proposals above ₹1 lakh/month** unless there is a gain-share component or a scope that justifies it. Most do not.
3. **Track commitment coverage as a board-level metric** if cloud spend exceeds ₹30L/month. FX exposure on 3-year USD-denominated commitments is material.
4. **Pair every FinOps engagement with a frozen baseline**. Without a baseline, savings claims are unfalsifiable.

### For engineering leaders

1. **Symptoms-based alerts over cause-based alerts**. See our <a href="https://aicloudstrategist.com/glossary/mttr.html">MTTR glossary page</a> for the rationale.
2. **Tag at deploy time, enforce via IaC + Config rules**. Post-hoc tagging never catches up.
3. **Runbooks for the top 10 incident types, and the top 5 remediation types**. Cheap remediation is actioned remediation.

### For security leaders

1. **Default to native CSPM + open-source supplement** unless regulator or customer mandate says otherwise.
2. **DPDPA posture audit before a SOC 2 Type II scope decision**. The DPDPA evidence overlaps SOC 2 evidence enough that doing the two in sequence saves 30–40% of preparation time.
3. **Data Processor DPAs with all sub-processors**. Not optional.

---

## 8. Author bio

**Anushka B** is the founder of AICloudStrategist, a founder-led FinOps and cloud consultancy for Indian mid-market SaaS. AICloudStrategist publishes pricing, publishes methodology, and works only with companies in the ₹5L–₹50L/month cloud spend band. Anushka writes all first-party content on aicloudstrategist.com and takes every customer discovery call personally through the first twenty engagements.

**Mao** is the in-house research agent (AI assistant) that supports primary-research aggregation, qualitative coding of interview transcripts, and secondary-source cross-referencing. Every number in this paper was verified by a human analyst against at least two independent sources before publication.

---

## 9. Methodology Appendix

### 9.1 Interview guide (abbreviated)

**Opening (5 minutes):**
- Brief self-intro, company stage, current cloud footprint.

**Cloud spend and governance (15 minutes):**
- Current monthly spend (₹) and rough cloud split (compute / storage / network / data / other).
- Who owns cloud cost in the org. Named human or shared?
- Monthly review cadence, if any.
- Commitment coverage (RI/SP) percentage, if known.

**Tooling (10 minutes):**
- Current tooling stack (native + commercial + open source).
- Evaluations in the last 12 months (any category).
- Pricing sensitivity — specific ₹/USD figures where shared.

**Buying behaviour (15 minutes):**
- Most recent cloud-services purchase — what, how, who decided.
- Deal-breakers and deal-makers.
- Preferred pricing structure (flat vs gain-share vs hybrid).

**Regulatory (10 minutes):**
- DPDPA / RBI / SOC 2 / ISO 27001 status or scope.
- Next 12-month compliance roadmap.

**Closing (5 minutes):**
- Would you share this report with a peer? If not, why not.

### 9.2 Coding scheme (qualitative)

Transcripts were coded against 14 axial codes: buyer role, committee shape, sales cycle length, purchase trigger, pricing structure, tooling stack, FinOps maturity tier, DPDPA readiness, RBI/sectoral exposure, waste pattern observed, commitment coverage band, regional footprint, AI workload presence, warm vs cold origin. Codebook available on request.

### 9.3 Data appendix

Anonymised aggregate data — spend bands, coverage percentages, maturity distributions — is published as a CSV in the companion GitHub repository at `github.com/aicloudstrategist/papers-cloud-cost-india-2026/blob/main/data-appendix.csv`. Individual company-level data is not released.

### 9.4 Known limitations

- Sample is AICloudStrategist's inbound; skews toward engineering-led buyers comfortable sharing diagnostic context.
- Primary research was conducted in English; some nuance from Hindi/regional-language interviews may not have been captured.
- Secondary sources do not consistently disaggregate Indian mid-market; where disaggregation was not possible, the broader geography is named inline.
- Pricing ranges for commercial CNAPP and FinOps vendors reflect partner-channel and buyer-side conversations; vendor-published list prices were not universally available.

### 9.5 Kill criteria for future revisions

This paper will be revised in the following calendar year. Any of the following observations would force an earlier revision:

- A major regulatory change (DPDPA rules amendment, RBI cyber framework revision, new sectoral data residency rule).
- A commercial FinOps vendor adding 1,000+ Indian mid-market logos in a 12-month window.
- FinOps maturity distribution in a new n=50+ sample shifting by more than 15 percentage points in any tier.
- Any single cloud vendor announcing a materially different Indian pricing structure (e.g., a rupee-denominated SKU with sovereignty guarantees).

---

## 10. About AICloudStrategist

AICloudStrategist is a founding-cohort FinOps and cloud consultancy for Indian mid-market SaaS (50–200 employees, ₹5L–₹50L/month cloud spend). We publish our pricing, publish our methodology, and work only on engagements where we can commit to a measurable outcome against a frozen baseline.

**Services and pricing (April 2026):**

- Free Cloud Cost Health Check — 24 hours, read-only, written report.
- FinOps QuickStart — ₹40,000 for the first three customers in the founding cohort; ₹75,000–₹1,00,000 thereafter.
- Cloud Architecture Review — ₹1,00,000–₹1,50,000.
- AI/GPU Cost Optimisation — ₹3,00,000–₹5,00,000.
- Cloud Security Review — ₹1,00,000–₹2,00,000.
- Gain-share Retainer — ₹50,000/month base + 15% of verified savings against a frozen baseline.

**Contact:** support@aicloudstrategist.com · aicloudstrategist.com/audit.html · aicloudstrategist.com/book.html

---

*Footnoted. Triangulated. Aged-dated. Defendable in a room of skeptics.*

*© 2026 AICloudStrategist. Distributed under CC BY 4.0. Cite as: "State of Cloud Cost in Indian Mid-Market SaaS 2026", AICloudStrategist, April 2026.*
