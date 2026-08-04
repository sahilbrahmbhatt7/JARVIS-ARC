import requests
import dns.resolver
import whois
import re
from datetime import datetime

#UI interaction
import eel

#assistant functions
from engine.voice.speakFunction import speak
from engine.voice.takecommad import takecommand 
from engine.config import state


def write_report(text,RF):
    with open(RF, "a", encoding="utf-8") as f:
        f.write(text + "\n")

def banner(RF):
    write_report("="*60,RF)
    write_report("OSINT AUTOMATION REPORT",RF)
    write_report(f"Generated on: {datetime.now()}",RF)
    write_report("="*60,RF)


def whois_lookup(domain,RF):
    write_report("\n[WHOIS INFORMATION]",RF)
    try:
        data = whois.whois(domain)
        write_report(f"Domain: {domain}",RF)
        write_report(f"Registrar: {data.registrar}",RF)
        write_report(f"Creation Date: {data.creation_date}",RF)
        write_report(f"Expiration Date: {data.expiration_date}",RF)
        write_report(f"Emails: {data.emails}",RF)
    except Exception as e:
        write_report(f"WHOIS failed: {e}",RF)


def subdomain_enum(domain,RF):
    write_report("\n[SUBDOMAIN ENUMERATION]",RF)
    subs = ["www", "mail", "dev", "test", "api", "admin"]
    for sub in subs:
        try:
            full = f"{sub}.{domain}"
            dns.resolver.resolve(full, "A")
            write_report(f"[+] Found: {full}",RF)
        except:
            pass


def email_scrape(domain,RF):
    write_report("\n[EMAIL SCRAPING]",RF)
    try:
        url = f"https://{domain}"
        r = requests.get(url, timeout=10)
        emails = set(re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", r.text))
        if emails:
            for email in emails:
                write_report(f"[+] Email Found: {email}",RF)
        else:
            write_report("No emails found",RF)
    except:
        write_report("Website not reachable",RF)


def username_check(username,RF):
    write_report("\n[USERNAME ENUMERATION]",RF)
    platforms = {
        "GitHub": f"https://github.com/{username}",
        "x": f"https://x.com/{username}",
        "Instagram": f"https://www.instagram.com/{username}",
        "Facebook": f"https://www.facebook.com/{username}",
        "Reddit": f"https://www.reddit.com/user/{username}",
        "LinkedIn": f"https://www.linkedin.com/in/{username}",
        "snapchat": f"https://www.snapchat.com/add/{username}",
                
    }

    for site, url in platforms.items():
        r = requests.get(url)
        if r.status_code == 200:
            write_report(f"[+] {username} found on {site}",RF)
        else:
            write_report(f"[-] {username} not found on {site}",RF)


def github_search(keyword,RF):
    write_report("\n[GITHUB LEAK SEARCH]",RF)
    url = f"https://api.github.com/search/code?q={keyword}"
    headers = {"Accept": "application/vnd.github.v3+json"}

    try:
        r = requests.get(url, headers=headers)
        results = r.json().get("items", [])[:5]
        for item in results:
            write_report(f"[+] Possible leak: {item['html_url']}",RF)
    except:
        write_report("GitHub search failed",RF)


@eel.expose
def run_osint(domain, username):
    
    domain = domain.strip()
    username = username.strip()
    RF = f"../../../OSINT/{username}osint_report.txt"
    open(RF, "w").close()
    
    banner(RF)
    whois_lookup(domain,RF)
    subdomain_enum(domain,RF)
    email_scrape(domain,RF)
    username_check(username,RF)
    github_search(domain,RF)

    write_report("\nOSINT scan completed successfully.",RF)
    print(f"OSINT scan finished. Report saved as {username}osint_report.txt")
    return 1

def osint_main():
    speak("Please provide the target domain")
    domain = takecommand()
    speak("Please provide the username to search")  
    username = takecommand()
    speak(f"Starting OSINT scan for domain {domain} and username {username}")
    speak("Please wait while I gather the information.")  

    check = run_osint(domain, username)
    if check == 1:
        speak("OSINT scan completed successfully. Check the report in osint folder on desktop.")  
        state.set_status(0)          
    else:
        speak("OSINT scan failed. Please try again.")
        state.set_status(0)