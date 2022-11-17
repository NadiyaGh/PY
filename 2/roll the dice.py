import random
print("Start! roll the dice...🎲")
while 1:
    dice = random.randint(1,6)
    print("Dice number is: ",dice)
    if dice != 6:
        break