# Why Indian Mid-Market Cloud Spend Will Double Before It Gets Optimised

*By Anushka B*

---

Here is a pattern I see in nearly every mid-market Indian tech company I engage with: their cloud bill is growing at 30–40% year-on-year. Their revenue is growing at 15–20%. Nobody has called a meeting about this.

Not because the CFO doesn't care. Because the CFO doesn't have the number framed that way. They see "cloud costs up ₹12 lakhs this quarter" and "revenue up 18%." Two separate line items. The ratio — the part that should be alarming — never gets calculated.

Run that ratio for three years in a row and you've quietly doubled your cloud spend as a percentage of revenue. A company that was spending 8% of revenue on cloud infrastructure is now spending 14–16%. The bill didn't feel like a crisis at any single point. It just... accumulated. That's the trap, and almost every company in the ₹20–150 crore ARR band is somewhere inside it.

Here's why it happens — and why most companies will let it compound further before they do anything structural about it.

---

## The Gap Is Not an Accident

Cloud spend and revenue are supposed to grow together. At early stage they don't, because you're investing ahead of demand. That's fine. The problem is when companies leave "investment mode" mentally but never actually change how cloud gets provisioned and governed.

The root mechanism is simple: **every team provisions for peak, but you're only ever at peak for a fraction of your hours**. An engineering team launching a new service doesn't spin up what they need right now — they spin up what they might need on a bad day in six months. That's rational individual behavior. Aggregated across twelve product teams, each doing the same thing, it becomes a structural tax.

Then the compounding kicks in. Old services get replatformed. New services get added. The old ones don't get decommissioned — they just go quiet. Dev and test environments run 24/7 because nobody's tracking them. RDS instances sit at 8% CPU utilization because nobody ever right-sized them after the initial scale-up. Each of these is a small number. Twelve teams, three years, zero governance: the numbers stop being small.

The 30-40% cloud growth is not primarily driven by business growth. It's driven by accumulation. New spend layers on top of old spend because there is no systematic mechanism to remove what's no longer needed.

---

## The Three Phases Every Indian Mid-Market Company Goes Through

I've never met a company that skipped directly to governance. Everyone moves through the same three phases, just at different speeds.

**Phase 1: Over-Provisioning**

This is the default state. Cloud feels abundant — that's the whole point — and the mental model of "always provision generously so nothing breaks" is deeply embedded in how most teams learned to build. Tagging is inconsistent or nonexistent. No one can tell you which team owns which resources. The AWS account is a single environment with no cost allocation by product, team, or service. Engineers are rewarded for uptime, not efficiency.

The bill grows. Finance notices eventually. A meeting happens.

**Phase 2: Awareness**

This is where most Indian mid-market companies are right now. A CFO or CTO looked at the bill, asked questions, and someone pulled a Cost Explorer report. They found some obvious waste — idle EC2 instances, an oversized RDS, a forgotten test environment burning ₹80,000 a month. They cut it. They felt good about it.

Six months later, the bill is back to where it was.

That's because awareness optimisation is a one-time event. It addresses the visible surface. It doesn't address the structural reasons the surface keeps accumulating. The company is still in Phase 1 operationally — they just had one cleanup cycle.

Phase 2 companies have the Cost Explorer open. They do not have a FinOps practice.

**Phase 3: Governance**

Phase 3 looks deceptively simple from the outside: someone owns the number, and that number is reviewed on a cadence. In practice, it requires four specific things to be true simultaneously:

1. **Resources are tagged and attributed** — every running workload can be traced to a team, product, or environment
2. **Budgets have owners and alerts** — not just a global AWS budget, but per-team, per-environment budgets with thresholds that actually notify the right person
3. **Commitment purchasing happens on a schedule** — RI coverage above 60%, reviewed quarterly, with a named person responsible
4. **Cost is an engineering metric, not a finance complaint** — engineering OKRs include unit cost targets; the platform team reviews cost alongside latency and error rates

None of this is technically complex. The gap between Phase 2 and Phase 3 is not a tooling gap. It is an ownership gap.

---

## What Separates the Companies That Get to Phase 3

I've watched companies make this transition. The ones that succeed do one thing differently from the ones that don't: **they stop treating cloud cost as a procurement problem and start treating it as an engineering problem.**

Phase 2 companies handle cloud cost through finance. The bill comes in, finance raises a question, engineering does an audit, something gets cut. The cycle is reactive, slow, and has no feedback loop into how services get built.

Phase 3 companies handle cloud cost the way they handle latency. There's a metric. There's an owner. There's a threshold that triggers investigation. When the metric moves, someone who understands the system looks at it — not someone who has to translate a billing report into a technical question before they can start diagnosing.

The organisational decision that enables this shift is assigning cloud cost to a named person in engineering — typically a platform engineer or a senior tech lead — who carries it as a metric alongside reliability and performance. Not a committee. Not a working group. One person, with a number, reviewed quarterly with finance.

The second distinguishing factor is **connecting spend to product lines**. The companies that reach Phase 3 can tell you what each product costs to run, not just what their total AWS bill is. This sounds like a tagging problem, but it's actually a culture problem — it requires product and engineering leaders to agree that infrastructure cost is a shared accountability, not something that lives entirely in a shared pool.

When a product team can see that their new feature increased EC2 costs by ₹3.2 lakhs per month, they make different architectural decisions. They consider caching. They think about Lambda versus always-on instances. They right-size at launch instead of provisioning for the peak they imagine and never reach.

Without that visibility, every team is optimising for their own delivery metrics and the cost consequence is externalized. Nobody's behaving badly. The system just doesn't generate the signal that would change behavior.

---

## The Compounding You Don't See Until It's Expensive

Here's the uncomfortable arithmetic. A ₹50 crore ARR company spending 10% of revenue on cloud — ₹5 crore annually — that grows cloud at 35% YoY while revenue grows at 20% will be spending 14.5% of revenue on cloud in three years. That's ₹8.4 crore on a ₹58 crore revenue base. The absolute number is ₹3.4 crore higher. The percentage point shift compresses every other margin line.

At Series B and beyond, this becomes a board conversation. Unit economics tighten, burn scrutiny intensifies, and the cloud bill that felt manageable in a high-growth phase suddenly looks like an obvious problem nobody addressed. The remediation at that point isn't a one-afternoon Cost Explorer exercise — it's a six-month FinOps engagement that should have been a 90-day governance program three years earlier.

The companies that double their cloud spend before they optimise are not underfunded or under-staffed. They are under-governed, in a very specific and fixable way.

---

## Where to Start

If your cloud spend is growing materially faster than your revenue and you don't have clear answers to these three questions, you are in Phase 2:

- Which team or product is driving the largest YoY cloud cost increase?
- What is your current Reserved Instance coverage, and who reviews it?
- Which of your environments (dev, staging, prod) have explicit budget owners?

A Cloud Cost Health Check will answer all three in one working session — baseline your current spend profile, identify the structural gaps keeping you in Phase 2, and give you the owner-metric-cadence framework to move into Phase 3 before the number compounds further.

The gap doesn't close on its own. Every month you're at 35% cloud growth and 18% revenue growth is a month the ratio is moving in the wrong direction.

[Book a Cloud Cost Health Check →](https://aicloudstrategist.com/book.html)

---

*Anushka B works on cloud cost architecture and FinOps governance for growth-stage and mid-market companies across India and Southeast Asia. She has seen the three-phase cycle more times than she'd like.*

---

*Tags: FinOps, Cloud Cost Optimisation, AWS, India Cloud, Mid-Market, Cloud Governance, ap-south-1*
