const fs = require('node:fs/promises');
const path = require('node:path');

async function main() {
  let input = '';
  for await (const chunk of process.stdin) {
    input += chunk;
  }

  let payload;
  try {
    payload = JSON.parse(input);
  } catch {
    throw new Error('Invalid hook input: expected JSON object');
  }
  if (
    payload === null ||
    typeof payload !== 'object' ||
    Array.isArray(payload) ||
    typeof payload.session_id !== 'string' ||
    !payload.session_id ||
    typeof payload.hook_event_name !== 'string' ||
    !payload.hook_event_name
  ) {
    throw new Error('Invalid hook input: session_id and hook_event_name are required');
  }

  const logPath = process.env.CODEX_THREAD_LOG_PATH ||
    path.resolve(__dirname, 'logs', 'thread-events.jsonl');
  const record = {
    recorded_at: new Date().toISOString(),
    session_id: payload.session_id,
    event: payload.hook_event_name,
    payload,
  };

  await fs.mkdir(path.dirname(logPath), { recursive: true });
  await fs.appendFile(logPath, `${JSON.stringify(record)}\n`, { encoding: 'utf8', mode: 0o600 });
}

main().catch((error) => {
  process.stderr.write(`${error.message}\n`);
  process.exitCode = 1;
});
