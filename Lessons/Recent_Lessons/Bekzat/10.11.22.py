#import random


#Names = []

#for num1 in range(0,4):
#    user_name = input('Bekzat')
#    Names.append(user_name)
#    print(Names)

#print('Список закончен')

#while len(Names)<4:
#    user_name = input('Bekzat')
#    Names.append(user_name)
#    print(Names)

#print('Список закончен ')        print('Вы угадали! загадочное число было ',random_int, f'Осталось {try_num} попыток')
        break
    elif user_num < random_int:
        print('Введите число меньше загадочного')
    elif user_num > random_int:
        print('Введите число больше загадочного')
    try_num = try_num - 1 
    print(try_num)
else:
    print('У вас не осталось попыток')
print('Игра закончена!')