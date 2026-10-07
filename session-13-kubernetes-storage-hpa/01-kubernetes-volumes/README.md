# Kubernetes volumes

`emptyDir` exists while a Pod is scheduled and disappears when that Pod is removed. It suits caches and temporary files. `hostPath` mounts a node path and ties the Pod to node layout, so it is mainly useful for local labs or node agents. A PersistentVolume represents cluster storage; a PersistentVolumeClaim requests it. A StorageClass describes how the cluster provisions matching volumes. Dynamic provisioning lets a PVC trigger creation of a backing volume without manually creating a PV.

The board Deployment mounts a 1 Gi PVC at `/data`, where SQLite writes its database. It uses one replica and `Recreate` because a ReadWriteOnce SQLite file should not be shared by multiple simultaneous writers. The Helm demonstration uses `emptyDir`, so its data is intentionally ephemeral.

```bash
kubectl apply -f ../final-devops-project/kubernetes/pvc.yaml
kubectl get pvc,pv,storageclass
kubectl describe pvc board-data
```
