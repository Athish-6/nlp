import nltk
# Download resources (only needed once)
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
# Example sentence
sentence = "Running is fun while swimming keeps you healthy."
# Tokenize and tag
words = nltk.word_tokenize(sentence)
pos_tags = nltk.pos_tag(words)
# Print gerunds (VBG tags)
print("Sentence:", sentence)
print("\nGerunds detected:")
for word, tag in pos_tags:
 if tag == "VBG": # VBG = Verb, Gerund/Present Participle
  print(word)