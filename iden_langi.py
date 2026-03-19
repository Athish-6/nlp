import langid
text = input("Enter text: ")
language, confidence = langid.classify(text)
print("Detected Language:", language)
print("Confidence Score:", confidence)