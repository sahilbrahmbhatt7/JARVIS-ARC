#system
import os
import webbrowser

#assistant functions
from engine.voice.speakFunction import speak
from engine.config.NAME import ASSISTANT_NAME

#database
import sqlite3


def openCommand(query):

    con = sqlite3.connect("jarvis.db")
    cursor = con.cursor()

    query = query.replace(ASSISTANT_NAME, "")
    query = query.replace("open", "")
    query.lower()

    app_name = query.strip()

    if app_name != "":

        try:
            cursor.execute(
                'SELECT path FROM sys_command WHERE name IN (?)', (app_name,))
            results = cursor.fetchall()

            if len(results) != 0:
                speak("Opening "+query)
                os.startfile(results[0][0])

            elif len(results) == 0: 
                cursor.execute(
                'SELECT url FROM web_command WHERE name IN (?)', (app_name,))
                results = cursor.fetchall()
                
                if len(results) != 0:
                    speak("Opening "+query)
                    print("from here")
                    webbrowser.open(results[0][0])

                else:
                    speak("This application is not found in the database")
                    # try:
                    #     os.system('start '+query)
                    # except:
                    #     speak("not found")
        except Exception as e:
            print(e)
            speak("some thing went wrong")