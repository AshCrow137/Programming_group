print("Enter month number")

month_number = int(input())


if month_number <= 0:
    print("That month doesnt exist")
elif month_number <3 or month_number == 12:
    print("Season is winter")
elif month_number <6:
    print("Season is spring")
elif month_number <9: 
    print("Season is summer")
elif month_number <12:
    print("Season is autumn")
else:
    print("That month doesnt exist")