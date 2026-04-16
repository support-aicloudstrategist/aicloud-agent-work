# Cost-Per-1000-Inferences: The One Number Every AI Product Team Should Know

*By Anushka B | AICloudStrategist*

---

Ask a founder how much their AI feature costs to run. Nine out of ten will tell you the monthly API bill. Maybe they'll quote the GPU spend. What almost none of them can tell you is the cost to serve one user action — one summarisation, one recommendation, one chat completion.

That number is cost-per-1000-inferences (CP1Ki). It is the unit economics of your AI product. Without it, you cannot price correctly. You cannot decide when to switch models. You cannot tell your CFO why the AI line item jumped 40 percent last quarter without looking like you've lost control of the system you built.

This post walks through exactly how to calculate it, shows a worked comparison across three common stacks, and explains how to instrument it so the number updates itself.

---

## What "inference" means here

One inference = one round-trip through your model: prompt in, completion out. A user clicking "Summarise this document" triggers one inference. A multi-turn chat session that generates ten responses triggers ten. For batch jobs, each item processed is one inference.

CP1Ki = total cost to serve 1,000 inferences in a given period.

That is it. Simple denominator, hard-to-get numerator — because the numerator varies by model, by hosting mode, by utilisation, and by prompt design.

---

## The calculation: managed APIs

For managed APIs (Anthropic Claude, OpenAI, Google Gemini via their direct or cloud endpoints), the cost structure is token-based:

**Total cost = (input tokens × input price) + (output tokens × output price)**

To get CP1Ki, you need two more things: average tokens per inference, and the model's published rate.

**Formula:**

```
CP1Ki = ((avg_input_tokens × input_$/1M) + (avg_output_tokens × output_$/1M)) × 1000 / 1,000,000
```

Or simplified: `CP1Ki = (avg_tokens_per_inference × blended_$/1M_tokens) / 1000`

The blended rate depends heavily on your input/output ratio. Most product use cases are input-heavy — system prompts, document context, retrieved chunks. A summarisation task might be 2,000 input tokens to 300 output tokens. A coding assistant might flip that ratio. Measure your actual distribution before benchmarking.

---

## Worked example: same task, three stacks

**Task:** Document summarisation — 1,800 input tokens (system prompt + document), 400 output tokens. Medium complexity, no streaming edge cases. Target: 10,000 inferences/day.

### Stack 1 — Claude Haiku 3.5 (Anthropic API)

- Input: $0.80 / 1M tokens
- Output: $4.00 / 1M tokens
- Per inference: (1800 × 0.80 + 400 × 4.00) / 1,000,000 = ($1.44 + $1.60) / 1,000,000 = $0.00304
- **CP1Ki: $3.04**
- Daily cost at 10K inferences: **$30.40**

### Stack 2 — GPT-4o (OpenAI API)

- Input: $2.50 / 1M tokens
- Output: $10.00 / 1M tokens
- Per inference: (1800 × 2.50 + 400 × 10.00) / 1,000,000 = ($4.50 + $4.00) / 1,000,000 = $0.0085
- **CP1Ki: $8.50**
- Daily cost at 10K inferences: **$85.00**

### Stack 3 — Llama 3 70B, self-hosted on AWS g5.xlarge

The g5.xlarge has one A10G GPU (24GB VRAM). Llama 70B in 4-bit quantisation fits, but barely — you will see throughput drop under concurrent load.

- On-Demand rate (us-east-1): $1.006/hour. 1-year Reserved: ~$0.636/hour. Use Reserved for any steady-state workload.
- At Reserved rate, monthly GPU cost: $0.636 × 730 = **$464/month**
- Add: EC2 storage (50GB gp3) ≈ $4/month, data transfer ≈ $5/month (internal traffic), monitoring overhead ≈ $3/month
- **Total infrastructure: ~$476/month**
- At 10K inferences/day × 30 days = 300,000 inferences/month
- **CP1Ki: ($476 / 300,000) × 1,000 = $1.59**

