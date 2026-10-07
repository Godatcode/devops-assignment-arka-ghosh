# Session 11: Kubernetes services and DNS

[`services.yaml`](services.yaml) defines a backend Deployment and ClusterIP, NodePort, LoadBalancer, ExternalName, and headless Services. ClusterIP is internal only; NodePort opens a node port; LoadBalancer asks a supported environment for an external balancer; ExternalName supplies a DNS alias; headless service has no virtual ClusterIP and returns Pod addresses. On a local cluster, LoadBalancer may show `<pending>` until a tunnel or load balancer implementation is installed.

```bash
kubectl apply -f services.yaml
kubectl get svc,endpoints -o wide
kubectl run dns-check --rm -it --image=busybox:1.36 --restart=Never -- nslookup demo-clusterip.default.svc.cluster.local
kubectl run web-check --rm -it --image=busybox:1.36 --restart=Never -- wget -qO- http://demo-clusterip
```

A ReplicaSet maintains the desired number of matching Pods. A Service selects Pods and routes traffic to them. A Deployment manages ReplicaSets and rollouts. A DaemonSet schedules a copy on each eligible node, often for node agents. A StatefulSet gives Pods stable identities and storage, which databases often need. See [`fqdn/README.md`](fqdn/README.md) and [`coredns/README.md`](coredns/README.md) for DNS details.
