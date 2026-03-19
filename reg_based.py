import re
text = "NLP combines linguistics, computer science, and AI."
# Split words using regex
tokens = re.findall(r'\w+', text)
print("Original Text:", text)
print("Tokens:", tokens)