import requests
import json
import time
import teleblackjack2



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
    global b_play_game
    global b_start_game
    global b_continue
    global players
    global deck
    text = message['text']
    user_id = message['chat']['id']

    
    if text == '/start':
        username = message['from']['username']
        send_message(user_id,f'Привет, {username}! Рад тебя видеть!')
        
    elif text == '/help':

        pass
    elif text == '/game':
        send_message(user_id,'Введите количество игроков')
        b_start_game =True
        return
    else:
        pass
    if b_start_game:
        if text:
            try:
                num_players = int(text)
                print(num_players)
                players = teleblackjack2.setup_players(num_players)
                
                b_start_game = False
                b_play_game = True
                deck = teleblackjack2.shuffle_deck()
                print('start game')
            except Exception as er:
                print(er)
                send_message(user_id,'Вы ввели недопустимое количество игроков! Попробуйте /game еще раз')
                b_start_game = False  
                 
    if b_play_game:
        if text == '/y':
            b_continue = True
        elif text == '/n':
            b_continue == False
            b_play_game = False
            return    
        
        active_player = players[0]
        print('Активный игрок: ',active_player)
        
        b_play_game = blackjack_game(deck,active_player,user_id) 
        print(b_play_game)
        if b_play_game:
            send_message(user_id,f'Берем карту? /y /n')
        

def blackjack_game(deck,active_player,user_id):
    global b_continue
    print(b_continue)
    if b_continue:
        card = teleblackjack2.draw_a_card(deck)
    else:
        return False
    if card != None:
        send_message(user_id,f'Вы вытянули {card}')
        active_player['score'] = teleblackjack2.update_score(card,active_player['score'])
        current_score = active_player['score']
        send_message(user_id,f'У вас {current_score} очков')
        win = teleblackjack2.b_win(active_player['score'])

        if win == None:
                    b_continue = True
        elif win == False:
                    b_continue = False
                    send_message(user_id,f'Вы проиграли')
                    return False
        elif win == True:
                    active_player['winner'] = True
                    b_continue = False
                    send_message(user_id,f'Вы победили!')
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
