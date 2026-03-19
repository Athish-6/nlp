import pyttsx3
engine = pyttsx3.init()
engine.save_to_file("Speech Processing using Python", 
"output_audio.mp3")
engine.runAndWait()
print("Audio file saved successfully")