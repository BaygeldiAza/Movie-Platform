FROM python:3.11-slim

WORKDIR /app

# No apt-get, no errors - THIS IS THE FIX
COPY requirements.txt .

# Install dependencies quietly and safely
RUN pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]