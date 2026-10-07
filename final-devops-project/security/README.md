# Security checks

The workflow runs unit tests, Python compilation, secret scanning with Gitleaks, filesystem and image scans with Trivy, and blocks image publication if a scan fails. The application uses parameterized SQLite queries, validates task titles, and runs in the container as an unprivileged user. The Kubernetes Deployment drops Linux capabilities and disallows privilege escalation.

The tracked `secret.example.yaml` contains a placeholder only. Create the real Secret outside Git. GitHub Actions uses the built-in `GITHUB_TOKEN` for GHCR; a live Kubernetes deployment also needs a protected `KUBECONFIG_B64` repository secret and an approved environment.
