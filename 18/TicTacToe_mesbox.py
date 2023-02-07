import sys
import random
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox
from PySide6.QtUiTools import QUiLoader

app = QApplication(sys.argv)
loader = QUiLoader()
main_window = loader.load("main.ui")
main_window.show()

######### FUNCTION #########
def two_player(row,column):
    global player
    if main_window.twoplayer_button.isChecked():
        if buttons[row][column].text() == "":
            if player == 1:
                buttons[row][column].setText("O")
                buttons[row][column].setStyleSheet("color:rgb(85, 137, 102); background-color:rgb(189, 238, 205 );\
                    font: 700 48pt ""Script MT Bold"";border-radius: 25%;")
                main_window.setStyleSheet("background-color:rgb(130, 212, 157)")
                player = 2
            elif player == 2:
                buttons[row][column].setText("X")
                buttons[row][column].setStyleSheet("color:rgb(182, 235, 241); background-color:rgb(86, 190, 203);\
                    font: 700 48pt ""Script MT Bold"";border-radius: 25%;")
                main_window.setStyleSheet("background-color:rgb(64, 158, 169)")
                player = 1
            check()
        else:
            return 
    if main_window.playerwithpc_button.isChecked():
        if buttons[row][column].text() == "":
            if player == 1:
                buttons[row][column].setText("O")
                buttons[row][column].setStyleSheet("color:rgb(85, 137, 102); background-color:rgb(189, 238, 205 );\
                    font: 700 48pt ""Script MT Bold"";border-radius: 25%;")
                main_window.setStyleSheet("background-color:rgb(130, 212, 157)")
                player = 2
            check()
            if player == 2:
                while( buttons[row][column].text() != ""):
                    row = random.randint(0,2)
                    column = random.randint(0,2)
                buttons[row][column].setText("X")
                buttons[row][column].setStyleSheet("color:rgb(182, 235, 241); background-color:rgb(86, 190, 203);\
                    font: 700 48pt ""Script MT Bold"";border-radius: 25%;")
                main_window.setStyleSheet("background-color:rgb(64, 158, 169)")
                player = 1
            check()
        else:
            return 

def check():
    for i in range(0,3):
        if (buttons[0][i].text()==buttons[1][i].text()==buttons[2][i].text()=="O") \
            or (buttons[i][0].text()==buttons[i][1].text()==buttons[i][2].text()=="O") \
            or (buttons[0][0].text()==buttons[1][1].text()==buttons[2][2].text()=="O") \
            or (buttons[0][2].text()==buttons[1][1].text()==buttons[2][0].text()=="O"):
            message = QMessageBox(text="player 1 win 🎉")
            message.setStyleSheet("background-color:rgb(130, 212, 157); color:rgb(85, 137, 102);")
            message.exec()
            main_window.showscoreO.setText(str(int(main_window.showscoreO.text())+1)) 
            NewGame()

    for i in range(0,3):
        if (buttons[0][i].text()==buttons[1][i].text()==buttons[2][i].text()=="X") \
            or (buttons[i][0].text()==buttons[i][1].text()==buttons[i][2].text()=="X") \
            or (buttons[0][0].text()==buttons[1][1].text()==buttons[2][2].text()=="X") \
            or (buttons[0][2].text()==buttons[1][1].text()==buttons[2][0].text()=="X"):
            message = QMessageBox(text="player 2 win 🎉")
            message.setStyleSheet("background-color:rgb(64, 158, 169); color:rgb(182, 235, 241);")
            message.exec()
            main_window.showscoreX.setText(str(int(main_window.showscoreX.text())+1))
            NewGame()
    k = 0
    for j in range(0,3):
        for i in range(0,3):
            if buttons[j][i].text() != "":
                k+=1
    if k == 9:
        message = QMessageBox(text="No one wins🙄")
        message.setStyleSheet("background-color:rgb(255, 255, 255); color:rgb(62, 62, 62);")
        message.exec()
        NewGame()

def NewGame():
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("color:rgb(85, 137, 102); background-color:rgb(189, 238, 205 );\
                font: 700 48pt ""Script MT Bold"";border-radius: 25%;")
    main_window.setStyleSheet("background-color:rgb(130, 212, 157)")

def basenewGame():
    for i in range(3):
        for j in range(3):
            buttons[i][j].setText("")
            buttons[i][j].setStyleSheet("color:rgb(85, 137, 102); background-color:rgb(189, 238, 205 );\
                font: 700 48pt ""Script MT Bold"";border-radius: 25%;")
    main_window.setStyleSheet("background-color:rgb(130, 212, 157)")
    main_window.showscoreX.setText("0")
    main_window.showscoreO.setText("0")
    

def About():
    message = QMessageBox(text="""
    💫Welcome to Tic Tac Toe! 
    This classic game is a great way to pass the time and challenge
    your friends.
    Tic Tac Toe is a two-player game where each player or pc!
    takes turns marking a 3x3 grid with their respective symbol 
    (X or O).
    The goal of the game is to be the first player to get three of 
    their symbols in a row, either horizontally, vertically, or 
    diagonally.
    If all nine squares are filled and no one has won, then it's 
    a draw.
    So grab a friend and start playing Tic Tac Toe! Have fun!😍🧡""")
    message.setStyleSheet("background-color:rgb(255, 255, 255); color:rgb(62, 62, 62); font: 700 11pt;")
    message.exec()

def write_text():
    main_window.signX.setStyleSheet("color:rgb(182,235, 241);")
    main_window.signO.setStyleSheet("color:rgb(85, 137, 102);")

##############################
buttons = [[main_window.button_00,main_window.button_01,main_window.button_02],
            [main_window.button_10,main_window.button_11,main_window.button_12],
            [main_window.button_20,main_window.button_21,main_window.button_22]]

player = 1
basenewGame()
write_text()
main_window.NewGame_button.clicked.connect(basenewGame)
main_window.about_button.clicked.connect(About)

for i in range(3):
    for j in range(3):
        buttons[i][j].clicked.connect(partial(two_player,i,j))

app.exec()