import os
import eel

from engine.features.sounds import *
from engine.core.command import *
from engine.database.db import *
from engine.services.RGB import start_rgb


def start():

    rgb_ready = start_rgb()
    if rgb_ready:
        print("RGB system ready.")
    else:
        print("RGB system not available. Continuing without it.")

    eel.init("www")


    playAssistantSound()
    os.system('start msedge.exe --app="http://localhost:8000/index.html"')
    eel.start('index.html',mode=None,host='localhost',block=True)

    # os.system("taskkill /F /IM msedge.exe")

def closeJarvis():
    os.system("taskkill /F /IM msedge.exe")

