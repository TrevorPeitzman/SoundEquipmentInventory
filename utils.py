import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import socket


scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").get_worksheet(0)  # Open the Backend, look at sheet 2


def datetimearray():
    current = datetime.datetime.now()  # https://www.w3schools.com/python/python_datetime.asp
    log = [str(current.date()), str(current.strftime("%X"))]
    return log


def quitlog():
    row = datetimearray() + ["USR TERMINATE", "QUIT"]
    sheet.append_row(row)


def internet_on():
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        print("NO INTERNET CONNECTION. QUITTING.")
        f = open("log.txt", "a")
        f.write(datetimearray() + " INTERNET DOWN")
        f.close()
        pass
    return False
