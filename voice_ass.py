import speech_recognition as sr
import pyttsx3
import datetime

listener = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    print(text)
    engine.say(text)
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print("You said:", command)
            return command
    except:
        return ""

def run_assistant():
    command = take_command()

    if "hello" in command:
        speak("Hello! How can I help you?")

    elif "time" in command:
        current_time = datetime.datetime.now().strftime('%I:%M %p')
        speak("Current time is " + current_time)

    elif "bye" in command or "exit" in command or "stop" in command:
        speak("Goodbye!")
        exit()

    else:
        speak("Sorry, I did not understand")

while True:
    run_assistant()