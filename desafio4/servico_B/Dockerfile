FROM python:3.12-slim

WORKDIR /servicoB

RUN pip install --no-cache-dir flask requests

COPY servicoB.py .

EXPOSE 5001

CMD ["python", "-u", "servicoB.py"]