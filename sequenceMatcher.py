from difflib import SequenceMatcher
def  similar (a,b):
    return SequenceMatcher(None,a,b).ratio()
word1 = "Apple"
word2 = "Appel"
word3 = "mango"
print(f"similarity between'{word1}'and '{word2}':{similar (word1,word2):.2f}")
print(f"similarity between'{word1}'and '{word3}':{similar (word1,word3):.2f}")