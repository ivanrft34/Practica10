from flask import Flask
import redis
import time

app = Flask(__name__)
cache = redis.Redis(host='redis-server', port=6379)

@app.route('/')
def get_data():
    data = cache.get('mensaje')
    if data:
        return f"Respuesta desde Redis (Nivel 2): {data.decode('utf-8')}"

    time.sleep(2)
    valor = "Datos procesados"

    cache.set('mensaje', valor)
    return f"Respuesta procesada (lenta): {valor}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
