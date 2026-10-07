# Session 17: CI/CD and DevSecOps

The final project combines build, unit tests, Gitleaks secret scanning, Bandit SAST, Trivy filesystem scanning (vulnerabilities, misconfiguration, and secrets), Docker build, Trivy image scanning, and GHCR image publication. The image step depends on the test and scan jobs, so a failed gate prevents publication. Kubernetes manifests and the Helm chart describe deployment after a cluster and credentials are provided.

SAST reviews source behavior; SCA checks dependency vulnerabilities; secret scanning looks for exposed credentials; image scanning checks packages in the built image. This small application uses only Python's standard library, so third-party Python dependency scanning has no package list to inspect, but base image packages still matter. The [security notes](../final-devops-project/security/README.md) explain runtime controls. Check the Actions run for actual scan results; a YAML file alone is not execution evidence.

The [successful pipeline run](https://github.com/Godatcode/devops-assignment-arka-ghosh/actions/runs/37658770948) shows the tests, Bandit, Gitleaks, Trivy filesystem and image scans, and the image job completing successfully.
