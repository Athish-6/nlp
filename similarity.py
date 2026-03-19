from difflib import SequenceMatcher

def similarity(word1, word2):
    return SequenceMatcher(None, word1, word2).ratio()

print(similarity("king", "kings"))
print(similarity("book", "books"))
