import nltk
from nltk.corpus import wordnet
from nltk.wsd import lesk
# Ensure necessary NLTK data is downloaded
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
sentence1 = "I need to deposit money into my bank account."
sentence2 = "The river bank was muddy after the storm."
# Tokenize sentences
tokens1 = nltk.word_tokenize(sentence1)
tokens2 = nltk.word_tokenize(sentence2)
# Apply the Lesk algorithm to find the best sense of the word 'bank'
# 'senses' provides all possible meanings for 'bank'
bank_senses = wordnet.synsets('bank')
sense1 = lesk(tokens1, 'bank', 'n') # 'n' specifies we are looking for a noun
sense2 = lesk(tokens2, 'bank', 'n')
print(f"Senses for 'bank': {bank_senses}\n")
print(f"Meaning in sentence 1: {sense1.definition()}")
print(f"Meaning in sentence 2: {sense2.definition()}")