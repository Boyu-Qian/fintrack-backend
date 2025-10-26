from flask import Flask, request, Response
from db import db
from config import Config
import time
from users.models import User
import logging
from logging.config import dictConfig
from prometheus_client import Counter, Histogram , Gauge ,generate_latest, CONTENT_TYPE_LATEST
from users.routes import bp as users_bp
from redis_client import redis_client as cache
from flask_cors import CORS
import sys

app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total app requests', ['method', 'endpoint','status_code'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'Request latency', ['endpoint'])

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    if request.path in ["/metrics", "/favicon.ico", "/healthz"]:
        return response
    latency = time.time() - request.start_time
    REQUEST_LATENCY.labels(request.endpoint).observe(latency)
    REQUEST_COUNT.labels(request.method, request.endpoint, str(response.status_code)).inc()
    return response

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)

CORS(app,origins=["http://localhost:8080,http://localhost:5173,*"],  # 前端地址
    supports_credentials=True  )
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    print("✅ All tables already exist:", db.metadata.tables.keys())

### Testing Redis
try:
    cache.set("test-user-service","user-service:success!")
    app.logger.error(f"Redis connection test:{cache.get('test-user-service')}")
except Exception as e:
    app.logger.error(f"Redis failed:{e}")

app.register_blueprint(users_bp, url_prefix='/api/users')

if __name__ == '__main__':
    app.run(debug=True,port=32222)
