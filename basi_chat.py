print("Simple Rule-Based Chatbot")
print("Type 'bye' to exit")
while True:
 user_input = input("You: ").lower()
 if user_input == "bye":
    print("Bot: Goodbye! Have a nice day.")
    break
 elif "hello" in user_input or "hi" in user_input:
    print("Bot: Hello! How can I help you?")
 elif "how are you" in user_input:
    print("Bot: I am fine. Thank you!")
 elif "your name" in user_input:
    print("Bot: I am a simple rule-based chatbot.")
 elif "nlp" in user_input:
    print("Bot: NLP stands for Natural Language Processing.")
 elif "time" in user_input:
  import datetime
  print("Bot: Current time is",
        datetime.datetime.now().strftime("%H:%M:%S")) 
else:
    print("Bot: Sorry, I don't understand that.")