# Используем официальный Python 3.11
FROM python:3.11-slim

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . .
RUN chmod +x start.sh

CMD ["./start.sh"]
