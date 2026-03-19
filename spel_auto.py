from autocorrect import Speller
spell = Speller()
text = input("Enter a word or sentence: ")
print("Corrected Text:", spell(text))