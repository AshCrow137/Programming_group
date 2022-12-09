# while True:
#     try:
#         num1 = int(input('enter the number'))
#         print(num1)

#         print(1/num1)
#     except ValueError:
#         print('error')
#     except ZeroDivisionError:
#         print('zero division')
#     except:
#         print('Unckown error')
#     else:
#         print('Jobs done')
#     finally:
#         print('Exit')
#         break
    
# try: 
#     a = '1237'
#     b = int(a)
#     print(b)
# except Exception as e:
#     print(e)
# print('Продолжаем работу')

# Создать список со словарями, содержащими в себе: 
# количество учеников
{'name':None,# пользователь должен ввести имя самостоятельно
'age': None, # этот ключ должен быть преобразован в целое число
'school': None,
'is_teacher':False
}

def setup_students():
    while True:
        students = []
        try:
            num_std = int(input('Students: '))
        except Exception as e:
            print(e)
            continue    
        else:
            break
    
    for num in range(1,num_std+1):

        while True:
            try:
                student = {
                            'name':input('Name: '),
                            'age': int(input('Age:')), 
                            'school': input('School: '),
                            'is_teacher':False
                }
            except Exception as e:
                print(e)
                continue
            else:
                break    
        students.append(student)

    print(students)

setup_students()    
