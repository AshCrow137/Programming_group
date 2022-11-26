import requests
import json
import time
import teleblackjack



TOKEN = '5526314084:AAGL5LqSz14D0urgu23ykxoSzWYFkAvaNI8' 

BOT_URL = f'https://api.telegram.org/bot{TOKEN}/' 

OFFSET = 0 



def get_updates(offset):
    tg_requests = requests.get(BOT_URL + f"getUpdates?offset={offset}")

    try:
        tg_req_data = json.loads(tg_requests.text)
        
        return tg_req_data

    except Exception as er:
        print(er)     

def send_message(chat_id,text_to_send):
    data = {
        'chat_id': chat_id,
        'text': text_to_send
    }

    while True:
        try:
            requests.post(BOT_URL + 'sendMessage', data)
            
        except Exception as er:
            print(er)  
        else:
            break 

def command_handler(message):
    text = message['text']
    user_id = message['chat']['id']
    if text == '/start':
        username = message['from']['username']
        send_message(user_id,f'Привет, {username}! Рад тебя видеть!')
        
    elif text == '/help':

        pass
    elif text == '/game':
        pass
    else:
        pass




while True:
    time.sleep(2)    

    try:

        user_data = get_updates(OFFSET)
        if not user_data['result']:
            print(user_data)
            continue

        result = user_data['result'][0]
        print(result)
        OFFSET = result['update_id'] + 1
        
        command_handler(result['message'])


    except Exception as er:
        print(er)
