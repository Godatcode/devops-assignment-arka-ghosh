# DevOps assignment

**Arka Ghosh · Enrollment 10110 · GitHub Godatcode**

This repository keeps the course exercises in session order. The final project is a small task board with tests, a Docker image, Kubernetes manifests, a Helm chart, Terraform infrastructure, monitoring endpoints, and a CI security gate. Each session README explains the commands, expected behavior, and what was actually checked. I kept credentials, Terraform state, and generated files out of Git.

| Session | Topic | Work |
|---|---|---|
| 1–2 | Linux fundamentals | [README](session-01-02-linux/README.md) |
| 3 | Shell scripting | [README](session-03-shell-scripting/README.md) |
| 4 | Networking | [README](session-04-networking/README.md) |
| 5 | Git and GitHub | [README](session-05-git/README.md) |
| 6 | Docker fundamentals | [README](session-06-docker-fundamentals/README.md) |
| 7 | Docker images | [README](session-07-docker-images/README.md) |
| 8 | Docker networking | [README](session-08-docker-networking/README.md) |
| 9 | Kubernetes fundamentals | [README](session-09-kubernetes-fundamentals/README.md) |
| 10 | Workloads and rollout strategies | [README](session-10-kubernetes-workloads/README.md) |
| 11 | Services and DNS | [README](session-11-kubernetes-services/README.md) |
| 12 | ConfigMap, Secret, Ingress | [README](session-12-kubernetes-config-ingress/README.md) |
| 13 | Storage, HPA, probes | [README](session-13-kubernetes-storage-hpa/README.md) |
| 14 | Troubleshooting | [README](session-14-kubernetes-troubleshooting/README.md) |
| 15 | Helm | [README](session-15-helm/README.md) |
| 16 | CI/CD and GitHub Actions | [README](session-16-cicd/README.md) |
| 17 | DevSecOps | [README](session-17-devsecops/README.md) |
| 18 | Terraform and AWS services | [README](session-18-terraform-iac/README.md) |
| 19 | Cloud infrastructure | [README](session-19-cloud-terraform/README.md) |
| 20 | Monitoring and GitOps | [README](session-20-monitoring-gitops/README.md) |
| 21 | Final project | [README](final-devops-project/README.md) |

## Verification

`python3 -m unittest -v` passes for the task board. Docker build and HTTP checks are recorded in the relevant session READMEs. The [local Kubernetes verification](CLUSTER_VERIFICATION.md) records the live cluster checks, including services, rollouts, storage, and Helm. A [GitHub Actions run](https://github.com/Godatcode/devops-assignment-arka-ghosh/actions/runs/37660421419) passed. Terraform was validated locally; AWS resources were not applied.
