# Your Reserved Instance Coverage Is Probably Under 30 Percent. Here Is Why That Matters.

*Published on aicloudstrategist.com/blog*

---

Every AWS account we audit has the same conversation.

"What is our Reserved Instance coverage?"

"High. Most of the fleet. Maybe 70, 75 percent."

We pull the report. It is 28 percent.

The gap between what engineering teams believe about their RI coverage and what the billing data actually shows is the single most expensive blind spot in mid-market AWS accounts. It is not a rounding error. It is a structural pricing penalty that compounds every month nobody looks.

## The math, in rupees

A t3.xlarge in ap-south-1 runs **$0.1856 per hour On-Demand** and **$0.1178 per hour on a 1-year No Upfront Reserved**. That is a **36.5 percent discount** — for a keystroke.

Here is what that means in practice. Say you run 20 t3.xlarge instances continuously. Six are RI-covered. Fourteen are not.

Those fourteen On-Demand instances cost **$1,896 a month**. If they were on a 1-year No Upfront RI, they would cost **$1,202**. The delta is **$694 a month. $8,330 a year.** For one instance family, in one region, at one commitment level.

Scale that exposure across the m5, r5, and c5 families that most mid-market engineering orgs run, and the unhedged position is typically **₹35 lakh to ₹1 crore a year** — sitting there, month after month, because nobody is running the coverage report.

## The 15-minute Cost Explorer check

You can do this now, on your own account:

1. AWS Cost Explorer → **Reservations** → **Coverage Report**
2. Granularity: **Monthly.** Date range: **last three months.**
3. Group by **Instance Type**
4. Filter to **ap-south-1** (or whichever region is your primary)
5. Sort by **On-Demand Cost**, descending

Any row where coverage is below 70 percent and On-Demand spend is above $500 a month is a purchase decision waiting to be made. The report also timestamps when coverage dipped — invaluable for tracing the dip back to the autoscaling change or the new service deployment that quietly outgrew the original commitment.

## Why this is worth doing before the CFO asks

Cloud costs become a board-level question about 12 months before engineering teams are ready for them. The conversation usually arrives as: *"Why has the bill grown 40 percent year-on-year?"*

The honest answer is almost always the same. Compute scaled. Commitments did not.

Running the coverage report once a quarter, with a named owner and a documented purchase policy, is the cheapest governance you will ever implement. It takes 15 minutes. The findings are usually uncomfortable. That is exactly the point.

If you want a second set of eyes on yours, our free 30-minute Cloud Cost Health Check is built for this conversation specifically. You share a 7-day Cost and Usage Report sample. We send back a two-page written summary by end of the same day, covering your top three leaks and the recoverable amount against each — founder-led, enterprise-reviewed.

**[Book the Health Check → aicloudstrategist.com/book.html](https://aicloudstrategist.com/book.html)**

---

*AICloudStrategist · Founder-led. Enterprise-reviewed. · FinOps for AWS, Azure, and GCP teams*
