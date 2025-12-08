from textblob import TextBlob
import sys

def analyze_sentiment():
    print("--- AI Sentiment Analyzer (Running in Docker) ---")
    
    while True:
        user_input = input("\nEnter a sentence (or type 'exit' to quit): ")
        
        if user_input.lower() == 'exit':
            print("Shutting down AI...")
            break
            
        blob = TextBlob(user_input)
        sentiment = blob.sentiment.polarity
        
        if sentiment > 0:
            mood = "Positive 😊"
        elif sentiment < 0:
            mood = "Negative 😠"
        else:
            mood = "Neutral 😐"
            
        print(f"Detected Sentiment: {mood} (Score: {sentiment:.2f})")

if __name__ == "__main__":
    analyze_sentiment()
