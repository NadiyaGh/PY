import random

Rand_Number = int(random.randint(10,999))

for i in range(5):
    level = input("Hard / Medium / Easy ? -> ")
    if level=="Hard" or level=="hard":
        level_num = 10
        break

    elif level=="Medium" or level=="medium":
        level_num = 20
        break

    elif level=="Easy" or level=="easy":
        level_num = 30
        break

    else:
        print("Your entry level is not defined! please try again... ")
        level_num = 0

if level_num != 0:
    print("You choose ",level,"level ! You can guess ",level_num," number.\n .....Start....." )
    User_guess = int(input("Enter a number between 10 - 1000 -> "))

    for i in range(level_num):
        if i != 0:
            User_guess = int(input("Enter your guess -> "))
        
        if User_guess == Rand_Number:
            print("You Win with ", i+1 , " guess! 🎉✨")
            break
        elif User_guess < Rand_Number:
            print("Go Up ⬆")
        elif User_guess > Rand_Number:
            print("Go Down ⬇")

    if i==(level_num-1):
        print("❌Game Over😱")
        
