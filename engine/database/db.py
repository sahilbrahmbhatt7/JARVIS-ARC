import csv
import sqlite3 #we use this database becuse this database is built in python
import eel
import io

con = sqlite3.connect("jarvis.db")
cursor = con.cursor()

    

@eel.expose
def addSys(key,path):

    keyword = key
    appPath = path

    query = "CREATE TABLE IF NOT EXISTS sys_command(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
    cursor.execute(query)

    query = f"INSERT INTO sys_command VALUES (null,'{keyword}', '{appPath}')"
    cursor.execute(query)
    con.commit()

@eel.expose
def addWeb(key,link):

    keyword = key
    webLink = link

    query = "CREATE TABLE IF NOT EXISTS web_command(id integer primary key, name VARCHAR(100), url VARCHAR(1000))"
    cursor.execute(query)

    query = f"INSERT INTO web_command VALUES (null,'{keyword}', '{webLink}')"
    cursor.execute(query)
    con.commit()

@eel.expose
def deleteSys(key):
    keyword = key

    query = f"DELETE FROM sys_command WHERE name = '{keyword}'"
    cursor.execute(query)
    con.commit()

@eel.expose
def deleteWeb(key):
    keyword = key

    query = f"DELETE FROM web_command WHERE name = '{keyword}'"
    cursor.execute(query)
    con.commit()

@eel.expose
def getWeb():
    # print("Fetching Web Apps...")

    query = "SELECT name, url FROM web_command"
    cursor.execute(query)

    data = cursor.fetchall() 

    # print("Web Apps:")
    # print(data)

    return data  

@eel.expose
def getSys():
    # print("Fetching System Apps...")

    query = "SELECT name, path FROM sys_command"
    cursor.execute(query)

    data = cursor.fetchall()  

    # print("System Apps:")
    # print(data)

    return data  

@eel.expose
def addVideo(key,link):

    keyword = key
    webLink = link

    query = "CREATE TABLE IF NOT EXISTS sys_videoFiles(id integer primary key, name VARCHAR(100), path VARCHAR(1000))"
    cursor.execute(query)

    query = f"INSERT INTO sys_videoFiles VALUES (null,'{keyword}', '{webLink}')"
    cursor.execute(query)
    con.commit()

@eel.expose
def deleteVideo(key):
    keyword = key

    query = f"DELETE FROM sys_videoFiles WHERE name = '{keyword}'"
    cursor.execute(query)
    con.commit()

@eel.expose
def getVideo():
    # print("Fetching System Apps...")

    query = "SELECT name, path FROM sys_videoFiles"
    cursor.execute(query)

    data = cursor.fetchall()  

    # print("System Apps:")
    # print(data)

    return data

@eel.expose
def addContact(name, number):
    name = name.lower()
    query = "CREATE TABLE IF NOT EXISTS contacts(id integer primary key, name VARCHAR(15), number VARCHAR(11))"
    cursor.execute(query)
    cursor.execute(f"INSERT OR IGNORE INTO contacts (name, number) VALUES ('{name}','{number}')")
    con.commit()


@eel.expose
def getContacts():
    cursor = con.cursor()
    cursor.execute("SELECT name, number FROM contacts")
    data = cursor.fetchall()
    print(eel._exposed_functions.keys())
    return data

@eel.expose
def deleteContact(name):
    cursor = con.cursor()
    cursor.execute(f"DELETE FROM contacts WHERE name = '{name}'")
    con.commit()

@eel.expose
def importContactsCSV(csv_text):
    print("Importing Contacts from CSV...")

    reader = csv.DictReader(io.StringIO(csv_text))

    for row in reader:
        name = row.get("name")
        number = row.get("number")

        if name and number:
            number = number.strip()

            # Ensure +91 format
            if not number.startswith("+91"):
                number = "+91" + number

            cursor.execute(f"INSERT OR IGNORE INTO contacts (name, number) VALUES ('{name.strip()}','{number}')")

    con.commit()
    getContacts()
    return "CSV Imported Successfully"


# while(1):
#     print("1.Web App")
#     print("2.System App")
#     print("3.Delete WebApp")
#     print("4.Delete System")
#     print("5.Exit")
#     ch = int(input("Enter Your Choice : "))
#     match ch:
#         case 1:
#             key = input("Enter Keyword : ")
#             link = input("Enter Link of the web app : ")
#             addWeb(key,link)
#             break
#         case 2:
#             key = input("Enter Keyword : ")
#             path = input("Enter path of app : ")
#             addSys(key,path)
#             break
#         case 3:
#             key = input("Enter Keyword : ")
#             deleteWeb(key)
#             break
#         case 4:
#             key = input("Enter Keyword : ")
#             deleteSys(key)
#             break
#         case 5:
#             exit()
#         case _:
#             exit()

