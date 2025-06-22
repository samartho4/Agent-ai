FROM python:3.11-slim
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir celery
CMD ["python", "-m", "apps.worker"]
