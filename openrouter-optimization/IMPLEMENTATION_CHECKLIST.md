# 🚀 Cost Optimization Implementation Checklist

Complete this checklist to ensure 95% cost savings are achieved.

## Phase 1: Foundation (Day 1-2)

### Configuration Files
- [x] `config/openrouter-models.json` - Model definitions & costs
- [x] `config/agent-models.json` - Agent-specific model mappings
- [x] `config/heartbeat-config.json` - Heartbeat schedule & settings
- [x] `config/session-optimization.json` - Session & memory settings
- [x] `config/.env.example` - Environment variable template
- [x] `config/.env` - Created (needs API key)

### Documentation
- [x] `docs/guides/COST_OPTIMIZATION_GUIDE.md` - Comprehensive implementation guide
- [x] `docs/architecture/COST_OPTIMIZATION_ARCHITECTURE.md` - System design
- [x] `SETUP_INSTRUCTIONS.md` - Quick setup steps
- [x] `scripts/setup-cost-optimization.sh` - Automated setup script

### Initial Steps
- [ ] **Copy OPENROUTER_API_KEY to `config/.env`**
  ```bash
  # Get your API key from https://openrouter.ai/keys
  # Edit config/.env and set OPENROUTER_API_KEY=your_key_here
  ```
- [ ] Run setup script to validate configs
  ```bash
  bash scripts/setup-cost-optimization.sh
  ```

## Phase 2: OpenRouter Integration (Day 2-3)

### In Your OpenClaw Instance (Telegram/Discord):

- [ ] **Tell bot to set up OpenRouter**
  ```
  I want to set up cost optimization with OpenRouter.
  My API key is: [paste from config/.env]
  
  Please configure:
  1. Set default model to openrouter/auto
  2. Register these models:
     - openrouter/google/gemini-2.5-flash-lite
     - openrouter/deepseek/deepseek-chat-v3.1
     - openrouter/anthropic/claude-sonnet-4.5
     - openrouter/anthropic/claude-opus-4-6
  ```

- [ ] **Verify models are loaded**
  ```
  /models
  ```
  Should show: openrouter/auto and 4 other models

- [ ] **Test auto-routing**
  Ask a simple question and check:
  ```
  Which model are you using?
  ```
  Should respond: `openrouter/auto` (or Gemini 2.5 Flash if auto selected it)

## Phase 3: Heartbeat Optimization (Day 3-4)

### Configure Scheduled Heartbeats

- [ ] **Set up 2x daily heartbeats (NOT intervals)**
  ```
  Please set up heartbeats:
  1. Morning: 09:00 Asia/Calcutta
     - Check: emails, calendar, urgent items
  2. Evening: 18:00 Asia/Calcutta
     - Check: summary, day review
  
  Settings:
  - Model: openrouter/google/gemini-2.5-flash-lite
  - Light context mode: ON
  - Isolated session: ON
  - Max tokens: 2000
  - Silent hours: 21:00-09:00
  
  Use cron schedule, NOT interval-based (important!)
  ```

- [ ] **Verify heartbeat schedule**
  ```
  /heartbeat status
  ```
  Should show: Schedule-based (09:00, 18:00), not "every 30 minutes"

- [ ] **Confirm heartbeat model**
  Should be using `openrouter/google/gemini-2.5-flash-lite` (cheap)

## Phase 4: Session Optimization (Day 4-5)

### Enable Auto-Compaction

- [ ] **Configure session compaction**
  ```
  Please set up automatic session compaction:
  - Threshold: 40,000 tokens
  - Strategy: Summarize old messages
  - Trigger: Automatic when exceeded
  - Max output tokens: 2000
  
  Reference: docs/guides/COST_OPTIMIZATION_GUIDE.md
  ```

- [ ] **Test manual compaction**
  After a conversation:
  ```
  /compact
  ```
  Should reduce context size significantly (e.g., 55K → 23K)

- [ ] **Monitor context size**
  ```
  /status
  ```
  Should show context usage below 40K tokens most of the time

## Phase 5: Memory Optimization (Day 5-6)

### QMD Installation (Optional but Recommended)

- [ ] **Ask bot to install QMD search**
  ```
  Can you install QMD (Quick Markdown Search)?
  Repository: https://github.com/your-repo/qmd
  
  This will make memory searches 100x more efficient.
  Please add to AGENTS.md for memory lookups.
  ```

- [ ] **Test QMD search**
  Try asking about something from past memory:
  ```
  What did I tell you about OpenRouter?
  ```
  Should use QMD (fast, cheap) instead of full-context search

- [ ] **Verify memory configuration**
  Check AGENTS.md includes QMD search before memory_search

## Phase 6: Agent-Specific Models (Day 6-7)

### Deploy Per-Agent Configurations

- [ ] **Assign models to specialized agents**
  
  For coding tasks:
  ```
  spawn_agent(type="coding", model="openrouter/anthropic/claude-sonnet-4.5")
  ```
  
  For research tasks:
  ```
  spawn_agent(type="research", model="openrouter/google/gemini-2.5-flash-lite")
  ```

- [ ] **Document agent assignments**
  Update `config/agent-models.json` as you create agents

- [ ] **Test specialized agents**
  Confirm each uses appropriate model via `/status`

## Phase 7: Monitoring & Validation (Week 2)

### Establish Cost Baseline

