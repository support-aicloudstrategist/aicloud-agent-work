# LinkedIn Post — GCP Multi-Region Egress (Post A: War Story)

---

The client's GCP bill had grown 3x in eight months. Their engineering lead insisted nothing had changed.

Something had changed.

We pulled their billing export into BigQuery and ran egress by source region. One line stood out: $14,000/month in inter-region data transfer — us-central1 to us-east1, firing continuously.

Their application ran in us-central1. Their analytics warehouse had been quietly provisioned in us-east1 during a late-night sprint. Every query, every pipeline flush, every dbt run crossed a regional boundary. 94% of their total egress bill was that single topology mistake.

The fix was a warehouse migration over one weekend. The monthly egress line dropped from $14,800 to under $900.

No new architecture. No vendor negotiation. One region flag in a Terraform file.

We documented the full breakdown as Case 2 in our proof library — the detection query, the migration runbook, the before/after billing diff.

If your GCP bill grew faster than your traffic, this is worth 30 minutes.

**Book a free Cloud Health Check → [link in bio]**

---
*AICloudStrategist | FinOps for GCP & AWS teams*
