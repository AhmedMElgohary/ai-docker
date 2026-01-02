# backend/main.py
from fastapi import FastAPI
from pydantic import BaseModel
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware

# 2. INITIALIZE APP
app = FastAPI()


# This tells the server: "Allow requests from anywhere (for now)"
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # In production, we would put ["http://localhost:5173"]
    allow_credentials=True,
    allow_methods=["*"], # Allow GET, POST, etc.
    allow_headers=["*"],
)

# 3. LOAD THE BRAIN (The Heavy Lifting)
print("Loading AI Model... please wait...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
print("AI Model Loaded!")

# 4. DEFINE NEW DATA FORMAT
# We used to accept 'value: float'. Now we accept 'text: str'.
class TextRequest(BaseModel):
    text: str
    temperature: float = 1.0

# 5. THE NEW ENDPOINT
@app.post("/summarize")
def summarize_text(request: TextRequest):
    # A. Get the text from the user
    input_text = request.text
    
    top_k_value = int(request.temperature * 50) + 10
    
    # B. Run the AI (Inference)
    # max_length=130: The summary won't be longer than this.
    # min_length=30: The summary won't be shorter than this.
    # do_sample=False: Forces the AI to be factual, not creative.
    prediction = summarizer(
        input_text, 
        max_length=130, 
        min_length=30, 
        do_sample=True,
        temperature = request.temperature,
        top_k=top_k_value,   #Forces diversity
        top_p=0.95)
    
    # C. Extract the text
    # The AI returns a list like [{'summary_text': '...'}], so we grab the first one.
    summary_result = prediction[0]['summary_text']
    
    return {"original_length": len(input_text), 
            "summary": summary_result, 
            "Creativity": request.temperature,
            "summary_length":len(summary_result)}