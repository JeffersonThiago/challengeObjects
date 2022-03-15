import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds',
'https://www.googleapis.com/auth/drive']


creds = ServiceAccountCredentials.from_json_keyfile_name('teste-344216-583c364fef50.json', scope)
client = gspread.authorize(creds)

def sheet_object(sheet_name, work_sheet_index):
    sheet = client.open(sheet_name).get_worksheet(work_sheet_index)
    return sheet


def get_spread_sheet_data(sheet_object):
    data = sheet_object.get_all_values()[1:11]
    return data

def update_spread_sheet(sheet_object, content):
    sheet_object.update('A13', content)



# def GetSpreadsheetData(sheet_name, work_sheet_index):
#     sheet = client.open(sheet_name).get_worksheet(work_sheet_index)
#     return sheet.get_all_values()[1:]
# data = GetSpreadsheetData(sheet_name, work_sheet_index)

