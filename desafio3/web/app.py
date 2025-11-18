import os
import psycopg2
import redis
from flask import Flask, jsonify

app = Flask(__name__)

DB_HOST = os.getenv("DB_HOST", "db")
DB_PORT = int(os.getenv("DB_PORT", "5432"))
DB_NAME = os.getenv("DB_NAME", "desafio_3_db")
DB_USER = os.getenv("DB_USER", "cesar")
DB_PASSWORD = os.getenv("DB_PASSWORD", "school")

REDIS_HOST = os.getenv("REDIS_HOST", "cache")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

# Conexão Redis (cache)
cache = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

def get_db_conn():
  return psycopg2.connect(
      host=DB_HOST,
      port=DB_PORT,
      dbname=DB_NAME,
      user=DB_USER,
      password=DB_PASSWORD,
  )

@app.route("/")
def index():
  return jsonify({"message": "Desafio 3 - Docker Compose Orquestrando Serviços"})

@app.route("/init-db")
def init_db():
  conn = get_db_conn()
  cur = conn.cursor()
  cur.execute("""
    CREATE TABLE IF NOT EXISTS acessos (
      id SERIAL PRIMARY KEY,
      descricao TEXT NOT NULL
    );
  """)
  conn.commit()
  cur.close()
  conn.close()
  return jsonify({"status": "ok", "detail": "Tabela acessos criada (se não existia)."})

@app.route("/db")
def db_test():
  conn = get_db_conn()
  cur = conn.cursor()
  cur.execute("INSERT INTO acessos (descricao) VALUES ('Acesso via /db');")
  conn.commit()

  cur.execute("SELECT COUNT(*) FROM acessos;")
  total, = cur.fetchone()

  cur.close()
  conn.close()
  return jsonify({"status": "ok", "total_registros": total})

@app.route("/cache")
def cache_test():
  valor_atual = cache.incr("contador_acessos")
  return jsonify({"status": "ok", "contador_cache": int(valor_atual)})

if __name__ == "__main__":
  app.run(host="0.0.0.0", port=8080)
