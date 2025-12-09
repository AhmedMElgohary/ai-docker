import requests
import time 

url = "http://127.0.0.1:8000/analyze"

reviews = [
    "This product is amazing, I love it!",
    "It arrived broken and I am very angry.",
    "The color is okay, but the size is weird.",
    "Worst experience of my life.",
    "Highly recommended for everyone!"
]

print("--- Starting automated AI Test ---")

for review in reviews:
    
    payload = {"text": review}

    response = requests.post(url, json = payload)

    data = response.json()

    print(f"Sent: '{review}'")
    print(f"AI Says: {data['sentiment']} (Score: {data['score']})")
    print("-" * 30)

    time.sleep(0.5)