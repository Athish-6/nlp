import datetime
print("Hello! I am your assistant.")
command = input("How can I help you? ").lower()
if "time" in command:
 time = datetime.datetime.now().strftime("%H:%M:%S")
 print("Current time is:", time)
elif "hello" in command:
 print("Hello! How are you?")
elif "bye" in command:
 print("Goodbye!")
else:
 print("Sorry, I don't understand.")