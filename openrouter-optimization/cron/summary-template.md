# Hourly Summary Template

Use this format for generating hourly session summaries:

```
📊 HOURLY SESSION SUMMARY

⏰ Period: {HOUR_START} - {HOUR_END}
📍 Timezone: Asia/Calcutta

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

💰 TOKEN USAGE & COST BY MODEL

| Model            | Input  | Output | In Cost | Out Cost | Total  |
|------------------|--------|--------|---------|----------|--------|
| Haiku 4.5        | {IN}   | {OUT}  | ${COST} | ${COST}  | ${TOT} |
| Gemini 2.5 Flash | {IN}   | {OUT}  | ${COST} | ${COST}  | ${TOT} |
| Sonnet 4.5       | {IN}   | {OUT}  | ${COST} | ${COST}  | ${TOT} |
| Opus 4.6         | {IN}   | {OUT}  | ${COST} | ${COST}  | ${TOT} |
| TOTAL            | {IN}   | {OUT}  | ${COST} | ${COST}  | ${TOT} |

📊 Cache Efficiency:
├─ Cached tokens: {CACHED} ({HIT_RATE}% hit rate)
├─ Cost savings: ${SAVED}
└─ Net cost: ${NET_COST}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📝 WORK SUMMARY

{ACTIVITY_SUMMARY}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Next Report: {NEXT_HOUR}
```

## Notes:
- Skip report if no activity detected (idle hour)
- Use Gemini 2.5 Flash for generation (cheapest)
- Keep summary brief (< 500 tokens)
- Only include models that were actually used
