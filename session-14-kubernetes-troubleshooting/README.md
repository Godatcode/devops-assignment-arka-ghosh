# Session 14: Kubernetes troubleshooting

I use `kubectl get pods -o wide` for status and node, `kubectl describe pod` for events and scheduling, `kubectl logs` for process errors, `kubectl exec` for in-container checks, `kubectl get events --sort-by=.lastTimestamp` for recent changes, `kubectl explain` for API fields, and `kubectl top` for resource pressure.

| Symptom | Investigation | Common root cause | Check after fix |
|---|---|---|---|
| CrashLoopBackOff | `logs --previous`, `describe` | Process exits or probe fails | `rollout status`, logs |
| ImagePullBackOff / ErrImagePull | Pod events | Bad tag, private registry auth | Image is pulled and Pod runs |
| Pending | Pod events, node capacity, PVC | No capacity, taint, or unbound volume | Pod receives node |
| ContainerCreating | Pod events, CNI/storage logs | Mount or network setup failure | Container starts |
| Service unavailable | Service selectors and EndpointSlices | Labels or target port mismatch | `curl` from debug Pod |
| DNS failure | CoreDNS logs and `nslookup` | CoreDNS or network policy | Internal FQDN resolves |
| Config failure | Env, ConfigMap/Secret name | Missing key or wrong name | App readiness becomes healthy |

Mini project: deliberately change the board image tag to a nonexistent tag, observe `ErrImagePull` in events, restore the correct tag, and check `kubectl rollout status deployment/board`. Separately change the Service selector to `app: wrong`, observe no endpoints, then restore `app: board`. These are reproducible fault injections; no cluster output is claimed here without a running cluster.
