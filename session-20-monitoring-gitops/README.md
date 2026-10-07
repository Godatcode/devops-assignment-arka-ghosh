# Session 20: Monitoring, observability, and GitOps

The board app exposes `/metrics`, `/healthz`, and `/readyz`; its container logs go to stdout. The [monitoring notes](../final-devops-project/monitoring/README.md) list checks and a sample alert. Metrics show numeric trends, logs show discrete events, and traces follow a request across services. Together they help answer what failed, when, and where. Kubernetes adds Pod health, CPU/memory, events, and service discovery to observe.

In GitOps, Git stores the desired state and a controller continuously reconciles the cluster against it. The [GitOps notes](../final-devops-project/gitops/README.md) describe the repository-to-cluster flow. A merged manifest change would be applied by a configured controller such as Argo CD; this repository does not claim that controller is installed.
