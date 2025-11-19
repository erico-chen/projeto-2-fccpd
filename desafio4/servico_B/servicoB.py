import os
import requests
from flask import Flask, jsonify

app = Flask(__name__)

# Host do service-a (nome do serviço/contêiner na rede Docker)
SERVICE_A_HOST = os.getenv("SERVICE_A_HOST", "servico_A")
SERVICE_A_PORT = int(os.getenv("SERVICE_A_PORT", "5008"))

@app.get("/users-detalhado")
def users_detalhado():
    url = f"http://{SERVICE_A_HOST}:{SERVICE_A_PORT}/users"
    try:
        resp = requests.get(url, timeout=5)
        resp.raise_for_status()
        users = resp.json()
    except Exception as e:
        return jsonify({"error": "Falha ao consultar service-a", "detail": str(e)}), 500

    mensagens = [
        f"Usuário {u['nome']} ativo desde {u['ativo_desde']}"
        for u in users
    ]

    return jsonify({
        "origem": "service-b",
        "mensagens": mensagens
    })

@app.get("/")
def health():
    return jsonify({"status": "ok", "service": "B"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)