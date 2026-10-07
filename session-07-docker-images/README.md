# Session 7: Docker images and multi stage build

The [`multistage-app/Dockerfile`](multistage-app/Dockerfile) compiles Java in a JDK stage and copies the `.class` file to a smaller JRE runtime stage. The running server listens on port 8080 and returns the exact required text.

```bash
docker build -t devops-assignment-multistage multistage-app
docker run -d --rm --name devops-assignment-multi -p 18080:8080 devops-assignment-multistage
curl -fsS http://localhost:18080
docker ps --filter name=devops-assignment-multi
docker rm -f devops-assignment-multi
```

The first request immediately after container start may race the Java process startup; retry after a second. [`docker-output.md`](docker-output.md) contains the successful response and port mapping. The Compose file builds Node.js, Python, and Java together with three different host ports.
