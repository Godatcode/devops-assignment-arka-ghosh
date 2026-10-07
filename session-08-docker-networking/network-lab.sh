#!/usr/bin/env bash
set -euo pipefail
prefix=devops-lab
for net in front back data; do docker network create "${prefix}-${net}" >/dev/null 2>&1 || true; done
docker run -d --name "${prefix}-frontend" --network "${prefix}-front" nginx:1.27-alpine
docker run -d --name "${prefix}-backend" --network "${prefix}-back" nginx:1.27-alpine
docker network connect "${prefix}-front" "${prefix}-backend"
docker run -d --name "${prefix}-db" --network "${prefix}-data"   -e MYSQL_ROOT_PASSWORD=lab-only-password mysql:8.4
docker network connect "${prefix}-data" "${prefix}-backend"
docker exec "${prefix}-frontend" wget -qO- http://"${prefix}-backend"
docker exec "${prefix}-backend" getent hosts "${prefix}-db"
docker inspect "${prefix}-backend" --format '{{json .NetworkSettings.Networks}}'
