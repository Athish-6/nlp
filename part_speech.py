import nltk
# Download resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger_eng')
# Example sentence
sentence = "The quick brown fox jumps over the lazy dog"
# Tokenize sentence into words
words = nltk.word_tokenize(sentence)
# Perform POS tagging
pos_tags = nltk.pos_tag(words)
# Print results
print("Sentence:", sentence)
print("\nPOS Tags:")
for word, tag in pos_tags:
 print(f"{word} -> {tag}")