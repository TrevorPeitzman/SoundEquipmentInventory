import gspread
import datetime
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint

scope = [ "https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive" ]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").sheet1  # Open the Backend, look at sheet 1

print("Welcome to the Sound Equipment Inventory System\nPlease scan an item barcode to begin.")


def main():
    while True:
        initcode = input("Barcode: ")

        try:
            str(initcode)
        except:
            print("Non-readable barcode entered. Please try again.")
            main()

        if (str(initcode) == "SHOP"):
            check_in(input("Scan Item Code: "))


# Function to check back in a given item barcode
def check_in(barcode: str):
    # Log the current date and time, then split it into two printable outputs
    log = datetime.datetime.now()   # https://www.w3schools.com/python/python_datetime.asp
    date = str(log.date())
    time = str(log.strftime("%X"))  # %X - means 24hr clock w/out miliseconds

    # Append row to inventory sheet. Requires array of strings.
    row = [date, time, barcode, "SHOP"]
    sheet.append_row(row)


check_in("poof")
