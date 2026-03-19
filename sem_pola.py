positive_words = {"good", "happy", "excellent"}
negative_words = {"bad", "sad", "poor"}
sentence = "The movie was excellent but the ending was poor"
words = sentence.lower().split()
score = 0
for word in words:
 if word in positive_words:
  score += 1
 elif word in negative_words:
  score -= 1
print("Semantic Score:", score)
if score > 0:
 print("Positive sentence")
elif score < 0:
 print("Negative sentence")
else:
 print("Neutral sentence")