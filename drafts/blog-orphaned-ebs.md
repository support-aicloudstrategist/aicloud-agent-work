# Orphaned EBS Volumes: The Quiet Compounding Cost Indian Engineering Teams Keep Missing

Every engineering team I talk to has done a cloud cost review at some point. Reserved Instance coverage, right-sizing EC2, maybe a pass at S3 storage tiers. What almost none of them have done is pull a list of every EBS volume currently sitting in `available` state — detached, idle, billing at full price, forgotten. In one mid-market engagement in ap-south-1 last year, that list came back with 38 volumes, 4.2 TB of storage, and a quiet ₹4.2 lakh annual bill attached to infrastructure nobody had touched in months. No alert had fired. No ticket existed. The spend was just compounding in the background.

---

## Why DeleteOnTermination Defaults to False (And Why That's the Root Cause)

When you launch an EC2 instance and attach an EBS volume — whether at launch time or afterwards — AWS sets `DeleteOnTermination` to `false` by default for any volume that isn't the root device. The root volume defaults to `true`; everything else defaults to `false`. The reasoning made sense when EBS was younger: detaching a data volume and reattaching it to a replacement instance is a legitimate operational pattern. Databases, persistent logs, shared storage — there are real use cases where you want a volume to outlive its host instance. AWS was being conservative, and in 2010 that was the right call.

The problem is that most workloads in 2024 are not doing any of that. They're running application servers, microservices, and ephemeral build agents that get terminated and respawned by Auto Scaling. The data volumes those instances used — 20 GB here, 100 GB there — don't get cleaned up. They enter `available` state, and AWS keeps billing for them at the full provisioned storage rate: $0.096 per GB-month for gp3 in ap-south-1, $0.114 per GB-month for gp2. A single forgotten 100 GB gp2 volume costs ₹970 per month. Thirty-eight of them, accumulated over two years of sprint cycles and team turnover, costs you ₹35,000 every month for nothing.

---

## A Pattern Study: 38 Volumes, 4.2 TB, ₹4.2 Lakh Per Year

The engagement referenced above was a Bengaluru-based SaaS company — Series B, 60-person engineering team, monthly AWS spend of roughly ₹18 lakh. Not a small operation, but not an enterprise with a dedicated FinOps function either. They ran a quarterly cost review, had reasonable Reserved Instance coverage on their production RDS fleet, and believed their AWS environment was reasonably tidy.

When we ran the initial discovery scan, the volume list told a different story. Thirty-eight EBS volumes in `available` state across ap-south-1a, ap-south-1b, and ap-south-1c. Total provisioned storage: 4.2 TB. The breakdown: 24 volumes were gp2 (legacy, never migrated to gp3), averaging 87 GB each. Fourteen were gp3, averaging 140 GB each. Oldest orphan: 19 months. Most recent: 11 days — from a failed staging deployment that no one had cleaned up. Annualised cost at ap-south-1 list pricing: ₹4,18,000 (~$5,000 USD). Not catastrophic in isolation. Compounded with the S3 storage sprawl and unused Elastic IPs we found in the same review, the total came to ₹11.2 lakh in recoverable annual spend — 6.2% of their total cloud bill. That's real money for a company that size.

---

## The 10-Minute Detection Command

You can surface every orphaned EBS volume in your AWS account in under ten minutes. Open your terminal, configure your credentials for the right account, and run:

```bash
aws ec2 describe-volumes \
  --region ap-south-1 \
  --filters Name=status,Values=available \
  --query 'Volumes[*].{
    ID:VolumeId,
    SizeGB:Size,
    Type:VolumeType,
    AZ:AvailabilityZone,
    Created:CreateTime,
    IOPS:Iops
  }' \
  --output table
```

This returns every volume not currently attached to a running or stopped instance. Add `--output json` and pipe through `jq` if you want to calculate total provisioned GB on the spot:

```bash
aws ec2 describe-volumes \
  --region ap-south-1 \
  --filters Name=status,Values=available \
  --query 'Volumes[*].Size' \
  --output json | jq 'add'
```

Multiply that number by $0.096 (gp3) or $0.114 (gp2) and then by 12 for your annual orphan cost. If the number surprises you, you're not alone. Run this across every region you operate in — us-east-1, eu-west-1, wherever your teams have ever spun something up — and total the figure before drawing any conclusions.

---

## The Governance Fix: Tagging and a 30-Day Quarantine Window

Deletion should be deliberate, not automatic. The correct fix is a quarantine pattern, not a nightly purge.

When a volume enters `available` state, tag it immediately: `quarantine-start: <ISO-8601-date>`. An EventBridge rule watching for EBS state-change events to `available` handles this without any polling. Pair it with a Lambda function or a daily cron job that queries for all volumes where that tag exists and the date is more than 30 days old — then either deletes them or files a Jira ticket for manual review depending on your team's risk appetite.

On the prevention side: update your launch templates and Auto Scaling group configurations to set `DeleteOnTermination: true` for all non-root volumes unless there's a documented reason otherwise. Enforce this as a policy check in your CI pipeline using a tool like `cfn-guard` or Open Policy Agent against your CloudFormation and Terraform plans. Tag every EBS volume at creation with `owner`, `team`, and `environment`. Any volume that reaches `available` state without those tags triggers an immediate alert. The tagging discipline pays dividends well beyond storage — it's the same metadata that makes cost allocation reports meaningful at the team and product level.

---

## The CFO View: Why This Compounds

The ₹4.2 lakh figure in the pattern study above is a point-in-time snapshot. It compounds in two ways that matter to finance.

First, it grows monotonically. Every sprint cycle, every staging environment spun up and torn down, every developer testing a new database configuration — all of it generates orphaned volumes unless the deletion policy is enforced at the infrastructure layer. Without a quarantine workflow, the volume of orphaned storage in an active engineering organisation roughly tracks headcount growth. A team that adds five engineers per quarter can expect its orphaned EBS footprint to grow 15–20% annually on spend alone.

Second, it obscures accountability. When cost is spread across dozens of untagged, ownerless volumes, it shows up as a diffuse line in the AWS Cost Explorer rather than attributable team or product spend. Finance sees the bill; engineering sees no actionable signal. That friction — the inability to connect cloud spend to business outcomes — is what makes cost governance feel like bureaucracy instead of engineering hygiene. Fix the tagging, fix the deletion policy, and you also fix the visibility problem.

The ₹4.2 lakh number is not the point. The point is that it existed for over a year without being visible to anyone in the organisation.

---

## Free Cloud Cost Health Check

If you want to run this audit across your full AWS environment — not just EBS, but idle load balancers, unattached Elastic IPs, forgotten snapshots, and Reserved Instance gaps — AICloudStrategist offers a free 30-minute Cloud Cost Health Check. No sales follow-up. A structured review call, a written summary of what we find, and a prioritised remediation list you can action immediately.

[Book your free Cloud Cost Health Check → aicloudstrategist.com/book.html](https://aicloudstrategist.com/book.html)

The cost of looking is zero. The cost of not looking is, apparently, ₹4.2 lakh a year.

---

— Anushka B, Founder · AICloudStrategist · Founder-led. Enterprise-reviewed.
