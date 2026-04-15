# Cloud Cost Health Check — ProdCo India Pvt Ltd

**Prepared for:** ProdCo India Pvt Ltd
**Period analysed:** 08 April 2026 to 15 April 2026
**Cloud(s):** AWS (ap-south-1 / Mumbai)
**Approximate monthly spend:** INR 18 lakh
**Date of report:** 15 April 2026

---

## Executive Summary

A 7-day billing sample from your AWS account reveals approximately **₹7,27,350 per month** in recoverable waste — equivalent to roughly 40% of your stated monthly spend. The single largest leak is archival data sitting in S3 Standard storage (a bucket named for cold data) at an estimated ₹9,66,000/month; a one-time lifecycle policy would cut that by 60%, recovering ₹5,79,600/month. The scale-up for your product launch added six m5.4xlarge EC2 instances running on full on-demand rates with no Savings Plan coverage, which a 30-minute purchase can reduce by 27%. Two orphaned EBS volumes and a development RDS instance running Multi-AZ 24/7 add a further ₹57,650/month that can be eliminated this week with zero production risk.

---

## Top 5 Quick Wins

| # | Finding | Estimated monthly saving (INR) | Time to implement | Owner to assign |
|---|---|---|---|---|
| 1 | S3 cold-data bucket in Standard storage — no lifecycle policy | ₹5,79,600 | 2 hours | Platform |
| 2 | Six m5.4xlarge instances on-demand with no Savings Plan coverage | ₹72,100 | 1 day | Platform / Finance |
| 3 | Two orphaned EBS volumes (unattached, billing continuously) | ₹35,700 | 2 hours | Engineering |
| 4 | Development RDS (db.m5.2xlarge) running Multi-AZ unnecessarily | ₹21,950 | 2 hours | Engineering |
| 5 | Stale EBS snapshot accumulation — no retention policy | ₹18,000 | 1 day | Platform |

**Total recoverable per month: ₹7,27,350** (approximate, based on 7-day sample)
**Annualised: ₹87,28,200**

---

## Detailed Findings

### 1. S3 cold-data bucket storing objects in Standard storage class

**What we see.** A single S3 bucket (resource ID redacted; usage type `APS3-TimedStorage-ByteHrs`, operation `StandardStorage`) accounts for $11,500 in the billing export — the largest single line item in the sample by a wide margin. The bucket name in the raw export signals archival or infrequently-accessed data.

**Why it's happening.** No S3 Lifecycle policy was configured when the bucket was created. All objects default to S3 Standard (approximately ₹2.10/GB-month in ap-south-1) and remain there indefinitely regardless of access frequency.

**How to fix.** Apply a Lifecycle rule to transition objects not accessed in 90 days to S3 Glacier Instant Retrieval (~₹0.42/GB-month, same retrieval SLA as Standard for most workloads). CLI:
```bash
aws s3api put-bucket-lifecycle-configuration \
  --bucket <bucket-name> \
  --lifecycle-configuration file://lifecycle.json
```
A sample `lifecycle.json` transitioning to `GLACIER_IR` at 90 days takes under 30 minutes to write and test.

**Risk:** Low. Data remains in the same bucket and region; first-byte latency is unchanged with Glacier Instant Retrieval. The Platform lead should verify no application assumes objects are always in Standard before applying.

---

### 2. Six m5.4xlarge EC2 instances on full on-demand pricing — no Savings Plan

**What we see.** Six instances (all `RunInstances`, `APS3-BoxUsage:m5.4xlarge`) each ran the full 168 hours of the sample period with no Reserved Instance or Savings Plan line items visible anywhere in the export. Extrapolated on-demand cost: ~₹2,67,200/month.

**Why it's happening.** The scale-up for the product launch was provisioned quickly on on-demand to avoid commitment risk. Post-launch, the fleet has stabilised but no commitment has been purchased.

**How to fix.** Purchase a 1-year Compute Savings Plan (no-upfront) covering the committed baseline via the AWS console or CLI. A Compute SP applies across any EC2 instance family and region, so it does not constrain future rightsizing. At current rates, a 27% effective discount saves ~₹72,100/month immediately. If post-launch analysis (CloudWatch CPU over 14+ days) shows 2–3 instances are underutilised, terminating them would recover an additional ~₹89,000/month — but that requires utilisation data not present in this sample.

**Risk:** Low for SP purchase (no architectural change). Instance termination is Medium — requires CPU/memory utilisation review first and sign-off from Engineering lead.

---

### 3. Two orphaned EBS volumes accumulating charges with no attached instance

**What we see.** Two gp2 volumes (operation `CreateVolume-Gp2`, no `lineItem_ResourceId` mapping to any running EC2 instance in the sample): combined 7-day cost $124.00, extrapolated monthly ₹35,700. Both volumes have been detached — likely left behind after instances were terminated during or after the scale-up.

