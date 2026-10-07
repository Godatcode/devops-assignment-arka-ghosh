# Session 15: Helm

The chart in [`../final-devops-project/helm`](../final-devops-project/helm) templates a Deployment and Service. `Chart.yaml` identifies the chart, `values.yaml` holds defaults, and templates render Kubernetes objects. A real `board-secret` must exist before install.

```bash
helm lint ../final-devops-project/helm
helm template board ../final-devops-project/helm
helm install board ../final-devops-project/helm
helm list
helm status board
helm get values board
helm upgrade board ../final-devops-project/helm --set title='Board v2'
helm history board
helm upgrade board ../final-devops-project/helm --set title='Board v3'
helm history board
helm rollback board 1
helm status board
helm uninstall board
helm repo list
helm search repo nginx
```

The rollback sequence is install → upgrade → verify → upgrade again → verify → rollback → verify. Check `kubectl get deployment,service` and the response through port forwarding at each step. The chart uses ephemeral storage to make this rollout exercise simple; the plain manifest deployment uses a PVC.
