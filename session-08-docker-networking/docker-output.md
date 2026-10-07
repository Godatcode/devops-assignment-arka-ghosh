# Docker networking output

Captured on 7 October 2026 with the three-network lab.

```text
$ docker exec devops-lab-frontend wget -qO- http://devops-lab-backend
<h1>Welcome to nginx!</h1>

$ docker exec devops-lab-backend getent hosts devops-lab-db
172.22.0.2        devops-lab-db  devops-lab-db
```

`docker inspect devops-lab-backend` showed membership in `devops-lab-front`, `devops-lab-back`, and `devops-lab-data`. The required backend connection to two networks was satisfied; I also attached it to the front network so the frontend could reach it, making three memberships. The frontend and database had no shared network.

The bind mount responded with `Hello students` before the host file changed and `Hello students, updated live` immediately after the file changed. The Nginx container was not restarted between requests. I stopped and removed the lab containers and networks after the check.
