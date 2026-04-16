# AI Architecture Review & Consulting

**Service code:** AICS-08
**Price range:** ₹1,50,000 – ₹3,00,000
**Timeline:** 2–3 weeks
**Delivery:** Founder-led. Enterprise-reviewed.

---

## Service Overview

An end-to-end review of your AI and ML infrastructure — from training pipelines and GPU fleet management to inference endpoints, model serving, and the operational layer that keeps it all running in production.

AI workloads are the fastest-growing cost centre in mid-market cloud accounts, and also the least governed. Most companies adopted AI infrastructure rapidly — a SageMaker notebook here, a GPU instance there, a model endpoint that nobody cost-benchmarked — and three quarters later the bill is ₹8L/month with no clarity on cost-per-inference, no autoscaling on endpoints, and training jobs running on on-demand p4d instances when spot capacity was available 80% of the time.

This review brings the same rigour we apply to cloud architecture — Well-Architected principles, cost-per-unit economics, right-sizing, lifecycle governance — to the AI/ML stack specifically.

## Ideal Client Profile

- Company running AI/ML workloads on AWS (SageMaker, Bedrock, EC2 GPU), Azure (Azure ML, Azure OpenAI), or GCP (Vertex AI, GKE with GPU node pools)
- Monthly AI/ML infrastructure spend between ₹3L and ₹30L — growing faster than the team's ability to govern it
- Engineering team building or deploying: LLM-powered features, recommendation engines, computer vision pipelines, NLP services, or custom model training
- No dedicated MLOps function — data scientists provision infrastructure, platform team doesn't review it
- Preparing to scale AI features to production (POC → production transition)
- Post-sticker-shock: the GPU bill arrived and leadership wants to understand what is actually needed vs what is running by inertia
- Evaluating build-vs-buy: self-hosted models vs managed API (OpenAI, Anthropic, Cohere) and needs a cost/latency/control framework for the decision

## Delivery Plan — Week by Week

### Week 1: Discovery and Inventory (Days 1–5)

**Day 1 — Kickoff**
- 90-minute session with ML lead, platform/infra lead, and CTO
- Define scope: which AI/ML workloads, which accounts/projects, training vs inference vs both
- Provision read-only access to compute, storage, model registries, and billing
- NDA and data handling agreement signed (especially important — training data metadata is sensitive)

**Day 2–3 — Infrastructure Inventory**

*Compute:*
- GPU instance inventory: type (p3/p4d/g5/A100/T4/L4), count, region, utilisation (GPU-Util%, GPU-Mem%)
- CPU-based ML compute: training clusters, batch inference, feature engineering jobs
- Spot vs On-Demand vs Reserved ratio for ML workloads
- Idle GPU detection: instances running but no training job active (CloudWatch GPU utilisation < 5% for >2 hours)

*Model Serving:*
- Inference endpoints: type (real-time, serverless, batch), instance behind each, autoscaling config (or lack of)
- Latency profile: p50/p95/p99 per endpoint
- Traffic patterns: requests per second over 30 days — is this endpoint serving 2 req/s at 3am on a g5.xlarge?
- Managed API usage: OpenAI / Anthropic / Bedrock / Vertex AI — token counts, cost per call, caching hit rate

*Training:*
- Training job history (last 90 days): instance types, duration, cost per job
- Dataset sizes and storage location (S3/GCS/Azure Blob — hot or cold tier?)
- Distributed training setup: how many nodes, communication backend (NCCL, Gloo), efficiency metrics
- Experiment tracking: MLflow / Weights & Biases / SageMaker Experiments — what's being logged?

*Pipeline and Orchestration:*
- Feature stores (if any): Feast, Tecton, SageMaker Feature Store — freshness, compute cost
- ETL/data pipeline: Airflow, Step Functions, Dataflow, Prefect — bottleneck identification
- Model registry and versioning: how models move from training → staging → production
- CI/CD for ML: automated retraining triggers, model validation gates, rollback mechanisms

**Day 4–5 — Team Interviews**
- 3–4 × 45-minute sessions:
  - Data science team: what are they building, what takes too long, what breaks
  - Platform/infra team: how do they provision GPU capacity, what's the approval process for new instances
  - Product team: which AI features are customer-facing, what's the latency SLA, what happens when inference is slow
  - Finance (if available): how is AI spend tracked, is there a cost-per-feature view

