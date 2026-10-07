# Session 16: CI/CD and GitHub Actions

CI builds and tests every change; CD publishes and deploys an approved version. [`../.github/workflows/pipeline.yml`](../../.github/workflows/pipeline.yml) defines jobs and steps on GitHub-hosted runners. The test job runs unit tests and Python compilation. The scan job checks code/config and secrets. The image job builds, scans, and pushes to GHCR only after the first two jobs pass.

A workflow is the YAML automation definition; a job is a set of steps on one runner. `GITHUB_TOKEN` is a short-lived workflow credential. The Docker image is the build artifact. For cluster deployment, store a kubeconfig as a protected secret and require an environment approval; this repository does not claim a live cluster deployment.

Run tests locally with `cd final-devops-project/application && python3 -m unittest -v`. The actual pipeline result is visible on the GitHub Actions tab after push.
