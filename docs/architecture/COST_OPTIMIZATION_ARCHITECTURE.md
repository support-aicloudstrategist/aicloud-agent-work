# Cost Optimization Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│         OpenClaw Agent Instance (Docker/VPS)            │
├─────────────────────────────────────────────────────────┤
│                                                           │
│  ┌──────────────────────────────────────────────────┐   │
│  │          Agent Router                             │   │
│  │  (Determines which model to use)                  │   │
│  └─────────────────┬──────────────────────────────┘   │
│                    │                                    │
│        ┌───────────┼───────────┐                       │
│        │           │           │                       │
│        ▼           ▼           ▼                       │
│  ┌─────────┐ ┌─────────┐ ┌──────────┐                │
│  │ OpenRouter Auto    │ │ Agent    │ │ Heartbeat    │
│  │ (Smart routing)    │ │ Models   │ │ Scheduler    │
│  └─────────┘ └─────────┘ └──────────┘                │
│        │           │           │                       │
│        └───────────┼───────────┘                       │
│                    │                                    │
│        ┌───────────▼──────────────┐                   │
│        │  Model Multiplexer       │                   │
│        │  (Routes to cheapest)    │                   │
│        └───────────┬──────────────┘                   │
│                    │                                    │
│        ┌───────────▼────────────────────────────────┐ │
│        │     OpenRouter API Bridge                   │ │
│        ├────────────────────────────────────────────┤ │
│        │ Available Models:                           │ │
│        │ • openrouter/auto (SMART - default)        │ │
│        │ • Gemini 2.5 Flash (tier1 - $0.075/M)     │ │
│        │ • Deepseek V3.1 (tier2 - $0.27/M)         │ │
│        │ • Claude Sonnet 4.5 (tier3 - $3/M)        │ │
│        │ • Claude Opus 4.6 (premium - $5/M)        │ │
│        └────────────────────────────────────────────┘ │
│                    │                                    │
│        ┌───────────▼────────────────────────────────┐ │
│        │  Session & Context Manager                 │ │
│        ├────────────────────────────────────────────┤ │
│        │ • Context Size: 50K max                    │ │
│        │ • Auto-compact at 40K                      │ │
│        │ • Strategy: Summarize old messages         │ │
│        │ • Output limit: 2K tokens                  │ │
│        └────────────────────────────────────────────┘ │
│                    │                                    │
│        ┌───────────▼────────────────────────────────┐ │
│        │  Memory & Search System                    │ │
│        ├────────────────────────────────────────────┤ │
│        │ • QMD Search (efficient markdown search)   │ │
│        │ • MEMORY.md (curated long-term memory)    │ │
│        │ • memory/YYYY-MM-DD.md (daily logs)       │ │
│        └────────────────────────────────────────────┘ │
│                    │                                    │
│        ┌───────────▼────────────────────────────────┐ │
│        │  Heartbeat Scheduler (Cron)                │ │
│        ├────────────────────────────────────────────┤ │
│        │ • 09:00 - Morning check                    │ │
│        │   (Email, calendar, urgent items)          │ │
│        │ • 18:00 - Evening check                    │ │
│        │   (Summary, day review)                    │ │
│        │ • Silent: 21:00-09:00                      │ │
│        │ • Model: Gemini 2.5 Flash (cheap)         │ │
│        │ • Context: Light mode (2K max)            │ │
│        └────────────────────────────────────────────┘ │
│                                                           │
└─────────────────────────────────────────────────────────┘
                         │
                         ▼
          ┌──────────────────────────────┐
          │   OpenRouter Cloud Services  │
          │  (Model Selection & Routing) │
          └──────────────────────────────┘
```

## Cost Flow Analysis

### Traditional Setup (❌ Expensive)
```
Every message loaded with ALL previous messages
Message 1: 1K tokens
Message 2: 1K + 1K = 2K tokens
Message 3: 1K + 2K = 3K tokens
...
Message 50: 50K tokens per message

Daily cost: 50 messages × 25K avg × $5/M input = $6.25/day = $187/month
```

### Optimized Setup (✅ Cheap)
```
Auto-compaction every 40K tokens
Message 1-10: Normal accumulation
  Tokens: 10K
Message 11-20: After compaction → Summarized
  Tokens: 8K (compressed from 20K)
Message 21-30: After compaction → Summarized
  Tokens: 8K (compressed from 30K)
...
Maximum context never exceeds 10K

Daily cost: 50 messages × 10K avg × $0.27/M avg = $0.135/day = $4/month
```

## Configuration Hierarchy

```
System Level (Permanent)
├── config/openrouter-models.json
│   └── Available models, costs, tiers
├── config/agent-models.json
│   └── Agent → Model assignments
├── config/heartbeat-config.json
│   └── Schedule, frequency, settings
├── config/session-optimization.json
│   └── Context management, compaction rules
└── config/.env
    └── API keys, secrets, environment vars

