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

def update_score(score):
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

deck = [1,2,3,4,5,6,78,9,10,11]*4
random.shuffle(deck)



b_continue = True
player_score = 0
while b_continue:

    card = draw_a_card()

    if draw_a_card() != None:
        print(card)
        player_score = update_score(card)
        win= b_win(player_score)
        if b_win(player_score) == True:
            break
        elif b_win(player_score) == False:
            break
    else:
        break
    b_continue = declision()

print('Игра окончена')