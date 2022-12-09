import requests
import json
import time

TOKEN = '5526314084:AAGL5LqSz14D0urgu23ykxoSzWYFkAvaNI8' 

BOT_URL = f'https://api.telegram.org/bot{TOKEN}/' 

OFFSET = 0

def get_updates(offset):
    tg_requests = requests.get(BOT_URL + f'getUpdates?offset={offset}')
    try:
        tg_req_data = json.loads(tg_requests.text)
        return tg_req_data
    except Exception as er:
        print(er)

def send_message(chat_id,text):
    message_data = {
        'chat_id': chat_id,
        'text': text
    }
    try:
        requests.post(BOT_URL + 'sendMessage', data= message_data)
    except Exception as er:
        print(er)

def command_handler(command):
    if command == '/start':
        send_message(user_id, 'Привет!')


while True:
    time.sleep(2)

    try:
        bot_data = get_updates(OFFSET)
        print(bot_data)
        result = bot_data['result']
        if not result:
            continue
        
        OFFSET = result[0]['update_id']+1
        user_text = result[0]['message']['text']
        user_id = result[0]['message']['chat']['id']
        command_handler(user_text)
   
   
    except Exception as er:
        print(er)
        continue
    
    