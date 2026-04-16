# How We Structure Gain-Share on FinOps Engagements (And Why Most Consultancies Don't Offer It)

*By Anushka B*

---

Most cloud consulting engagements work like this: you pay a fixed fee, the consultant delivers a report, and whatever savings materialise are yours to capture — or not. The consultant gets paid either way.

I've been on the receiving end of those reports. The recommendations are technically correct. The spreadsheet math checks out. The presentation deck is immaculate. And then the engagement ends, the consultant moves to the next client, and your engineering team looks at a 47-item action list and asks who, exactly, is supposed to implement all of this and by when.

Six months later, your cloud bill has gone up. The report is on a SharePoint that three people have bookmarked and zero people have opened since the kickoff meeting. You've spent ₹8–12 lakhs on analysis that produced no verified savings.

This is not a hypothetical. It is the standard outcome for the majority of flat-fee cloud cost engagements in Indian mid-market companies.

Gain-share is the structural fix. Here's how it works, how we structure it, and why the firms with the biggest logos on their proposals won't touch it.

---

## The Alignment Problem with Flat-Fee

A flat-fee FinOps engagement has one aligned incentive: the consultant wants to deliver something that looks thorough enough to justify the invoice.

That is not the same incentive as: *the consultant wants your cloud bill to go down*.

When a firm bills ₹15 lakhs for a cloud cost assessment, their interest is in the assessment — the output, the document, the presentation. Whether you act on it is your problem. Whether the actions work is, frankly, also your problem. The engagement is over.

This isn't malice. It's just how fixed-scope professional services work. The risk is entirely on your side of the table. You pay for advice. Results are not contracted.

Gain-share inverts this completely. The consulting firm gets paid based on what they actually save you. They have every reason to find the biggest wins, help you implement them, and stay engaged until savings are verified. If the savings don't materialise, they don't get paid. That's alignment.

---

## How We Structure It

Every gain-share engagement we do has four components. None of them are negotiable, because removing any one of them creates the wrong incentives somewhere in the arrangement.

**1. The savings floor**

We don't start sharing until verified savings cross a minimum monthly threshold. The floor protects you from paying a share on noise — small optimisations that accounting rounding error could produce anyway without any intervention.

Our standard floor is ₹2 lakhs per month in verified gross savings. Below that, the engagement is still running, we're still working, but no share is due. This also filters out engagements where the opportunity isn't large enough to justify the structure — if your bill is ₹5 lakhs/month total, gain-share doesn't make sense.

**2. The percentage share**

Above the floor, we take a percentage of gross verified savings. For FinOps engagements, our standard is 25%. This means for every ₹100 in savings we generate above the floor, ₹25 goes to us and ₹75 stays with you.

Why 25%? It reflects the work involved — not just the analysis, but the implementation support, the RI purchase coordination, the tag governance setup, the Savings Plans modelling, the two-weeks-in call when your DevOps lead pushes back on rightsizing recommendations. It prices in the risk we're taking that none of this works. And it leaves you with 75 paise of every rupee saved — a return profile that no fixed-fee engagement can match because fixed-fee doesn't require the savings to exist.

**3. The measurement window**

Savings are measured on a rolling 6-month basis from the date each optimisation is implemented, not from contract start. This is important.

Cloud bills fluctuate. A month-one win might be obscured by new workloads in month two. The 6-month window smooths for growth, for architectural changes, for seasonality. We compare actual spend against a modelled counterfactual baseline (what you would have spent without the intervention), adjusted for workload growth. Every calculation is shown to you in full before any invoice is generated.

At the end of 6 months, we produce a verified savings statement — a line-by-line reconciliation of every recommendation, what was implemented, and what it saved. That document is the billing basis.

**4. The cap**

There is a maximum payout in each engagement. Ours is typically set at 1.5× the fixed-fee equivalent for a comparable scope assessment — so if the same engagement done flat-fee would have cost ₹12 lakhs, our gain-share cap is ₹18 lakhs.

