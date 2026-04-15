# Your Reserved Instance Coverage Is Probably Under 30 Percent. Here Is Why That Matters.

*Published on aicloudstrategist.com/blog*

---

Most AWS accounts we audit have Reserved Instance coverage below 30 percent. The teams running them believe it is higher. The gap between belief and reality is where the bill grows.

Coverage below 30 percent means the majority of your steady-state compute is running at On-Demand rates. This is not a rounding error. It is a structural pricing penalty that compounds every month you do not address it.

**The math in ap-south-1**

A t3.xlarge in ap-south-1 costs $0.1856/hour On-Demand. The 1-year No Upfront Reserved rate is $0.1178/hour — a 36.5 percent reduction.

If you are running 20 t3.xlarge instances continuously and only six are RI-covered, the 14 unprotected instances cost $1,896/month. Covered, they cost $1,202/month. The difference is $694/month — $8,330/year — for one instance family in one region.

Scale that across m5, r5, and c5 families and the exposure is typically $40,000–$120,000 annually for a mid-sized engineering org.

**The 15-minute Cost Explorer check**

1. Open AWS Cost Explorer → **Reservations** → **Coverage Report**
2. Set granularity to **Monthly**, date range to last three months
3. Group by **Instance Type**
4. Filter to **ap-south-1** (or your primary region)
5. Sort by **On-Demand Cost** descending

Any row showing coverage below 70 percent with On-Demand cost above $500/month is a purchase decision. The report timestamps when coverage dipped — useful for tracing back to autoscaling changes or new service deployments that outgrew existing commitments.

The check takes 15 minutes. The findings are usually uncomfortable. That is the point.

---

**Book a free RI Coverage Audit → [link in bio]**

*AICloudStrategist | FinOps for AWS teams*
