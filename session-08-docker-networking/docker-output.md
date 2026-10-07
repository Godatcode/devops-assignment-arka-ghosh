# Docker networking output

Captured on 7 October 2026 with the three-network lab.

```text
$ docker exec devops-lab-frontend wget -qO- http://devops-lab-backend
<h1>Welcome to nginx!</h1>

$ docker exec devops-lab-backend getent hosts devops-lab-db
172.22.0.3        devops-lab-db  devops-lab-db
```

`docker inspect devops-lab-backend` showed membership in `devops-lab-front` and `devops-lab-back` only. The frontend shares front with the backend; the database shares back with the backend and also joins data. The backend is on exactly two networks.

The bind mount responded with `Hello students` before the host file changed and `Hello students, updated live` immediately after the file changed. The Nginx container was not restarted between requests. I stopped and removed the lab containers and networks after the check.