**Why it's happening.** When EC2 instances are terminated, EBS volumes set to "Do Not Delete on Termination" (the non-default setting) survive as detached volumes and continue to bill at the full gp2 rate.

**How to fix.**
```bash
# List all unattached volumes
aws ec2 describe-volumes \
  --filters Name=status,Values=available \
  --query 'Volumes[*].[VolumeId,Size,CreateTime]'

# Take a final snapshot, then delete
aws ec2 create-snapshot --volume-id vol-xxxxx --description "pre-delete backup"
aws ec2 delete-volume --volume-id vol-xxxxx
```
Set the EC2 default termination behaviour to delete root and data volumes together, or enforce it via an AWS Config rule.

**Risk:** Low. Take one snapshot per volume before deletion as a safety net (snapshot cost is negligible relative to the volume cost).

---

### 4. Development RDS instance (db.m5.2xlarge) running Multi-AZ around the clock

**What we see.** A database identified as a development instance (`CreateDBInstance`, `APS3-Multi-AZUsage:db.m5.2xl`) ran 168 hours at $152.40 for the 7-day period — the same cost as the production primary RDS instance. Multi-AZ billing roughly doubles the single-AZ rate.

**Why it's happening.** The dev instance was likely cloned from a production snapshot or a production-parity template that included Multi-AZ. Development environments rarely need cross-AZ failover.

**How to fix.** Disable Multi-AZ via the console or:
```bash
aws rds modify-db-instance \
  --db-instance-identifier db-dev-<redacted> \
  --no-multi-az \
  --apply-immediately
```
Additionally, schedule the dev instance to stop outside business hours (evenings and weekends) using AWS Instance Scheduler — this can recover a further 60% on top of the Multi-AZ saving, but requires a separate implementation pass.

**Risk:** Low. Dev environment; no production SLA impact. Engineering lead approval sufficient.

---

### 5. Stale EBS snapshot with no retention policy

**What we see.** One snapshot (`APS3-EBS:SnapshotUsage`, operation `CreateSnapshot`) with 1,200 GB-Mo of storage and a 7-day cost of $62.40 — extrapolated monthly ₹18,000. The resource ID in the export (`snap-stale-*` pattern) indicates this is part of an unmanaged, accumulating snapshot set.

**Why it's happening.** Manual snapshots or backup jobs that create snapshots without a corresponding deletion policy accumulate indefinitely. Each retained snapshot charges at the incremental data stored.

**How to fix.** Audit all snapshots older than 90 days and verify they are not referenced by any AMI or cross-account share:
```bash
aws ec2 describe-snapshots --owner-ids self \
  --query 'Snapshots[?StartTime<=`2026-01-14`].[SnapshotId,VolumeSize,StartTime]'
```
Enable AWS Data Lifecycle Manager (DLM) with a 30-day retention rule for all future automated snapshots. This prevents the same accumulation recurring.

**Risk:** Low. Verify no AMI references the snapshot before deletion (`aws ec2 describe-images --filters Name=block-device-mapping.snapshot-id,Values=snap-xxxxx`).

---

## What we did NOT analyse

- **Reserved Instance coverage strategy.** Assessing the correct RI term and payment option requires 30+ days of usage data to distinguish stable baseline from burst capacity. The Savings Plan recommendation above is directional; a full commitment strategy needs a longer sample.
- **EC2 rightsizing.** Determining whether m5.4xlarge is the correct size for each instance requires CloudWatch CPU and memory utilisation data, which is not present in a CUR export alone.
- **NAT Gateway optimisation.** The sample shows ₹21,000/month in NAT Gateway charges. Routing S3 and DynamoDB traffic through VPC Gateway Endpoints (free) eliminates the processing fee for those services, but this requires mapping which services your instances call — outside the scope of this CUR-only review.
- **RDS production rightsizing and RI coverage.** The production RDS (`db.m5.2xlarge`) has no RI coverage visible in the sample. An RDS Reserved Instance (1-year) saves ~30% but requires confirming the instance type is stable.
- **Data transfer and egress costs.** The sample shows 300 GB of internet data transfer out from one EC2 instance at $38.40/7d. Root-causing whether this is expected application traffic or misconfigured replication requires application-level tracing.
- **Non-cloud and SaaS spend.** This report covers AWS billing only.

---

## Recommended next step

The three actions executable this week — S3 lifecycle policy, orphaned volume deletion, and RDS Multi-AZ disable — alone recover an estimated ₹6,37,250/month with no architectural risk. Let's convert these quick wins into an implementation sprint: fixed price, 2 weeks, gain-share on verified savings. Reply to this email to schedule a kickoff call.

---

*Report generated by AICloudStrategist for ProdCo India Pvt Ltd. This is a starter analysis from a 7-day billing sample — full savings discovery typically requires 30+ days of billing history. Confidentiality: this report contains data extracted from your billing export and is shared only with the engagement stakeholders. AWS account identifiers have been redacted from this document.*

*Rajiv · AICloudStrategist · support@aicloudstrategist.com*
