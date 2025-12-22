import whisper
from text_normalizer import to_telugu

model = whisper.load_model("small")

AUDIO_FILES = [
    "input_clean.wav",
    "input2.wav",
    "input3.wav",
    "input4.wav"
]

current_index = 0

def speech_to_text():
    global current_index

    if current_index >= len(AUDIO_FILES):
        return None, None

    audio_file = AUDIO_FILES[current_index]
    turn_id = current_index
    current_index += 1

    result = model.transcribe(
        audio_file,
        language="te",
        task="transcribe",
        temperature=0.0
    )

    raw_text = result["text"]
    telugu_text = to_telugu(raw_text)

    return turn_id, telugu_text
