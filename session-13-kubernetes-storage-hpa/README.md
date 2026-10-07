# Session 13: Storage, HPA, and probes

The [volume notes](01-kubernetes-volumes/README.md) compare `emptyDir`, `hostPath`, PV, PVC, and StorageClass. The final project's board Deployment mounts a PVC, has liveness and readiness probes, and sets CPU requests needed by HPA. The [`hpa.yml`](hpa.yml) targets 70% CPU utilization; [`load-generator.yaml`](load-generator.yaml) sends HTTP requests. A Metrics Server must be installed for `kubectl top` and CPU HPA values. The mini project is the task board with persistent SQLite storage.

```bash
kubectl apply -f ../final-devops-project/kubernetes/
kubectl apply -f hpa.yml
kubectl get hpa,pods,pvc
kubectl apply -f load-generator.yaml
kubectl top pods
kubectl describe hpa board
kubectl delete -f load-generator.yaml
```

The ConfigMap, real Secret, and image must exist before the Deployment becomes ready. Scaling a single-file SQLite database horizontally is inappropriate; the HPA manifest demonstrates the mechanism but should be paired with a shared database before increasing replicas in a real deployment.
