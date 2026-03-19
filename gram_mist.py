import language_tool_python
tool = language_tool_python.LanguageTool('en-US')
text = input("Enter a sentence: ")
matches = tool.check(text)
for match in matches:
 print("Mistake:", match.message)
 print("Suggestion:", match.replacements)
 print("-----")