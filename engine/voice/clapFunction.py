import sounddevice as sd
import numpy as np
import time
import engine.config.state as state
import pyautogui as autogui

THRESHOLD = 0.6
MAX_DURATION = 0.10
CLAP_WINDOW = 1.0
COOLDOWN = 0.5
PEAK_RATIO = 4.0

clap_times = []
sound_start = None
last_trigger_time = 0



def listen_clap():
    print("👂 Listening for double clap...")

    def detect(indata, frames, time_info, status):
        global sound_start, clap_times, last_trigger_time

    

        audio = indata[:, 0]
        volume = np.linalg.norm(audio)
        peak = np.max(np.abs(audio))
        avg = np.mean(np.abs(audio)) + 1e-6

        current_time = time.time()

        if peak / avg < PEAK_RATIO:
            return

        if volume > THRESHOLD and sound_start is None:
            sound_start = current_time

        elif volume <= THRESHOLD and sound_start is not None:
            duration = current_time - sound_start
            sound_start = None

            if duration < MAX_DURATION:
                if current_time - last_trigger_time > COOLDOWN:
                    # print("👏 Sharp clap detected")

                    clap_times.append(current_time)
                    if len(clap_times) > 2:
                        clap_times.pop(0)

                    if len(clap_times) == 2:
                        if clap_times[1] - clap_times[0] < CLAP_WINDOW:
                            last_trigger_time = current_time
                            clap_times.clear()

                            status = state.get_status()   
                            print("🔥 Double Clap Detected!")
                            print(status)
                            if status == 0:
                                autogui.keyDown("win")
                                autogui.press("o")
                                autogui.keyUp("win")
                                print("🔥 DOUBLE CLAP ACTIVATED!")
                                print("Real Activation Sent to Jarvis")
                                state.set_status(1)
                                print("Status Updated to 1")


    with sd.InputStream(callback=detect):
        while True:
            time.sleep(0.1)

        