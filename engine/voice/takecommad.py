import eel
import speech_recognition as sr

@eel.expose
def takecommand():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        eel.DisplayMessage("Listening...")

        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)

        audio = r.listen(source, 10, 6)

    try:
        print("Recognaizing...")
        eel.DisplayMessage("Recognaizing...")
        query = r.recognize_google(audio, language= 'en-in')
        print(f"User Said: {query}")
        eel.DisplayMessage(query)
        

    except Exception as e:
        return ""
    
    return query.lower()