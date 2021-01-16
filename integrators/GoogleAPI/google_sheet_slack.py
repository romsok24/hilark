from __future__ import print_function
import os, pickle, requests, json
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

# Below code is based on Google examples here: https://developers.google.com/sheets/api/quickstart/python
# If modifying these scopes, delete the file token.pickle.
exec(open('psikuta/config.py').read())

def main():
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'psikuta/credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                range=SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])


    if not values:
        print('[INF] Brak danych w arkuszu.')
    else:
        with open('psikuta/ostatni-wiersz.json','r')  as json_ostatni_r:
            lokalny_wiersz = json.load(json_ostatni_r)
            if lokalny_wiersz[1] == values[-1][1]:
                if lokalny_wiersz[5] == values[-1][5]:
                    print(f'Brak zmian w rejestrze zadań IT: ostatni nr w rej: { lokalny_wiersz[1] } vs w jsonie lokalnym: { values[-1][1] }')
                else:
                    print(f'Zmiana statusu zadania nr {values[-1][1]} ( {values[-1][4]} ) zostanie zapisane do jsona.')
                    with open('psikuta/ostatni-wiersz.json','w') as json_ostatni_w:
                        json.dump(values[-1], json_ostatni_w)
                        sl_payload = {
                            'channel': '#zadaniait',
                            'username': 'Aktualizacja zadania',
                            'text': 'W rejestrze zadań IT zaktualizowano zadanie o nr ' + values[-1][1] +'\nTreść zadania: ' + values[-1][4] + '\n Zmiana statusu z: ' + lokalny_wiersz[5] + '\n na: ' + values[-1][5] ,
                            'icon_emoji': ':repeat_one:'
                        }
                        r = requests.post(sl_url,data=json.dumps(sl_payload).replace('done',':white_check_mark: Done'))
                        print('Slack send %s' % {json.dumps(sl_payload).replace('done',':white_check_mark: Done')} )
                        print(f'Zmiana statusu')
            else:
                print(f'Nowe zadanie o nr {values[-1][1]} ( {values[-1][4]} ) zostanie zapisane do jsona.')
                with open('psikuta/ostatni-wiersz.json','w') as json_ostatni_w:
                    json.dump(values[-1], json_ostatni_w)
                sl_payload = {
                    'channel': '#zadaniait',
                    'username': 'Nowe zadanie',
                    'text': '<@aleksander> W rejestrze zadań IT utworzono nowe zadanie o nr ' + values[-1][1] +'\nTreść zadania: ' + values[-1][4] + '\n Utworzono dnia: ' + values[-1][3] + '\n Status: ' + values[-1][5] ,
                    'icon_emoji': ':new:'
                }
                r = requests.post(sl_url,data=json.dumps(sl_payload).replace('done',':white_check_mark: Done'))
                print('Slack send %s' % {json.dumps(sl_payload).replace('done',':white_check_mark: Done')} )

if __name__ == '__main__':
    main()
