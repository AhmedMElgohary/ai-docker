FROM python:3.9-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt
RUN python -m textblob.download_corpora

# Expose port 8000 (The standard FastAPI port)
EXPOSE 8000

# Command to run the uvicorn server
# host 0.0.0.0 means "listen to requests from outside the container"
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
