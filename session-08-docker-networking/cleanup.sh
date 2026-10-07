#!/usr/bin/env bash
set -euo pipefail
for c in frontend backend db bind host; do docker rm -f "devops-lab-${c}" 2>/dev/null || true; done
for n in front back data; do docker network rm "devops-lab-${n}" 2>/dev/null || true; done
