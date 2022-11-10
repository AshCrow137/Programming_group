import random


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

#print('Список закончен ')

#for int1 in range(0,6):
#    result = (int1*117 + 87)//13 * (21**int1)


random_int = random.randint(1,100)
print(random_int)

try_num = 10
while try_num > 0:
    user_num = int(input('Введите число: '))
    if user_num <1 or user_num > 100:
        print('Вы ввели неверное число! Введите число от 1 до 100')
        continue
    
    if user_num == random_int:
        print('Вы угадали! загадочное число было ',random_int, f'Осталось {try_num} попыток')
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