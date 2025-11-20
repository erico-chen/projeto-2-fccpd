FROM python:3.12-slim

WORKDIR /app

RUN pip install --no-cache-dir flask

COPY premiacao.py .

EXPOSE 5002

CMD ["python", "-u", "premiacao.py"]
