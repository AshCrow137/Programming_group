# for/else
# В цикле for:

# блок else выполняется в том случае, если цикл завершил итерацию списка
# но else не выполняется, если в цикле был выполнен break
# Пример цикла for с else (блок else выполняется после завершения цикла for)

for num in range(10):
    print(num)
else:
    print("Досчитали до девяти")    

# Пример цикла for с else и break в цикле (из-за break блок else не выполняется)

for num in range(10):
    if num == 5:
        print("досчитали до пяти")
        break
    else:
        print(num)
else:
    print("Досчитали до девяти")        

# Пример цикла for с else и continue в цикле (continue не влияет на блок else) 

for num in range(10):
    if num == 5:
        print("досчитали до пяти")
        continue
    else:
        print(num)
else:
    print("Досчитали до девяти")   




# while/else
# В цикле while:

# блок else выполняется в том случае, если условие в while ложно
# else не выполняется, если в цикле был выполнен break
# Пример цикла while с else (блок else выполняется после завершения цикла while)

i = 0
while i <=10:
    print(i)
    i +=1
else:
    print("Досчитали до десяти")    

# Пример цикла while с else и break в цикле (из-за break блок else не выполняется)


i = 0
while i <=10:
    if i == 3:
        break
    else:
        print(i)
        i +=1
else:
    print("Досчитали до десяти")    