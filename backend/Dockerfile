# 1. THE BASE
FROM python:3.9-slim

# 2. THE SETUP
WORKDIR /app

# 3. THE INSTALLATION (The Nuclear Fix)
# We type the names directly here so there is NO MISTAKE.
RUN pip install --no-cache-dir fastapi uvicorn pydantic torch transformers requests

# 4. THE CODE
COPY . .

# 5. THE STARTUP
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]