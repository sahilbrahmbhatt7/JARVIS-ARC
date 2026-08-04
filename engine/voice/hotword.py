import pvporcupine
import pyaudio
import struct
import time
import engine.config.state as state
import pyautogui as autogui
from engine.config.NAME import ASSISTANT_NAME


def hotword():
    porcupine=None
    paud=None
    audio_stream=None
    try:
       
        # pre trained keywords as define in readme file 
        porcupine=pvporcupine.create(keywords=[ASSISTANT_NAME,]) 
        paud=pyaudio.PyAudio()
        audio_stream=paud.open(rate=porcupine.sample_rate,channels=1,format=pyaudio.paInt16,input=True,frames_per_buffer=porcupine.frame_length)
        
        # loop for streaming
        while True:
            keyword=audio_stream.read(porcupine.frame_length)
            keyword=struct.unpack_from("h"*porcupine.frame_length,keyword)

            # processing keyword comes from mic 
            keyword_index=porcupine.process(keyword)

            # checking first keyword detetcted for not
            if keyword_index>=0:
                
                # allCommands()

                # pressing shorcut key win+j this will press virtually so user can activate jarvis without pressing shortcut key
                
                status = state.get_status()   
                if status == 0:
                    print("hotword detected")
                    autogui.keyDown("win")
                    autogui.press("j")
                    time.sleep(2)
                    autogui.keyUp("win")
                    state.set_status(1)
                
    except:
        # it will reset the librery
        if porcupine is not None:
            porcupine.delete()
        if audio_stream is not None:
            audio_stream.close()
        if paud is not None:
            paud.terminate()
