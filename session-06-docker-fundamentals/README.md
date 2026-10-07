# Session 6: Docker Hello World applications

The six required folders each contain source and a Dockerfile: `nodejs-app`, `python-app`, `java-app`, `Apache-app`, `React-app`, and `nginx-app`. Node and Python use small HTTP servers; Java uses the JDK HTTP server; React is built with Vite and served by Nginx; Apache and Nginx serve static HTML.

From this folder, build and verify each image:

```bash
docker build -t hello-node nodejs-app
docker run -d --rm --name hello-node -p 13000:3000 hello-node
curl -fsS http://localhost:13000

docker build -t hello-python python-app
docker run -d --rm --name hello-python -p 18000:8000 hello-python
curl -fsS http://localhost:18000

docker build -t hello-java java-app
docker run -d --rm --name hello-java -p 18081:8080 hello-java
curl -fsS http://localhost:18081

docker build -t hello-apache Apache-app
docker run -d --rm --name hello-apache -p 18082:80 hello-apache
curl -fsS http://localhost:18082

docker build -t hello-react React-app
docker run -d --rm --name hello-react -p 18083:80 hello-react
curl -fsS http://localhost:18083

docker build -t hello-nginx nginx-app
docker run -d --rm --name hello-nginx -p 18084:80 hello-nginx
curl -fsS http://localhost:18084
```

Cleanup: `docker rm -f hello-node hello-python hello-java hello-apache hello-react hello-nginx`. [`docker-output.md`](docker-output.md) records checked responses.
