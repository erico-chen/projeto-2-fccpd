FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir flask psycopg2-binary redis

COPY app.py .

EXPOSE 8080

CMD ["python", "-u", "app.py"]