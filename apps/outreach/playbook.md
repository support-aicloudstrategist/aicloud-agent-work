# AICloudStrategist — Outreach Playbook v1.1

---

## 1. Warm-Network WhatsApp Voice-Note Script

### Spoken Script (~60 seconds)

> "Hey [Name] — Rajiv here. We worked together back in [2018 / at our old firm / on the [ClientX] engagement] — must be [X] years now. Hope you're doing well, and the family too.
>
> Quick update from my side: after 22 years with Fortune 500 systems integrators and global consulting firms, I've just started my own cloud cost consultancy — AICloudStrategist. The focus is helping Indian companies cut their AWS, Azure, or GCP bills by 20 to 30 percent in about four weeks. FinOps practices, open source tooling — proper analysis, measurable savings.
>
> I'm offering a free 30-minute Cloud Cost Health Check right now — no pitch, just a clear look at where the spend is going. If you or anyone in your network is spending a few lakhs a month on cloud, I'd genuinely like to help.
>
> Drop me a message when you get a moment. And let's catch up properly regardless — it's been too long."

### Written Fallback (when voice note is not possible)

"Hey [Name] — Rajiv here, we worked together back in [year / at the old place]. Just launched AICloudStrategist — helping Indian companies cut cloud bills 20-30% in 4 weeks using FinOps, and I'm offering a free 30-min Cloud Cost Health Check right now with no strings attached.

If you or anyone in your network is spending a few lakhs a month on cloud and wants a second opinion on the bill, I'd genuinely like to help. Good to reconnect."

---

## 2. LinkedIn Connection-Request 5-Message Sequence

### Message 0 — Connection Request Note

*(LinkedIn cap ~300 characters)*

Hi [Name] — we worked together some years back. I've just launched AICloudStrategist, helping Indian SMBs cut cloud costs 20-30% in 4 weeks using FinOps. Would be good to reconnect. — Rajiv

*(~192 characters)*

---

### Message 1 — Day 2 after acceptance

Thanks for connecting, [Name].

I put together an AWS Cost Optimisation Checklist — 30 common leak points that come up repeatedly in mid-size cloud setups. No form, just the PDF: aicloudstrategist.com/downloads/aws-cost-cutting-checklist-indian-smbs.pdf.

If your team is on AWS and the bill has been creeping up, it may flag a few quick wins. Happy to talk through anything on it.

*(~59 words)*

---

### Message 2 — Day 5

[Name], one number worth knowing: the average Reserved Instance coverage ratio in accounts I review is 34%. For stable workloads, it should be above 70%.

That gap alone typically represents 15-20% in avoidable spend — no re-architecture required.

If cloud costs are on your radar, I offer a free 30-minute Health Check — structured, no sales process. Details: aicloudstrategist.com/book.html.

*(~63 words)*

---

### Message 3 — Day 10

[Name] — the FinOps Maturity Self-Assessment on aicloudstrategist.com/downloads might be worth 10 minutes.

It maps 4 stages of cloud financial management with specific indicators for each. Most mid-market companies I speak to are at Stage 1 and are unaware of it.

The document gives you a baseline — no call required. If it raises questions, I'm easy to reach.

*(~57 words)*

---

### Message 4 — Day 18 (graceful exit)

[Name] — I've sent a few notes and haven't heard back, which is completely fine.

If cloud cost work becomes relevant down the line, I'm at support@aicloudstrategist.com. The free 30-min Health Check and both downloads remain available at aicloudstrategist.com whenever useful.

Wishing you well. — Rajiv

*(~48 words)*

---

## 3. Cold Email 3-Email Sequence

*(Plain text. Send from support@aicloudstrategist.com. Personalise First Name and Company at minimum. Warm up a secondary sending domain first if volume exceeds 30/day.)*

---

### Email 1

**Subject:** Quick question about your cloud bill

Hi [First Name],

My name is Rajiv — I run AICloudStrategist, a cloud cost consultancy based in Rohini, Delhi.

Most Indian companies spending INR 5L+ a month on AWS, Azure, or GCP have 15-30% in avoidable spend. Not from re-architecture — from Reserved Instance gaps, idle compute, and storage that hasn't been reviewed since the original setup.

I offer a free 30-minute Cloud Cost Health Check: a structured look at where the spend is going, no sales process.

Worth a quick conversation?

Rajiv
AICloudStrategist | aicloudstrategist.com
Rohini, Delhi 110085

*To stop receiving emails from me, reply "unsubscribe."*

---

### Email 2

**Subject:** Cloud cost review — still relevant?

Hi [First Name],

A brief follow-up to my earlier note.

One pattern I see often: companies that moved to cloud during 2020-2022 under pressure and haven't revisited the cost baseline since. The architecture made sense then. Three years of unreviewed auto-scaling and provisioning later, the picture looks different.

A recent engagement took a company from INR 18L to INR 11L per month — same workloads, no re-architecture, four weeks.

Happy to send the FinOps Maturity Assessment if it's useful.

Rajiv
AICloudStrategist | aicloudstrategist.com
Rohini, Delhi 110085

*To stop receiving emails from me, reply "unsubscribe."*

---

### Email 3

**Subject:** Last note from me, [First Name]

Hi [First Name],

Last follow-up — I won't be sending more after this.

If cloud cost optimisation isn't on the agenda right now, that's completely fine. If it becomes relevant in Q3 or Q4, I'm at support@aicloudstrategist.com.

