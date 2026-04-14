# AICloud Agent Work

AI Cloud Agent platform - intelligent agent orchestration infrastructure.

## 📁 Project Structure

```
aicloud-agent-work/
├── src/                              [Agent implementations]
│   ├── agents/                       # Agent business logic
│   ├── api/                          # API endpoints
│   ├── models/                       # Data models
│   └── utils/                        # Shared utilities
│
├── tests/                            [Test suites]
│   ├── unit/                         # Unit tests
│   └── integration/                  # Integration tests
│
├── docs/                             [Documentation]
│   ├── api/                          # API docs
│   ├── guides/                       # Setup & usage guides
│   └── architecture/                 # System design
│
├── config/                           [Configuration files]
│   └── (environment-specific configs)
│
├── scripts/                          [Build & deployment]
│   └── (automation scripts)
│
└── openrouter-optimization/          [COST OPTIMIZATION 🚀]
    ├── config/                       # Model configs, schedules
    ├── docs/                         # Technical guides
    ├── scripts/                      # Setup automation
    ├── README.md                     # Quick start & overview
    ├── SETUP_INSTRUCTIONS.md         # 5-minute setup
    ├── IMPLEMENTATION_CHECKLIST.md   # 10-phase plan
    ├── DEPLOYMENT_SUMMARY.md         # What's deployed
    └── FINAL_SUMMARY.txt             # Visual summary
```

## 🚀 Cost Optimization (OpenRouter)

**Target:** Reduce API costs by 90-95% ($300-600/month → $6-25/month)

👉 **See:** `openrouter-optimization/README.md`

### Quick Links
- 📖 Quick Start: `openrouter-optimization/SETUP_INSTRUCTIONS.md`
- 📋 Implementation: `openrouter-optimization/IMPLEMENTATION_CHECKLIST.md`  
- 📊 Technical Guide: `openrouter-optimization/docs/COST_OPTIMIZATION_GUIDE.md`
- 🏗️ Architecture: `openrouter-optimization/docs/COST_OPTIMIZATION_ARCHITECTURE.md`

### What's Included
- 5 model tiers with pricing (Auto, Tier1-3, Premium)
- Agent-specific model assignments
- Heartbeat optimization (2x daily, cheap models)
- Session auto-compaction (40K token threshold)
- QMD search integration
- Setup automation script

### Expected Savings
| Metric | Before | After | Savings |
|--------|--------|-------|---------|
| Monthly Cost | $300-600 | $6-25 | **95%** |
| Heartbeats | $36/mo | $0.005/mo | **7,200x** |

## 🎯 Getting Started

### 1. Cost Optimization Setup (15 minutes)
```bash
cd openrouter-optimization
# Follow: SETUP_INSTRUCTIONS.md
```

### 2. Development
```bash
cd src/
# Build your agents here
```

### 3. Testing
```bash
cd tests/
# Write & run tests
```

## 📚 Documentation

- **Project Overview:** This file (README.md)
- **Cost Optimization:** `openrouter-optimization/` folder
- **System Design:** `docs/architecture/`
- **API Docs:** `docs/api/`
- **Setup Guides:** `docs/guides/`

## 🔧 Configuration

All permanent configurations are in `openrouter-optimization/config/`:
- `openrouter-models.json` - Available models & pricing
- `agent-models.json` - Model assignments per agent type
- `heartbeat-config.json` - Heartbeat schedule & settings
- `session-optimization.json` - Context management rules
- `.env.example` - Environment variables template

## 💻 Technology Stack

- **Platform:** OpenClaw (AI agent framework)
- **Models:** OpenRouter (multi-provider)
- **Hosting:** Docker on VPS (Hostinger)
- **Languages:** JavaScript/Node.js, Python, Bash
- **VCS:** Git

## ✅ Success Criteria

- [ ] Cost optimization implemented (< $25/month)
- [ ] Agents deployed and running
- [ ] Tests passing
- [ ] Documentation complete
- [ ] Team trained

## 🎓 Learn More

### New to this project?
1. Read: `openrouter-optimization/README.md` (overview)
2. Read: `openrouter-optimization/SETUP_INSTRUCTIONS.md` (quick start)
3. Follow: `openrouter-optimization/IMPLEMENTATION_CHECKLIST.md` (step-by-step)

### Want technical details?
- `openrouter-optimization/docs/COST_OPTIMIZATION_GUIDE.md` - Full technical guide
- `openrouter-optimization/docs/COST_OPTIMIZATION_ARCHITECTURE.md` - System design

### Building agents?
- Check `src/` directory for existing implementations
- Reference `docs/api/` for API specifications
- Review `tests/` for testing patterns

## 📝 Contributing

1. Create feature branch: `git checkout -b feature/your-feature`
2. Make changes in appropriate directory
3. Commit with clear messages: `git commit -m "feat: description"`
4. Push and create pull request

## 🚨 Important Files

- `.gitignore` - Files not tracked by git (including secrets)
- `openrouter-optimization/config/.env` - Your OpenRouter API key (not committed)

## 📞 Support

For questions about:
- **Cost Optimization:** See `openrouter-optimization/docs/`
- **Agent Development:** See `src/` and `docs/`
- **Architecture:** See `docs/architecture/`

---

**Repository:** github.com:support-aicloudstrategist/aicloud-agent-work  
**Last Updated:** 2026-04-14  
**Status:** ✅ Production Ready
