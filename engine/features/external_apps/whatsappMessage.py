#database connection
import sqlite3

#assistant functions
from engine.voice.speakFunction import speak
from engine.voice.takecommad import takecommand

#for sending whatsapp message
import pywhatkit


def whatsApp():
    con = sqlite3.connect("jarvis.db")
    cursor = con.cursor()

    speak("please give me the name of the contact to send message")
    name = takecommand().lower()
    cursor.execute(f"SELECT number FROM contacts WHERE name = '{name}'")
    result = cursor.fetchone()
    if result:
        number = result[0]
        speak("please give me the message to send")
        message = takecommand()
        speak("Do you want to add somthing else to the message? if yes then say add more")
        check = takecommand().lower()
        if "add more" in check:
            speak("what would you like to add?")
            extra = takecommand()
            message = message + " " + extra
        pywhatkit.sendwhatmsg_instantly(number, message, tab_close=True)
        speak(f"Message sent to {name} successfully")
    else:
        speak("contact not found in database")