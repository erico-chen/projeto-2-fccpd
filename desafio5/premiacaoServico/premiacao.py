from flask import Flask, jsonify

app = Flask(__name__)

PREMIACAO = [
    {"id": 101, "tenista_id": 1, "premiacao_carreira": 50000000},
    {"id": 102, "tenista_id": 2, "premiacao_carreira": 49300000},
    {"id": 103, "tenista_id": 3, "premiacao_carreira": 24300000},
]


@app.get("/premiacoes")
def get_premiacoess():
    return jsonify(PREMIACAO)


@app.get("/")
def health():
    return jsonify({"status": "ok", "service": "servico-premiacao"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002)
