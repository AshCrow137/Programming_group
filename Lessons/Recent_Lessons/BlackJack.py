import random
def draw_a_card():
    if len(deck)>0:

        return deck.pop(-1)
    else:
        print('Колода закончилась')
        return None
       
def update_score(current_score,score):
    current_score = current_score + score
    print('Текущее количество очков: ',current_score)    
    return current_score

def draw_decision():
    player_score = 0
    while True:
        decision = input('Берем карту? y/n')
        if decision == 'y':
            card = draw_a_card()
            
            if card:
                print('Вы вытянули', card)
                player_score = update_score(player_score,card)
                if b_win(player_score) == None:
                    pass
                elif b_win(player_score):
                    print("Вы победили!")
                    break
                else:
                    print('Вы проиграли!') 
                    break           
            else:
                break 
        elif decision =='n':
            print('Текущее количество очков: ',player_score)
            break 
        else:
            print('Вы ввели неправильную команду!')
            continue   
    return False

def b_win(current_score):
    if current_score ==21: 
        return True
    elif current_score>21:
        return False
    else:
        return None   


deck = [2,3,4,5,6,7,8,9,10,11]*4   
random.shuffle(deck)

b_continue = True
while b_continue:
    b_continue = draw_decision()
print('Игра окончена!')    