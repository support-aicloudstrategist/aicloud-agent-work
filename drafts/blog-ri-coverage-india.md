# Why 70% of Indian Mid-Market Cloud Accounts Have Reserved Instance Coverage Below 30%

*By Anushka B*

---

There's a number that keeps coming up in every cloud cost conversation I have with Indian mid-market companies. Not the bill. Not the growth rate. The coverage number.

Ask a CTO what their RI coverage is. They'll say "we have Reserved Instances." Ask the finance lead. They'll say "yes, engineering took care of that." Pull the AWS Cost Explorer report. 22%. Maybe 27% if you're generous about how you count convertible RIs purchased two years ago that no longer match any running instance family.

This is the belief-vs-data gap that costs Indian companies, conservatively, ₹40–80 crore in aggregate every year — not from bad architecture, not from over-provisioned instances, but from a purchase that never got made. The discount was there. The runway was there. Someone just never pulled the trigger.

Here's why. And more importantly, here's how you fix it in one afternoon.

---

## The Structural Problem Nobody Wants to Own

Reserved Instances sit in a uniquely awkward position inside most mid-market Indian tech companies. They're a financial instrument that requires engineering knowledge to purchase correctly. That combination guarantees ownership confusion.

**Engineering teams** understand instance families, utilization curves, and what workload will be running six months from now. But they don't control procurement budgets. They're not incentivized to reduce spend — they're incentivized to ship. RI purchasing isn't on their OKRs. If the bill goes up because coverage is low, finance complains, but engineering doesn't feel that pain directly.

**Finance teams** control the budget and understand that RIs save money. But they don't know a c5.xlarge from an r5.2xlarge. When engineering submits an RI purchase request — if they ever do — it goes through a procurement process designed for SaaS subscriptions and server hardware. Standard lead time: 3–6 weeks of approvals. By the time the purchase goes through, the usage has shifted and the RI is already partially mismatched.

**The result:** Nobody owns it. RIs get purchased reactively — when a CFO sees a large bill and says "why aren't we using Reserved Instances?" — not proactively, on a cadence that matches actual usage growth.

---

## The Finance Calendar Problem

Indian mid-market companies typically run on April–March fiscal years. Cloud usage doesn't care about fiscal years.

Here's what actually happens: RI purchasing conversations happen in Q4 (January–March) during budget reviews. Engineering is heads-down on pre-fiscal-year launches. Finance is closing books. The conversation gets tabled. Q1 starts (April), everyone is busy with new-year planning. By Q2, the bill has grown 20% and the moment to lock in the right instance mix has passed.

Meanwhile, AWS bills on a rolling month. The on-demand meter runs continuously. That gap between "we should buy RIs" and "we actually bought RIs" is where the money disappears.

The companies that have coverage above 60% don't have smarter engineers. They have a named RI owner — usually a platform or FinOps engineer — with a calendar reminder every 90 days that says: *pull utilization report, calculate coverage gap, submit purchase request by end of week.*

That's the entire secret.

---

## The ap-south-1 Pricing Math (Run This on Your Account Today)

Let's be specific. Here is what low coverage actually costs you, using current ap-south-1 on-demand versus 1-year no-upfront RI pricing across the four instance families that dominate Indian mid-market workloads:

| Family | On-Demand/hr | 1-Yr RI/hr | Savings | Annual savings per instance |
|--------|-------------|-----------|---------|----------------------------|
| t3.medium | $0.052 | $0.031 | 40% | ~$184 |
| m5.large | $0.096 | $0.058 | 40% | ~$333 |
| r5.large | $0.126 | $0.076 | 40% | ~$438 |
| c5.large | $0.085 | $0.051 | 40% | ~$298 |

Now apply this to a realistic mid-market environment: 200 instances, mix-weighted average of roughly $0.09/hr on-demand, running at 70% steady-state utilization (meaning 140 instances should be RI-covered at any time).

At 25% RI coverage: 35 instances on RIs, 105 on on-demand.
At 70% RI coverage: 98 instances on RIs, 42 on on-demand.

The delta — 63 instances shifted from on-demand to 1-year no-upfront RI — saves approximately:

**63 × $0.09 × 0.40 × 8,760 hours = ~$19,900/year**

