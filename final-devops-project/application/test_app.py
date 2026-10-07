import json
import os
import tempfile
import threading
import unittest
from http.client import HTTPConnection
from http.server import ThreadingHTTPServer
from pathlib import Path
from unittest.mock import patch

import app


class AppTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.temp = tempfile.TemporaryDirectory()
        app.DB = Path(cls.temp.name) / "board.db"
        app.TOKEN = "test-token"
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), app.Handler)
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.temp.cleanup()

    def request(self, method, path, body=None, headers=None):
        conn = HTTPConnection("127.0.0.1", self.server.server_port)
        conn.request(method, path, body, headers or {})
        response = conn.getresponse()
        result = response.status, response.read().decode()
        conn.close()
        return result

    def test_health_and_metrics(self):
        self.assertEqual(self.request("GET", "/healthz")[0], 200)
        self.assertIn("board_tasks_total", self.request("GET", "/metrics")[1])

    def test_task_creation_requires_token(self):
        body = json.dumps({"title": "Check deployment"})
        self.assertEqual(self.request("POST", "/api/tasks", body)[0], 401)
        status, data = self.request("POST", "/api/tasks", body, {"Authorization": "Bearer test-token"})
        self.assertEqual(status, 201)
        self.assertEqual(json.loads(data)["title"], "Check deployment")
        self.assertIn("Check deployment", self.request("GET", "/api/tasks")[1])

    def test_rejects_invalid_input(self):
        self.assertEqual(self.request("POST", "/api/tasks", json.dumps({"title": ""}), {"Authorization": "Bearer test-token"})[0], 400)


if __name__ == "__main__":
    unittest.main()
