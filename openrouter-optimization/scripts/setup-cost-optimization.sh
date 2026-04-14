#!/bin/bash
set -e

echo "🚀 AICloud Cost Optimization Setup"
echo "===================================="
echo ""

# Color codes
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Step 1: Verify configurations
echo -e "${YELLOW}Step 1: Verifying configuration files...${NC}"
CONFIG_DIR="../config"
REQUIRED_FILES=(
  "openrouter-models.json"
  "agent-models.json"
  "heartbeat-config.json"
  "session-optimization.json"
  ".env.example"
)

for file in "${REQUIRED_FILES[@]}"; do
  if [ -f "$CONFIG_DIR/$file" ]; then
    echo -e "${GREEN}✓${NC} $file found"
  else
    echo -e "${RED}✗${NC} $file NOT found - CRITICAL"
    exit 1
  fi
done

# Step 2: Create .env if doesn't exist
echo ""
echo -e "${YELLOW}Step 2: Setting up environment file...${NC}"
if [ ! -f "$CONFIG_DIR/.env" ]; then
  cp "$CONFIG_DIR/.env.example" "$CONFIG_DIR/.env"
  echo -e "${GREEN}✓${NC} Created $CONFIG_DIR/.env"
  echo -e "${YELLOW}⚠️  IMPORTANT: Edit $CONFIG_DIR/.env and add your OPENROUTER_API_KEY${NC}"
else
  echo -e "${GREEN}✓${NC} $CONFIG_DIR/.env already exists"
fi

# Step 3: Validate JSON
echo ""
echo -e "${YELLOW}Step 3: Validating JSON configurations...${NC}"
for file in "${REQUIRED_FILES[@]}"; do
  if [[ $file == *.json ]]; then
    if jq . "$CONFIG_DIR/$file" > /dev/null 2>&1; then
      echo -e "${GREEN}✓${NC} $file is valid JSON"
    else
      echo -e "${RED}✗${NC} $file has invalid JSON"
      exit 1
    fi
  fi
done

# Step 4: Create logs directory
echo ""
echo -e "${YELLOW}Step 4: Setting up logging...${NC}"
mkdir -p logs
echo -e "${GREEN}✓${NC} logs/ directory ready"

# Step 5: Create setup documentation
echo ""
echo -e "${YELLOW}Step 5: Generating documentation...${NC}"

cat > SETUP_INSTRUCTIONS.md << 'INSTRUCTIONS'
# 🚀 Cost Optimization Setup - Final Steps

Your configuration files are ready. Now implement in OpenClaw:

## Quick Setup (5 minutes)

### 1. Add OpenRouter API Key
```bash
cat config/.env
# Copy your OPENROUTER_API_KEY value
```

### 2. In OpenClaw (Telegram/Discord)
Tell your bot:
```
I want to set up cost optimization with OpenRouter.
My API key is: [paste from .env]

Please configure:
1. Set default model to openrouter/auto (auto-routing)
2. Configure heartbeats: 2x daily at 09:00 and 18:00 with Gemini 2.5 Flash
3. Enable auto-compaction at 40K tokens
4. Set light context mode on heartbeats
5. Enable QMD search for memory lookups

Reference my configs in:
- config/openrouter-models.json
- config/agent-models.json
- config/heartbeat-config.json
- config/session-optimization.json
```

### 3. Verify Setup
After bot confirms, check status:
```
/status
```

Should show:
- Model: openrouter/auto
- Heartbeat: Schedule-based (not interval)
- Context management: Enabled

## Expected Savings

**Before:** $300-600/month (Opus 4.6 default + constant heartbeats)
**After:** $6-25/month (auto-routing + 2x daily heartbeats)
**Savings: 95%+** 🎉

## Key Configurations

### Model Routing
- **openrouter/auto** - Automatically selects cheapest model per task (DEFAULT)
- **Gemini 2.5 Flash** - Research, light tasks (~$0.075/M input tokens)
- **Deepseek V3.1** - General reasoning, moderate complexity
- **Claude Sonnet 4.5** - Complex reasoning, code generation
- **Claude Opus 4.6** - RESERVED for critical tasks only

### Heartbeat Settings
- Schedule: 09:00 AM & 6:00 PM (Asia/Calcutta timezone)
- Model: Gemini 2.5 Flash (cheap)
- Light context mode: ON
- Isolated session: ON
- Silent hours: 21:00-09:00 (no late-night checks)

### Session Management
- Auto-compact threshold: 40K tokens
- Max output: 2,000 tokens
- Memory search: QMD (not full-context)

## Monitoring

Track your savings:
1. Check OpenRouter billing dashboard (openrouter.ai)
2. Monitor with `/status` in OpenClaw (shows tokens per session)
3. Review compaction metrics (how often context compacts)

## Troubleshooting

**Q: Bot can't find openrouter models?**
- Ensure OPENROUTER_API_KEY is set correctly in .env
- Check OpenRouter account status

**Q: Heartbeats still running too often?**
- Confirm schedule-based config is applied (not interval-based)
- Check "schedule" in heartbeat-config.json

**Q: Performance degraded with cheap models?**
- Use manual agent-models.json for critical tasks
- Assign Claude Sonnet 4.5 to coding-agent

## Reference Documentation

- `docs/guides/COST_OPTIMIZATION_GUIDE.md` - Comprehensive guide
- `config/openrouter-models.json` - Available models & costs
- `config/agent-models.json` - Agent-specific model assignments
- `config/heartbeat-config.json` - Heartbeat schedule & optimization
- `config/session-optimization.json` - Session/memory settings

---

**You're all set!** Your infrastructure is now optimized for 95% cost savings. 🚀
INSTRUCTIONS

echo -e "${GREEN}✓${NC} Setup instructions created"

# Step 6: Summary
echo ""
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo -e "${GREEN}✓ SETUP COMPLETE${NC}"
echo -e "${GREEN}════════════════════════════════════════${NC}"
echo ""
echo "Next steps:"
echo "1. Edit config/.env with your OPENROUTER_API_KEY"
echo "2. Read SETUP_INSTRUCTIONS.md"
echo "3. Configure OpenClaw with the settings"
echo "4. Monitor savings!"
echo ""
echo "Configuration files ready:"
echo "  • config/openrouter-models.json"
echo "  • config/agent-models.json"
echo "  • config/heartbeat-config.json"
echo "  • config/session-optimization.json"
echo "  • config/.env (needs API key)"
echo ""
echo "Documentation:"
echo "  • docs/guides/COST_OPTIMIZATION_GUIDE.md"
echo "  • SETUP_INSTRUCTIONS.md"
echo ""