### Week 2: Analysis and Optimisation Framework (Days 6–10)

**Day 6–7 — Cost-Per-Unit Economics**

This is the core analytical output — mapping AI infrastructure spend to business-meaningful units:

| Metric | What it tells you |
|---|---|
| **Cost per training run** | Are you spending ₹45K per fine-tuning job when spot + checkpointing could bring it to ₹18K? |
| **Cost per 1K inferences** | Is your real-time endpoint costing ₹12 per 1K requests when a batch endpoint at ₹1.50 would meet the latency SLA? |
| **GPU utilisation rate** | A p4d.24xlarge at 15% GPU-Util is burning ₹1.2L/month on a workload that fits on a g5.xlarge at ₹25K/month |
| **Cost per model iteration** | Total cost from data prep → training → evaluation → deployment — the number your data science lead needs to make prioritisation decisions |
| **Managed API cost per feature** | If you're calling GPT-4o for a summarisation feature at 50K calls/day, is the marginal cost per user sustainable at your current pricing? |

**Day 8–9 — Architecture Assessment**

Scored against 6 dimensions:

| Dimension | What we assess |
|---|---|
| **Compute Right-Sizing** | GPU family selection, instance sizing, spot strategy, idle detection |
| **Model Serving Architecture** | Real-time vs batch vs serverless, autoscaling, multi-model endpoints, caching |
| **Data Pipeline Efficiency** | Feature freshness vs compute cost, redundant ETL, storage tier alignment |
| **MLOps Maturity** | Experiment tracking, model registry, automated retraining, monitoring, drift detection |
| **Build vs Buy** | Self-hosted models vs managed APIs — cost/latency/control trade-off matrix |
| **Cost Governance** | Per-team GPU budgets, chargeback, approval workflows for expensive instances |

Each finding scored **Critical / High / Medium / Low** by cost impact and operational risk.

**Day 10 — Draft Report**
- Architecture diagrams: training pipeline, inference architecture, data flow
- Gap analysis with scoring
- Remediation roadmap: 30 / 60 / 90-day lanes

### Week 3 (if needed): Presentation and Handover (Days 11–15)

**Day 11 — Internal Review**
- Senior-architect oversight review — calibrating recommendations to the team's maturity and GPU budget reality

**Day 12 — Executive Presentation**
- 60-minute session: current AI infra state → cost-per-unit economics → top 5 optimisation levers → roadmap → build-vs-buy framework
- Formatted for CTO + CFO audience: rupee figures on every recommendation

**Day 13–15 — Handover**
- Full report package delivered
- 2 × 45-minute working sessions with ML and platform teams
- Build-vs-buy decision framework document (reusable for future model/API evaluations)
- Optional: scope an Implementation Sprint to execute top recommendations

## Pricing — INR

| Scope | Price | Timeline |
|---|---|---|
| Inference-only review (endpoints, APIs, serving) | ₹1,50,000 | 2 weeks |
| Full review (training + inference + pipeline + MLOps) | ₹2,25,000 | 2–3 weeks |
| Multi-cloud or multi-team AI estate | ₹3,00,000 | 3 weeks |

**Payment terms:** 50% advance, 50% on delivery.
**Gain-share option:** If the review identifies GPU/inference cost savings exceeding ₹1.5L/month, a 15% gain-share on verified savings in the first 6 months can replace or supplement the fixed fee.

## Deliverables

1. **AI Infrastructure Architecture Diagrams** — training pipeline, inference architecture, data flow (draw.io / Excalidraw, editable)
2. **Cost-Per-Unit Economics Report** — cost per training run, per 1K inferences, per model iteration, per managed API call — the numbers your ML lead and CFO both need
3. **6-Dimension Gap Analysis** — scored findings table (Critical/High/Medium/Low) with effort and cost-impact estimates
4. **GPU Right-Sizing Recommendations** — instance-level: current type → recommended type, with expected monthly savings in INR
5. **Build vs Buy Decision Framework** — reusable framework for evaluating self-hosted vs managed API for any new AI feature, covering cost, latency, data privacy, and vendor lock-in dimensions
6. **Remediation Roadmap** — 30/60/90-day plan with named owners, prioritised by INR impact
7. **Executive Summary** — 2-page boardroom-ready document: AI spend trajectory, top risks, recommended actions
8. **Knowledge Transfer Sessions** — 2 × 45-minute recorded sessions

