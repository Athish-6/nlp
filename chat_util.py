import nltk
from nltk.chat.util import Chat, reflections
pairs = [
 ["hi|hello|hey", ["Hello!", "Hi there!"]],
 ["what is your name ?", ["I am an NLP chatbot."]],
 ["how are you ?", ["I am fine, thank you!"]],
 ["(.*) your name ?", ["My name is ChatBot."]],
 ["bye", ["Goodbye! Have a great day!"]],
]
chatbot = Chat(pairs, reflections)
print("Start chatting with the bot (type 'bye' to stop)")
chatbot.converse()