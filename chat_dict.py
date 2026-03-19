import datetime
responses = {
 "hello": "Hi there!",
 "hi": "Hello!",
 "how are you": "I'm doing well!",
 "what is your name": "I am a rule-based chatbot.",
 "nlp": "NLP means Natural Language Processing."
}
print("Chatbot is running... Type 'bye' to exit.")
while True:
 user_input = input("You: ").lower()
 if user_input == "bye":
    print("Bot: Goodbye!")
    break
 elif user_input in responses:
    print("Bot:", responses[user_input])
 elif "time" in user_input:
    print("Bot: Current time is", 
datetime.datetime.now().strftime("%H:%M:%S"))
 else:
    print("Bot: I don't understand. Can you rephrase?")