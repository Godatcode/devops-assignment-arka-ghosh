# Monitoring

The application exposes `/healthz`, `/readyz`, and Prometheus text metrics at `/metrics`. The Deployment has scrape annotations. On a cluster with Prometheus, a scrape job can select annotated Pods. `board_tasks_total` shows saved task count and `board_uptime_seconds` shows process uptime. Container stdout provides request logs through `kubectl logs deployment/board`.

Example checks:

```bash
kubectl port-forward service/board 18080:80
curl http://localhost:18080/metrics
kubectl top pods
kubectl logs deployment/board --tail=50
```

An alert can trigger when `up{job="board"} == 0` for five minutes. In a production deployment, add request count and latency histograms, central log storage, and tracing.
