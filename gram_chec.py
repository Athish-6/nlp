import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
text = input("Enter a sentence: ")
matches = tool.check(text)
corrected_text = language_tool_python.utils.correct(text, matches)
print("Corrected Text:", corrected_text)