FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["/bin/sh", "-c", "4","gunicorn -w 4 0.0.0.0:32222 --access-logfile - app:app 1>&2"]