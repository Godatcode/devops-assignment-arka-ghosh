# Local Kubernetes verification — 7 October 2026

I used a one-node Kind cluster (Kubernetes v1.37.0) to run the manifests. These are observed results, not expected output. The local cluster has no cloud load balancer, Ingress controller, or Metrics Server.

## Workloads and rollout strategies

- `rolling-demo` reached three available nginx replicas, then completed an image update to `nginx:1.28-alpine`.
- `blue` and `green` Deployments both rolled out. The `color-demo` Service selector changed from `version=blue` to `version=green`.
- `stable` and `canary` Deployments rolled out with ten Pods total (nine stable and one canary).
- `recreate-demo` rolled out, then completed an image update to `nginx:1.28-alpine`.
- `lifecycle-demo` reached `Succeeded` and appeared as `Completed` in `kubectl get pod`.

## Services, DNS, and configuration

- All five service examples were created. `demo-nodeport` used `30080`; the local `demo-loadbalancer` external IP remained `<pending>`, as expected without a load balancer implementation.
- A BusyBox Pod resolved `demo-clusterip.default.svc.cluster.local` to `10.96.43.100` through CoreDNS (`10.96.0.10`) and fetched the nginx welcome page over HTTP.
- The headless service had two backend Pod addresses in its endpoints.
- The `config-demo` Pod became Ready, and its log printed `Hello from ConfigMap`.

## Final task board

The `board` Deployment pulled the published GHCR image, reached `1/1 Running`, and its `board-data` PVC became `Bound`. Through `kubectl port-forward svc/board 18081:80`, `/healthz` and `/readyz` returned `ok`; `/metrics` exposed `board_tasks_total`; a POST to `/api/tasks` created `Kubernetes check`, and GET returned it.

I restarted `deployment/board`. After its rollout completed and I re-established port forwarding, GET `/api/tasks` still returned `[{"id": 1, "title": "Kubernetes check"}]`, confirming the SQLite file survived the Pod replacement through the PVC.

For a troubleshooting check, I changed the `board` Service selector to `app=wrong`. Its EndpointSlice had no addresses. Restoring `app=board` restored the backend address.

## Helm

`helm lint final-devops-project/helm` passed. I installed the `board-helm` release, upgraded it with titles `Board v2` and `Board v3`, then rolled back to revision 1. Revision 4 was reported as `deployed` with `Rollback to 1`; the `board-helm-board` Deployment had `1/1` available replicas and its Service was present.

The [GitHub Actions run for commit `cca4e43`](https://github.com/Godatcode/devops-assignment-arka-ghosh/actions/runs/37660421419) passed its test, security scan, and image jobs. AWS resources were not applied: the Terraform projects were formatted, initialized without a backend, and validated locally.
