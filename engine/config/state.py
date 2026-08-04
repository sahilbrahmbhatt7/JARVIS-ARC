import eel

global status
status = 1

@eel.expose
def set_status(new_status=0):
    global status
    status = new_status
    print(f"Status set to {status}")

def get_status():
    global status
    print(f"Current status: {status}")
    return status