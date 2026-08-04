#assostant function
from engine.voice.speakFunction import speak
from engine.voice.takecommad import takecommand

#database
import sqlite3

#UI interaction
import eel


def readFile():

    con = sqlite3.connect("jarvis.db")
    cursor = con.cursor() 
    
    speak("Which file you want to listen? stored in databse or defualt file")
    ans = takecommand()
    if "database" in ans:
        speak("Please provide the file name to read.")
        file = takecommand()
        try:
            cursor.execute(
                'SELECT path FROM sys_videoFiles WHERE name IN (?)', (file,))
            results = cursor.fetchall()
            if len(results) != 0:
                with open(results[0][0], "r") as code_file:
                    content = code_file.read()
                eel.receiverText(str(content))
                # speak(f"The content of {file_name} is as follows:")
                speak(content)
        except FileNotFoundError:
            speak("File Not found in database") 

    else:      
        speak("Please provide the file name to read.")
        file_name = takecommand()
        try:
            with open(f"./UserText/{file_name}.txt", "r") as code_file:
                content = code_file.read()
            eel.receiverText(str(content))
            speak(f"The content of {file_name} is as follows:")
            speak(content)
        except FileNotFoundError:
            speak(f"Sorry, I could not find a file named {file_name}.txt in the UserText folder.")

def writeToFile():
    speak("What would you like to write in to file?")
    txt = takecommand()
    speak("Any thing else? if yes than say add more")
    check = takecommand()
    if "yes" in check or "yeah" in check or "add more" in check:
        while True:
            speak("What else you want to add?")
            more_txt = takecommand()
            txt = txt + " " + more_txt
            speak("Anything else?")
            check = takecommand()
            if "yes" in check or "add" in check or "ofcourse" in check:
                continue
            else:
                break
    speak("What whould you like to name the file?")
    file_name = takecommand()
    with open(f"../user_writed_files/{file_name}.txt", "w") as code_file:
        code_file.write(str(txt))
    eel.receiverText(str(txt))
    speak(f"This is written into file and saved to {file_name}.txt file.")
