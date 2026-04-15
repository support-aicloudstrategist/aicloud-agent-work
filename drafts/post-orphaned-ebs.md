# LinkedIn Post — Orphaned EBS Volumes (Post C: Indian Cloud Market Observation)

---

Indian engineering teams have largely closed the compute waste conversation. Reserved Instances, Savings Plans, right-sizing — standard practice now in mature Bengaluru and Hyderabad orgs.

EBS volumes are a different story.

Earlier this month we reviewed an ap-south-1 account for a mid-market SaaS company. The finding: **38 unattached EBS volumes. 4.2 TB in total. Nothing reading, nothing writing.** Every one of them was still being billed.

Every one had been orphaned at instance termination.

The mechanism is unglamorous. AWS sets `DeleteOnTermination=false` by default for volumes attached after instance launch. A developer attaches a data volume for a migration. Weeks later the instance is terminated — by automation, a Jira ticket, an autoscaling lifecycle event — and the volume outlives it. Billed at $0.10 per GB-month, forever, with nothing touching it.

4.2 TB × $0.10 × 12 = **$5,040 per year**, or roughly **₹4.2 lakh**, disappearing into nothing.

And this is the part worth saying out loud: the Indian mid-market has invested seriously in compute governance. EBS governance lags by 12 to 18 months across most accounts we have reviewed. Snapshots compound the problem. Autoscaling groups accelerate it.

The 4.2 TB in that audit was not an anomaly. It was a baseline. If you have not run this check, you almost certainly have your own version of it quietly running up a bill.

```bash
aws ec2 describe-volumes \
  --filters Name=status,Values=available \
  --query "Volumes[].[VolumeId,Size,CreateTime,Tags]" \
  --output table
```

Run it this week. Tag what you find. Delete what nobody claims after 30 days.

— Anushka B, Founder · AICloudStrategist
*Founder-led. Enterprise-reviewed.*

---
