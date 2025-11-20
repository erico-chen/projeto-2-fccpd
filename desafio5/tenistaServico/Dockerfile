FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY tenista.py .

EXPOSE 5001

CMD ["python", "-u", "tenista.py"]