On paper, self-hosted wins by 2x on CP1Ki at this volume. But there are four numbers this calculation does not include: engineer time to maintain vLLM config and model updates (~4 hrs/month at senior rates), the cost of the g5.xlarge sitting at 30 percent utilisation on weekends, latency SLA misses when the single instance queues up under burst load, and the on-call rotation that now owns a GPU. At 300K inferences/month, the self-hosted advantage often disappears once you account for fully-loaded operational cost.

The crossover point — where self-hosted infrastructure genuinely beats managed API cost including ops overhead — is typically above 2–3M inferences/day for a team without existing MLOps tooling. Our [AI/GPU Cost Audit Checklist](https://aicloudstrategist.com/resources/ai-gpu-cost-audit-checklist.pdf) has a worksheet that lets you plug in your actual volumes and team rates to find your specific crossover.

---

## Why CP1Ki changes your pricing decisions

Most AI product teams price on intuition or competitor benchmarking. Neither is a business model.

If your CP1Ki is $3.04 (Haiku stack above) and your product charges ₹299/month for unlimited summarisations, you need to know how many summarisations a power user runs before you're underwater. At ₹299 ≈ $3.60 and CP1Ki of $3.04, you have exactly $0.56 of gross margin before you pay for servers, support, and salary. One user who runs 1,000 summarisations/month wipes out 92 paying users' margin.

This is not a hypothetical. I see it regularly in FinOps audits of AI-native startups. The unit economics were never calculated; the product was priced on vibes.

CP1Ki also tells you when to switch models mid-product. If your quality threshold is met by Haiku, there is no business case for GPT-4o at 2.8x the cost per inference. But if a specific feature — legal clause analysis, code generation — requires GPT-4o quality, you can route that feature specifically to the expensive model and keep the rest of the product on Haiku. That routing decision needs CP1Ki to justify itself in a board update.

---

## How to instrument it

You cannot manage what you do not measure at the right granularity. API bills and GPU invoices tell you monthly totals. You need per-feature, per-inference data.

**Step 1: Tag every inference call at the point of code.**

Add a metadata tag to every API call that identifies the feature generating it:

```python
response = client.messages.create(
    model="claude-haiku-3-5",
    max_tokens=500,
    messages=[...],
    metadata={"user_id": user_id}  # Anthropic API
)
# Log separately: feature_tag="document_summariser", tokens_in=X, tokens_out=Y
```

For self-hosted models behind vLLM or Triton, tag at the reverse proxy layer (Nginx, Envoy) or in your application middleware before the model call. The tag should carry: feature name, user tier, model version, timestamp.

**Step 2: Export billing data by tag into your data warehouse.**

For managed APIs: pull usage logs from the provider's API (Anthropic Usage API, OpenAI Usage endpoint, AWS Cost and Usage Report for Bedrock). Join on timestamp to your application log's feature tag. For self-hosted: allocate GPU cost by the fraction of total requests that feature generated in that billing period.

A simple dbt model or even a spreadsheet pivot on feature_tag × (tokens_in + tokens_out) × rate gives you CP1Ki per feature, updated daily.

**Step 3: Alert on CP1Ki drift.**

Set a threshold alert: if CP1Ki for any feature exceeds 120 percent of its 30-day baseline, page the on-call engineer. Common causes — prompt bloat (someone added 800 tokens to the system prompt), model version change, or a bug causing retry storms. Catching this early has saved clients $8,000–$15,000 in a single incident.

---

## The number you owe your team

CP1Ki is not a finance metric. It is an engineering metric that finance can read. It tells your CTO where the AI spend is going. It tells your product manager which features are subsidising which. It tells your pricing team the floor below which a plan cannot be profitable.

If you cannot answer "what does it cost us to serve 1,000 of these AI responses?" for every AI feature in production, you are flying blind.

---

**Book an AI Architecture Review** — we calculate CP1Ki across your full model stack, identify the routing decisions that would cut your inference cost by 30–60 percent, and deliver a prioritised implementation plan in two weeks.

Download the [AI/GPU Cost Audit Checklist](https://aicloudstrategist.com/resources/ai-gpu-cost-audit-checklist.pdf) first — it gives you the data you'll need to walk into that conversation.

→ [Book the AI Architecture Review](https://aicloudstrategist.com/book.html)

---

*Anushka B | Founder, AICloudStrategist | Founder-led. Enterprise-reviewed.*
