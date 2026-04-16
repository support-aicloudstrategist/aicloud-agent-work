---
topic: Kubernetes node pool right-sizing
week: 3
post: 1
cadence_slot: Tuesday W3
---

# LinkedIn Post — Kubernetes Node Pool Right-Sizing

A client running 3 EKS node pools on m5.4xlarge — every pod request set to 2 vCPU / 4 GB.

Reality? Average utilisation: **11% CPU, 18% memory.**

They were paying ₹4.2L/month to run air.

Here's what right-sizing looked like in practice:

→ Pulled 30 days of VPA (Vertical Pod Autoscaler) recommendations  
→ Matched actual p95 usage to instance family — moved most workloads to m5.large + m5.xlarge  
→ Split pools: spot for stateless batch, on-demand for stateful services  
→ Set PodDisruptionBudgets so the ops team didn't panic on scale-down events

Result: **₹1.8L/month saved. No re-architecture. No downtime.**

This isn't magic — it's just reading the metrics your cluster already produces.

Most teams skip this because it feels risky. It isn't, if you do it with proper guardrails and senior-architect oversight before you touch production.

If your Kubernetes bill has grown faster than your headcount this year, that's the signal.

DM me or book a free 30-min Cloud Cost Health Check → aicloudstrategist.com

— Anushka B | Founder, AICloudStrategist | Founder-led. Enterprise-reviewed.
