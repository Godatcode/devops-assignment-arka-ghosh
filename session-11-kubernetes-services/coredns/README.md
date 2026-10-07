# CoreDNS

CoreDNS is the cluster DNS server. Pods send DNS queries to its Service IP. The Kubernetes plugin answers Service and Pod names from the API; external names are forwarded upstream. The Corefile in the `kube-system` ConfigMap controls plugins, forwarding, caching, and health checks.

```bash
kubectl -n kube-system get deployment coredns
kubectl -n kube-system get configmap coredns -o yaml
kubectl run dns-check --rm -it --image=busybox:1.36 --restart=Never -- nslookup kubernetes.default.svc.cluster.local
kubectl -n kube-system logs deployment/coredns --tail=50
```

If lookup fails, inspect the Pod's `/etc/resolv.conf`, the CoreDNS Pods and Service, network policies, and CoreDNS logs. Then test an internal name and an external name separately.
