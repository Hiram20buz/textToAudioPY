from gtts import gTTS
from pydub import AudioSegment
from pydub.playback import play

def text_to_speech(text):
    tts = gTTS(text)
    tts.save("output.mp3")  # Save the speech to a file

def main():
    text = "Hello, how are you?"
    text_to_speech(text)

    # Load the audio file and play it
    sound = AudioSegment.from_mp3("output.mp3")
    play(sound)

if __name__ == "__main__":
    main()

