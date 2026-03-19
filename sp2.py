import spacy
nlp = spacy. load ("en_core_web_md")

word1 = "dog"
word2 = "cat"
word3 = "building"

doc1 = nlp (word1)
doc2 = nlp (word2)
doc3 = nlp (word3)

print(f"Similaritybetween'{word1}'and'{word2}':{doc1.similarity(doc2):.2f}")
print(f"Similaritybetween'{word1}'and'{word3}':{doc1.similarity(doc3):.2f}")