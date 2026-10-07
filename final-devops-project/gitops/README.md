# GitOps workflow

The desired Kubernetes state is stored in `kubernetes/` and the Helm chart. A pull request changes manifests, CI validates them, and the reviewer merges them. A GitOps controller such as Argo CD would compare the cluster with this repository, apply approved changes, and report drift. This repository does not claim a live Argo CD installation.

For a cluster that has Argo CD, configure an Application with the repository URL, `path: final-devops-project/kubernetes`, destination namespace, and automated sync only after verifying the image and Secret setup. Keep real secrets in an external secret store or a sealed/encrypted mechanism.
