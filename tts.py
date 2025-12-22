from gtts import gTTS
import sounddevice as sd
import soundfile as sf
import uuid
import os

def speak(text):
    filename = f"response_{uuid.uuid4().hex}.mp3"
    gTTS(text=text, lang="te").save(filename)

    data, sr = sf.read(filename)
    sd.play(data, sr)
    sd.wait()

    os.remove(filename)
