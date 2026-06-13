# Start from a slim Python image
FROM python:3.14-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/spasylki_az .

# Start FastAPI application in uvicorn
CMD uvicorn main:app --host 0.0.0.0 --port $PORT --workers 1
