import gspread
from oauth2client.service_account import ServiceAccountCredentials
from pprint import pprint


# use creds to create a client to interact with the Google Drive API
scope = ["https://spreadsheets.google.com/feeds",'https://www.googleapis.com/auth/spreadsheets',
         "https://www.googleapis.com/auth/drive.file","https://www.googleapis.com/auth/drive"]
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

# Find a workbook by name and open the first sheet
# Make sure you use the right name here.
sheet = client.open("Legislators 2017").sheet1

# Extract and print all of the values
list_of_hashes = sheet.get_all_records()

data = sheet.get_all_records()

row = sheet.row_values(1)
col = sheet.col_values(1)

cell = sheet.cell(1, 1)

insertRow = ["hello", "test", 1001, "out"]
sheet.insert_row(insertRow, 9)
sheet.append_row(insertRow)

pprint(cell)
