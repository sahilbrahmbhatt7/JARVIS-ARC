# engine/voice/jarvis_voice.py

from TTS.api import TTS
import torch
import numpy as np
import sounddevice as sd
import threading

tts_lock = threading.Lock()

device = "cuda" if torch.cuda.is_available() else "cpu"
print("Loading TTS model on:", device)

tts = TTS("tts_models/en/vctk/vits", progress_bar=False).to(device)


def generate_audio(text):
    with tts_lock:
        wav = tts.tts(
            text=text,
            speaker="p251",
            speed=0.25
        )

        wav = np.array(wav) * 1.5
        wav = np.clip(wav, -1.0, 1.0)

        sd.play(wav, tts.synthesizer.output_sample_rate)
        sd.wait()