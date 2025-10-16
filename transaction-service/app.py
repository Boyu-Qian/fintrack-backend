from flask import Flask, request, Response
from db import db
from flask_cors import CORS
from config import Config
import time
from prometheus_client import Counter, Histogram ,generate_latest, CONTENT_TYPE_LATEST
from transactions.routes import transactions_bp
from transactions.models import Transaction
app = Flask(__name__)

REQUEST_COUNT = Counter('app_requests_total', 'Total app requests', ['method', 'endpoint','status_code'])
REQUEST_LATENCY = Histogram('http_request_latency_seconds', 'Request latency', ['endpoint'])

@app.before_request
def before_request():
    request.start_time = time.time()

@app.after_request
def after_request(response):
    latency = time.time() - request.start_time
    REQUEST_LATENCY.labels(request.path).observe(latency)
    REQUEST_COUNT.labels(request.method, request.path, response.status_code).inc()
    return response

@app.route("/metrics")
def metrics():
    return Response(generate_latest(), mimetype=CONTENT_TYPE_LATEST)


CORS(app,origins=["http://localhost:8080,http://localhost:5173", "https://www.fintrack.site", "https://fintrack.site"],supports_credentials=True)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    print("✅ All tables already exist:", db.metadata.tables.keys())


app.register_blueprint(transactions_bp, url_prefix='/api/transactions')

if __name__ == '__main__':
    app.run(debug=True,port=32223)
