import requests
import json
import time


TOKEN = '5986985385:AAFzeuAJnp7OnNu2_nOxPRkHM0WbD6QqD4o'

BOT_URL = f'https://api.telegram.org/bot{TOKEN}/'

OFFSET = 0

def get_updates(offset):
    tg_requests = requests.get(BOT_URL + f"getUpdates?offest={offset}")

    try:
       tg_req_data = json.loads(tg_requests.text)
       
       return tg_req_data

    except Exception as er:
        print(er)

def command_handler(text):

    if text == '/start':
        pass
    elif text == '/help':
        pass
    else:
        pass

while True:
    time.sleep(2)

    try:
        user_data = get_updates(OFFSET)
        result = user_data['result'][0]
        print(result)

        
    except Exception as er:
        print(er)