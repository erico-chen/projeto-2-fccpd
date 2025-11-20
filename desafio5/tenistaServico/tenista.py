from flask import Flask, jsonify

app = Flask(__name__)

TENISTAS = [
    {"id": 1, "nome": "Carlos Alcaraz", "virou_profissional": "2018"},
    {"id": 2, "nome": "Jannik Sinner", "virou_profissional": "2018"},
    {"id": 3, "nome": "Taylor Fritz", "virou_profissional": "2015"},
]


@app.get("/tenistas")
def get_tenistas():
    return jsonify(TENISTAS)


@app.get("/")
def health():
    return jsonify({"status": "ok", "service": "servico-tenista"}), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
