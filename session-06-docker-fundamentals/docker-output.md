# Docker verification

Commands were run on 7 October 2026 with Docker Engine 29.2.0. Each response below came from a running local container.

| Folder | Image build | HTTP response |
|---|---|---|
| `nodejs-app` | pass | `<h1>Hello World from Node.js</h1>` |
| `python-app` | pass | `<h1>Hello World from Python</h1>` |
| `java-app` | pass | `<h1>Hello World from Java</h1>` |
| `Apache-app` | pass | `<!doctype html><html><head><title>Apache</title></head><body><h1>Hello World from Apache</h1></body></html>` |
| `React-app` | pass | Browser rendered `Hello World from React` at `localhost:18083` |
| `nginx-app` | pass | `<!doctype html><html><head><title>Nginx</title></head><body><h1>Hello World from Nginx</h1></body></html>` |
