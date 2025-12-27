from stt import speech_to_text
from tts import speak
from agent import agent_step

USER_TELUGU = []

print("🤖 ప్రభుత్వ పథకాల వాయిస్ ఏజెంట్ ప్రారంభించబడింది")

while True:
    turn_id, raw_text = speech_to_text()

    if turn_id is None:
        print("")
        break

    print("📝 వినియోగదారు:", USER_TELUGU[turn_id])

    response = agent_step(turn_id)
    print("🤖 ఏజెంట్:", response)

    speak(response)
