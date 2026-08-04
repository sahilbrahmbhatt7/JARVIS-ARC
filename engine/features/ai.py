# ai helper hugchat
from hugchat import hugchat

#helper functions
from engine.helper.helper import fetch_line

#assistant functions
from engine.voice.speakFunction import speak
from engine.voice.takecommad import takecommand
from engine.config import state

#UI interaction
import eel

@eel.expose
def generate_code():
    speak("Please describe the functionality you want in the code.")
    code_description = takecommand()
    speak("Generating code based on your description. Please wait.")
    code_response = devloperNeeds(code_description)
    speak("Code Generated Successfully. what whould you like to name the file?")
    file_name = takecommand()
    # Save the generated code to a text file
    with open(f"./Code_Is_Here/{file_name}.txt", "w") as code_file:
        code_file.write(str(code_response))
    eel.receiverText(str(code_response))
    speak(f"The code has been generated and saved to {file_name}.txt file.")
    state.set_status(0)

def devloperNeeds(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    print(response)
    return response

def chatBot(query):
    user_input = query.lower()
    chatbot = hugchat.ChatBot(cookie_path="engine\cookies.json")
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)
    response = chatbot.chat(user_input)
    fres = fetch_line(response)
    speak(fres)
    speak("would you like to save this response in a text file?")
    check = takecommand().lower()
    if "yes" in check or "sure" in check or "of course" in check or "yeah" in check:
        speak("what would you like to name it?")
        file_name = takecommand().lower()
        with open(f"./ChatBot_Output/{file_name}.txt", "w") as file:
            file.write(str(response))
        speak(f"The response has been generated and saved to {file_name}.txt file.")
    print(fres)
    return response

