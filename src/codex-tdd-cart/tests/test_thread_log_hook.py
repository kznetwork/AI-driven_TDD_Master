import json
import os
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HOOK = ROOT / "log-thread.cjs"
CONFIG = ROOT / ".codex" / "hooks.json"
EVENTS = {
  "SessionStart",
  "SessionEnd",
  "PreToolUse",
  "PermissionRequest",
  "PostToolUse",
  "UserPromptSubmit",
  "PreCompact",
  "PostCompact",
  "SubagentStart",
  "SubagentStop",
  "Stop",
  "Interrupt",
}


def run_hook(tmp_path, payload):
  log_path = tmp_path / "logs" / "thread-events.jsonl"
  result = subprocess.run(
    ["node", str(HOOK)],
    input=payload,
    text=True,
    capture_output=True,
    cwd=tmp_path,
    env={**os.environ, "CODEX_THREAD_LOG_PATH": str(log_path)},
    check=False,
  )
  return result, log_path


def test_thread_hook_preserves_every_event_payload(tmp_path):
  events = [
    {
      "session_id": "thr_123",
      "turn_id": "turn_1",
      "hook_event_name": "PreToolUse",
      "tool_name": "Bash",
      "tool_use_id": "call_1",
      "tool_input": {"command": "printf 'hello'"},
    },
    {
      "session_id": "thr_123",
      "turn_id": "turn_1",
      "hook_event_name": "PostToolUse",
      "tool_name": "Bash",
      "tool_use_id": "call_1",
      "tool_input": {"command": "printf 'hello'"},
      "tool_response": {"output": "hello", "exit_code": 0},
    },
    {
      "session_id": "thr_other",
      "hook_event_name": "SessionEnd",
      "reason": "other",
    },
  ]

  for event in events:
    result, log_path = run_hook(tmp_path, json.dumps(event))
    assert result.returncode == 0, result.stderr
    assert result.stdout == ""

  records = [json.loads(line) for line in log_path.read_text(encoding="utf-8").splitlines()]
  assert [record["payload"] for record in records] == events
  assert [record["session_id"] for record in records] == [event["session_id"] for event in events]
  assert [record["event"] for record in records] == [event["hook_event_name"] for event in events]
  assert all(record["recorded_at"].endswith("Z") for record in records)


def test_thread_hook_rejects_invalid_input_without_logging(tmp_path):
  result, log_path = run_hook(tmp_path, "not json")

  assert result.returncode != 0
  assert "Invalid hook input" in result.stderr
  assert not log_path.exists()


def test_thread_hook_registers_all_supported_events():
  config = json.loads(CONFIG.read_text(encoding="utf-8"))

  assert EVENTS <= config["hooks"].keys()
  for event in EVENTS:
    handlers = config["hooks"][event]
    assert any(
      hook["type"] == "command" and hook["command"] == "node log-thread.cjs"
      for group in handlers
      for hook in group["hooks"]
    ), event
