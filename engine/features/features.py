# import os
# import re
# from shlex import quote
# import sqlite3
# import struct
# import subprocess
# import time
# import webbrowser
# from playsound import playsound
# import eel
# import pvporcupine
# import pyaudio
# import pyautogui
# from engine.command import allCommands, speak ,takecommand
# from engine.config import ASSISTANT_NAME
# import pywhatkit as kit
# import subprocess
# import pygame
# import pywhatkit
# from engine.helper.helper import extract_port_info , format_port_info
# from engine.helper.helper import extract_yt_term, remove_words , fetch_line
# from hugchat import hugchat
# from engine import state


# #Click

# @eel.expose


# def findContact(query):
    
#     words_to_remove = [ASSISTANT_NAME, 'make', 'a', 'to', 'phone', 'call', 'send', 'message', 'wahtsapp', 'video']
#     query = remove_words(query, words_to_remove)

#     try:
#         query = query.strip().lower()
#         cursor.execute("SELECT mobile_no FROM contacts WHERE LOWER(name) LIKE ? OR LOWER(name) LIKE ?", ('%' + query + '%', query + '%'))
#         results = cursor.fetchall()
#         print(results[0][0])
#         mobile_number_str = str(results[0][0])

#         if not mobile_number_str.startswith('+91'):
#             mobile_number_str = '+91' + mobile_number_str

#         return mobile_number_str, query
#     except:
#         speak('not exist in contacts')
#         return 0, 0


# #nmap



