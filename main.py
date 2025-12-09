from textblob import TextBlob
from fastapi import FastAPI
from pydantic import BaseModel

# Initializing
app = FastAPI()

# Defining the Data Model
class SentimentRequest(BaseModel):
    text: str

# Creating the Endpoint
@app.post("/analyze")
def analyze_sentiment(request: SentimentRequest):
    blob = TextBlob(request.text)
    polarity = blob.sentiment.polarity
            
    if polarity > 0:
        mood = "Positive 😊"
    elif polarity < 0:
        mood = "Negative 😠"
    else:
        mood = "Neutral 😐"
    return {
        "received_text": request.text,
        "sentiment": mood,
        "score": polarity
    }

# root check
@app.get("/")
def home():
    return {"message": "AI Sentiment API is running!"}