The AWS Cost Optimisation Checklist is at aicloudstrategist.com/downloads — free, no form, may be a useful reference regardless.

Wishing you a good quarter.

Rajiv
AICloudStrategist | aicloudstrategist.com
Rohini, Delhi 110085

*To stop receiving emails from me, reply "unsubscribe."*

---

## 4. LinkedIn Post Cadence — 4 Templates

*(Post Tuesday and Thursday for Month 1. These 4 cover the first two weeks. Rotate angles after.)*

---

### Post A — Credibility / War Story

A company was spending INR 18L a month on AWS. Six weeks later: INR 11L. Same workloads, same team, no re-architecture.

Where did the INR 7L go?

Reserved Instance coverage was at 12% — the recommendation for stable workloads is 70% or above. Savings Plans hadn't been reviewed in two years. Three S3 buckets with intelligent tiering disabled were holding 47TB of data that hadn't been queried in over a year.

The remediation took one senior engineer and four weeks. The tooling was Infracost running in their CI pipeline and OpenCost for cluster-level visibility. Both open source. No new licences.

The CFO had been asking about cloud costs for 18 months. The answer was sitting in Cost Explorer the whole time.

This is the kind of work AICloudStrategist does. If your cloud bill has grown faster than your business and no one's done a structured review — I'd like to take a look. Free 30-min Cloud Cost Health Check, details in bio.

---

### Post B — Practical FinOps Tip with Numbers

If your AWS Reserved Instance coverage is below 70% for stable workloads, you are paying a premium you don't have to.

Here's a check you can run in 15 minutes:

Go to AWS Cost Explorer → Reserved Instance → Coverage. Look at the coverage percentage for your EC2 fleet over the last 30 days. Anything below 70% for workloads running 24x7 is On-Demand spend that could be converted.

Reference point: a t3.xlarge On-Demand in ap-south-1 costs roughly INR 12,500 per month. The same instance on a 1-year No-Upfront RI costs around INR 7,900. That is 37% off, zero architectural change.

Scale that across a 20-instance fleet and you are looking at INR 90,000 saved per month. One afternoon of analysis. No code changes. The saving shows up in the next billing cycle.

Want help running this across your account? Free 30-min Cloud Cost Health Check — link in bio.

---

### Post C — Indian Cloud Market Observation

Indian cloud spending crossed $15 billion in 2024. A significant share of that growth came from companies that were not structured to manage cloud finances at scale.

What I see in conversations across NCR mid-market companies: teams that adopted cloud fast during 2020-2022 are now 3-4 years into architectures that were built for speed, not cost efficiency. No one reviewed the baseline. The bill grew with the business, so it looked normal.

Egress charges, orphaned snapshots, over-provisioned RDS instances — these do not appear as a flagged line item in a quarterly review. They compound quietly. INR 2-3L a month in avoidable spend is not unusual for a 100-person company running a reasonable cloud workload.

The companies getting ahead of this are the ones asking the cost question before the CFO does.

I started AICloudStrategist because I have seen this pattern too many times, and the savings are repeatable once someone actually looks. If this resonates, share it with your CTO or drop me a message.

---

### Post D — Personal / Why I'm Doing This

After 22 years across Fortune 500 systems integrators and global consulting firms, I have started something of my own.

Not because the work inside large organisations wasn't good — it was. But most of the cloud cost analysis I did, the reviews that saved companies INR 30-50L a year, stayed inside those walls. The mid-market founders and CFOs running INR 5-20L per month cloud bills did not get a senior architect's time. They got a vendor call and a proposal.

AICloudStrategist is one practitioner, direct engagement, and a clear outcome: 20-30% reduction in cloud spend within four weeks. No junior teams handling the actual analysis, no offshore hand-offs, no 20-page readout that no one acts on. Based in Rohini Delhi, working with Indian SMBs and mid-market companies on AWS, Azure, and GCP.

April 2026 is the start. The first offer is a free 30-minute Cloud Cost Health Check — a structured look at your setup, no sales process.

If you are spending INR 5L or more a month on cloud and have not had a proper cost review, link is in bio.

---

## 5. First-Reply Playbook

| Reply Type | Example Phrases | Immediate Next Action |
|---|---|---|
| **Ready to schedule** | "Yes, let's connect." / "Set up a call." / "When are you free?" | Reply within 2 hours. Send Calendly link for the 30-min Health Check (aicloudstrategist.com/book.html). Add one sentence on the call format: "We'll pull up Cost Explorer together, I'll identify 3-5 specific areas to investigate, and you'll get a written summary by end of day." |
| **Soft interest / more info** | "Tell me more." / "Send the checklist." / "What does the Health Check cover?" | Send the relevant PDF link (aicloudstrategist.com/downloads) immediately. Follow with one short paragraph describing the Health Check format. Close with: "Happy to walk through it in 30 minutes, no obligation." Include Calendly link at the bottom. |
| **Deferred / not now** | "We've sorted this." / "Budget is locked." / "Reach me in Q3." | Acknowledge without pushing. Log a follow-up date in Notion (60-90 days out). Reply: "Understood — I'll check back in [specific month]. Sending the checklist in the meantime, it may be a useful reference when you revisit." Do not contact again before the noted date. |

---

## Usage Note

Never release a batch without your own approval via Telegram first. If daily send volume crosses 30, use a secondary sending domain — e.g. outreach.aicloudstrategist.com — to protect the primary domain's sender reputation. Log every reply in Notion CRM tagged by stage: interested / later / not interested.
