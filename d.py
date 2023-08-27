from gtts import gTTS
import os
from playsound import playsound

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")  # Save the speech to a file
    playsound("output.mp3")  # Play the saved speech using playsound

text = "Hello, how are you?"
text_to_speech(text)

