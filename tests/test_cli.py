import json
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from pathlib import Path
import subprocess
import sys
import tempfile
from threading import Thread
import unittest


ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples" / "candidates.json"


class ModelEndpoint(BaseHTTPRequestHandler):
    def do_POST(self):
        body = json.loads(
            self.rfile.read(int(self.headers["Content-Length"]))
        )
        self.server.calls.append((self.path, body))
        prompt = body["messages"][0]["content"]
        content = "Reading card"
        if "仅输出 JSON" in prompt:
            content = json.dumps({
                "summary": "Screened candidates",
                "papers": [{"paper_id": "example-device", "reason": "Matches the task"}],
            })
        response = {"choices": [{"message": {"content": content}}]}
        self.send_response(200)
        self.send_header("Content-Type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response).encode("utf-8"))

    def log_message(self, *args):
        pass


class CliTest(unittest.TestCase):
    def test_standalone_and_combined_modes(self):
        server = HTTPServer(("127.0.0.1", 0), ModelEndpoint)
        self.addCleanup(server.server_close)
        server.calls = []
        thread = Thread(target=server.serve_forever, daemon=True)
        thread.start()
        self.addCleanup(thread.join, 5)
        self.addCleanup(server.shutdown)
        with tempfile.TemporaryDirectory() as temp:
            selected = Path(temp) / "selected.json"

            def run(mode, source, *options):
                result = subprocess.run(
                    [sys.executable, "scripts/run.py", mode, "Find cross-day RF work",
                     "--input", str(source), "--model", "openai/demo",
                     "--base-url", f"http://127.0.0.1:{server.server_port}/v1", *options],
                    cwd=ROOT,
                    env=dict(os.environ, OPENAI_API_KEY="mock", NO_PROXY="127.0.0.1",
                             PYTHONUTF8="1"),
                    capture_output=True,
                    encoding="utf-8",
                    timeout=10,
                )
                self.assertEqual(result.returncode, 0, result.stderr)
                return result.stdout

            shortlist = run("search", EXAMPLE, "--save-selected", str(selected))
            self.assertIn("example-device", shortlist)
            self.assertNotIn("example-type", shortlist)
            self.assertNotIn("Reading card", shortlist)
            original = json.loads(EXAMPLE.read_text(encoding="utf-8"))[0]
            self.assertEqual(json.loads(selected.read_text(encoding="utf-8")), [original])

            self.assertEqual(run("read", selected).strip(), "Reading card")
            combined = run("both", EXAMPLE)
            self.assertLess(combined.index("example-device"), combined.index("Reading card"))

        self.assertEqual(len(server.calls), 4)
        for path, body in server.calls:
            self.assertEqual(path, "/v1/chat/completions")
            self.assertEqual(body["model"], "demo")
        for index in (1, 3):
            prompt = server.calls[index][1]["messages"][0]["content"]
            self.assertIn(original["abstract"], prompt)
            self.assertNotIn("example-type", prompt)


if __name__ == "__main__":
    unittest.main()
