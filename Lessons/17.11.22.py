# while True:
#     try: 
#        num1 = int(input('enter the number'))
#        print(num1)

#        print(1/num1)
#     except ValueError:
#        print('error')
#     except ZeroDivisionError:
#        print('zero division')
#     except:
#         print('Unkown error')
#     else:
#         print('Jobs done')
#     finally:
#         print('Exit')
#         break









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
               students = {
                            'name':input('Name'),
                            'age' : int(input('Age')),
                            'school' : input('school: '),
                            'is_teacher' : False
        }
            except Exception as e:
                print(e)
      

        