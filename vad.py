import nltk
nltk.download('vader_lexicon')
from nltk.sentiment import SentimentIntensityAnalyzer
# Download the VADER lexicon (needs to be run once)
try:
 nltk.data.find('sentiment/vader_lexicon.zip')
except nltk.downloader.DownloadError:
 nltk.download('vader_lexicon')
# Sample text with social media features
text = "This phone is AMAZING!!! But the battery life sucks. 😠"
# Initialize the SentimentIntensityAnalyzer
analyzer = SentimentIntensityAnalyzer()
# Get the sentiment scores
scores = analyzer.polarity_scores(text)
print(f"Text: {text}")
print(f"Sentiment Scores: {scores}")
# Determine overall sentiment based on the 'compound' ' score
compound_score = scores['compound']
if compound_score >= 0.05:
 print("Overall Sentiment: Positive")
elif compound_score <= -0.05:
 print("Overall Sentiment: Negative")
else:
 print("Overall Sentiment: Neutral")