---
title: "Azure Cost Optimisation Checklist for Indian SMBs"
subtitle: "30 leak points we see repeatedly in mid-market Azure accounts"
author: "AICloudStrategist · Anushka B, Founder"
date: "April 2026"
geometry: "margin=18mm"
fontsize: 11pt
papersize: a4
---

# Azure Cost Optimisation Checklist for Indian SMBs

*30 leak points we see repeatedly in mid-market Azure accounts. INR figures reference Central India / South India region, April 2026.*

> Built and maintained by [AICloudStrategist](https://aicloudstrategist.com) · Founder-led. Enterprise-reviewed. · support@aicloudstrategist.com

---

## How to use this checklist

Work through the 30 items. Mark each **DONE**, **NOT APPLICABLE**, or **ACTION REQUIRED**. Any ACTION REQUIRED item with an estimated saving above ₹10,000/month becomes a Jira ticket before this document goes in a drawer.

The 30 items are ordered by typical INR impact across the Indian mid-market accounts we have reviewed. None require re-architecture. Most can be closed in a day of engineering time.

---

## Section 1 — Compute (Items 1–8)

### 1. Over-provisioned Virtual Machines

**What leaks:** VMs sized for peak load running 24×7 at 10–20% CPU utilisation.
**How to detect:**
```bash
az vm list --query "[].{name:name,size:hardwareProfile.vmSize}" -o table
# Then check Azure Monitor → Metrics → Percentage CPU over 30 days, per VM
```
**Fix:** Right-size to a smaller SKU family (D2s_v5 → B2s, D4s_v5 → D2s_v5). The B-series is designed for burstable workloads at 40–55% discount.
**Typical saving:** ₹8,000–₹35,000/VM/month.

### 2. Reserved Instances / Savings Plan coverage below 70%

**What leaks:** Steady-state workloads running on pay-as-you-go when 1-year or 3-year Reserved Instances / Savings Plans would reduce cost by 40–60%.
**How to detect:** Azure Portal → Cost Management → Reservations → Recommendations
**Fix:** Purchase 1-year No-Upfront Reserved Instances for any VM family running >70% of hours. Azure Savings Plans (introduced 2022) offer flexibility across VM families at ~35% discount.
**Typical saving:** 30–55% on covered workloads.

### 3. Dev / test environments running 24×7

**What leaks:** Non-prod VMs billed for 168 hours/week when only used 40 hours/week.
**How to detect:** Filter Cost Management by tag `Environment=dev|test|staging`. Check Azure Monitor for activity patterns.
**Fix:** Azure Automation → Start/Stop VMs during off-hours (free extension). Or migrate to Azure DevTest Labs for built-in scheduling.
**Typical saving:** 60–75% on non-prod compute.

### 4. Azure Hybrid Benefit not claimed

**What leaks:** Windows Server VMs paying per-core licensing when existing Software Assurance licences would cover them.
**How to detect:** Cost Management → filter Product = "Virtual Machines" with Windows. Look for "without Azure Hybrid Benefit".
**Fix:** Enable Azure Hybrid Benefit on eligible VMs — one-click in Azure Portal.
**Typical saving:** Up to 40% on Windows Server VM cost.

### 5. Legacy VM SKUs (A-series, D-series v1/v2)

**What leaks:** Older VM generations priced 20–40% higher than current-gen equivalents for the same performance.
**How to detect:** Cost Management → VM size analysis. Flag any A_v2, D_v1, D_v2, D_v3 instances.
**Fix:** Migrate to D_v5 or D_v6 series (latest generation). Performance improves and cost drops simultaneously.
**Typical saving:** 20–30%/VM/month.

### 6. AKS node pools provisioned for peak

**What leaks:** Node pools sized for peak traffic that occurs 2 hours/day, idle 22 hours.
**How to detect:**
```bash
az aks nodepool list --cluster-name <name> --resource-group <rg> -o table
# Check Azure Monitor → Insights → AKS → Node pool utilisation
```
**Fix:** Enable Cluster Autoscaler. Use scheduled scaling for predictable traffic patterns. Consider Azure Virtual Nodes (ACI) for bursty workloads.
**Typical saving:** ₹20,000–₹80,000/cluster/month.

### 7. Spot VMs not used for batch / CI / stateless workloads

**What leaks:** Pay-as-you-go VMs running interruptible workloads when Spot VMs at 60–90% discount are available.
**How to detect:** Identify fault-tolerant workloads: CI runners, batch jobs, dev environments, stateless web tiers.
**Fix:** Use Spot VMs for these. Azure sends a 30-second eviction warning — implement graceful shutdown.
**Typical saving:** 60–90% on eligible workloads.

### 8. App Service Plans oversized

**What leaks:** P1v3 ($146/month) running a workload that fits on B1 ($13/month).
**How to detect:** App Service → Scale Up → current plan + metrics. Check CPU + memory over 30 days.
**Fix:** Scale down to the smallest plan that meets p95 utilisation with 30% headroom.
**Typical saving:** ₹5,000–₹12,000 per app service.

---

## Section 2 — Storage (Items 9–14)

### 9. Blob Storage in Hot tier holding cold data

**What leaks:** Hot tier at $0.018/GB/month storing data untouched for 12+ months.
**How to detect:**
```bash
az storage blob list --account-name <name> --container-name <container> \
  --query "[?properties.lastModified<'2025-04-01'].{name:name,size:properties.contentLength}" -o table
```
**Fix:** Lifecycle management policy → transition blobs untouched 90+ days to Cool tier ($0.0100), 180+ days to Archive tier ($0.00099).
**Typical saving:** 60–95% on cold data.

### 10. Unattached Managed Disks

**What leaks:** Disks orphaned after VM deletion, still billed monthly.
**How to detect:**
```bash
az disk list --query "[?managedBy==null].{name:name,sizeGb:diskSizeGb,location:location}" -o table
```
**Fix:** Automated cleanup after 30 days of unattached status. Use Azure Resource Graph for scheduled queries.
**Typical saving:** ₹200–₹1,500 per disk per month.

### 11. Premium SSD where Standard SSD would suffice

**What leaks:** P30 (1 TiB at $135/month) on dev VMs when E30 Standard SSD ($75/month) has adequate IOPS.
**How to detect:** Disk performance metrics → IOPS and throughput utilisation over 30 days. If under 50% of Premium SSD limits consistently, Standard is fine.
**Fix:** Migrate to Standard SSD (v2) for 40–50% discount. Performance is adequate for most non-prod and many prod workloads.
**Typical saving:** ₹4,000–₹15,000 per disk.

### 12. Stale Snapshots

**What leaks:** Daily snapshots accumulating indefinitely at full storage cost.
**How to detect:**
```bash
az snapshot list --query "[?timeCreated<'2026-01-01'].{name:name,size:diskSizeGb}" -o table
```
**Fix:** Retention policy — keep 30 days of daily, 12 months of monthly, purge the rest. Azure Backup handles this natively.
**Typical saving:** ₹5,000–₹25,000/month across a typical account.

### 13. File Shares over-provisioned

**What leaks:** Premium file shares provisioned at 10 TiB, actually storing 1 TiB.
**How to detect:** Storage account → File shares → capacity vs provisioned.
**Fix:** Resize file shares to actual usage + 20% buffer. Premium is billed on provisioned size, not used.
**Typical saving:** 40–80% on Premium file share cost.

### 14. Blob versioning + soft delete without limits

**What leaks:** Every blob version retained forever, turning a 500 GB container into 5 TB.
**How to detect:** Storage account → Data protection → soft delete + versioning settings.
**Fix:** Set soft delete retention to 14 days (not default 90). Configure version retention — keep 10 most recent per blob.
**Typical saving:** 50–85% on affected containers.

---

## Section 3 — Databases (Items 15–19)

### 15. Azure SQL Database oversized

**What leaks:** Gen5 Business Critical at 16 vCore (₹1.2L/month) running a workload that fits in 4 vCore Gen5 General Purpose (₹18K/month).
**How to detect:** Azure SQL Database → Metrics → DTU/CPU/Memory % over 30 days.
**Fix:** Scale down, or migrate to Serverless tier for dev/test which auto-pauses after inactivity.
**Typical saving:** 60–85% on oversized instances.

### 16. Azure Database for MySQL/PostgreSQL — High Availability on non-prod

**What leaks:** HA-enabled database for dev or test environments doubles the cost for no production value.
**How to detect:** Check High Availability setting per database. Filter by environment tag.
**Fix:** Disable HA on all non-prod databases.
**Typical saving:** 50% on affected databases.

### 17. Cosmos DB Provisioned Throughput with no autoscale

**What leaks:** 40,000 RU/s provisioned for peak when average load is 3,000 RU/s.
**How to detect:** Cosmos DB → Metrics → Normalized RU Consumption. If average is <20% of provisioned, autoscale is better.
**Fix:** Enable Autoscale Throughput — max RU/s stays the same, but billing tracks actual usage with a floor at 10%.
**Typical saving:** 40–70% on Cosmos DB cost.

### 18. Redis Cache oversized

**What leaks:** Premium P2 ($720/month) for a cache that holds 500 MB of data.
**How to detect:** Azure Cache for Redis → Metrics → Used Memory vs Total Memory.
**Fix:** Right-size to the smallest tier meeting throughput + memory needs. Basic/Standard is fine for dev/staging.
**Typical saving:** ₹15,000–₹50,000/month per instance.

### 19. Azure Database Reserved Capacity not purchased

**What leaks:** Pay-as-you-go Azure SQL / MySQL / PostgreSQL when Reserved Capacity at 20–55% discount is available.
**How to detect:** Cost Management → Reservations → Recommendations → Azure SQL.
**Fix:** Purchase 1-year No-Upfront Reserved Capacity for databases with stable workload.
**Typical saving:** 20–55% on database compute.

---

## Section 4 — Networking (Items 20–24)

### 20. Unused Public IPs

**What leaks:** Each Standard Public IP: ₹360/month, even when unattached.
**How to detect:**
```bash
az network public-ip list --query "[?ipConfiguration==null].name" -o tsv
```
**Fix:** Delete unused Public IPs. Use Dynamic allocation where possible.
**Typical saving:** ₹360 × number of orphaned IPs.

### 21. Cross-region bandwidth

**What leaks:** Services in different regions transferring data at ₹1.80–₹3.60/GB.
**How to detect:** Cost Management → Data Transfer → cross-region egress bytes by source/destination.
**Fix:** Co-locate services that communicate frequently. Use VNet peering within the same region (free). For multi-region deployments, cache or replicate rather than fetch on-demand.
**Typical saving:** ₹20,000–₹1,50,000/month depending on scale.

### 22. Application Gateway / Load Balancer standard tier when Basic suffices

**What leaks:** Application Gateway v2 (₹15,000/month baseline) for low-traffic workloads.
**How to detect:** Application Gateway → Metrics → connections/second + data processed.
**Fix:** For low-traffic apps, use Basic Load Balancer (free) + Azure Front Door for CDN where needed.
**Typical saving:** ₹10,000–₹25,000/gateway/month.

### 23. ExpressRoute circuits over-provisioned

**What leaks:** 1 Gbps ExpressRoute circuit at ₹1.8L/month running at 50 Mbps average.
**How to detect:** ExpressRoute → Metrics → Bits in/out per second.
**Fix:** Downsize to the next tier (100 Mbps → ₹22K/month) if consistently under-utilised.
**Typical saving:** 50–85% on circuit cost.

### 24. VPN Gateway SKU oversized

**What leaks:** VpnGw5 (₹45K/month) for a site-to-site VPN that handles 500 Mbps and 20 tunnels.
**How to detect:** VPN Gateway metrics → tunnel throughput + count.
**Fix:** Size to actual needs. VpnGw1 (₹12K/month) handles 650 Mbps and 30 tunnels.
**Typical saving:** 60–80% on VPN cost.

---

## Section 5 — Platform / Management (Items 25–27)

### 25. Log Analytics ingestion without filters

**What leaks:** All diagnostic logs sent to Log Analytics at ₹220/GB ingestion + ₹12/GB/month retention.
**How to detect:** Log Analytics Workspace → Usage → top ingesting resources.
**Fix:** Filter aggressively. Send only what is queried. Use Basic Logs tier (₹45/GB) for high-volume verbose logs. Archive older than 90 days to Blob Storage.
**Typical saving:** 40–80% on Log Analytics bill.

### 26. Azure Monitor metrics — custom metric explosion

**What leaks:** Application Insights ingesting 50M custom metrics/month at ₹220/GB.
**How to detect:** Application Insights → Usage → billing per data type.
**Fix:** Use Sampling to reduce by 50–90%. Disable logging for verbose dependency telemetry.
**Typical saving:** 50–80% on Application Insights cost.

### 27. Dev/Test subscriptions not used

**What leaks:** Azure Dev/Test subscriptions offer discounted rates — but only if activated.
**How to detect:** Verify subscription type for all non-prod workloads.
**Fix:** Convert non-prod subscriptions to Dev/Test offer (requires eligible Visual Studio subscription).
**Typical saving:** 15–30% on non-prod compute.

---

## Section 6 — Governance (Items 28–30)

### 28. No resource tagging policy

**What leaks:** Cost attribution impossible without tags. Shadow IT accumulates.
**How to detect:** Azure Policy → check for required-tag policies.
**Fix:** Enforce mandatory tags via Azure Policy: `Environment`, `Project`, `CostCenter`, `Owner`. Block resource creation without them.
**Typical saving:** Indirect — unlocks all the above.

### 29. Orphaned Resource Groups

**What leaks:** RGs from former employees, abandoned projects, stale tests.
**How to detect:**
```bash
az group list --query "[?tags.LastActive<'2025-10-01'].name" -o tsv
```
**Fix:** Tag every RG with `Owner` and `LastActive`. Monthly review. Delete after approval.
**Typical saving:** ₹10,000–₹1L/month depending on scale.

### 30. Azure Advisor recommendations unacted

**What leaks:** Azure Advisor highlights cost opportunities — most accounts have ₹20K–₹2L/month of recommendations sitting unacted.
**How to detect:** Azure Portal → Advisor → Cost tab.
**Fix:** Review weekly. Close every recommendation with either Action, Dismiss + Reason, or Postpone with date.
**Typical saving:** 20–40% on a typical first pass.

---

## Summary

| Section | Items | Typical Impact |
|---|---|---|
| Compute | 1–8 | 30–50% of total savings |
| Storage | 9–14 | 15–25% |
| Databases | 15–19 | 10–20% |
| Networking | 20–24 | 8–15% |
| Platform / Management | 25–27 | 5–10% |
| Governance | 28–30 | Unlocks the rest |

**Aggregate target:** a typical Indian mid-market Azure account working through this list closes 20–35% of monthly spend over 4–6 weeks of effort.

---

## If you want a second pair of eyes

If you would like us to work through this on your own Azure estate, a free 30-minute **Cloud Cost Health Check** is the starting point. You share a sample billing export. We send back a two-page written summary the same day covering the three highest-impact leaks we see — with specific rupee figures traced to your own data.

**[Book your free Health Check → aicloudstrategist.com/book.html](https://aicloudstrategist.com/book.html)**

---

*AICloudStrategist · Anushka B, Founder · Rohini, Delhi 110085 · support@aicloudstrategist.com*
*Founder-led. Enterprise-reviewed.*

— Anushka B, Founder · AICloudStrategist
