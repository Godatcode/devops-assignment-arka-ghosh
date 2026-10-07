import json
import html
import os
import sqlite3
import time
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path

STARTED = time.time()
DB = Path(os.getenv("DATA_DIR", "/tmp/devops-board")) / "board.db"
TITLE = os.getenv("APP_TITLE", "DevOps Task Board")
TOKEN = os.getenv("APP_TOKEN", "")


def connect():
    DB.parent.mkdir(parents=True, exist_ok=True)
    connection = sqlite3.connect(DB)
    connection.execute("CREATE TABLE IF NOT EXISTS tasks (id INTEGER PRIMARY KEY, title TEXT NOT NULL)")
    return connection


class Handler(BaseHTTPRequestHandler):
    def send(self, status, body, content_type="text/plain; charset=utf-8"):
        data = body.encode() if isinstance(body, str) else body
        self.send_response(status)
        self.send_header("Content-Type", content_type)
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def do_GET(self):
        if self.path in ("/healthz", "/readyz"):
            try:
                with connect() as db:
                    db.execute("SELECT 1")
                self.send(200, "ok")
            except sqlite3.Error:
                self.send(503, "database unavailable")
        elif self.path == "/metrics":
            with connect() as db:
                count = db.execute("SELECT COUNT(*) FROM tasks").fetchone()[0]
            body = "# HELP board_tasks_total Number of saved tasks\n# TYPE board_tasks_total gauge\nboard_tasks_total %d\n# HELP board_uptime_seconds Process uptime\n# TYPE board_uptime_seconds gauge\nboard_uptime_seconds %.0f\n" % (count, time.time() - STARTED)
            self.send(200, body, "text/plain; version=0.0.4")
        elif self.path == "/api/tasks":
            with connect() as db:
                tasks = [{"id": row[0], "title": row[1]} for row in db.execute("SELECT id,title FROM tasks ORDER BY id DESC")]
            self.send(200, json.dumps(tasks), "application/json")
        elif self.path == "/":
            safe_title = html.escape(TITLE)
            page = f"""<!doctype html><html><head><meta name=viewport content='width=device-width, initial-scale=1'><title>{safe_title}</title><style>body{{font:16px system-ui;max-width:640px;margin:60px auto;padding:0 20px}}input,button{{padding:10px;font:inherit}}li{{margin:10px 0}}</style></head><body><h1>{safe_title}</h1><p>A small task board deployed through the DevOps pipeline.</p><input id=task placeholder='Task title'><button onclick='save()'>Add</button><ul id=list></ul><script>async function load(){{const r=await fetch('/api/tasks');document.querySelector('#list').innerHTML=(await r.json()).map(t=>'<li>'+t.title.replaceAll('&','&amp;').replaceAll('<','&lt;')+'</li>').join('')}}async function save(){{const title=document.querySelector('#task').value;await fetch('/api/tasks',{{method:'POST',headers:{{'Content-Type':'application/json','Authorization':'Bearer '+(sessionStorage.token||'')}},body:JSON.stringify({{title}})}});load()}}load()</script></body></html>"""
            self.send(200, page, "text/html; charset=utf-8")
        else:
            self.send(404, "not found")

    def do_POST(self):
        if self.path != "/api/tasks":
            return self.send(404, "not found")
        if TOKEN and self.headers.get("Authorization") != "Bearer " + TOKEN:
            return self.send(401, "unauthorized")
        try:
            length = int(self.headers.get("Content-Length", "0"))
            if length > 4096:
                return self.send(413, "too large")
            payload = json.loads(self.rfile.read(length))
            title = payload["title"]
            if not isinstance(title, str) or not 1 <= len(title.strip()) <= 120:
                return self.send(400, "invalid title")
            with connect() as db:
                cursor = db.execute("INSERT INTO tasks(title) VALUES (?)", (title.strip(),))
            self.send(201, json.dumps({"id": cursor.lastrowid, "title": title.strip()}), "application/json")
        except (ValueError, KeyError, TypeError, json.JSONDecodeError):
            self.send(400, "bad request")


if __name__ == "__main__":
    ThreadingHTTPServer(("0.0.0.0", int(os.getenv("PORT", "8080"))), Handler).serve_forever()
