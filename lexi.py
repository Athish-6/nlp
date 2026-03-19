import nltk

nltk.download('punkt')
text = "student loves learning NLP and Python programming."
# Tokenize into words
words = nltk.word_tokenize(text)
print("Original Text:", text)
print("Tokens:", words)