## Tooling Stack

| Category | Tools |
|---|---|
| GPU utilisation monitoring | NVIDIA DCGM / nvidia-smi, CloudWatch GPU metrics, NVML |
| Infrastructure inventory | AWS Config, SageMaker describe-* APIs, Vertex AI API, Azure ML CLI |
| Cost analysis | OpenCost (with GPU label support), Infracost, native Cost Explorer / Billing Export |
| Model serving analysis | SageMaker Inference Recommender, Vertex AI Model Evaluation, custom latency benchmarking |
| MLOps maturity | MLflow, Weights & Biases (if client uses), SageMaker Experiments |
| IaC analysis | Terraform plan, Checkov, tfsec |
| Pipeline profiling | Airflow task duration metrics, Step Functions execution history, Dataflow job metrics |

All open-source where possible. Client owns all tooling.

## Out of Scope

- Model quality review (we review infrastructure and cost, not model accuracy or bias)
- Training dataset curation or labelling
- Application-layer code (prompt engineering, model fine-tuning logic)
- Penetration testing of AI endpoints (recommend separate AI red-teaming engagement)
- Cloud architecture review for non-AI workloads (covered by Service 07)
- Ongoing monitoring or MLOps implementation (can be scoped as a follow-on Implementation Sprint)

## When This Service Makes Sense

- **GPU bill shock** — the AI infrastructure line item tripled in two quarters and nobody can explain which workloads are driving it
- **POC to production** — you have a working prototype and need to architect the production infrastructure before launch
- **Build vs buy decision** — you are evaluating self-hosted LLMs vs OpenAI/Anthropic/Bedrock APIs and need a structured cost/latency/control framework
- **Scaling AI features** — what works for 1K users/day may not survive 100K users/day without architectural changes
- **Investor / board scrutiny** — AI spend is the fastest-growing line item and leadership wants clarity and governance before the next board meeting
- **Team transition** — the original ML engineer left, and the team is operating inherited GPU infrastructure they don't fully understand

## Build vs Buy: The Framework We Use

One of the most valuable outputs of this review is a reusable decision framework for evaluating self-hosted models vs managed APIs. The framework scores each option across 5 dimensions:

| Dimension | Self-Hosted | Managed API |
|---|---|---|
| **Unit cost at scale** | Lower at high volume (amortised GPU) | Higher marginal cost, lower fixed cost |
| **Latency control** | Full control, co-located | Vendor-dependent, network latency |
| **Data privacy** | Data stays in your VPC | Data leaves your boundary (unless private endpoints) |
| **Operational burden** | You own uptime, scaling, patching, model updates | Vendor owns uptime, you own integration |
| **Vendor lock-in** | Low (open models, your infra) | Medium-High (prompt formats, fine-tunes, embeddings) |

The framework produces a scored recommendation per use case — not a blanket "self-host everything" or "use APIs for everything." The right answer varies by workload.

## References

- AWS Well-Architected Machine Learning Lens (2025): https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/
- Google Cloud MLOps Best Practices: https://cloud.google.com/architecture/mlops-continuous-delivery-and-automation-pipelines-in-machine-learning
- Azure ML Well-Architected: https://learn.microsoft.com/en-us/azure/well-architected/service-guides/azure-machine-learning
- NVIDIA GPU Cloud (NGC) Optimisation Guide: https://docs.nvidia.com/deeplearning/frameworks/
- MLflow Documentation: https://mlflow.org/docs/latest/index.html
- Chip Huyen — Designing Machine Learning Systems (O'Reilly, 2022): industry-standard reference for ML system architecture
- Stanford MLSys Seminar: https://mlsys.stanford.edu — cutting-edge research on ML infrastructure efficiency
- FinOps for AI/ML Workloads — FinOps Foundation: https://www.finops.org/wg/ai-ml/
- SageMaker Inference Recommender: https://docs.aws.amazon.com/sagemaker/latest/dg/inference-recommender.html
- Anthropic API Pricing and Token Economics: https://www.anthropic.com/pricing

---

*AICloudStrategist · Founder-led. Enterprise-reviewed.*
*Anushka B, Founder · support@aicloudstrategist.com*
