FROM python:3.11-slim
WORKDIR /code
COPY . /code
RUN pip install --no-cache-dir fastapi uvicorn[standard]
CMD ["uvicorn", "apps.api.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
