import pyfiglet
import colorama
from colorama import Fore
import time
import random
start_time = time.time()


################### function ####################
def show():
    for row in game_board:
        for cell in row:
            if cell == "X":
                print(Fore.RED + "X", end = " ")
            elif cell == "O":
                print(Fore.BLUE + "O", end = " ")
            else:
                print(Fore.RESET + cell, end = " ")
        print(Fore.RESET)

def check_game(symbol):
    win = False
    for i in range(0,3):
        if (game_board[0][i]==game_board[1][i]==game_board[2][i]==symbol) or (game_board[i][0]==game_board[i][1]==game_board[i][2]==symbol):
            win = True
    if (game_board[0][0]==game_board[1][1]==game_board[2][2]==symbol) or (game_board[0][2]==game_board[1][1]==game_board[2][0]==symbol):
            win = True
    
    if  win ==True:
        if symbol == "X" and choose == 2:
            print("player 1 win 🎉")
        elif symbol == "X" and choose == 1:
            print("player win 🎉")
        elif symbol == "O" and choose == 2:
            print("player 2 win 🎉")
        elif symbol == "O" and choose == 1:
            print("Computer win 🎉")
        print("How long you played : ",(time.time() - start_time)," s")
        exit(0)
    
    k = 0
    for j in range(0,3):
        for i in range(0,3):
            if game_board[j][i] != "_":
                k+=1
    if k == 9:
        print("No one wins :(")




#title
title = pyfiglet.figlet_format("Welcome to Tic Tac Toe game",font="digital")
print(title)
#game board
game_board = [["_","_","_"],["_","_","_"],["_","_","_"]]
#menu
menu = pyfiglet.figlet_format("\n\t\tMenu\n1. play with computer \n2. two players ",font="digital")
print(menu)
choose = int(input("Enter your choice(1/2) -> "))
#first show empty table
show()

################## GAME ###################
while True:
    
    if choose == 1:
        print("Player -> ")
    else:
        print("player 1 -> ")

    while True:
        row = int (input("row -> "))
        col = int (input("col -> "))
        col -= 1
        row -= 1
        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "_":
                game_board[row][col] = "X"
                break
            else:
                print("You have placed the X in the duplicate place :/")
        else:
            print("The entered coordinates are out of range...")

    show()
    symbol = "X"
    check_game(symbol)

    if choose == 1:
        print("Computer -> ")
    else:
        print("player 2 -> ")

    while True:
        if choose == 1:
            row = random.randint(0,2)
            col = random.randint(0,2)
        else:
            row = int (input("row -> "))
            col = int (input("col -> "))
            col -= 1
            row -= 1

        if 0 <= row <= 2 and 0 <= col <= 2:
            if game_board[row][col] == "_":
                game_board[row][col] = "O"
                break
            else:
                if choose == 2:
                    print("You have placed the O in the duplicate place :/")
        else:
            print("The entered coordinates are out of range... :/// ")

    show()
    symbol = "O"
    check_game(symbol)