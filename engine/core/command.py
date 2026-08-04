#system commands and functions
import os

#UI functions
import eel

#helper functions
from engine.helper.helper import has_space

#sevices
from engine.services.RGB import set_color

#voice functions
from engine.voice.takecommad import takecommand
from engine.voice.speakFunction import speak

#state management
import engine.config.state as state


@eel.expose
def allCommands(message=1):
    print("Message received in allCommands:", message)
    if message == 1 :
        query = takecommand()
        print(query)
        eel.senderText(query)

    else:
        
        query = message
        eel.senderText(query)
    try:

        #modes
        if "battle" in query:
            speak("Activating battle mode.")
            eel.setTheme("red")()
            set_color(255, 0, 0)  # Red color for battle mode

        elif "pookie" in query or "pokemon" in query or "pink" in query:
            speak("Activating pookie mode.")
            eel.setTheme("pink")()
            set_color(255, 20, 147)  # Pink color for pookie mode

        elif "normal" in query:
            speak("Returning to normal mode.")
            eel.setTheme("blue")()
            set_color(25, 0, 255)  # Blue color for normal mode

        elif "peace" in query:
            speak("peacefull mode is now active.")
            eel.setTheme("orange")()
            set_color(255, 140, 0)

        #pre recoreded sounds and dialogues
        elif "don't like" in query:
            from engine.features.sounds import gamansanthal
            gamansanthal()

        elif "siri" in query:
            from engine.features.sounds import bajuma
            bajuma()

        elif "violence" in query:
            from engine.features.sounds import Violence
            Violence()

        elif "damage" in query:
            from engine.features.sounds import cd
            cd()
        
        elif "full form" in query:
            speak("Just a… Rather Very Intelligent System. If you do not like it… you cannot change it. Because… my boss likes it.")            

        elif "introduce" in query:
            from engine.features.sounds import playAssistantSoundStart
            playAssistantSoundStart()
            

        elif "about yourself" in query:
            from engine.features.sounds import playAssistantSoundStart
            playAssistantSoundStart()
            

        elif "wake up" in query:
            from engine.features.sounds import daddyHome
            daddyHome()
            

        elif "password" in query:
            from engine.features.sounds import lejane
            lejane()
            

        elif "steam" in query:
            from engine.features.sounds import playGamingSoundStart
            playGamingSoundStart()
            set_color(255, 0 ,0)
            speak("Steam is opening boss, get ready for gaming. Jarvis is out")
            os.startfile(r"C:\Program Files (x86)\Steam\steam.exe")
            from main import closeJarvis
            closeJarvis()
            exit()
            

        elif "madara" in query:
            from engine.features.sounds import MadaraUchiha
            MadaraUchiha()  
            
        
        elif "pain" in query:
            from engine.features.sounds import pain
            pain()
            

        elif "scared" in query:
            from engine.features.sounds import Fear
            Fear()
            

        elif "legend" in query:
            from engine.features.sounds import ghar
            ghar()
            

        elif "tale" in query:
            from engine.features.sounds import The_Tale_of_naruto
            The_Tale_of_naruto()
            

        elif "itachi" in query:
            from engine.features.sounds import itachi
            itachi()
            
        
        elif "naruto" in query or "Naruto" in query or "Naruto Uzumaki" in query:
            from engine.features.sounds import narutoUzumaki
            narutoUzumaki()
            

        #opening apps and websites
        elif "open" in query:
            from engine.features.openApps import openCommand
            openCommand(query)
            

        #playing youtube videos
        elif "on youtube" in query:
            from engine.features.external_apps.youtubeFunction import PlayYoutube
            PlayYoutube(query)
            

        #nmap
        elif "scan" in query:
            from engine.features.cyberSecurity.nmap import nmap_scanning
            nmap_scanning()

        #osint
        elif "osint" in query or "information gathering" in query or "gather information" in query:
            from engine.features.cyberSecurity.osint import osint_main
            osint_main()

        #code generation
        elif "generate code" in query or "developer mode" in query or "code" in query:
            from engine.features.ai import generate_code
            generate_code()
            
        #writing and reading files
        elif "write" in query or "save to file" in query:
            from engine.features.readAndWrite import writeToFile
            writeToFile()
            

        elif "read" in query or "open file" in query or "show me file" in query:
            from engine.features.readAndWrite import readFile
            readFile()
            

        #chatBot
        elif "from bot" in query or "chatbot" in query or "chat with bot" in query or "from your point of view" in query or "as per your information" in query or "as your pov" in query:
            print("chatBot")
            from engine.features.ai import chatBot
            chatBot(query)
            

        #opening video files
        elif "video" in query:
            from engine.features.videoPlayFunction import playVideoFile
            playVideoFile()
            

        #sending whatsapp messages
        elif "send message" in query or "message" in query or "whatsapp" in query:
            from engine.features.external_apps.whatsappMessage import whatsApp
            whatsApp()
            

        #exiting
        elif "exit" in query or "quit" in query or "close" in query:
            speak("Copy that boss! jarvis is out")
            from main import closeJarvis
            closeJarvis()
            exit()

        elif "na" in query or "nahi" in query or "no" in query or "cancel" in query:
            speak("Okay boss, command cancelled.")

        else: 
            speak("The Command is not recognized. To add command go to settings or would you like to let me search over internet. if yes than say search")
            ans = takecommand()
            if "search" in ans:
                speak("Searching...")
                print("chatBot")
                from engine.features.ai import chatBot
                chatBot(query)
            

    except Exception as e:
        print(e)
        speak("The Command is not recognized. To add command go to settings")
        

    eel.ShowHood()


@eel.expose
def engine_loop(message=1):
    print("Engine loop called with message:", message)
    current_state = state.get_status()
    if current_state == 1:
        print("Executing allCommands from engine_loop")
        allCommands(message)
        state.set_status(0)

