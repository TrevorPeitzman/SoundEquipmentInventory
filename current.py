import gspread
import utils
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").get_worksheet(1)  # Open the Backend, look at sheet 2


def add_entry(barcode: str, location: str):
    """ Add entry in 'CurrentState' sheet denoting new item barcode checked in/out to location """
    # Log the current date and time and append row to inventory sheet
    row = utils.datetimearray() + [barcode, location]
    sheet.append_row(row)


def where_is(barcode: str):
    """ Somewhat self-explanatory function that returns the current location of barcode """
    try:
        cell = sheet.find(barcode)
        location = sheet.cell(cell.row, cell.col + 1).value
        return str(location)

    except:
        return str("nowhere. NO CURRENT LOCATION FOR " + barcode)


def update_location(barcode: str, location: str):
    """ Change the last location of barcode to location """
    try:
        cell = sheet.find(barcode)
        sheet.update_cell(cell.row, cell.col + 1, location)
        sheet.update_cell(cell.row, cell.col - 2, utils.datetimearray()[0])
        sheet.update_cell(cell.row, cell.col - 1, utils.datetimearray()[1])

    except:
        add_entry(barcode, location)
        print(barcode + " has no previous location.")

