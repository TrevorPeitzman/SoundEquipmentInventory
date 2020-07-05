import gspread
import utils
import datetime
from oauth2client.service_account import ServiceAccountCredentials

scope = ["https://spreadsheets.google.com/feeds", 'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]

creds = ServiceAccountCredentials.from_json_keyfile_name("sei_creds.json", scope)

client = gspread.authorize(creds)

sheet = client.open("Inventory Backend").get_worksheet(1)  # Open the Backend, look at sheet 2


def add_entry(barcode: str, location: str):
    """ Add entry in 'CurrentState' sheet denoting new item barcode checked in/out to location """
    # Log the current date and time and append row to inventory sheet
    row = utils.datetime_array() + [barcode, location]
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
        cell = sheet.find(barcode, in_column=3)
        sheet.update_cell(cell.row, cell.col + 1, location)
        sheet.update_cell(cell.row, cell.col - 2, utils.datetime_array()[0])
        sheet.update_cell(cell.row, cell.col - 1, utils.datetime_array()[1])

    except:
        add_entry(barcode, location)
        print(barcode + " has no previous location.")


def get_retired():
    """ Returns an array of the items marked with location "RETIRE" in CurrentState sheet """
    retired = []
    cell_list = sheet.findall("RETIRE", in_column=4)

    for i in cell_list:
        item = sheet.cell(i.row, i.col - 1).value
        retired.append(str(item))

    return retired


def get_lost():
    nowarray = utils.datetime_array()[0]
    nowdate = datetime.date(int(nowarray[0:4]), int(nowarray[5:7]), int(nowarray[9:11]))
    criteriontime = utils.get_lostitem_time()

    all_itemdates = sheet.col_values(1)
    all_itemdates.remove("Date")
    lastdate = []
    lostitems = []
    lastplace = []
    row = 2

    for i in all_itemdates:
        if datetime.date(int(i[0:4]), int(i[5:7]), int(i[9:11])) < criteriontime:
            lastdate.append(sheet.cell(row, 1))
            lostitems.append(sheet.cell(row, 3))
            lastplace.append(sheet.cell(row, 4))
        row += 1

    print(criteriontime < nowdate)
    print(lostitems)
    return None
