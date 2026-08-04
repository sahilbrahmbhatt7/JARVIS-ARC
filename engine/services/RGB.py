import subprocess
import time
import atexit
from openrgb import OpenRGBClient
from openrgb.utils import RGBColor

client = None
keyboard = None

OPENRGB_PATH = r"C:\Program Files\OpenRGB\OpenRGB.exe"
PORT = 6742


# ----------------------------
# START RGB SYSTEM
# ----------------------------
def start_rgb():
    global client, keyboard

    try:
        client = OpenRGBClient(port=PORT)
        print("✅ Connected to OpenRGB")
    except:
        print("⚠ OpenRGB not running. Starting server...")
        subprocess.Popen(
            f'"{OPENRGB_PATH}" --server --startminimized',
            shell=True
        )
        time.sleep(5)

        try:
            client = OpenRGBClient(port=PORT)
            print("✅ Connected after starting server")
        except:
            print("❌ Failed to connect to OpenRGB")
            return False

    try:
        for device in client.devices:
            if "keyboard" in device.name.lower():
                keyboard = device
                print("🎹 Keyboard detected:", device.name)
                break

        if keyboard is None:
            print("❌ No keyboard found")
            return False

    except Exception as e:
        print("Device error:", e)
        return False

    return True


# ----------------------------
# SET COLOR (MAIN FUNCTION)
# ----------------------------
def set_color(r, g, b):
    if keyboard is None:
        print("RGB not initialized")
        return

    try:
        keyboard.set_color(RGBColor(r, g, b))
        print(f"🎨 Color set to ({r}, {g}, {b})")
    except Exception as e:
        print("Color error:", e)


# ----------------------------
# CLEAN EXIT
# ----------------------------
def shutdown_rgb():
    global client
    if client:
        try:
            client.disconnect()
            print("🔌 RGB disconnected cleanly")
            exit(0)
        except:
            pass


atexit.register(shutdown_rgb)