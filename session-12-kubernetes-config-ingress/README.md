# Session 12: ConfigMaps, Secrets, and Ingress

The ConfigMap demo injects `GREETING` into a Pod. The Secret example injects a value but contains only a placeholder; real secrets should be created outside Git. A Kubernetes Secret is base64 encoded in the manifest and needs encryption at rest and access controls for stronger protection.

```bash
kubectl apply -f config-demo.yaml
kubectl logs config-demo
cp secret-demo.example.yaml secret-demo.local.yaml
# Edit the placeholder locally, then:
kubectl apply -f secret-demo.local.yaml
kubectl logs secret-demo
```

For Ingress, apply the final project's Deployment and Service, install an Ingress controller, then apply [`../final-devops-project/kubernetes/ingress.yaml`](../final-devops-project/kubernetes/ingress.yaml). `curl -H 'Host: board.local' http://<ingress-address>/` checks host routing. Ingress is the API object describing HTTP routes; the controller is the running software that reads it and configures a proxy. Both are required for traffic to flow.

Troubleshooting: if the Pod is pending, check `kubectl describe pod`; if it starts but cannot read a value, check ConfigMap and Secret names; if the Service works but Ingress does not, check controller Pods, ingress class, host header, and `kubectl describe ingress`. The repository excludes `*.local.yaml` files.
