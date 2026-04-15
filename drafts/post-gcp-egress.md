# LinkedIn Post — GCP Multi-Region Egress (Post A: War Story)

---

The client's GCP bill had tripled in eight months. Their engineering lead insisted nothing had changed.

Something had changed.

We pulled their billing export into BigQuery and ran egress by source region. One line jumped off the screen: **$14,000 a month in inter-region data transfer.** us-central1 to us-east1. Firing continuously. All day, every day.

Their application ran in us-central1. Their analytics warehouse had been quietly spun up in us-east1 during a late-night sprint months earlier — a decision that made sense in the moment and nobody ever revisited. Every query, every pipeline flush, every dbt run was crossing a regional boundary. **94% of their entire egress bill was that single topology mistake.**

The fix took one weekend. Migrate the warehouse back to us-central1. Update three Terraform files. Validate the downstream pipelines on Sunday evening.

The next billing cycle told the story: monthly egress dropped from **$14,800 to under $900.** Over ₹14 lakh a year, recovered. No new architecture. No vendor negotiation. One region flag in an IaC file.

This is the pattern we see again and again. The most expensive cloud mistakes are never the dramatic ones. They are the quiet ones — a region chosen at 2am, an auto-scaler that forgot to scale down, an RI that expired without anyone noticing. They compound for months before anyone asks the right question.

If your cloud bill has grown faster than your traffic, it is almost certainly hiding something similar. The free 30-minute Cloud Cost Health Check exists for exactly this — we pull your billing export, find the top three leaks, and send you a written summary the same day. No pitch. No follow-up sequence. Just clarity.

**aicloudstrategist.com/book.html**

— Anushka B, Founder · AICloudStrategist
*Founder-led. Enterprise-reviewed.*

---
