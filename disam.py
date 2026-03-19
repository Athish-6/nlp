import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet as wn

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('omw-1.4')

def disambiguate_sentence(sentence):

    tokens = nltk.word_tokenize(sentence)

    print("\nSentence:", sentence)
    print("Word Sense Disambiguation Results:\n")

    for word in tokens:

        sense = lesk(tokens, word)

        if sense:
            print(f"Word: {word}")
            print(f"Predicted Sense: {sense.name()}")
            print(f"Definition: {sense.definition()}\n")


sentence1 = "I went to the bank to deposit money."
sentence2 = "The fisherman sat on the bank of the river."
sentence3 = "The bass was painted on the wall while the musician played bass."

disambiguate_sentence(sentence1)
disambiguate_sentence(sentence2)
disambiguate_sentence(sentence3)
