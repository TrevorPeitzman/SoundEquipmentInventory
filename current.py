import gspread
import utils
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
          "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").get_worksheet(1)  # Open the Backend, look at sheet 2


def check_in(barcode: str):
    """ Update location of item barcode to 'SHOP' """
    # Log the current date and time and append row to inventory sheet
    row = utils.datetimearray() + [ barcode, "SHOP" ]
    sheet.append_row(row)


def whereis(barcode: str):
    print("lol")
    