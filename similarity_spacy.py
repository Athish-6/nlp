import spacy 
nlp=spacy.load("en_core_web_sm")

word1= nlp("king")
word2= nlp("queen")
print(word1.similarity(word2))

