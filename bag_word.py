sentence = "I eat an apple"
words = sentence.lower().split()
food_items = {"apple", "rice", "bread"}
actions = {"eat", "drink"}
for word in words:
 if word in food_items:
  print(f"'{word}' is a FOOD item")
 if word in actions:
  print(f"'{word}' is an ACTION")