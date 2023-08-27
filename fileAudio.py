from gtts import gTTS
from playsound import playsound

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")  # Save the speech to a file
    playsound("output.mp3")  # Play the saved speech using playsound

def main():
    # Read text from a text file
    with open("input.txt", "r") as file:
        text = file.read()

    text_to_speech(text)

if __name__ == "__main__":
    main()

