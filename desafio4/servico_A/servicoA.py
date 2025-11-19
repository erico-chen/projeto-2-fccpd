from flask import Flask, jsonify

app = Flask(__name__)

USERS = [
    {"id": 1, "nome": "Gabi", "ativo_desde": "2021-01-01"},
    {"id": 2, "nome": "Jorge", "ativo_desde": "2022-03-15"},
    {"id": 3, "nome": "Saulo", "ativo_desde": "2023-07-10"},
]

@app.get("/users")
def get_users():
    return jsonify(USERS)

@app.get("/")
def health():
    return jsonify({"status": "ok", "service": "A"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5008)