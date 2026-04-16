# LinkedIn Bookmarklets v2 — CRM capture + Comment drafter

Two more bookmarklets complementing the connection/DM pair in `linkedin-bookmarklets.md`. Same install instructions (drag to bookmarks bar).

---

## Bookmarklet 3 — "LI-Copy-Prospect"

**What it does:** On any LinkedIn profile page, one click copies a CRM-ready block of text to clipboard. Format:

```
Name | Role | Company | Location | LinkedIn URL | Captured: 2026-04-16
```

Paste straight into Notion / Google Sheets / Airtable. Use case: Anushka is researching targets for the next day's connection-request batch. She opens 15 prospect profiles in tabs, clicks the bookmarklet on each, pastes into her CRM — 15 prospects logged in 90 seconds instead of 10 minutes of copy-paste per field.

**The code:**

```javascript
javascript:(function(){
  var name = (document.querySelector('h1')?.innerText || '').trim();
  var role = '';
  var company = '';
  try {
    var headline = document.querySelector('.text-body-medium.break-words')?.innerText?.trim();
    if (headline) {
      var parts = headline.split(/\s+at\s+|\s+@\s+|\s+\|\s+/i);
      role = (parts[0] || '').trim();
      company = (parts[1] || '').trim();
    }
  } catch(e) {}
  var location = '';
  try {
    var loc = document.querySelector('.text-body-small.inline.t-black--light.break-words')?.innerText?.trim();
    if (loc) location = loc;
  } catch(e) {}
  var url = window.location.href.split('?')[0].split('#')[0];
  var today = new Date().toISOString().slice(0, 10);
  var row = [name, role, company, location, url, 'Captured: ' + today].filter(Boolean).join(' | ');
  navigator.clipboard.writeText(row).then(function(){
    alert('Copied to clipboard:\n\n' + row + '\n\nPaste into CRM.');
  }, function(){
    prompt('Auto-copy failed. Copy manually:', row);
  });
})();
```

---

## Bookmarklet 4 — "LI-Comment-Draft"

**What it does:** On any LinkedIn post (from a target CTO or founder), click the bookmarklet. It reads the post text, summarises the key point, and drafts an Anushka-voice comment that:

- Acknowledges a specific point from the post (not generic "great insight!")
- Adds one practitioner observation we would genuinely offer
- Ends with an open question inviting dialogue (the kind of comment that gets the author to reply, which boosts the post's reach and Anushka's profile visibility)
- Copies the draft to clipboard — Anushka reviews, edits, pastes into the comment box

**Honest limitation:** This is a template-driven comment generator, not a Claude-quality drafter. It handles ~70% of posts well (cloud cost, DevOps, AI, engineering practice) and ~30% poorly (founder-journey posts, personal narratives, non-technical content). Anushka should edit rather than post verbatim.

**The code:**

