# UI interaction
import eel

#process
import subprocess

#assistant functions
from engine.voice.speakFunction import speak
from engine.voice.takecommad import takecommand
from engine.config import state

#helper functions
from engine.helper.helper import extract_port_info, format_port_info, has_space
from engine.voice.takecommad import takecommand






def run_nmap(target, scan_type):
    scan_commands = {
        "1": ["nmap", target],
        "2": ["nmap", "-F", target],
        "3": ["nmap", "-p-", target],
        "4": ["nmap", "-sV", target],
        "5": ["nmap", "-O", target],
        "6": ["nmap", "-A", target]
    }

    command = scan_commands.get(scan_type)

    
    result = subprocess.run(
        command,
        capture_output=True,
        text=True
    )

    return result.stdout

@eel.expose
def nmapMain(query,scanType):
    target = query

    scan_type = scanType
    # print(target,scan_type)

    full_output = run_nmap(target, scan_type)
    eel.receiverText(full_output)


    # Extract only ports
    port_info = extract_port_info(full_output)
    speak("this are the port information of the site")
    formated_port_info = format_port_info(port_info)
    speak(formated_port_info)
    speak("for more information check chatbox")

    print("\n===== PORT INFORMATION =====")
    if port_info:
        print(port_info)
    else:
        print("No port data found.")

    print("\n===== FULL NMAP OUTPUT =====")
    print(full_output)


def nmap_scanning():
    speak("please give me domain of that site you want to scan")
    domain = takecommand()
    while True:
        check = has_space(domain)
        if check:
            speak("please give me only domain not anything else")
            domain = takecommand()
        else:
            if domain:
                print("success..",domain)
                speak(f"Ok so now tell me which type of scan you want to perform with {domain}. there is many type of scan i can perform like.")
                speak("Basic, Fast scan, All Ports, Service Version, OS Detection")
                typeofscan = takecommand()
                speak(f"So you want to perform {typeofscan} on {domain}. it take some moment, for while you can seat back and relax")
                if "basic" in typeofscan:
                    scanType = "1"
                    from engine.features import nmapMain
                    nmapMain(domain,scanType)
                    state.set_status(0)
                    break
                elif "fast" in typeofscan:
                    scanType = "2"
                    from engine.features import nmapMain
                    nmapMain(domain,scanType)
                    state.set_status(0)
                    break
                elif "all" in typeofscan:
                    scanType = "3"
                    from engine.features import nmapMain
                    nmapMain(domain,scanType)
                    state.set_status(0)
                    break
                elif "service" in typeofscan:
                    scanType = "4"
                    from engine.features import nmapMain
                    nmapMain(domain,scanType)
                    state.set_status(0)
                    break
                elif "detection" in typeofscan:
                    scanType = "5"
                    from engine.features import nmapMain
                    nmapMain(domain,scanType)
                    state.set_status(0)
                    break
                elif "aggressive" in typeofscan:
                    scanType = "6"
                    from engine.features import nmapMain
                    nmapMain(domain,scanType)
                    state.set_status(0)
                    break
                else:
                    speak("i didn't perform that scan")
                    state.set_status(0)
                    break
            else:
                speak("Sorry I didnt get it")
                break