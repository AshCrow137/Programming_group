import requests
import json
import time
import teleblackjack




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
    global b_continue
    global b_start_game
    global b_players_game
    global players
    global deck

    text = message['text']
    user_id = message['chat']['id']
    if text == '/start':
        user_name = message['from']['username']
        send_message(user_id,f'Привет, {user_name}! Рад тебя видеть')
        
    elif text == '/help':

        send_message(user_id,('/start/help'),f'Я еще ничего не умею! Ты ввел недоступную команду')
        pass
    elif text == '/game':
        send_message(user_id,'Введите количество игроков')
        b_start_game = True
        return
    else:
        pass
    if b_start_game:
        if text:
            try:
                num_players = int(text)
                players = teleblackjack.setup_players(num_players)
                deck = teleblackjack.shuffle_deck()
                b_start_game = False
                b_play_game = True
            except Exception as er:
                print(er)
                send_message(user_id,'Вы ввели недопустимое количество игроков. попробуйте /game занова')
                b_start_game = False
    if b_play_game:
        if text  == '/y':
            b_continue = True
        elif text == '/n':
            b_play_game = False
            b_continue = False
            return
        active_player = players[0]
        b_play_game = play_blackjack(deck,active_player,user_id)
        if b_play_game:
            send_message(user_id, 'Берем карту? /y /n')

def play_blackjack(deck,active_player,user_id):
    global b_continue
    if b_continue:
        card = teleblackjack.draw_a_card(deck)
    else:
        return False
    
    if card != None:
                send_message(user_id,f'Вы вытянули {card}')
                print(card)
                active_player['score'] = teleblackjack.update_score(card,active_player['score'])
                current_score = active_player['score']
                send_message(user_id, f'У вас {current_score} очков')

                win = teleblackjack.b_win(active_player['score'])

                if win == None:
                    pass
                elif win == False:
                    send_message(user_id, 'Вы проиграли')
                    return False
                elif win == True:
                    active_player['winner'] = True
                    send_message(user_id, 'Вы выиграли')
                    return False
    else:
            b_continue = False
    return True

b_continue = True
b_start_game = False
b_play_game = False
players = None
deck = None




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
