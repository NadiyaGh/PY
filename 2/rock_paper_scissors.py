import random
u_score = 0 
c_score = 0
Choise = ["rock","paper","scissors"]
print("Hello! Welcome to << Rock, Paper, Scissors >> game!\nGame rules:\nYou compete with the computer!\nIn this game, you can try your luck three times and earn points!\nIf you and the computer guess the same, points will be added to both sides.\nIf your points are more than the computer, you win๐ \nIf the computer scores more than you or equal, the computer wins!๐ฅบ\n")
for i in range(3):
    c_choice = random.choice(Choise)
    u_choice = input("rock / paper / scissors ? -> ")

    print("๐ป: ",c_choice ,"\n๐ค: ",u_choice)
    if (c_choice == "rock" and u_choice == "scissors") or (c_choice == "paper" and u_choice == "rock") or (c_choice == "scissors" and u_choice == "paper"):
        c_score += 1
    elif (c_choice == "rock" and u_choice == "paper") or (c_choice == "paper" and u_choice == "scissors") or (c_choice == "scissors" and u_choice == "rock"):
        u_score += 1
    else:
        u_score += 1
        c_score += 1

if(c_score >= u_score):
    print("You lose! ๐ฅบ\nyour score is -> ",u_score ,"\ncomputer score is -> ",c_score)
if(c_score < u_score):
    print("You Win! ๐\nyour score is -> ",u_score ,"\ncomputer score is -> ",c_score)

