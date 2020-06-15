import gspread
import utils
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").get_worksheet(1)  # Open the Backend, look at sheet 2


def add_entry(barcode: str, location: str):
    """ Update location of item barcode to 'SHOP' """
    # Log the current date and time and append row to inventory sheet
    row = utils.datetimearray() + [barcode, location]
    sheet.append_row(row)


def where_is(barcode: str):
    try:
        cell = sheet.find(barcode)
        location = sheet.cell(cell.row, cell.col + 1).value
        return location

    except:
        return "Unable to locate " + barcode


def update_location(barcode: str, location: str):
    try:
        cell = sheet.find(barcode)
        sheet.update_cell(cell.row, cell.col + 1, location)

    except:
        print("Unable to locate " + barcode + ".")

