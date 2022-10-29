# str_input =   input('Введите команду: ')

# if str_input == 'Привет' or str_input == 'привет' or str_input == ' привет': # Если хотя бы одно условие выполняется, 
# # то весь блок истина
#     print('Привет пользователь! Я новый бот9000')

# elif str_input == 'Пока':
#     print('Прощай! Надеюсь на скорую встречу')  

# else:
#     print("Неизвестная команда!")   


num1 = int(input('Введите число 1: '))
num2 = int(input('Введите число 2: '))

if num1 >0 and num2 > 0:
    print('Числа больше нуля')
    if num1 >5 :
        print(num1)
    if num2 > 7:
        print(num2)    
else:
    print('Одно из чисел меньше или равно нулю')    
