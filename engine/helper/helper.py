import re
import random

def extract_yt_term(command):
    # Define a regular expression pattern to capture the song name
    pattern = r'play\s+(.*?)\s+on\s+youtube'
    # Use re.search to find the match in the command
    match = re.search(pattern, command, re.IGNORECASE)
    # If a match is found, return the extracted song name; otherwise, return None
    return match.group(1) if match else None

def remove_words(input_string, words_to_remove):
    # Split the input string into words
    words = input_string.split()

    # Remove unwanted words
    filtered_words = [word for word in words if word.lower() not in words_to_remove]

    # Join the remaining words back into a string
    result_string = ' '.join(filtered_words)

    return result_string

def fetch_line(response,num_lines=4):
    text = str(response)
    lines = text.split('\n')
    fetched_lines = '\n'.join(lines[:num_lines])
    return fetched_lines
#Nmap Port
def extract_port_info(nmap_output):
    port_lines = []
    capture = False

    for line in nmap_output.splitlines():
        if line.startswith("PORT"):
            capture = True
            port_lines.append(line)
            continue

        if capture:
            if line.strip() == "":
                break
            port_lines.append(line)

    return "\n".join(port_lines)

#space 

def has_space(text):
    if " " in text:
        return True
    else:
        return False

# formate port info
def format_port_info(port_output):
    lines = port_output.strip().split("\n")
    result = []

    # skip header line
    for line in lines[1:]:
        parts = line.split()

        if len(parts) >= 3:
            port = parts[0]
            state = parts[1]
            service = parts[2]

            sentence = f"Port {port} is {state} and the service used is {service}"
            result.append(sentence)

    return "\n".join(result)

def voice_out_choice():
    numbers = [1,2,3,4,5,6,7,8,9,10,11]
    random_number = random.choice(numbers)
    return random_number
    # print("Random number:", random_number)


