# LinkedIn Post — Orphaned EBS Volumes (Post C: Indian Cloud Market Observation)

---

Indian cloud teams have largely closed the compute waste conversation. Reserved Instances, Savings Plans, right-sizing — these are now standard operating practice for mature engineering orgs in Bengaluru and Hyderabad.

EBS volumes are a different story.

In a recent engagement with a mid-sized SaaS company (anonymised), we scanned their ap-south-1 account and found 38 unattached EBS volumes totalling 4.2 TB. Every volume was fully provisioned, generating charges. Every one had been orphaned at EC2 instance termination.

The mechanism is mundane: AWS sets `DeleteOnTermination=false` by default for EBS volumes attached after instance launch. A developer attaches a data volume, the instance is terminated weeks later — via automation, a Jira ticket, an autoscaling lifecycle event — and the volume persists, billed at $0.10/GB-month with nothing reading or writing to it.

The Indian mid-market has invested seriously in compute governance. EBS governance lags by 12–18 months across most accounts we see. Snapshots compound this. Autoscaling groups accelerate it.

The 4.2 TB in that audit was not an anomaly. It was a baseline.

---
*AICloudStrategist | FinOps for AWS teams*
