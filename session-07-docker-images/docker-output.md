# Multi stage Docker output

Captured on 7 October 2026. The first request immediately after starting Java returned an empty response while the process started; a retry succeeded.

```text
$ docker build -t devops-assignment-multistage multistage-app
... exporting to image ... DONE
$ curl -fsS http://localhost:18080
Hello World from Docker multi-stage build
$ docker ps --filter name=devops-assignment-multi --format 'table {{.Names}}\t{{.Ports}}'
NAMES                   PORTS
devops-assignment-multi   0.0.0.0:18080->8080/tcp, [::]:18080->8080/tcp
```
