# What Your AWS Cost Explorer Dashboard Is Not Showing You

You open Cost Explorer. You see a number. Maybe it's ₹18 lakhs this month, up from ₹14 lakhs last month. You click around. You look at the service breakdown. EC2 is the biggest line. S3 is doing something weird. Lambda barely registers. You close the tab feeling vaguely informed and entirely unequipped to do anything about it.

Here's the thing nobody tells you about Cost Explorer: it is a reporting tool, not a diagnostic tool. It shows you what you spent. It does not show you *why*, or *which decision* caused it, or whether the commitments you made six months ago are still working in your favor. Those three gaps — what I call the dashboard blindspots — are where most cloud overspend hides. And they hide very, very well.

Let's pull them into the light.

---

## Blindspot 1: Cross-Service Attribution

Cost Explorer organizes costs by service. EC2 gets its column. RDS gets its column. Data Transfer gets its own little mystery column that nobody fully understands. What it does not show you is the chain of causation *between* services — and that chain is where the real cost story lives.

Consider a common architecture: an API Gateway endpoint triggers a Lambda, which processes a file, which lands in S3, which triggers another Lambda for transformation, which writes to DynamoDB, which streams changes to Kinesis. You have six services touching one business transaction. Cost Explorer shows you six separate numbers. It does not show you that 60% of your Lambda invocations exist *solely to serve* that one data pipeline, or that a 3x increase in API traffic last Tuesday sent DynamoDB write costs up ₹2.4 lakhs in 48 hours.

The result: your engineering team optimizes Lambda because it looks expensive. But Lambda is cheap — it is doing exactly what it should. The actual problem is the upstream API design generating redundant invocations. Nobody sees this because nobody is looking at the services as a system.

**Surface it with Athena (against your CUR export):**

```sql
SELECT
  line_item_usage_start_date AS usage_date,
  line_item_product_code AS service,
  SUM(line_item_unblended_cost) AS daily_cost_usd,
  LAG(SUM(line_item_unblended_cost)) OVER (
    PARTITION BY line_item_product_code
    ORDER BY line_item_usage_start_date
  ) AS prev_day_cost_usd
FROM your_cur_table
WHERE
  line_item_usage_start_date >= DATE_ADD('day', -30, CURRENT_DATE)
  AND line_item_unblended_cost > 0
GROUP BY 1, 2
ORDER BY 2, 1;
```

Bring this output into a spreadsheet and look for services whose costs move in lockstep — same spike days, same dip days. That correlation is your cross-service attribution map. Once you can see which services breathe together, you know which ones belong to the same workload, and you can start reasoning about cost at the *transaction* level rather than the *service* level.

At one SaaS client we worked with, this analysis revealed that 40% of their RDS cost was attributable to a single reporting module that ran at 2 AM. It looked like a database cost on Cost Explorer. It was actually a product decision: the reports were generating full table scans on production infra instead of a read replica.

---

## Blindspot 2: Spike Causation

Cost Explorer will show you a spike. It will not tell you what caused it. You will see a bar that is taller than the others, maybe ₹3.5 lakhs in a single day against a ₹60,000 daily average, and you will have to become a detective with no crime scene tape and no witnesses.

The dashboard gives you a filter. You can cut by region, by service, by tag. But if your tags are inconsistent — and they almost always are — you are filtering noise through more noise. And even when you find the service responsible, Cost Explorer stops there. It will not tell you which deployment triggered it, which team pushed a config change, which autoscaling policy misread a metric.

Spike causation requires you to correlate cost data with operational events. Cost Explorer cannot do this. You need to bring the two datasets together.

**Surface it with Athena + CloudTrail cross-join:**

```sql
SELECT
  c.line_item_usage_start_date,
  c.line_item_product_code,
  c.line_item_usage_type,
  ROUND(SUM(c.line_item_unblended_cost), 2) AS cost_usd,
  c.resource_tags_user_environment AS environment,
  c.resource_tags_user_service AS service_tag
FROM your_cur_table c
WHERE
  c.line_item_usage_start_date BETWEEN DATE '2026-04-01' AND DATE '2026-04-15'
  AND c.line_item_unblended_cost > 0
GROUP BY 1, 2, 3, 5, 6
HAVING SUM(c.line_item_unblended_cost) > (
  SELECT AVG(daily_total) * 2.5
  FROM (
    SELECT
      line_item_usage_start_date,
      SUM(line_item_unblended_cost) AS daily_total
    FROM your_cur_table
    WHERE line_item_usage_start_date >= DATE_ADD('day', -60, DATE '2026-04-01')
    GROUP BY 1
  )
)
ORDER BY 4 DESC;
```

