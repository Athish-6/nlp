import nltk
nltk.download('movie_reviews')
nltk.download('punkt')
from textblob import TextBlob
# Sample text
text = "The movie was surprisingly good, but the ending was a bit disappointing."
# Create a TextBlob object
analysis = TextBlob(text)
# Get sentiment polarity (-1.0 to 1.0, where 1.0 is very positive)
polarity = analysis.sentiment.polarity
# Get subjectivity (0.0 to 1.0, where 1.0 is very subjective/opinionated)
subjectivity = analysis.sentiment.subjectivity
print(f"Text: {text}")
print(f"Polarity: {polarity}")
print(f"Subjectivity: {subjectivity}")
# Classify as positive, negative, or neutral based on polarity
if polarity > 0:
 print("Sentiment: Positive")
elif polarity < 0:
 print("Sentiment: Negative")
else:
 print("Sentiment: Neutral")