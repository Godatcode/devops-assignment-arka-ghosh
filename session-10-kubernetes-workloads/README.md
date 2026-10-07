# Session 10: Pods, ReplicaSets, Deployments

Four strategy manifests are included: [`rolling.yaml`](rolling.yaml), [`blue-green.yaml`](blue-green.yaml), [`canary.yaml`](canary.yaml), and [`recreate.yaml`](recreate.yaml). Rolling update allows one surge Pod and one unavailable Pod. Blue and green run side by side; switching the Service selector from `blue` to `green` moves traffic. Canary has nine stable replicas and one canary replica behind one Service, an approximate 10% split because Service routing is per endpoint rather than a precise traffic weight. Recreate removes old Pods before creating new ones.

```bash
kubectl apply -f rolling.yaml
kubectl rollout status deployment/rolling-demo
kubectl set image deployment/rolling-demo web=nginx:1.28-alpine
kubectl rollout history deployment/rolling-demo
kubectl get pods -w

kubectl apply -f blue-green.yaml
kubectl patch service color-demo -p '{"spec":{"selector":{"app":"color-demo","version":"green"}}}'
kubectl get endpoints color-demo

kubectl apply -f canary.yaml
kubectl get pods -l app=canary-demo --show-labels
kubectl apply -f recreate.yaml
kubectl set image deployment/recreate-demo web=nginx:1.28-alpine
```

[`pod-lifecycle.yaml`](pod-lifecycle.yaml) runs a short job-like Pod to observe Pending → Running → Succeeded with `kubectl get pod lifecycle-demo -w` and `kubectl describe pod lifecycle-demo`. Exact intermediate states depend on polling speed.
