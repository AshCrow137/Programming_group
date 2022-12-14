#Булевые типы данных | Boolean


# В Python истинными и ложными значениями считаются не только True и False.

# истинное значение:

# любое ненулевое число
# любая непустая строка
# любой непустой объект

# ложное значение:

# 0
# None
# пустая строка
# пустой объект
# Остальные истинные и ложные значения, как правило, логически следуют из условия

some_list = [1,2,3]

empty_list = []

print(bool(some_list))

print(bool(empty_list))

print(bool(0))

print(bool(1))


# if/elif/else
# Конструкция if/elif/else позволяет делать ответвления в ходе программы. Программа уходит в ветку при выполнении определенного условия.

# В этой конструкции только if является обязательным, elif и else опциональны:

# Проверка if всегда идет первой.
# После оператора if должно быть какое-то условие: если это условие выполняется (возвращает True), то действия в блоке if выполняются.
# С помощью elif можно сделать несколько разветвлений, то есть, проверять входящие данные на разные условия.
# Блок elif это тот же if, но только следующая проверка. Грубо говоря, это «а если …»
# Блоков elif может быть много.
# Блок else выполняется в том случае, если ни одно из условий if или elif не было истинным.

some_number = 3

if some_number == 5:
    print("Equal 5")
elif some_number <5:
    print("Less than 5")
else:
    print("More than 5")   

# При помощи булевых значений можно также проверять списки на наличие или отсутствие в них переменных

list_to_test = [1,2,3]

if list_to_test:
    print("Not empty")

# Тот же результат можно было бы получить несколько иначе:
if list_to_test != 0:
    print("Not empty")

# Операторы сравнения
# Операторы сравнения, которые могут использоваться в условиях    

a = 5 
b = 10

a > b #False

a < b #True

a == b #False. Знак == означает равенство, а равно b 

b == b #True

a >= b #False

a <= b #True

a != b #True. Знак != означает "Не равно". a не равно b 

