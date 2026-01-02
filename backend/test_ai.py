# backend/test_ai.py
from transformers import pipeline

# 1. LOAD THE PIPELINE
# This will download about 1.6GB of data the first time you run it.
# We are using "facebook/bart-large-cnn" - a famous summarizer model.
print("Downloading/Loading model... this might take a minute...")
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# 2. THE INPUT TEXT
article = """
The Apollo program, also known as Project Apollo, was the third United States human spaceflight program carried out by the National Aeronautics and Space Administration (NASA), which succeeded in preparing and landing the first humans on the Moon from 1968 to 1972. It was first conceived in 1960 during the Eisenhower administration as a three-man spacecraft to follow the one-man Mercury project which would put the first Americans in space. Apollo was later dedicated to President John F. Kennedy's national goal of "landing a man on the Moon and returning him safely to the Earth" by the end of the 1960s, which he proposed in an address to Congress on May 25, 1961.
"""

# 3. RUN PREDICTION
print("Thinking...")
summary = summarizer(article, max_length=60, min_length=30, do_sample=False)

# 4. PRINT RESULT
print("--- SUMMARY ---")
print(summary[0]['summary_text'])