import random
# Создать колоду
# Перемешать колоду
# Тянуть карты из колоды
# складвать очки с вытянутый картой
#
def draw_a_card():
    if deck:                      #if(dect)= 0
         card = deck.pop(-1)
    else:
        print('колода пуста')
        card = None
    return card

def update_score(score,player_score):
    current_score = player_score + score
    print(f'У вас {current_score} очков')
    return current_score
def declision():
    while True:
        des  = input('Брать карту? y/n')
        if des == "y":
            return True
        elif des == "n":
            return False
        else:
            print("Вы ввели недоступную команду! ")
            continue

def b_win(score):
    if score == 21:
        print('Вы победили!')
        return True
    elif score > 21:
        print('Вы проиграли!')
        return False
    elif score < 21:
        return None

def setup_players():
    num_players = int(input('Введите количиство играков'))
    players = []
    for num1 in range(1,num_players + 1):
        player = {
            'name':f'player_N_{num1}',
            'score' : 0,
            'winner' :False
        }
        players.append(player)
    print(players)
    return players

def find_winner(players_to_find):
    for player in players_to_find:
        if player['winner'] == True:
            winner = player
            return winner

    if winner == None:
        p_winners = []
        for player in players_to_find:
            score = player['score']
            if score > 20:
                pass
            else:
                 p_winners.append(player)
        p_winners.sort()

        print(p_winners)
        win_score = p_winners[-1]
        for player in players_to_find:
            if player['score'] == win_score:
                winner = player
                return player

deck = [1,2,3,4,5,6,7,8,9,10,11]*4
random.shuffle(deck)



while True:
    try:
        players = (setup_players)
    except Exception as er:
        print()





players = setup_players()

for active_player in players:
    print('Активный игрок: ',active_player)
    b_continue = True

    while b_continue:

        card = draw_a_card()

        if draw_a_card() != None:
            print(card)
            active_player['score'] = update_score(card,active_player['score'])
            win= b_win(active_player['score'])
            if win == None:
                pass
            elif win == False:
                break
            elif win == True:
                active_player['winner'] = True
                break
        else:
            break
        b_continue = declision()


print(players)

print (find_winner (players))

print('Игра окончена')