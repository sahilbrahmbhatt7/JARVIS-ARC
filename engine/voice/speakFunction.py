import eel
from engine.voice.jarvis_voice import generate_audio


@eel.expose
def speak(text,stop=False):
    text = str(text)

    # UI updates stay here
    eel.DisplayMessage(text)
    eel.receiverText(text)

    # Audio engine call
    generate_audio(text)