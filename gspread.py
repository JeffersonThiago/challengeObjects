from __future__ import print_function
import os.path
import challenge
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from selenium import webdriver


SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

def main():
    creds = None

    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'client_secret.json', SCOPES)
            creds = flow.run_local_server(port=0)
       

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    try:
        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId='1ZHAZaPhsU_VwsnIbcA5QXUYKepvs2TTlG-fckwtJG1M',
                                    range='Página1!A2:G11').execute()
        values = result.get('values', [])
        driver = webdriver.Chrome("C:/Users/jefferson.oliveira/Desktop/chromedriver.exe")
        pagina = challenge.rpachallenge(driver)

        pagina.accessSystem()
        pagina.startChallenge()
        
        for value in values:
            pagina.fillForm(value[0],value[1],value[2],value[3],value[4],value[5],value[6])

        resposta = pagina.getResults()


        result = sheet.values().update(spreadsheetId='1ZHAZaPhsU_VwsnIbcA5QXUYKepvs2TTlG-fckwtJG1M',
                            range='Página1!A13', valueInputOption="RAW", body={"values":resposta}).execute()

    except HttpError as err:
        print(err)

if __name__ == '__main__':
    main()