- [ ] **Note pre-optimization costs**
  - Check OpenRouter billing dashboard
  - Screenshot current spending
  - Target: $300-600/month (likely current)

- [ ] **Monitor first week of optimization**
  - Check daily costs on OpenRouter dashboard
  - Track token usage per session
  - Verify no regressions in performance

- [ ] **Review weekly report**
  - Expected: 50-70% reduction in week 1
  - Check heartbeat frequency (should be exactly 2x/day)
  - Verify context compaction is working

### Expected Costs

```
Week 1 (partial transition):
- Target: $150-300/month if fully optimized

Week 2-4 (full optimization):
- Target: $6-25/month
- Your likely range: $12-18/month

Monthly savings target:
- If previous: $300-600/month → NOW: $6-25/month
- Savings: 95%+
```

## Phase 8: Production Hardening (Week 2-3)

### Performance Validation

- [ ] **Test complex reasoning tasks**
  - Verify Sonnet 4.5 models perform well for coding
  - Check Deepseek works for multi-step reasoning
  - Confirm Gemini handles light tasks efficiently

- [ ] **Monitor latency**
  - OpenRouter auto may add slight routing latency
  - Should be <2 seconds per request
  - If too slow: Switch to manual routing

- [ ] **Validate cost/performance tradeoff**
  - Is the 95% cost reduction acceptable?
  - Any tasks degraded too much?
  - Adjust agent models if needed

### Establish Monitoring

- [ ] **Set up cost alerts**
  - OpenRouter dashboard alerts if usage spikes
  - Alert at: $2/month (warns of runaway usage)

- [ ] **Weekly cost review**
  - Every Monday: Check spending
  - Compare to target ($6-25/month)
  - Identify anomalies

- [ ] **Monthly documentation**
  - Update MEMORY.md with cost figures
  - Document any performance changes
  - Record optimization lessons learned

## Phase 9: Scaling (Week 3-4)

### Multi-Environment Deployment

- [ ] **Dev environment**
  - Same config as production
  - Test new agents here first

- [ ] **Staging environment** (if applicable)
  - Full load testing with real models
  - Cost projection for scaled usage

- [ ] **Production environment**
  - All systems verified
  - Monitoring active
  - Alerts configured

### Team Enablement

- [ ] **Document for team members**
  - Share `docs/guides/COST_OPTIMIZATION_GUIDE.md`
  - Run training: "How to use agent models efficiently"
  - Show cost dashboard

- [ ] **Create agent templates**
  - Coding agent template (Sonnet 4.5)
  - Research agent template (Gemini 2.5)
  - General agent template (auto-routing)

## Phase 10: Success Metrics (Ongoing)

### Track These Numbers

- [ ] **Monthly OpenRouter bill**
  - Pre-optimization: $300-600
  - Post-optimization target: $6-25
  - Win condition: < $30/month

- [ ] **Context compaction efficiency**
  - Track: How many times per day context compacts
  - Expected: 2-5 times per day
  - Healthy if: < 50K tokens before compact

- [ ] **Heartbeat token usage**
  - Per heartbeat: < 2000 tokens
  - Cost per heartbeat: < $0.01
  - 60 heartbeats/month = < $0.60

- [ ] **Model distribution**
  - Gemini 2.5: 70% of requests (cheap)
  - Deepseek: 20% of requests (medium)
  - Sonnet/Opus: 10% of requests (for complex tasks)

- [ ] **Performance satisfaction**
  - Is feature parity maintained? (Yes/No)
  - Any user complaints? (None expected)
  - System stability? (Should be same or better)

## Troubleshooting Guide

### Problem: Costs not decreasing
**Solution:**
1. Verify default model is actually `openrouter/auto`
2. Check heartbeat frequency (should be 2x/day, not every 30 min)
3. Confirm auto-compaction is triggering (check session logs)

### Problem: Slow responses
**Solution:**
1. OpenRouter auto may add routing latency
2. Switch to specific models: Sonnet for complex, Gemini for simple
3. Check OpenRouter API status

### Problem: Quality degradation
**Solution:**
1. Gemini 2.5 Flash may be used too much
2. Assign important tasks to Sonnet 4.5 via agent-models.json
3. Test with Deepseek V3.1 (good balance)

### Problem: Memory searches timing out
**Solution:**
1. Install QMD if not done
2. Reduce memory file sizes (move to daily files)
3. Use memory_search more sparingly

## Completion Checklist

- [ ] All config files created ✓
- [ ] OpenRouter API key added to .env
- [ ] Default model set to openrouter/auto
- [ ] Heartbeats configured (2x daily, cheap model)
- [ ] Auto-compaction enabled
- [ ] QMD search installed
- [ ] Agent models assigned
- [ ] Costs tracked and validated
- [ ] Team trained
- [ ] Production running

## Expected Timeline

| Phase | Duration | Status |
|-------|----------|--------|
| Setup | 1-2 days | ✓ DONE |
| Integration | 1-2 days | → NOW |
| Optimization | 3-5 days | → NEXT |
| Validation | 1 week | |
| Hardening | 1 week | |
| Scaling | 1 week | |
| **Total** | **4 weeks** | ~95% savings achieved |

---

**Start Date:** 2026-04-14
**Target Completion:** 2026-05-12
**Expected Savings:** 90-95% ($300+ to <$25/month)

🚀 Ready? Start with Phase 1 and update this checklist as you go!