The cap protects you in the tail scenario: we find a catastrophic misconfiguration that was silently burning ₹80 lakhs a year, we fix it in week two, and suddenly the uncapped 25% share is ₹20 lakhs. The cap makes the arrangement predictable for budgeting and removes the awkward dynamic where a single lucky find produces an invoice that feels disproportionate.

---

## A Worked Example

Let's make this concrete.

A Series C SaaS company, AWS-primary, ~₹60 lakhs/month cloud bill. They came to us having done one prior cloud cost exercise that produced a report but no implemented savings. Baseline coverage: 19% RI, no Savings Plans, significant inter-region data transfer, 34 oversized RDS instances.

Engagement starts. Over eight weeks we implement: RI purchases bringing coverage to 68%, Savings Plans for Lambda and Fargate, cross-region egress rerouting via VPC endpoints, RDS rightsizing on 28 of 34 instances.

**Month 1–6 verified savings: ₹14.2 lakhs/month gross, averaged**

Savings floor: ₹2 lakhs. Net share-eligible savings: ₹12.2 lakhs/month.

Our 25% share: ₹3.05 lakhs/month.

Over 6 months: ₹18.3 lakhs. Cap (1.5× flat-fee equivalent of ₹12 lakhs) = ₹18 lakhs. So we invoice ₹18 lakhs.

**Their net position:** ₹14.2 × 6 = ₹85.2 lakhs in gross savings. Minus ₹18 lakhs to us. Net retained: ₹67.2 lakhs over 6 months.

Compare that to a flat-fee engagement: ₹12 lakhs, a PDF, zero guaranteed savings. The gain-share engagement cost them ₹6 lakhs more. It returned ₹67.2 lakhs in verified savings. The math is not subtle.

---

## Why the Big Four Won't Do This

This is the question I get most often, usually from procurement teams who want to know if I'm the only one doing this or if they should be comparing us to Deloitte on this basis.

The answer is structural, not accidental.

Large consulting firms bill by the hour and by the head. A partner-led engagement at a Big Four or major SI has an internal cost structure built around utilisation — getting a billing rate applied to as many analyst hours as possible. Gain-share breaks that model entirely. It ties revenue to an outcome that happens over a 6-month period, not to the hours delivered in Q1. It requires the firm to carry risk on its own P&L across an engagement lifecycle that doesn't map to quarterly targets.

There's also a risk aversion problem. A firm that bills ₹500 crore a year across hundreds of engagements has no incentive to introduce a compensation structure where a client relationship produces zero revenue if the savings don't materialise. The fixed-fee model is safe. It protects margin. It insulates partners from delivery risk.

And there's a practical capability gap. Doing gain-share correctly requires deep implementation capability — not just analysis, but the ability to actually push a Savings Plans purchase, re-engineer a data transfer path, execute a tag governance rollout. Large firms often staff these engagements with analysts whose job is to document recommendations, not implement them. Gain-share collapses when you can't execute. They know this about themselves.

Smaller specialists can carry implementation risk because they have to. It's how we compete.

---

## The Invitation

If your cloud bill is above ₹20 lakhs/month and you've had at least one prior cost assessment that didn't deliver verified savings, gain-share is worth a serious conversation.

I'll tell you upfront in the first call whether your environment has enough opportunity to justify the structure. If it doesn't, I'll tell you that too — along with what a focused fixed-scope engagement would look like instead.

No pitch decks. No discovery questionnaire with 40 fields. Thirty minutes, your latest billing export, and an honest conversation about what's actually on the table.

That's the starting point.

---

*Anushka B works on cloud cost architecture and FinOps strategy for growth-stage and mid-market companies across India and Southeast Asia. She takes gain-share engagements because she is confident in the work.*

---

*Tags: FinOps, Cloud Cost Optimization, Gain-Share, AWS, GCP, Cloud Consulting, India Cloud, Mid-Market*
