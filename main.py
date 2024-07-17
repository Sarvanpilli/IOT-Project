from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import pyttsx3
from RPLCD.i2c import CharLCD
from time import sleep
import pygame
import datetime
import os

SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']

def play_song():
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3")
    pygame.mixer.music.play()

def main():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('calendar', 'v3', credentials=creds)

    now = datetime.datetime.utcnow().isoformat() + 'Z'
    print('Getting the upcoming 10 events')
    events_result = service.events().list(calendarId='primary', timeMin=now, maxResults=10, singleEvents=True, orderBy='startTime').execute()
    events = events_result.get('items', [])

    if not events:
        print('No upcoming events found.')
        return

    engine = pyttsx3.init()
    lcd = CharLCD('PCF8574', 0x27, cols=16, rows=2)

    try:
        for event in events:
            start_time_str = event['start'].get('dateTime', event['start'].get('date'))
            start_time = datetime.datetime.fromisoformat(start_time_str)

            event_summary = f"Event: {event['summary']} at {start_time_str}"
            print(event_summary)
            engine.say(event_summary)
            
            lcd.clear()
            lcd.write_string(f'{event["summary"][:16]}')
            sleep(2)
            lcd.cursor_pos = (1, 0)
            lcd.write_string(f'at {start_time_str[:16]}')
            
            while datetime.datetime.now() < start_time:
                lcd.clear()
                current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                lcd.cursor_pos = (0, 0)
                lcd.write_string(f'{event["summary"][:16]}')
                lcd.cursor_pos = (1, 0)
                lcd.write_string(f'{current_time[:16]}')
                sleep(1)

            play_song()
            sleep(5)

        engine.runAndWait()
    except Exception as e:
        print(f'Error: {e}')
    finally:
        lcd.clear()

if _name_ == '_main_':
    main()