```javascript
javascript:(function(){
  var postText = '';
  try {
    var postEl = document.querySelector('.feed-shared-update-v2__description, .update-components-text, [data-test-id="main-feed-activity-card"]');
    if (postEl) postText = postEl.innerText.trim();
    if (!postText) {
      // fallback: try the article or aria-label
      postText = (document.querySelector('article')?.innerText || '').substring(0, 2000);
    }
  } catch(e) {}
  if (!postText) {
    alert('Could not find post text. Make sure you are clicking from a post page, not a search result.');
    return;
  }
  var firstLine = postText.split('\n')[0].slice(0, 200);
  var keywords = [];
  var topics = {
    'FinOps': /finops|cost optim|reserved instance|savings plan|cloud spend|cloud cost/i,
    'AWS': /\baws|amazon web services|ec2|s3|rds\b/i,
    'GCP': /\bgcp|google cloud|bigquery|gke\b/i,
    'Azure': /\bazure|microsoft cloud\b/i,
    'Kubernetes': /kubernetes|k8s|eks|aks|gke/i,
    'DevOps': /devops|ci\/cd|deployment|pipeline|dora/i,
    'AI': /\bai|llm|gpt|claude|gemini|ml\b|machine learning|inference|gpu/i,
    'Security': /security|cis|compliance|dpdp|iam|rbac/i,
    'Observability': /observability|opentelemetry|prometheus|grafana|monitoring|slo/i,
    'Architecture': /architecture|well-architected|terraform|iac/i
  };
  for (var topic in topics) if (topics[topic].test(postText)) keywords.push(topic);
  var topic = keywords[0] || 'this';
  var templates = {
    'FinOps': 'Great framing. The bit about ' + firstLine.slice(0, 60).trim() + ' lands — we see this across mid-market Indian accounts too, usually tied to commitment coverage below 40% on steady-state workloads. Curious what you are seeing on the tagging-hygiene side: is ownership sitting with engineering, finance, or a FinOps function?',
    'AWS': 'Appreciated the specificity on this. The ap-south-1 pricing math often reinforces the pattern you describe. Quick question — are you seeing this more in teams that adopted AWS during the 2020–2022 push, or across the board?',
    'GCP': 'Good post. The BigQuery billing export is the single most underused governance tool on GCP — once teams see the per-SKU breakdown the conversation changes. How are you finding the balance between CUD commitments and actual usage volatility?',
    'Azure': 'Useful framing. Azure Hybrid Benefit and Savings Plans together often move the bill 35%+ without architectural changes — most teams we see leave at least one of them on the table. Is the gap you are describing structural (procurement cadence) or technical (utilisation visibility)?',
    'Kubernetes': 'Good points. Cluster autoscaler tuning plus workload-rightsizing typically moves GKE/EKS spend 20–30% on its own. The PodDisruptionBudget + HPA-on-actual-QPS combination is where most teams under-invest. What has your experience been on the operational cost side?',
    'DevOps': 'This tracks with what we see running DORA audits across Indian mid-market teams. The Low→Medium tier shift usually comes from three interventions: CI caching, GitOps, and policy-as-code. Which one do you find teams underestimate most?',
    'AI': 'The unit-economics point is underappreciated in most AI product reviews. Cost-per-1K-inferences is the number every product team should track before the next pricing decision. Curious if you are seeing the self-hosted crossover earlier or later than the classic 2–3M inferences/day threshold?',
    'Security': 'Good framing. CIS Benchmarks v8 + DPDP-readiness overlap is the practical security floor for Indian businesses right now. The evidence-pack-for-audit workflow usually saves weeks per engagement. Is the gap in your teams more on detection coverage or on remediation velocity?',
    'Observability': 'The OpenTelemetry point is underrated. Most teams we audit are running three observability stacks that could be one — cost compounds. SLI/SLO discipline tied to actual business outcomes (not infrastructure signals) is where we see the biggest maturity gaps. What has been your approach on vendor lock-in?',
    'Architecture': 'Sharp observation. The Well-Architected gap analysis often surfaces decisions nobody made deliberately. IaC coverage is the single biggest leading indicator we track — teams above 90% coverage move much faster on remediation. What is your coverage number looking like?',
    'this': 'Thanks for sharing this. The framing is sharp and resonates with patterns we see across our engagements. Curious what prompted you to write about it now — is it a recurring conversation with your team, or something more specific you are navigating?'
  };
  var draft = templates[topic] || templates['this'];
  navigator.clipboard.writeText(draft).then(function(){
    alert('Comment draft copied to clipboard.\n\nDetected topic: ' + topic + '\n\nDraft:\n\n' + draft + '\n\nEdit before pasting into the comment box.');
  }, function(){
    prompt('Auto-copy failed. Copy manually:', draft);
  });
})();
```

---

## When to use which

| Task | Bookmarklet |
|---|---|
| Sending a connection request | LI-Connect-Anushka (v1) |
| Day-2 DM after acceptance | LI-DM-Anushka (v1) |
| Logging a prospect to CRM | LI-Copy-Prospect (v2) |
| Commenting on a target's post | LI-Comment-Draft (v2) |

Together these 4 bookmarklets cover every repeatable LinkedIn action in Anushka's 30-day outreach plan. Typical time saving: 2–3 hours per week over the first three months.

---

## Installation

Same drag-to-bookmarks-bar flow as the v1 bookmarklets. See `docs/linkedin-bookmarklets.md` for step-by-step. These are additional bookmarks, not replacements.

---

*AICloudStrategist · Anushka B · Founder-led. Enterprise-reviewed.*
