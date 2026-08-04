#database
import sqlite3

#assistant functions
from engine.voice.speakFunction import speak
from engine.voice.takecommad import takecommand

#os function
import os

def playVideoFile():
        
        con = sqlite3.connect("jarvis.db")
        cursor = con.cursor()

        speak("give me the keyword to play or open the file?")
        query = takecommand()     

        try:
                cursor.execute(
                    'SELECT path FROM sys_videoFiles WHERE name IN (?)', (query,))
                results = cursor.fetchall()
                if len(results) != 0:
                    speak("Opening "+query)
                    os.startfile(results[0][0])
        except:
                speak("some thing went wrong")