Session Level (Runtime)
├── Heartbeat sessions (isolated, cheap)
├── Main sessions (auto-routing)
└── Specialized agents (per agent-models.json)
```

## Model Selection Decision Tree

```
           ┌─────────────────────┐
           │  Incoming Prompt    │
           └──────────┬──────────┘
                      │
           ┌──────────▼──────────┐
           │ Use Auto Mode?      │
           └──┬─────────────┬────┘
              │             │
              ▼             ▼
            YES            NO
             │              │
             ▼              ▼
        ┌─────────┐    ┌──────────────┐
        │ OpenRouter   │ Check agent- │
        │ Auto Routing │ models.json  │
        │ (smart!)     │              │
        └─────────┘    └──────────────┘
             │              │
    ┌────────┼──────────────┼─────────┐
    │        │              │         │
    ▼        ▼              ▼         ▼
  Simple  Complex       Agent   Special
   task    task         type    config
    │        │           │        │
    ▼        ▼           ▼        ▼
  Gemini  Deepseek   Per-agent  Override
  2.5    V3.1      settings    model
  Flash             assignment

Result: Most cost-effective model selected
```

## Token Lifecycle

### Without Optimization
```
Memory Accumulation Problem:
┌─────────────────────────────────────────────────────┐
│  SESSION START                                      │
├─────────────────────────────────────────────────────┤
│ Message 1: 5K tokens                                │
│ Message 2: 5K old + 5K new = 10K tokens            │
│ Message 3: 10K old + 5K new = 15K tokens           │
│ Message 4: 15K old + 5K new = 20K tokens           │
│ Message 5: 20K old + 5K new = 25K tokens           │
│ ...                                                  │
│ Message 50: 245K old + 5K new = 250K tokens        │
│                                                      │
│ Total tokens sent in conversation: 6,275K          │
│ Cost: $31.375 (at $5/M)                            │
└─────────────────────────────────────────────────────┘
```

### With Optimization (Auto-Compaction)
```
Smart Memory Management:
┌──────────────────────────────────────────────────────┐
│  SESSION START                                       │
├──────────────────────────────────────────────────────┤
│ Message 1-10: 5K → 10K → 15K ... 50K                │
│              [COMPACTION TRIGGERS AT 40K]            │
│ ↓ Summarized context: 20K (compressed from 50K)    │
│ Message 11-20: 20K → 25K → 30K ... 60K             │
│               [COMPACTION TRIGGERS AT 40K]           │
│ ↓ Summarized context: 18K (compressed from 60K)    │
│ Message 21-50: Max context never exceeds 40K        │
│                                                       │
│ Total tokens sent in conversation: ~1,200K          │
│ Cost: $3.24 (at $2.70/M average)                   │
│                                                       │
│ SAVINGS: 80% vs. no optimization                    │
└──────────────────────────────────────────────────────┘
```

## QMD Search Efficiency

### Traditional Memory Search
```
Query: "Remember my OpenRouter API key?"

System loads:
├── MEMORY.md (50KB)
├── memory/2026-04-14.md (30KB)
├── memory/2026-04-13.md (25KB)
├── memory/2026-04-12.md (20KB)
└── 100+ other memory files (500KB)

Total: 625KB loaded into context
Token cost: ~15,000 tokens per search
```

### QMD Search (Optimized)
```
Query: "Remember my OpenRouter API key?"

QMD:
├── Index all .md files locally (no token cost)
├── Search for "OpenRouter API"
├── Return: 3 matching lines only

Total: ~200 bytes loaded into context
Token cost: ~5 tokens per search

SAVINGS: 3000x more efficient!
```

## Cost Projections

### Scenario 1: Development Team (5 agents)

**Unoptimized:**
- 5 agents × $300/month = $1,500/month
- 5 heartbeats × $50/month = $250/month
- Memory searches × $100/month = $100/month
- **TOTAL: $1,850/month**

**Optimized:**
- 5 agents × $4/month = $20/month
- 5 heartbeats × $0.50/month = $2.50/month
- Memory searches × $0.10/month = $0.50/month
- **TOTAL: $22.50/month**

**SAVINGS: 98% = $1,827.50/month** 🎉

### Scenario 2: Enterprise Deployment (50 agents)

**Unoptimized:**
- 50 agents × $300/month = $15,000/month
- 50 heartbeats × $50/month = $2,500/month
- Advanced features & memory = $1,000/month
- **TOTAL: $18,500/month**

**Optimized:**
- 50 agents × $4/month = $200/month
- 50 heartbeats × $0.50/month = $25/month
- Advanced features & memory = $5/month
- **TOTAL: $230/month**

**SAVINGS: 98% = $18,270/month** 🎉

## Implementation Timeline

### Week 1: Foundation
- [ ] Day 1: Config files created (DONE)
- [ ] Day 2: OpenRouter API key integrated
- [ ] Day 3: Auto-routing tested with sample prompts
- [ ] Day 4: Heartbeat scheduling configured
- [ ] Day 5: Initial cost baseline established

### Week 2: Optimization
- [ ] Day 1: Session compaction enabled
- [ ] Day 2: QMD search installed
- [ ] Day 3: Agent-specific models configured
- [ ] Day 4: Memory optimization applied
- [ ] Day 5: First cost reduction metrics

### Week 3: Validation
- [ ] Day 1-3: Performance testing
- [ ] Day 4-5: Cost validation against baseline

### Week 4: Production
- [ ] All systems live
- [ ] Monitoring dashboard active
- [ ] Monthly cost tracking begins

---

**Expected Result:** 90-95% cost reduction within 1 month ✨
