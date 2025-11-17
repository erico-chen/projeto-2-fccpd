from flask import Flask
import datetime

app = Flask(__name__)

@app.get("/")
def index():
    now = datetime.datetime.utcnow().isoformat()
    return f"Servidor ativo. Horário UTC: {now}Z\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
