FROM python:3.10-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV FLASK_APP app.py
ENV FLASK_RUN_HOST 0.0.0.0
ENV PORT 5001

WORKDIR /app

RUN mkdir -p /app/instance
RUN mkdir -p /app/migrations/versions

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5001

CMD ["sh", "-c", "flask db upgrade && gunicorn --bind 0.0.0.0:5001 app:app"]