In rupees at current rates: roughly **₹16.5 lakhs per year**. From a purchase decision that takes 20 minutes to execute once the analysis is done.

For companies running 500+ instances, multiply accordingly. The ₹40–50 lakh annual savings figure I cite is not aggressive — it's arithmetic.

The 3-year RI math is even more compelling (62–65% savings versus on-demand), but most Indian mid-market companies are understandably reluctant to commit 3 years. The 1-year no-upfront RI is the easiest entry point: no capital required, immediate savings, 12-month flexibility to reassess.

---

## The Governance Framework: Three Non-Negotiable Elements

Having bought RIs once does not mean you have an RI program. Most companies that are at 25% coverage have bought RIs — they just haven't maintained them. Here's the minimum viable governance structure:

**1. Named owner with a 90-day mandate**
One person — not a team, one person — owns RI coverage as a metric. Their job every quarter: pull the AWS Cost Explorer RI utilization and coverage reports, identify the coverage gap, and submit a purchase request or Convertible RI exchange. This role is not full-time. It's 3 hours every 90 days. But it has to be someone's name on it.

**2. Documented purchase policy**
Two decisions need to be written down, agreed upon, and not relitigated every time: (a) what utilization threshold triggers an RI purchase (recommended: any instance type running >60% of hours over the trailing 30 days), and (b) what your RI term preference is (1-year no-upfront as default, revisit 3-year for databases and core infra annually). Without this written down, every purchase request becomes a negotiation. With it, the named owner executes against a policy.

**3. Quarterly coverage review in the finance calendar**
Not ad hoc. Not when someone notices the bill. Scheduled. Last month of every quarter, 45-minute meeting: RI owner presents coverage number, gap, and proposed purchases. Finance approves or adjusts. Done. This meeting makes RI purchasing a process instead of a heroic one-time effort.

These three things are not complex. The reason 70% of mid-market Indian accounts don't have them is not incompetence — it's that nobody told them this was the playbook.

---

## The One-Afternoon Action Plan

If you're reading this and your RI coverage is below 30%, here's exactly what to do this afternoon:

**Step 1 (20 minutes): Pull your baseline.**
Log into AWS Cost Explorer → Reservations → Coverage. Set the trailing 90-day window. Export the instance-level breakdown. Note the three highest on-demand spend lines that have no RI coverage.

**Step 2 (15 minutes): Run the math.**
For each of those three instance types: monthly on-demand spend × 40% = monthly savings. Multiply by 12. That's the annual saving from buying 1-year no-upfront RIs for those workloads. You now have a business case with a rupee number.

**Step 3 (10 minutes): Make the purchase or start the approval.**
If you have direct AWS console access and authority to commit, buy the 1-year no-upfront RIs now. No upfront cost. Savings start within the hour. If you need finance approval, send the math from Step 2 as the approval request with a one-sentence note: "This is a commitment to continue running instances we are already running, at 40% lower cost."

**Step 4 (5 minutes): Set the 90-day reminder.**
Calendar invite, 90 days from today, to yourself and whoever owns finance. Subject: "RI Coverage Review — [Month] [Year]." Recurring. This is the act that converts a one-time purchase into a program.

Total elapsed time: 50 minutes. Total annualized impact: measured in lakhs.

---

## The Deeper Issue

The 70% statistic isn't primarily a technical problem. It's a coordination problem dressed up as a cloud problem. Engineering knows the instances. Finance controls the budget. Nobody owns the intersection.

Every Indian mid-market company I've worked with that has coverage above 65% made one organizational decision: they assigned a person, gave them a metric, and put that metric in a recurring calendar. The tooling doesn't matter. The instance family knowledge doesn't matter that much. The 40% savings math is simple enough that a spreadsheet handles it.

What matters is that someone decided this was worth owning — and then actually owned it.

Your AWS bill doesn't negotiate. Every month you're below 30% coverage is a month you paid on-demand prices for committed workloads. The discount is sitting there waiting. The only question is whether you're going to go get it.

---

*Anushka B works on cloud cost architecture for growth-stage and mid-market companies across India and Southeast Asia. If your RI coverage number is giving you anxiety, she's the person to call.*

---

*Tags: AWS, Reserved Instances, FinOps, Cloud Cost Optimization, ap-south-1, India Cloud, Mid-Market*
