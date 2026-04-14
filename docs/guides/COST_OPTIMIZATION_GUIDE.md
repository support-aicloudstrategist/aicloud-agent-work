# Cost Optimization Guide - 90-95% Savings

This guide implements the complete cost optimization strategy from the finetune-openrouter-config.

## 🎯 Objectives

- Reduce API costs from $300-600/month → $6-25/month
- Maintain performance for complex tasks
- Automate cost-efficient routing
- Prevent context accumulation

## 📋 Setup Checklist

### Phase 1: OpenRouter Configuration

- [ ] Create `config/.env` from `config/.env.example`
- [ ] Add your `OPENROUTER_API_KEY`
- [ ] Verify config files are in place:
  - `config/openrouter-models.json`
  - `config/agent-models.json`
  - `config/heartbeat-config.json`
  - `config/session-optimization.json`

### Phase 2: Model Setup

#### Auto Mode (Recommended)
```bash
# Default to auto-routing for cost optimization
DEFAULT_MODEL=openrouter/auto
```

**Benefits:**
- Automatically selects cheapest model per task
- Simple tasks → Gemini 2.5 Flash (~$0.075/M input)
- Complex tasks → Deepseek/Sonnet as needed
- No manual switching required

#### Manual Mode (Optional)
Switch models for specific agents using agent-models.json:
- **Coding**: Claude Sonnet 4.5 (reliable for complex code)
- **Research**: Gemini 2.5 Flash (fast, cheap)
- **Reasoning**: Deepseek V3.1 (balanced)
- **Mail/Light**: Gemini 2.5 Flash (minimal cost)

### Phase 3: Heartbeat Optimization

**Current Setup:**
```json
{
  "schedule": ["09:00", "18:00"],
  "model": "openrouter/google/gemini-2.5-flash-lite",
  "lightContextMode": true,
  "isolatedSession": true
}
```

**What This Does:**
1. ✅ Runs only 2x daily (morning + evening) instead of every 30 minutes
2. ✅ Uses cheapest model (saves 50x vs Opus)
3. ✅ Light context mode = minimal token loading
4. ✅ Isolated sessions = no conversation history pollution
5. ✅ Silent hours = no runs 21:00-09:00

**Cost Impact:**
- 30-min interval + Opus 4.6 = ~$50/month
- 2x daily + Gemini 2.5 = ~$0.50/month
- **Savings: 100x** ✨

### Phase 4: Session Compaction

**The Silent Killer Problem:**
By message 50, you're paying for all 50 messages every time you send one.

**Solution:**
Auto-compact when context exceeds 40k tokens:
```json
{
  "autoCompactThreshold": "40k",
  "compactionStrategy": "summarize"
}
```

**Manual Command:**
```
/compact
```

**Before/After:**
- Before: 55,000 tokens
- After: 23,000 tokens
- **Savings: 58%** per session

### Phase 5: QMD Search Installation

QMD = Quick Markdown Diff Search. Local search instead of full-context loading.

```bash
# Install QMD
git clone https://github.com/your-repo/qmd.git
npm install

# Add to AGENTS.md:
# Before answering anything about prior work, decisions, or todos:
# 1. Search MEMORY.md via QMD
# 2. Load specific lines with memory_get
```

**Impact:**
- Memory search: 5,000 tokens (full-context) → 50 tokens (QMD)
- **Savings: 100x per search** ✨

## 💰 Cost Breakdown

### Monthly Estimates (30 heartbeats + 50 main chats)

**UNOPTIMIZED (Opus 4.6 default):**
```
Heartbeats (30 × 30min intervals):
  30 heartbeats × 5K tokens × $5/M = $0.75/day = $22/month
Main chats (50 messages × 25K context avg):
  50 × 25K × $5/M = $6.25/day = $187/month
TOTAL: ~$210/month
```

**OPTIMIZED (Auto-routing + 2x daily heartbeats + compaction):**
```
Heartbeats (2 × daily × cheap model):
  2 × 1K tokens × $0.075/M = $0.00015/day = $0.005/month
Main chats (50 messages × 10K context avg):
  50 × 10K × $0.27/M (avg) = $0.135/day = $4/month
TOTAL: ~$4/month
```

**Savings: 52x = 98% reduction** 🎉

## 🔧 Implementation Steps

### 1. Environment Setup
```bash
cp config/.env.example config/.env
# Edit .env with your OPENROUTER_API_KEY
```

### 2. Verify Configurations
```bash
# Check all configs are valid JSON
for f in config/*.json; do jq . "$f" > /dev/null && echo "$f: OK"; done
```

### 3. Apply to OpenClaw Instance
In your OpenClaw Telegram chat:
```
/new
(or in existing session)

Tell the bot:
"I want to set up cost optimization. Here's my OpenRouter API key: [key]
Please configure:
1. Auto-routing to openrouter/auto
2. Heartbeats 2x daily (9 AM, 6 PM) with Gemini 2.5
3. Auto-compact at 40K tokens
4. Light context mode + isolated sessions
5. QMD search for memory"
```

### 4. Set Permanent Defaults

In OpenClaw config (usually `~/.config/openclaw/config.json` or via Hostinger dashboard):
```json
{
  "agents": {
    "default_model": "openrouter/auto",
    "fallback_model": "openrouter/google/gemini-2.5-flash-lite"
  },
  "heartbeat": {
    "enabled": true,
    "schedule": ["09:00", "18:00"],
    "model": "openrouter/google/gemini-2.5-flash-lite"
  }
}
```

### 5. Verify It's Working

After setup, check:
```
/status
```

Should show:
- ✅ Model: openrouter/auto (or specific model if set)
- ✅ Heartbeat: Running on schedule (not interval)
- ✅ Context management: Compaction enabled

## ⚠️ Important Notes

1. **API Key Security**: Add to `.env`, never commit to git
2. **Gradual Rollout**: Test new models on research tasks first
3. **Performance Baseline**: Document costs before/after
4. **Critical Tasks**: Reserve Opus 4.6 for truly important reasoning

## 📊 Monthly Cost Monitoring

Track actual usage:
```bash
# Check OpenRouter billing dashboard regularly
# Monitor session tokens with /status command
# Review memory compaction logs
```

## 🚀 Advanced: Per-Agent Configuration

Once optimized globally, you can fine-tune individual agents:

```javascript
// For a coding agent spawned with sessions_spawn:
{
  "model": "openrouter/anthropic/claude-sonnet-4.5",
  "lightContext": true,
  "timeout": 120
}

// For research/lightweight tasks:
{
  "model": "openrouter/google/gemini-2.5-flash-lite",
  "lightContext": true
}
```

## ✅ Success Criteria

Your setup is optimized when:
- [ ] Default model is auto-routing or budget model
- [ ] Heartbeats run 2x daily, not constantly
- [ ] Auto-compact triggers at 40K tokens
- [ ] Memory searches use QMD, not full-context
- [ ] Monthly bill is <$25
- [ ] Performance is acceptable for all use cases

---

**Reference:** finetune-openrouter-config.txt.txt from GitHub
**Last Updated:** 2026-04-14
