import time
import requests
from datetime import datetime, timezone

SERVER_URL = "http://server:8080"

while True:
    timestamp = datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")
    print(f"[CLIENTE] {timestamp} → GET {SERVER_URL}")
    try:
        response = requests.get(SERVER_URL)
        print("Resposta:", response.text.strip())
    except Exception as e:
        print("Erro ao conectar:", e)

    time.sleep(5)
