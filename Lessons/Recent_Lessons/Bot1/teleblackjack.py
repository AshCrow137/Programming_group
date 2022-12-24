import random
# Создать колоду
# Перемешать колоду
# Тянуть карты из колоды
# Складывать очки с вытянутой картой
# Если игрок набрал больше 21 он проиграл
# Если ровно 21 он выиграл
# Если меньше 21, он может решить, брать карту или не брать
# 
def draw_a_card(deck):
    if deck:                    #if len(deck)!= 0
        card = deck.pop(-1)
    else:
        print('Колода пуста')
        card = None
    return card

def update_score(score,player_score):
    current_score = player_score + score
    print(f'У вас {current_score} очков')
    return  current_score

def decision(des):
    while True:
       
        if des == "y":
            return True
        elif des == "n":
            return False
        else:
            print("Вы ввели недопустимую команду! ") 
            continue       

def b_win(score):
    if score ==  21:
        print('Вы победили!')
        return True
    elif score > 21:
        print('Вы проиграли!')
        return False
    elif score < 21:
        return None        

def setup_players():


    
    players = []
    for num1 in range(1,num_players + 1):
        player = {
            'name': f'Player_N_{num1}',
            'score': 0,
            'winner':False
        }
        players.append(player)

    print(players)
    return players

def find_winner(players_to_find):
    winner = None
    for player in players_to_find:
        if player['winner'] == True:
            winner = player
            return winner

    if winner == None:
        p_winners = []
        for player in players_to_find:
            score = player["score"]  
            if score > 20:
                pass
            else:
                p_winners.append(score)
        p_winners.sort()

        print(p_winners)
        win_score = p_winners[-1]
        for player in players_to_find:
            if player['score'] == win_score:
                winner = player
                return player

def shuffle_deck():
    deck = [2,3,4,6,7,8,9,10,11]*4
    random.shuffle(deck)
    return deck

def blackjack():

    

    deck = setup_players(num_players = int(input('Введите количество игроков')))


players = setup_players()

for active_player in players:

    print('Активный игрок: ',active_player)
    b_continue = True

    while b_continue:
        
        card = draw_a_card()

        if card != None:
            print(card)
            active_player['score'] = update_score(card,active_player['score'])
            win = b_win(active_player['score'])

            if win == None:
                pass
            elif win == False:
                break
            elif win == True:
                active_player['winner'] = True
                break
        else:
            break
        b_continue = decision(input('Брать карту? y/n'))


print(players)

print(find_winner(players))

print('Игра окончена')    