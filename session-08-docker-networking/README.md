# Session 8: Docker networking and volumes

[`network-lab.sh`](network-lab.sh) creates three bridge networks: front, back, and data. Frontend joins front, MySQL joins data, and backend joins both front and data. The script checks frontend-to-backend HTTP and backend-to-database DNS. Docker's embedded DNS resolves container names only on a shared user-defined network. The database password in this isolated lab is an example value; use a secret for real deployment.

```bash
./network-lab.sh
./cleanup.sh
```

For the bind mount, [`site/index.html`](site/index.html) initially says **Hello students**:

```bash
docker run -d --rm --name devops-lab-bind -p 18085:80   -v "$PWD/site:/usr/share/nginx/html:ro" nginx:1.27-alpine
curl -fsS localhost:18085
printf '<h1>Hello students, updated live</h1>\n' > site/index.html
curl -fsS localhost:18085
docker rm -f devops-lab-bind
```

The second response changes without restarting the container because Nginx reads the mounted host file. On native Linux, `docker run --network host httpd:2.4` serves Apache on host port 80. Docker's host networking differs on macOS/Colima, and port 80 is already occupied on this machine, so I documented that host-only exercise without claiming a successful local run.

An overlay network connects containers on multiple Docker hosts through Swarm. A manager creates the network, Docker distributes network membership, and encapsulated traffic can reach services across hosts. A single-host bridge exercise does not prove cross-host overlay behavior.

The [captured Docker output](docker-output.md) shows the network and bind-mount checks from this machine.
