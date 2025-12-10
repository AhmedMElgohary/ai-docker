FROM python:3.9-slim

WORKDIR /app

# 1. Install System Dependencies
RUN apt-get update && apt-get install -y git && rm -rf /var/lib/apt/lists/*

# 2. Install PyTorch CPU-Only
# FIX: Use --extra-index-url so it can still find standard tools on PyPI
RUN pip install --no-cache-dir torch --extra-index-url https://download.pytorch.org/whl/cpu

# 3. Copy Requirements
COPY requirements.txt .

# 4. Install the rest
RUN pip install --no-cache-dir -r requirements.txt

# 5. Copy the App Code
COPY . .

# 6. Setup the Server
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]