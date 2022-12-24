# clear
# Метод clear позволяет очистить словарь

dict1 = { "username":"cyberkiller",
"password": 12345,
"account type": "free"
}

print(dict1)

dict1.clear()

print(dict1)

# copy
# Метод copy позволяет создать полную копию словаря.


# Если указать, что один словарь равен другому,
# получившийся словарь будет ссылать на предыдущий,
# и таким образом, изменяя значение в исходном словаре,
# будут изменяться значения и во всех его копиях

dict1 = { "username":"cyberkiller",
"password": 12345,
"account type": "free"
}

dict2 =dict1

print(dict2)

dict1["password"] = 123456

print(dict2)

# Поэтому, если нужно сделать копию словаря, надо использовать метод copy()

dict2 = dict1.copy()

print(dict2)

dict1["password"] = 1234567

print(dict1)

print(dict2)

# В таком случае при изменении значения первого словаря, значение всех его копий изменяться не будет 


# get
# Если при обращении к словарю указывается ключ, которого нет в словаре, возникает ошибка
# Метод get запрашивает ключ, и если его нет, вместо ошибки возвращает None.

print(dict1.get("age"))

# Метод get() позволяет также указывать другое значение вместо None

print(dict1.get("age","Not defined"))



# setdefault
# Метод setdefault ищет ключ, и если его нет, вместо ошибки создает ключ со значением None

result1 = dict1.setdefault("email")

print(result1)

print(dict1)

# Второй аргумент позволяет указать, какое значение должно соответствовать ключу


result1 = dict1.setdefault("new email", "@gmail.com")

print(result1)

print(dict1)




# keys, values, items
# Методы keys, values, items возвращают ключи, значения,
# и пары значение-ключ соответственно

print(dict1.keys())

print(dict1.values())

print(dict1.items())

# del
# Функция del yдаляет ключ и значение

del dict1["account type"]

print(dict1)

# update
# Метод update позволяет добавлять в словарь содержимое другого словаря

dict2 = {"first name": "Alex",
"last name": "Gamburg"}

dict1.update(dict2)

print(dict1)