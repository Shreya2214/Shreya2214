import random

print("Welcome user, this is a game of Roll the dice")
print("Disclaimer:the number should be less than or equal to 10")
num = input("Enter the number of dice you wish to roll: ")
num = int(num)

dice = random.randint(1,6)

if num == 10:
    print(dice * 10)
elif num == 9:
    print(dice * 9)
elif num == 8:
    print(dice * 8)
elif num == 7:
    print(dice * 7)
elif num == 6:
    print(dice * 6)
elif num == 5:
    print(dice * 5)
elif num == 4:
    print(dice * 4)
elif num == 3:
    print(dice * 3)
elif num == 2:
    print(dice * 2)
elif num == 1:
    print(dice)
else:
    print("Invalid number of dices")
