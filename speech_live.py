import speech_recognition as sr
import pyaudio 

r = sr.Recognizer()

with sr.Microphone() as source:
    print("Speak something...")
    r.adjust_for_ambient_noise(source, duration=1)
    audio = r.listen(source)

try:
    print("You said:")
    print(r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not recognize speech")
except sr.RequestError:
    print("Check your internet connection")