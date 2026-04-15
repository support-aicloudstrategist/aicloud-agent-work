# The GCP Cost Optimisation Checklist for Indian SMBs

## 25 leak points to fix before your next billing cycle

*Built by AICloudStrategist — founder-led, enterprise-reviewed. Pricing references asia-south1 (Mumbai) on-demand rates, April 2026.*

---

## Why this document exists

Most mid-market Indian companies on Google Cloud are running a version of the same bill: a GKE cluster that never scales down at night, a Cloud SQL instance sized for a load test that ended nine months ago, a warehouse in the wrong region silently charging egress on every query. None of it shows up as a flagged line item. All of it compounds.

This checklist is every pattern we have found repeatedly across Indian SaaS, D2C, and fintech accounts — distilled to 25 items, each with a detection command, a fix, and a realistic rupee estimate of what it is costing you today. None of the items require an architectural rewrite. Most can be closed in under a day of engineering time.

## How to use it

Work through each item once. Mark **DONE**, **NOT APPLICABLE**, or **ACTION REQUIRED**. Any ACTION REQUIRED item with a savings estimate above ₹10,000 a month becomes a Jira ticket before this document goes in a drawer. That is the whole playbook.

Run the detection commands against one project first to calibrate. Then extend to the rest of the org.

---

## Section 1 — Compute & GKE (Items 1–7)

---

### 1. GKE Cluster Autoscaler Disabled or Misconfigured

**What leaks:** Node pools provisioned for peak capacity run at that size permanently. Off-hours, nights, and weekends — you pay for idle nodes.

**How to detect:**
```bash
gcloud container clusters list --format="table(name,location,currentNodeCount,autoscaling)"
# Any cluster showing autoscaling: disabled with currentNodeCount > 3 is a candidate
```

**Fix:** Enable cluster autoscaler with a minimum of 1 and a realistic maximum. Set `--min-nodes=1 --max-nodes=<peak_capacity>` per node pool.

**Typical saving:** ₹15,000–₹60,000/month for a 10-node cluster running 40% idle on average.

---

### 2. Vertical Pod Autoscaler (VPA) Not Deployed

**What leaks:** Pods request resources set during initial deployment and never revisited. Over-requested CPU and memory locks node capacity even when pods consume a fraction of it.

**How to detect:** Run VPA in recommendation mode for 7 days:
```bash
kubectl apply -f https://github.com/kubernetes/autoscaler/releases/latest/download/vertical-pod-autoscaler.yaml
# Review recommendations: kubectl describe vpa <name> | grep "Lower Bound\|Target\|Upper Bound"
```

**Fix:** Apply VPA in Auto mode to non-stateful workloads. Expect 20–40% node count reduction for over-provisioned deployments.

**Typical saving:** ₹20,000–₹80,000/month depending on cluster size.

---

### 3. Development/Staging GKE Clusters Running 24 × 7

**What leaks:** Dev clusters sized for convenience, not cost. Running overnight and on weekends when no engineer is active.

**How to detect:**
```bash
gcloud container clusters list --project=PROJECT_ID
# Cross-reference cluster name against environment tagging
```

**Fix:** Use node pool autoscaler with min-nodes=0 for non-production clusters. Schedule scale-down via Cloud Scheduler + a GKE resize job. Dev clusters should run 8 hours/day, 5 days/week — 60% fewer node-hours.

**Typical saving:** ₹25,000–₹1,20,000/month across dev and staging environments.

---

### 4. GKE Standard Clusters Where Autopilot Would Suffice

**What leaks:** Standard clusters require you to manage node sizing. Under-utilised node pools are billed in full. Autopilot bills per pod resource request, eliminating idle node waste.

**How to detect:** If cluster average CPU utilisation is below 50% and workloads are stateless, Autopilot pricing will likely be lower.

