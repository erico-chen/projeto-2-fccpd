import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

TENISTA_SERVICE_HOST = os.getenv("TENISTA_SERVICE_HOST", "tenista-service")
TENISTA_SERVICE_PORT = int(os.getenv("TENISTA_SERVICE_PORT", "5001"))

PREMIACAO_SERVICE_HOST = os.getenv("PREMIACAO_SERVICE_HOST", "premiacao-service")
PREMIACAO_SERVICE_PORT = int(os.getenv("PREMIACAO_SERVICE_PORT", "5002"))


def build_url(host, port, path):
    return f"http://{host}:{port}{path}"


@app.get("/tenistas")
def get_tenistas():
    url = build_url(TENISTA_SERVICE_HOST, TENISTA_SERVICE_PORT, "/tenistas")
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        tenistas = resp.json()
        return jsonify(tenistas), resp.status_code
    except Exception as e:
        return jsonify({"error": "Falha ao consultar servico-tenista", "detail": str(e)}), 502


@app.get("/premiacoes")
def get_premiacoes():
    url = build_url(PREMIACAO_SERVICE_HOST, PREMIACAO_SERVICE_PORT, "/premiacoes")
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        premiacoes = resp.json()
        return jsonify(premiacoes), resp.status_code
    except Exception as e:
        return jsonify({"error": "Falha ao consultar servico-premiacao", "detail": str(e)}), 502


@app.get("/")
def health():
    return jsonify({"status": "ok", "service": "api-gateway"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
