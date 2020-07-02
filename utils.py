import datetime
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import socket


def datetimearray():
    """ An SEI favorite. Return the famous datetimearrray for item logging purposes """
    current = datetime.datetime.now()  # https://www.w3schools.com/python/python_datetime.asp
    log = [str(current.date()), str(current.strftime("%X"))]
    return log


def internet_on():
    """ Test to see if the internet is working. If it isn't, log the date and time. """
    try:
        # connect to the host -- tells us if the host is actually reachable
        socket.create_connection(("www.google.com", 80))
        return True
    except OSError:
        print("NO INTERNET CONNECTION. QUITTING.")
        f = open("log.txt", "a")
        f.write(str(datetimearray()) + " INTERNET DOWN\n")
        f.close()
        exit(420)
        return False


internet_on()

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

history_sheet = client.open("Inventory Backend").get_worksheet(0)  # Open the Backend, look at sheet 1
currentstate_sheet = client.open("Inventory Backend").get_worksheet(1)  # Open the Backend, look at sheet 2
rules_sheet = client.open("Inventory Backend").get_worksheet(2)  # Open the Backend, look at sheet 3


def quitlog():
    """ Simply log the time and date that the user quit the system into the Backend sheet. """
    row = datetimearray() + ["USR TERMINATE", "QUIT"]
    history_sheet.append_row(row)



