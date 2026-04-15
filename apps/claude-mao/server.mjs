import http from 'node:http';
import { spawn } from 'node:child_process';
import crypto from 'node:crypto';

const PORT = Number(process.env.SHIM_PORT || 8080);
const TOKEN = process.env.SHIM_TOKEN || '';
// Cost telemetry only — Max subscription OAuth draws from plan rate limits, not $.
// Budget here acts as a safety circuit breaker against runaway loops.
const DAILY_RUN_CAP = Number(process.env.SHIM_DAILY_RUN_CAP || 500);

const usage = { day: new Date().toISOString().slice(0, 10), telemetryCostUsd: 0, runs: 0 };
function rollover() {
  const today = new Date().toISOString().slice(0, 10);
  if (today !== usage.day) { usage.day = today; usage.telemetryCostUsd = 0; usage.runs = 0; }
}

function json(res, status, body) {
  res.writeHead(status, { 'content-type': 'application/json' });
  res.end(JSON.stringify(body));
}

function readBody(req) {
  return new Promise((resolve, reject) => {
    const chunks = [];
    req.on('data', c => chunks.push(c));
    req.on('end', () => {
      const raw = Buffer.concat(chunks).toString('utf8');
      if (!raw) return resolve({});
      try { resolve(JSON.parse(raw)); } catch (e) { reject(e); }
    });
    req.on('error', reject);
  });
}

function authed(req) {
  if (!TOKEN) return true;
  const h = req.headers['authorization'] || '';
  return h === `Bearer ${TOKEN}`;
}

async function runClaude({ prompt, sessionId, maxTurns, resume, cwd }) {
  return new Promise((resolve) => {
    const args = [
      '-p', '--output-format', 'json',
      '--permission-mode', 'bypassPermissions',
    ];
    if (resume && sessionId) {
      args.push('--resume', sessionId);
    } else if (sessionId) {
      args.push('--session-id', sessionId);
    }
    if (maxTurns) args.push('--max-turns', String(maxTurns));
    const child = spawn('claude', args, {
      stdio: ['pipe', 'pipe', 'pipe'],
      cwd: cwd || '/home/mao',
    });
    let out = '', err = '';
    child.stdout.on('data', d => out += d);
    child.stderr.on('data', d => err += d);
    child.on('close', code => resolve({ code, out, err }));
    child.stdin.write(prompt);
    child.stdin.end();
  });
}

const server = http.createServer(async (req, res) => {
  rollover();
  if (req.method === 'GET' && req.url === '/healthz') {
    return json(res, 200, { ok: true, usage });
  }
  if (req.method === 'GET' && req.url === '/usage') {
    return json(res, 200, { usage, dailyRunCap: DAILY_RUN_CAP, note: 'costUsd is cosmetic telemetry; Max subscription draws from plan rate limits only' });
  }
  if (!authed(req)) return json(res, 401, { error: 'unauthorized' });
  if (req.method === 'POST' && req.url === '/run') {
    if (usage.runs >= DAILY_RUN_CAP) {
      return json(res, 429, { error: 'daily_run_cap_exceeded', usage, dailyRunCap: DAILY_RUN_CAP });
    }
    let body;
    try { body = await readBody(req); } catch { return json(res, 400, { error: 'bad_json' }); }
    const prompt = (body.prompt || '').trim();
    if (!prompt) return json(res, 400, { error: 'missing_prompt' });
    const resume = !!body.session_id;           // caller passed an existing id → resume
    const sessionId = body.session_id || crypto.randomUUID();
    const maxTurns = body.max_turns || 20;
    const runId = crypto.randomUUID();
    const started = Date.now();
    let { code, out, err } = await runClaude({ prompt, sessionId, maxTurns, resume });
    // Fallback: if resume failed because session disappeared, fall through to a fresh one
    if (resume && code !== 0 && /not found|no.*session|session.*does not/i.test(err)) {
      const fresh = crypto.randomUUID();
      ({ code, out, err } = await runClaude({ prompt, sessionId: fresh, maxTurns, resume: false }));
    }
    let parsed = null; try { parsed = JSON.parse(out); } catch {}
    const telemetryCost = parsed?.total_cost_usd || 0;
    usage.telemetryCostUsd += telemetryCost;
    usage.runs += 1;
    return json(res, 200, {
      run_id: runId,
      session_id: sessionId,
      exit_code: code,
      duration_ms: Date.now() - started,
      telemetry_cost_usd: telemetryCost,
      result: parsed?.result ?? null,
      raw: parsed,
      stderr: err.slice(0, 2000),
    });
  }
  json(res, 404, { error: 'not_found' });
});

server.listen(PORT, '0.0.0.0', () => {
  console.log(`[shim] listening on :${PORT} runCap=${DAILY_RUN_CAP}/day auth=${TOKEN ? 'on' : 'OFF'}`);
});
