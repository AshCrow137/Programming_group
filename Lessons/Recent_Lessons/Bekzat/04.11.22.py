#list1  = [4,7,2,3,9,'str', [0,1,2,3]]


#for elim1 in list1:
#    print(elim1)

#doc_name = 'document_n_'
#for doc_num in range(1,11):
#    name = doc_name + str(doc_num)
#    print(name)
   
#bool1 = True
#num1 = 0
#while bool1:
#    num1 = num1 +1
#    if num1 == 13:
#        bool = False


# print('отсчет окончен')


#list2 = [11,12,15,16,0,2,4,'str1',6,3,6,7]

#for elem2 in list2:
#    print(elem2)
#    if type(elem2) == type('str'):
#        pass
#        print('выходим из цикла')
#else:
#    pass
#
#print('Следующая итеграция')
#print("Цикл успешно завершен")

#num1 = 0 
#while num1 <=14:

#    num1 = num1 +1
#     print(num1)
#     continue
#    if num1 == 5:
        # continue
#    elif num1 == 7:
#        pass
#    elif num1 == 10:
#        break
#
#    print('следующая интеграция')
#print('цикл завершен')



b_continue = True
while b_continue:
    user_num = float(input("Введите число,которое будет умножение на 2:"))
    result = user_num*2
    print(result)
    user_continue = input('продолжить?    y/n?')
    if user_continue == 'y':
        print("продалжаем")
    elif user_continue == 'n':
        print("заканчиваем")
        break
    else:
        print('Неверная команада. Начинаем занова')
print('до скорых встреч')