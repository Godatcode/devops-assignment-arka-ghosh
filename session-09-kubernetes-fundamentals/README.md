# Session 9: Kubernetes fundamentals

Kubernetes has a control plane (API server, scheduler, controller manager, and etcd) and worker nodes (kubelet, container runtime, kube-proxy or equivalent networking). A Pod is the smallest scheduling unit; a Deployment manages ReplicaSets and rollout; a Service gives a stable endpoint for selected Pods.

For a local Minikube lab:

```bash
minikube start --driver=docker
kubectl cluster-info
kubectl get nodes -o wide
kubectl create deployment hello --image=nginx:1.27-alpine
kubectl expose deployment hello --port=80 --type=NodePort
kubectl get pods,deployments,services -o wide
kubectl describe deployment hello
minikube service hello --url
kubectl delete service hello
kubectl delete deployment hello
```

At the initial check on this machine, `kubectl cluster-info` had no configured cluster and returned connection refused at `localhost:8080`. The later manifests are included for execution once a cluster is available.
