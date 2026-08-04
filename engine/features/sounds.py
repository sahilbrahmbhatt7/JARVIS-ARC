import time
import pygame
import engine.config.state as state
import eel

from engine.voice.speakFunction import speak

@eel.expose
def playAssistantSound():
    music_dir = "www\\assets\\vendore\\audio\\click.wav"

@eel.expose
def playAssistantSoundY():
    from engine.helper.helper import voice_out_choice
    choice = voice_out_choice()
    if choice == 1:
        speak("Yes sir")
    elif choice == 2:
        speak("How Can i help you?")
    elif choice == 3:
        speak("Yes Boss")
    elif choice == 4:
        speak("mister leader of the free galaxy is back. honer you!")
    elif choice == 5:
        speak("Finally Boss is here. Tell me what i can do for you boss")
    elif choice == 6:
        speak("Long time no see boss.")
    elif choice == 7:
        speak("yes mister leader of the free galaxy. how can i help you?")
    elif choice == 8:
        speak("look who is here. mister leader of the akatski")
    elif choice == 9:
        speak("yes my king!")
    elif choice == 10:
        speak("just say the word sir")
    elif choice == 11:
        speak("yes nemesis prime")    

@eel.expose
def bootLoading():
    music_dir = "www\\assets\\vendore\\audio\\bootload.wav"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   
    time.sleep(1)

    pygame.mixer.music.stop()  
    state.set_status(0) 


#start up voice

def playAssistantSoundStart():
    music_dir = "www\\assets\\vendore\\audio\\JARVISStartup.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(21)

    pygame.mixer.music.stop()   


def gamansanthal():
    music_dir = "www\\assets\\vendore\\audio\\gamanSantahl.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(29)

    pygame.mixer.music.stop()   


def Violence():
    music_dir = "www\\assets\\vendore\\audio\\Violance.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(15)

    pygame.mixer.music.stop()   



def cd():
    music_dir = "www\\assets\\vendore\\audio\\colaitaldamage.mp3"

    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(17)

    pygame.mixer.music.stop()   



def pain():
    music_dir = "www\\assets\\vendore\\audio\\pain.mp3"

    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(18)

    pygame.mixer.music.stop()   



def bajuma():
    music_dir = "www\\assets\\vendore\\audio\\BajumaBesva.mp3"

    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(15)

    pygame.mixer.music.stop()   



def playGamingSoundStart():
    music_dir = "www\\assets\\vendore\\audio\\gamingStartJarvis.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(17)

    pygame.mixer.music.stop()   


def MadaraUchiha():
    music_dir = "www\\assets\\vendore\\audio\\wakeUptoReal.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()  
    time.sleep(80)

    pygame.mixer.music.stop()  


def lejane():
    music_dir = "www\\assets\\vendore\\audio\\rajKumar.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(14)

    pygame.mixer.music.stop()   


def Fear():
    music_dir = "www\\assets\\vendore\\audio\\FEAR.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(9)

    pygame.mixer.music.stop()   


def ghar():
    music_dir = "www\\assets\\vendore\\audio\\ghar_bhegu_tha_ne_bhai.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(2)

    pygame.mixer.music.stop()   


def gali():
    music_dir = "www\\assets\\vendore\\audio\\gali.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(7)

    pygame.mixer.music.stop()   


def daddyHome():
    music_dir = "www\\assets\\vendore\\audio\\daddyshome.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(13)

    pygame.mixer.music.stop()   


def narutoUzumaki():
    music_dir = "www\\assets\\vendore\\audio\\NarutoUzumaki.wav"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(38)

    pygame.mixer.music.stop()   


def The_Tale_of_naruto():
    music_dir = "www\\assets\\vendore\\audio\\The_Tale_of_naruto.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(23)

    pygame.mixer.music.stop()   


def itachi():
    music_dir = "www\\assets\\vendore\\audio\\itachi.mp3"
    pygame.mixer.init()

    pygame.mixer.music.load(music_dir)
    pygame.mixer.music.play()   

    time.sleep(3)

    pygame.mixer.music.stop()   