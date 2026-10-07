FROM python:3.12-alpine
WORKDIR /app
COPY application/app.py .
RUN mkdir -p /data && chown -R 65532:65532 /data /app
USER 65532:65532
ENV PORT=8080 HOST=0.0.0.0 DATA_DIR=/data PYTHONDONTWRITEBYTECODE=1
EXPOSE 8080
HEALTHCHECK --interval=30s --timeout=3s CMD python -c "import urllib.request; urllib.request.urlopen('http://127.0.0.1:8080/healthz', timeout=2)" || exit 1
CMD ["python", "app.py"]
