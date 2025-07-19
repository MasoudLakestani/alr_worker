FROM python:3.12-slim

WORKDIR /app

COPY pyproject.toml poetry.lock* ./

RUN pip install --no-cache-dir redis>=6.2.0,<7.0.0 python-dotenv

COPY add_to_redis.py .
COPY .env .

CMD ["python", "add_to_redis.py"]