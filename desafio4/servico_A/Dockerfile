FROM python:3.12-slim

WORKDIR /servicoA

RUN pip install --no-cache-dir flask

COPY servicoA.py .

EXPOSE 5008

CMD ["python", "-u", "servicoA.py"]