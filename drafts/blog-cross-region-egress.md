# The Cross-Region Egress Mistake That Quietly Tripled a GCP Bill

*Published on aicloudstrategist.com/blog*

---

Two line items. One billing export query. ₹14 lakh recovered per year.

That is the short version of Case 2 from our proof library. The longer version is this: a funded SaaS company watched their GCP bill triple over eight months. Their engineering lead was confident nothing had changed architecturally. He was technically right — no new services, no traffic spike, no notable infrastructure expansion. What had changed was one region flag in one Terraform file, written during a late-night sprint six months earlier.

Their analytics warehouse had been provisioned in `us-east1`. Their application ran in `us-central1`. Every dbt run, every pipeline flush, every scheduled query crossed a regional boundary. The inter-region data transfer line was ₹12.4 lakh per year — 94% of their total GCP egress bill. Nobody had noticed because it appeared as a network line item, not an infrastructure line item, and nobody was watching network costs.

The fix took one weekend. The monthly egress bill dropped from ₹1.24 lakh to under ₹7,500. Annualised recovery: ₹14 lakh.

---

## The Mechanism: Why Cross-Region Egress Compounds Silently

GCP charges for data leaving a region — to the internet, to another GCP region, or to another cloud. Within the same continent, inter-region transfer is priced at $0.01/GB. That sounds negligible until you account for what actually crosses that boundary in a typical data stack.

Every data pipeline has a fan-out problem. A single dbt model refresh doesn't move one file — it moves the source tables, the intermediate materialisation, the result set, and the audit logs. A 10 GB raw dataset becomes 60–80 GB in transit by the time transformations, tests, and exports complete. Run that pipeline 8 times a day and your "small 10 GB table" is generating 480–640 GB of inter-region traffic daily. At $0.01/GB, that's $4.80–$6.40 per day, $144–$192 per month — per pipeline. Add five more pipelines, a real-time Pub/Sub feed, and a Dataflow job flushing to BigQuery, and the line item scales to thousands of dollars before anyone notices.

The compounding effect has three drivers:

**Invisibility.** GCP's billing console groups network costs under a single service line. Without a billing export query filtering on SKU descriptions, you cannot tell whether $5,000 in "Networking" costs is internet egress, inter-region transfer, or Cloud CDN. Most teams do not run that query until something forces them to.

**Habituation.** Bills grow gradually. A 3x increase over eight months feels different from a 3x increase overnight. Engineers adapt to the new normal rather than investigating the delta.

**Ownership gaps.** The team that provisioned the warehouse in the wrong region has often left. The team running dbt doesn't own the infrastructure config. Nobody holds the cross-cutting network cost line.

---

## How to Detect It: The BigQuery Billing Export Query

If you have GCP billing export enabled to BigQuery — and you should — this query surfaces every inter-region transfer SKU ranked by cost in the last 30 days:

```sql
SELECT
  project.id                                AS project_id,
  resource.location                         AS source_region,
  sku.description                           AS sku,
  ROUND(SUM(usage.amount), 2)              AS total_gib,
  ROUND(SUM(cost), 2)                       AS cost_usd_30d,
  ROUND(SUM(cost) * 12, 2)                 AS annualised_cost_usd
FROM
  `<YOUR_PROJECT>.<YOUR_DATASET>.gcp_billing_export_v1_*`
WHERE
  DATE(usage_start_time) >= DATE_SUB(CURRENT_DATE(), INTERVAL 30 DAY)
  AND (
      LOWER(sku.description) LIKE '%inter region%'
   OR LOWER(sku.description) LIKE '%interregion%'
   OR (
        LOWER(sku.description) LIKE '%egress%'
    AND LOWER(sku.description) NOT LIKE '%internet%'
      )
  )
  AND cost > 0
GROUP BY
  1, 2, 3
ORDER BY
  cost_usd_30d DESC
LIMIT 50;
```

Replace `<YOUR_PROJECT>` and `<YOUR_DATASET>` with your billing export destination. The `*` wildcard catches both the standard and detailed export table naming conventions.

What to look for: any row where `annualised_cost_usd` exceeds $1,000 and the source region is your primary application region. If a single SKU line exceeds $5,000 annualised, you have a topology problem, not a pricing problem. Sort by `annualised_cost_usd` descending and work top to bottom.

If you haven't enabled billing export yet, do it now. GCP retains billing data in the console for 12 months; the export to BigQuery is the only way to query it programmatically and retain history beyond that window.

---

## The Fix: Three Options, One Right Answer

Once you've identified the offending traffic, you have three remediation paths in order of preference:

**1. Warehouse co-location.** Move the analytics resource into the same region as the application generating the data. This eliminates the transfer entirely. It is the correct fix in 80% of cases. The weekend migration in Case 2 was this: a BigQuery dataset recreation in `us-central1`, a pipeline repoint, a dbt `profiles.yml` change, a `terraform apply`. No architectural change; one flag.

**2. VPC peering with regional enforcement.** If your services are spread across regions for legitimate reasons, establish VPC Network Peering within a single region and route internal traffic through it. Peered VPC traffic within a region does not incur inter-region charges. This is the right fix when multi-region deployment is intentional but data transfer patterns aren't designed around it.

**3. Scheduled sync with regional staging.** For scenarios where real-time cross-region transfer is unavoidable — a source system that cannot move, a partner integration with a fixed endpoint — implement a scheduled sync that batches transfers and lands data in a regional staging bucket. Downstream consumers read from the local copy. Transfer happens once, on schedule, not continuously for every query. This reduces both cost and latency for read-heavy workloads.

What is not a fix: buying committed use discounts against a network topology that's wrong. You would be paying for the privilege of making the mistake more efficiently.

---

## When Cross-Region IS the Right Architecture

Cross-region deployments are not inherently a cost mistake. There are two scenarios where they are the correct call and the egress cost is a justified line item:

**Genuinely global customer base.** If you have users in North America, Europe, and APAC, serving them from a single region means high latency for two of the three groups. The performance cost to users exceeds the egress cost to you. Architect for proximity, monitor transfer costs per region as a known budget item, and optimise routing rather than trying to eliminate multi-region entirely.

**Regulatory data residency.** India's DPDP Act, the EU's GDPR, and several BFSI-sector mandates require specific data categories to remain within defined geographic boundaries. If your compliance posture requires eu-west1 to hold European customer records, that data cannot move to your application region in `us-central1` without a legal review. Here, egress cost is the price of compliance. Model it explicitly rather than treating it as waste.

The test: if cross-region transfer exists for convenience — because the first engineer to provision the warehouse chose a region at random, or because a staging environment was never migrated to match production — that is waste. If it exists because your architecture requires geographic distribution, it is cost of goods.

---

## Closing

The ₹14 lakh Case 2 recovery was not from a complex optimisation. It was from reading a billing export, identifying one wrong region, and moving a dataset. The entire intervention was scoped and executed in under 72 hours.

Most GCP environments we audit have at least one active inter-region topology mistake. The transfer line is small enough to miss in a high-level review and large enough to matter at year-end. The query above costs nothing to run.

If you want a structured review — not just egress, but the full network cost profile, commitment coverage, and idle resource footprint — book a free Cloud Cost Health Check. We document every finding in writing before the first invoice.

[Book your free Cloud Cost Health Check → aicloudstrategist.com/book.html](https://aicloudstrategist.com/book.html)

The cost of looking is zero. The cost of the wrong region flag is, apparently, ₹14 lakh a year.

---

*— Anushka B, Founder · AICloudStrategist · Founder-led. Enterprise-reviewed.*
