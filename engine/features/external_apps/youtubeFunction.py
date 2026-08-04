# assistant functions
from engine.voice.speakFunction import speak
from engine.helper.helper import extract_yt_term
import pywhatkit as kit

def PlayYoutube(query):
    search_term = extract_yt_term(query)
    print(search_term)
    if search_term != None:
        speak("Playing "+search_term+" on YouTube")
        kit.playonyt(search_term)
    else:
        speak("Not Found")