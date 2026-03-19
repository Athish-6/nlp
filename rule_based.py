text = input("Enter text: ").lower()
if any(ch in text for ch in ['அ','ஆ','இ','உ','எ','ஓ']):
 print("Language: Tamil")
elif any(ch in text for ch in ['ह','क','म']):
 print("Language: Hindi")
else:
 print("Language: English (assumed)")