**Fix:** Evaluate migration to Autopilot for stateless workloads. Use [Google's Autopilot pricing calculator](https://cloud.google.com/kubernetes-engine/pricing) with your actual pod resource requests.

**Typical saving:** 20–35% on node costs for clusters with spiky or low average utilisation.

---

### 5. Idle VMs (Stopped but Not Deleted)

**What leaks:** Stopped Compute Engine instances do not charge for CPU or memory. They do charge for attached persistent disks and any reserved static IPs. Long-lived stopped instances accumulate disk charges indefinitely.

**How to detect:**
```bash
gcloud compute instances list --filter="status=TERMINATED" \
  --format="table(name,zone,disks[].diskSizeGb,lastStartTimestamp)"
# Flag instances not started in >30 days
```

**Fix:** Delete instances stopped for more than 30 days. Snapshot disks first if recovery is possible. Review with the owning team before deletion.

**Typical saving:** ₹500–₹2,000/month per stopped instance depending on disk size.

---

### 6. Oversized Machine Families (N2 When E2 Suffices)

**What leaks:** N2 machines are 20–30% more expensive than E2 for identical vCPU/memory configurations. Many general-purpose web and API workloads do not benefit from N2's higher per-core performance.

**How to detect:**
```bash
gcloud compute instances list --format="table(name,machineType,zone)"
# Filter for n2- prefix and cross-check CPU utilisation in Cloud Monitoring
```

**Fix:** For instances with average CPU below 40%, test on equivalent E2 types. `e2-standard-4` costs ~$0.134/hr vs `n2-standard-4` at ~$0.190/hr in asia-south1.

**Typical saving:** ₹8,000–₹40,000/month across a fleet of 10–20 VMs.

---

### 7. Preemptible / Spot VMs Not Used for Batch and CI Workloads

**What leaks:** Fault-tolerant batch jobs, data pipelines, CI runners, and ML training running on standard on-demand VMs.

**How to detect:** Identify workloads that are stateless, retry-safe, or short-lived. CI/CD runners and ETL jobs are primary candidates.

**Fix:** Switch to Spot VMs. Spot pricing in asia-south1 is 60–91% below on-demand depending on machine type. Configure retry logic or use managed instance groups with replacement on preemption.

**Typical saving:** ₹30,000–₹2,00,000/month for teams with heavy batch or CI workloads.

---

## Section 2 — Cloud SQL (Items 8–11)

---

### 8. Cloud SQL Instance Tier Right-Sizing

**What leaks:** Cloud SQL instances provisioned at launch for anticipated peak load and never resized. Database CPU and memory utilisation often sits below 20% in production for most SMBs.

**How to detect:**
```bash
# In Cloud Monitoring, query:
# cloudsql.googleapis.com/database/cpu/utilization
# cloudsql.googleapis.com/database/memory/utilization
# Filter by instance, look at 30-day average
```

A `db-custom-8-32768` (8 vCPU, 32 GB) running at 15% average CPU costs ~$500/month in asia-south1. A `db-custom-2-8192` (2 vCPU, 8 GB) costs ~$130/month and handles the same load.

**Fix:** Right-size to a tier where average CPU stays below 60%. Resize during a maintenance window — downtime is ~60 seconds for primary instances.

**Typical saving:** ₹15,000–₹60,000/month.

---

### 9. High Availability Enabled on Dev/Staging Cloud SQL Instances

**What leaks:** HA doubles the instance cost by provisioning a standby replica in a second zone. Dev and staging databases rarely need HA.

**How to detect:**
```bash
gcloud sql instances list --format="table(name,settings.availabilityType,settings.tier)"
# Flag REGIONAL availability type on non-production instances
```

**Fix:** Set `availabilityType` to `ZONAL` for dev and staging. Production: keep HA. Non-production: remove it.

**Typical saving:** ₹8,000–₹30,000/month depending on instance tier.

---

### 10. Cloud SQL Dev Instances Without Auto-Pause

**What leaks:** Cloud SQL for PostgreSQL and MySQL do not support auto-pause (unlike Cloud SQL for SQL Server in some configurations). Dev instances run 24 × 7 by default.

**Fix:** Schedule instance start/stop via Cloud Scheduler:
```bash
gcloud scheduler jobs create http stop-dev-db \
  --schedule="0 20 * * 1-5" \
  --uri="https://sqladmin.googleapis.com/v1/projects/PROJECT/instances/INSTANCE/stopReplica" \
  --oauth-service-account-email=SERVICE_ACCOUNT
```
Running 9 hours/day, 5 days/week reduces dev DB uptime by 73%.

**Typical saving:** ₹5,000–₹20,000/month per dev instance.

---

### 11. Cloud SQL Disk Autoresize Left Unchecked

**What leaks:** `storageAutoResize` is enabled by default. Disks grow automatically and never shrink. A burst load event causes disk to expand to 500 GB; load passes; you pay for 500 GB permanently.

**How to detect:**
```bash
gcloud sql instances describe INSTANCE_NAME --format="value(settings.storageAutoResizeLimit,settings.dataDiskSizeGb)"
```

**Fix:** Set `storageAutoResizeLimit` to a reasonable ceiling. Monitor actual disk usage vs allocated size. If current usage is 40 GB and disk shows 300 GB, export → re-create instance at correct size → restore.

**Typical saving:** ₹2,000–₹15,000/month depending on overage.

---

## Section 3 — Cloud Storage (Items 12–14)

---

### 12. No Lifecycle Rules on Cloud Storage Buckets

**What leaks:** All objects land in Standard storage and age there indefinitely. Standard costs ₹2.1/GB/month in asia-south1. Nearline costs ₹1.05/GB/month (30-day minimum). Coldline costs ₹0.42/GB/month (90-day minimum). Archive costs ₹0.13/GB/month.

**How to detect:**
```bash
gsutil ls -L gs://BUCKET_NAME | grep "Lifecycle"
# Or check all buckets:
for b in $(gsutil ls); do echo "$b:"; gsutil lifecycle get $b; done
```

**Fix:** Apply lifecycle rules. Typical policy for logs and backups:
```json
{
  "rule": [
    {"action": {"type": "SetStorageClass", "storageClass": "NEARLINE"},
     "condition": {"age": 30}},
    {"action": {"type": "SetStorageClass", "storageClass": "COLDLINE"},
     "condition": {"age": 90}},
    {"action": {"type": "SetStorageClass", "storageClass": "ARCHIVE"},
     "condition": {"age": 365}}
  ]
}
```

**Typical saving:** ₹10,000–₹80,000/month for teams storing more than 5 TB of log or media data.

---

### 13. Multi-Region or Dual-Region Buckets for Single-Region Apps

**What leaks:** Multi-region Cloud Storage costs 2× Nearline and applies Standard pricing at the multi-region rate. Most Indian SMBs do not need multi-region redundancy for internal data.

**How to detect:**
```bash
gsutil ls -L gs://BUCKET_NAME | grep "Location type\|Location constraint"
# Flag MULTI or DUAL-REGION buckets
```

**Fix:** Migrate non-critical data to single-region `asia-south1` buckets. Standard asia-south1: $0.026/GB vs multi-region asia: $0.036/GB — 38% more expensive.

**Typical saving:** ₹5,000–₹30,000/month for large multi-region buckets.

---

### 14. No Object Versioning Expiry on Versioned Buckets

**What leaks:** Versioning enabled for compliance or accident recovery, but no expiry on non-current versions. Every overwrite creates a permanent copy billed in full.

**How to detect:**
```bash
gsutil versioning get gs://BUCKET_NAME
gsutil lifecycle get gs://BUCKET_NAME
# If versioning is ON and lifecycle has no DeleteObjectAfterDays for non-current, it's leaking
```

**Fix:** Add a lifecycle rule to delete non-current versions after your retention window (e.g., 30 days):
```json
{"action": {"type": "Delete"},
 "condition": {"numNewerVersions": 3, "isLive": false}}
```

**Typical saving:** ₹3,000–₹25,000/month for high-churn buckets.

---

## Section 4 — Networking (Items 15–19)

---

### 15. Cross-Region Egress (Services Deployed Across Regions)

**What leaks:** GCP charges $0.01–$0.08/GB for traffic crossing regional boundaries within GCP. Microservices split across regions generate continuous inter-region traffic — every API call, every database query.

**How to detect:** Pull billing export into BigQuery:
```sql
SELECT
  resource.labels.location AS source_region,
  sku.description,
  SUM(cost) AS total_cost
FROM `PROJECT.billing_dataset.gcp_billing_export_*`
WHERE sku.description LIKE '%Egress%'
  AND _PARTITIONTIME >= TIMESTAMP_SUB(CURRENT_TIMESTAMP(), INTERVAL 30 DAY)
GROUP BY 1, 2
ORDER BY 3 DESC
LIMIT 20;
```

Flag any cross-region egress line above ₹5,000/month.

**Fix:** Co-locate dependent services in the same region. For new deployments, enforce region via Terraform variables and org policies.

**Typical saving:** ₹10,000–₹2,00,000/month (see Case 2 in our proof library — one client saved ₹11.5L/month from a single region topology fix).

---

### 16. Unattached Static External IP Addresses

**What leaks:** GCP charges $0.010/hr (~₹660/month) for each reserved static external IP that is not attached to a running resource. Addresses reserved for testing, failed deployments, or decommissioned load balancers accumulate silently.

**How to detect:**
```bash
gcloud compute addresses list --filter="status=RESERVED" \
  --format="table(name,region,status,users)"
# RESERVED with no users = billing with no function
```

**Fix:** Release unattached addresses immediately:
```bash
gcloud compute addresses delete ADDRESS_NAME --region=asia-south1
```

**Typical saving:** ₹660–₹6,600/month per address. Teams often find 5–15 orphaned addresses.

---

### 17. Unused Cloud NAT Gateways

**What leaks:** Cloud NAT charges $0.0138/hr per gateway (~₹910/month) plus $0.045/GB processed. Gateways provisioned for environments that were torn down, or for subnets that no longer have outbound traffic, continue to accrue the hourly base charge.

**How to detect:**
```bash
gcloud compute routers list
gcloud compute routers get-nat-mapping-info ROUTER_NAME --region=REGION
# Cross-reference with active VM count in associated subnets
```

**Fix:** Delete Cloud NAT gateways in subnets with zero active VMs. For low-traffic environments, consolidate to a shared NAT rather than per-environment gateways.

**Typical saving:** ₹900–₹5,000/month per unused gateway.

---

### 18. Premium Network Tier on Workloads That Don't Need It

**What leaks:** GCP defaults to Premium network tier, which routes traffic via Google's backbone globally. Standard tier uses public internet for routing and costs 20–40% less for egress. Internal APIs, back-end services, and admin tools rarely require Premium tier.

**How to detect:**
```bash
gcloud compute instances list --format="table(name,networkInterfaces[].networkTier)"
gcloud compute forwarding-rules list --format="table(name,region,networkTier)"
```

**Fix:** Switch non-user-facing services to Standard tier. User-facing services with latency SLAs: keep Premium. Internal microservices and batch pipelines: Standard.

**Typical saving:** ₹5,000–₹40,000/month for high-egress workloads.

---

### 19. Firewall Rules Allowing Broad Egress (Unintentional Data Transfer)

**What leaks:** Overly permissive egress firewall rules allow services to make unintended external calls — telemetry libraries phoning home, misconfigured SDK defaults, or accidental cross-region communication. This drives up both egress costs and security exposure.

**How to detect:** Enable VPC Flow Logs and query in Log Explorer for unexpected external destination IPs. Review `google.vpc.flows` logs sorted by bytes transferred.

**Fix:** Restrict egress to known endpoints via firewall policies. Investigate any external destination generating more than 1 GB/day unexpectedly.

**Typical saving:** Varies; forensic value often exceeds direct cost saving.

---

## Section 5 — Committed Use Discounts (Items 20–21)

---

### 20. No Resource-Based Committed Use Discounts on Steady-State VMs

**What leaks:** On-demand pricing for compute that has run continuously for more than 3 months. Resource-based CUDs offer 37% discount (1-year) or 55% discount (3-year) on n1/n2/e2 machine types in exchange for a commitment to a specific vCPU and memory amount — no instance type lock-in.

**How to detect:**
```bash
gcloud compute commitments list --format="table(name,region,status,plan,endTimestamp)"
# If empty or commitments don't cover majority of steady-state vCPU, action required
```
Cross-reference with GCP Recommender:
```bash
gcloud recommender recommendations list \
  --recommender=google.compute.commitment.UsageCommitmentRecommender \
  --location=asia-south1 --project=PROJECT_ID
```

**Fix:** Purchase CUDs for baseline vCPU and memory that ran every hour last month. Do not commit to peak — commit to your floor.

**Typical saving:** 37–55% on committed resources. For a 20-vCPU baseline, that is ₹25,000–₹50,000/month.

---

### 21. No Committed Use Discounts on Cloud SQL

**What leaks:** Cloud SQL has its own CUD program, separate from compute CUDs. 1-year commitments on Cloud SQL offer 25–52% discounts depending on database engine and tier. Most teams are unaware this exists.

**How to detect:**
```bash
gcloud sql tiers list
# Check GCP Console → Billing → Commitments for any existing SQL commitments
```

**Fix:** Review Cloud SQL spend in billing export. For any instance running consistently for 3+ months, purchase a 1-year Cloud SQL CUD. Commitment is on vCPUs, not instance type.

**Typical saving:** 25–52% on Cloud SQL line items. For a `db-custom-4-16384` costing ₹25,000/month, that is ₹6,000–₹13,000/month.

---

## Section 6 — Orphaned & Unused Resources (Items 22–25)

---

### 22. Orphaned Persistent Disks

**What leaks:** When a GKE pod or VM is deleted, attached persistent disks are not automatically deleted unless `reclaimPolicy: Delete` is set. Disks persist in READY state, billed at $0.048/GB/month (SSD) or $0.024/GB/month (Standard HDD) in asia-south1 — with nothing reading or writing to them.

**How to detect:**
```bash
gcloud compute disks list --filter="NOT users:*" \
  --format="table(name,sizeGb,type,zone,lastAttachTimestamp)"
# All rows returned are orphaned disks
```

For GKE PersistentVolumes:
```bash
kubectl get pv --all-namespaces | grep Released
```

**Fix:** Snapshot any disk you are not certain is safe to delete, then delete the disk. For new GKE clusters, set `reclaimPolicy: Delete` on StorageClasses for non-critical data.

**Typical saving:** ₹5,000–₹40,000/month. Accounts running GKE for 12+ months routinely accumulate 1–5 TB of orphaned disks.

---

### 23. Artifact Registry / Container Registry Storing All Image Tags Indefinitely

**What leaks:** Every `docker push` stores a new image layer set. CI pipelines pushing on every commit generate hundreds of image versions per month. Registry storage is billed at $0.10/GB/month. A moderately active team accumulates 500 GB–2 TB within a year.

**How to detect:**
```bash
gcloud artifacts repositories list
gcloud artifacts docker images list LOCATION-docker.pkg.dev/PROJECT/REPO \
  --include-tags --format="table(package,tags,createTime,updateTime)"
# Sort by createTime, count images older than 30 days
```

**Fix:** Set a cleanup policy on Artifact Registry to retain only the last N versions per image:
```bash
gcloud artifacts repositories set-cleanup-policies REPO \
  --project=PROJECT --location=LOCATION \
  --policy='[{"name":"delete-old","action":{"type":"Delete"},"condition":{"olderThan":"30d","tagState":"tagged"}}]'
```

**Typical saving:** ₹3,000–₹20,000/month for CI-heavy teams.

---

### 24. Cloud Logging Sinks Exporting All Logs to BigQuery or Storage

**What leaks:** The default `_Default` log sink retains logs in Cloud Logging at $0.50/GB ingestion above the 50 GB/month free tier. Teams adding BigQuery export sinks for analysis pay double — once for Logging ingestion, once for BigQuery storage and query. More critically, verbose application logs (DEBUG level, all request logs) are often exported when only ERROR and WARN are needed.

**How to detect:**
```bash
gcloud logging sinks list --format="table(name,destination,filter)"
# Review: does filter exclude DEBUG/INFO? Are high-volume log names excluded?
```

Check monthly log ingestion volume in Cloud Monitoring:
```
logging.googleapis.com/billing/bytes_ingested
```

**Fix:** Add log exclusion filters to suppress DEBUG and INFO logs from noisy sources. Set sink filters to export only `severity >= WARNING`. Estimated ingestion reduction: 60–80% for most workloads.

**Typical saving:** ₹5,000–₹35,000/month depending on log volume.

---

### 25. Cloud Run and Cloud Functions Minimum Instances Misconfigured

**What leaks:** `min-instances` set to avoid cold starts on non-latency-critical services keeps containers running permanently. Each minimum instance bills for idle CPU and memory even with zero traffic. A single `min-instances=5` setting on a Cloud Run service with 512 MB memory costs ~$18/month at rest — before any requests.

**How to detect:**
```bash
gcloud run services list --format="table(metadata.name,spec.template.metadata.annotations)"
# Look for run.googleapis.com/minScale annotation values > 0
```

**Fix:** Set `min-instances=0` for internal tools, admin panels, and async workers where a 1–3 second cold start is acceptable. Reserve `min-instances > 0` for user-facing APIs with documented latency SLAs.

**Typical saving:** ₹3,000–₹25,000/month for teams with multiple Cloud Run services.

---

## Summary Table

| # | Leak Point | Effort | Typical Monthly Saving |
|---|-----------|--------|----------------------|
| 1 | GKE Cluster Autoscaler disabled | Low | ₹15K–₹60K |
| 2 | VPA not deployed | Medium | ₹20K–₹80K |
| 3 | Dev GKE clusters 24×7 | Low | ₹25K–₹1.2L |
| 4 | Standard clusters vs Autopilot | Medium | 20–35% node cost |
| 5 | Idle stopped VMs | Low | ₹500–₹2K/VM |
| 6 | N2 where E2 suffices | Low | ₹8K–₹40K |
| 7 | No Spot/Preemptible for batch | Medium | ₹30K–₹2L |
| 8 | Cloud SQL oversized tier | Low | ₹15K–₹60K |
| 9 | HA on dev Cloud SQL | Low | ₹8K–₹30K |
| 10 | Dev Cloud SQL 24×7 | Low | ₹5K–₹20K |
| 11 | SQL disk autoresize uncapped | Medium | ₹2K–₹15K |
| 12 | No Storage lifecycle rules | Low | ₹10K–₹80K |
| 13 | Multi-region buckets single-region apps | Medium | ₹5K–₹30K |
| 14 | No versioning expiry | Low | ₹3K–₹25K |
| 15 | Cross-region egress | Medium | ₹10K–₹2L+ |
| 16 | Unattached static IPs | Low | ₹660–₹6.6K |
| 17 | Unused Cloud NAT gateways | Low | ₹900–₹5K |
| 18 | Premium tier on internal services | Low | ₹5K–₹40K |
| 19 | Overpermissive egress firewall | Medium | Variable |
| 20 | No compute CUDs on steady-state VMs | Low | ₹25K–₹50K |
| 21 | No Cloud SQL CUDs | Low | ₹6K–₹13K |
| 22 | Orphaned persistent disks | Low | ₹5K–₹40K |
| 23 | Artifact Registry unlimited retention | Low | ₹3K–₹20K |
| 24 | Log sinks exporting all severity levels | Medium | ₹5K–₹35K |
| 25 | Cloud Run min-instances over-set | Low | ₹3K–₹25K |

---

## Next Step

Run the detection commands for items where you marked ACTION REQUIRED. If more than five items need remediation, book a structured Cloud Health Check — we run the full audit, prioritise by savings-to-effort ratio, and deliver a remediation backlog your engineers can execute sprint by sprint.

**Book a free 30-minute GCP Health Check → [link in bio]**

---

*AICloudStrategist | FinOps for GCP & AWS teams serving Indian SMBs*
*Prices and rates verified April 2026. Exchange rate used: ₹83/USD.*
