FROM python:3.11-slim

ENV DEBIAN_FRONTEND=noninteractive

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY market.py .

EXPOSE 5000

CMD ["python", "market.py"]