This query flags usage types that crossed 2.5x their 60-day baseline on any given day. Feed those dates and services back into CloudTrail with an event time filter. You will find your culprit — a deployment, a cron job that ran twice, an autoscaling group that got stuck in a loop and spun up 80 instances at ₹8/hour for six hours.

We ran this analysis for a fintech client after a single day cost them ₹11 lakhs against their ₹1.4 lakh daily average. CloudTrail correlation surfaced a data migration script that had a bug in its pagination logic, reprocessing the same 2 TB of data six times. Cost Explorer showed a spike. This query showed a root cause.

---

## Blindspot 3: Commitment Drift

This one is quiet. It does not announce itself as a spike. It just slowly bleeds you.

When you bought Reserved Instances or Savings Plans, they made sense. The workload was predictable. The instance family was right. EC2 RI coverage was at 82% and your finance team was happy. That was eight months ago.

Since then, your team migrated a service to Fargate. You rightsized three m5.2xlarge instances down to m5.xlarge. You moved a batch workload to Spot. Your RI coverage report still shows 80% — but it is covering the *wrong* things. You are paying commitment pricing for capacity you are no longer using the way you planned, while your new workloads run on-demand at full price.

Cost Explorer's RI and Savings Plans utilization reports show you *utilization* — whether your commitments are being consumed. They do not show you *alignment* — whether the workloads consuming them are the same workloads that justified the purchase.

**Surface it with Athena:**

```sql
SELECT
  reservation_reservation_a_r_n AS ri_arn,
  line_item_usage_type,
  line_item_product_code,
  resource_tags_user_service AS service_tag,
  resource_tags_user_team AS team_tag,
  SUM(reservation_unused_quantity) AS unused_units,
  SUM(reservation_unused_recurring_fee) AS wasted_cost_usd,
  SUM(line_item_unblended_cost) AS total_commitment_cost_usd,
  ROUND(
    SUM(reservation_unused_recurring_fee) /
    NULLIF(SUM(line_item_unblended_cost), 0) * 100, 1
  ) AS waste_pct
FROM your_cur_table
WHERE
  line_item_usage_start_date >= DATE_ADD('day', -90, CURRENT_DATE)
  AND reservation_reservation_a_r_n IS NOT NULL
  AND reservation_reservation_a_r_n != ''
GROUP BY 1, 2, 3, 4, 5
HAVING waste_pct > 20
ORDER BY wasted_cost_usd DESC;
```

Anything above 20% waste on a commitment over 90 days is a commitment that has drifted from its original purpose. For a company spending ₹25 lakhs/month on AWS with 30% committed, even 25% waste on commitments translates to ₹1.87 lakhs a month in pure waste — infrastructure you are paying for and not using, because the workload moved on without the commitment budget following it.

---

## What to Do Next

Cost Explorer is not broken. It is just doing what it was designed to do: report totals. Your job is not to stare at totals. Your job is to understand the architecture decisions, deployment events, and procurement choices that produce those totals — and to change the ones that are costing you money without delivering value.

The three queries above are a starting point. They require that your CUR export is set up, your tagging is at least partially consistent, and someone on your team is willing to write SQL instead of reading pie charts. If those conditions are not yet true at your organization, that is also information — it means your cost visibility foundation has gaps that will compound as your cloud spend scales.

If you want a structured way to find out exactly where your AWS spend is leaking — cross-service, spike-related, and commitment-based — the **Cloud Cost Health Check** is where to start. It is a 2-week engagement: we pull your CUR data, run attribution and drift analysis, and give you a prioritized list of actions with INR impact estimates attached to each one.

You will leave knowing exactly what Cost Explorer was not showing you — and what it is going to cost you if you keep not looking.

**Book your Cloud Cost Health Check →**
