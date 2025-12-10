from transformers import pipeline
from fastapi import FastAPI
from pydantic import BaseModel

# Initializing
app = FastAPI()

# Loading the AI summarization model 
print("Loading AI Model... this may take a moment.")
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")


# Defining the Input format
class TextRequest(BaseModel):
    text: str

@app.get("/")
def home():
    return {"message": "AI Summarizer is Ready!"}

# Creating the Endpoint
@app.post("/summarize")
def summarize_text(request: TextRequest):
    input_length = len(request.text.split())
    # Allow it to be shorter (30% of original) to force rephrasing
    max_len = max(10, int(input_length * 0.3)) 
    
    # Enable Sampling (Creativity)
    summary_list = summarizer(
        request.text, 
        max_length=max_len, 
        min_length=5, 
        do_sample=True,      
        temperature=0.7      
    )
    
    summary_text = summary_list[0]['summary_text']

    return {
        "original_length": input_length,
        "summary_length": len(summary_text.split()),
        "summary": summary_text
    }