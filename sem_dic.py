semantic_dict = {
 "dog": "an animal",
 "cat": "an animal",
 "apple": "a fruit",
 "car": "a vehicle"
}
word = input("Enter a word: ").lower()
if word in semantic_dict:
 print(f"Meaning of '{word}': {semantic_dict[word]}")
else:
 print("Meaning not found")