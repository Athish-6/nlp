from langdetect import detect
text = input("Enter text: ")
language = detect(text)
print("Detected Language Code:", language)