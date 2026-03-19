import nltk
nltk.download('wordnet')
from nltk.corpus import wordnet as wn
w1=wn.synsets('car')[0]
w2=wn.synsets("automobile")[0]
print(w1.path_similarity(w2))