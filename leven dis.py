import nltk 
nltk.download('punkt')
from nltk.metrics.distance import edit_distance
word1= "kitten"
word2= "sitting"
distance= edit_distance(word1, word2)
print("Edit Distance:",distance)