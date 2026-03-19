import nltk
nltk.download('punkt')
text = "NLP is fun. Lexical analysis helps in breaking text into tokens."
# Tokenize into sentences
sentences = nltk.sent_tokenize(text)
print("Original Text:", text)
print("Sentences:", sentences)