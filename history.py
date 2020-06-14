import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").sheet1  # Open the Backend, look at sheet 1


def check_in(barcode: str):
    """ Check back in item barcode """
    # Log the current date and time, then split it into two printable outputs
    log = datetime.datetime.now()   # https://www.w3schools.com/python/python_datetime.asp
    date = str(log.date())
    time = str(log.strftime("%X"))  # %X - means 24hr clock w/out miliseconds

    # Append row to inventory sheet. Requires array of strings.
    row = [date, time, barcode, "SHOP"]
    sheet.append_row(row)


def check_out(barcode: str, new_location: str):
    """ Check out item barcode to new_location """
    # Log the current date and time, then split it into two printable outputs
    log = datetime.datetime.now()   # https://www.w3schools.com/python/python_datetime.asp
    date = str(log.date())
    time = str(log.strftime("%X"))  # %X - means 24hr clock w/out miliseconds

    # Append row to inventory sheet. Requires array of strings.
    row = [date, time, barcode, new_location]
    sheet.append_row(row)