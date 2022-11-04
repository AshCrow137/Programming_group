def current_season(month): #month - параметр ункции
    if month <= 0:
        print("That month doesnt exist")
    elif month <3 or month == 12:
        print("Season is winter")
    elif month <6:
        print("Season is spring")
    elif month <9: 
        print("Season is summer")
    elif month <12:
        print("Season is autumn")
    else:
        print("That month doesnt exist")


user_month1 = int(input('enter month 1number:'))
user_month2 = int(input('enter month 2number:'))
user_month3 = int(input('enter month 3number:'))
user_month4 = int(input('enter month 4number:'))

current_season(user_month1)
current_season(user_month2)
current_season(user_month3)
current_season(user_month4)
