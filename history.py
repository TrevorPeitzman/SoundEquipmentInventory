import gspread
import utils
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").get_worksheet(0)  # Open the Backend, look at sheet 1


def check_in(barcode: str):
    """ Add entry in 'History' sheet denoting item barcode checked in """
    # Log the current date and time and append row to inventory sheet
    row = utils.datetime_array() + [barcode, "SHOP"]
    sheet.append_row(row)


def check_out(barcode: str, new_location: str):
    """ Add entry in 'History' sheet denoting item barcode checked out to new_location """
    # Append row of date, time , barcode and location to History sheet.
    row = utils.datetime_array() + [barcode, new_location]
    sheet.append_row(row)
