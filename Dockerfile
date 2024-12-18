FROM python:3.9-slim
WORKDIR /app
COPY . .
RUN pip install --no-cache-dir redis psycopg2-binary Django>=3.2
CMD ["python", "manage.py"]
