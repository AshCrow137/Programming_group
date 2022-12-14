# Оператор break
# Оператор break позволяет досрочно прервать цикл:

# break прерывает текущий цикл и продолжает выполнение следующих выражений
# если используется несколько вложенных циклов, break прерывает 
# внутренний цикл и продолжает выполнять выражения, следующие за 
# блоком * break может использоваться в циклах for и while
# Пример с циклом for

for i in range(10):
    if i< 7:
        print(i)
    else:
        break    

# Пример с циклом while


a = 0
while a<10:
    if a == 5:
        break
    else:
        print(a)
        a = a + 1


# Оператор continue
# Оператор continue возвращает управление в начало цикла. 
# То есть, continue позволяет «перепрыгнуть» оставшиеся выражения в цикле и перейти к следующей итерации.

# Пример с циклом for    

for num in range(10):
    if num == 3:
        continue
        print("Этого сообщения никто не увидит")
    else:
        print(num)

# Пример с циклом while

b = 0
while b <=15:
     
    if b == 10:
        print("Пропускаем 10")
        b = b + 1
        continue
        print("Этого никто не увидит")
    else:
        print(b)
        b = b + 1



# Оператор pass

# Оператор pass ничего не делает. Фактически, это такая заглушка для объектов.

# Например, pass может помочь в ситуации, когда нужно прописать 
# структуру скрипта. Его можно ставить в циклах, функциях, классах. 
# И это не будет влиять на исполнение кода.

# Пример использования pass

for num2 in range(10):
    if num2<5:
        pass
    else:
        print(num2)
