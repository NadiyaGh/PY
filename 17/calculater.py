import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")

def sum():
    global number1
    global operator
    operator = "+"
    number1 = int(main_window.showtext.text())    
    main_window.showtext.setText("")
    
def sub():
    global number1
    global operator
    operator = "-"
    number1 = int(main_window.showtext.text())    
    main_window.showtext.setText("")

def multi():
    global number1
    global operator
    operator = "*"
    number1 = int(main_window.showtext.text())    
    main_window.showtext.setText("")

def devision():
    global number1
    global operator
    operator = "/"
    number1 = int(main_window.showtext.text())    
    main_window.showtext.setText("")

def Sin():
    ...
def Cos():
    ...
def tan():
    ...
def cot():
    ...
def log():
    ...
def Sqrt():
    ...

def Num(number):
    if number=="1":
        main_window.showtext.setText(main_window.showtext.text()+'1')
    elif number=="2":
        main_window.showtext.setText(main_window.showtext.text()+'2')
    elif number=="3":
        main_window.showtext.setText(main_window.showtext.text()+'3')
    elif number=="4":
        main_window.showtext.setText(main_window.showtext.text()+'4')
    elif number=="5":
        main_window.showtext.setText(main_window.showtext.text()+'5')
    elif number=="6":
        main_window.showtext.setText(main_window.showtext.text()+'6')
    elif number=="7":
        main_window.showtext.setText(main_window.showtext.text()+'7')
    elif number=="8":
        main_window.showtext.setText(main_window.showtext.text()+'8')
    elif number=="9":
        main_window.showtext.setText(main_window.showtext.text()+'9')
    elif number=="0":
        main_window.showtext.setText(main_window.showtext.text()+'0')
    

def find_result():
    number2 = int(main_window.showtext.text())
    print(operator)
    if operator=="+":
        result = number1 + number2
        main_window.showtext.setText(str(result))

    elif operator=="-":
        result = number1 - number2
        main_window.showtext.setText(str(result))

    elif operator=="*":
        result = number1 * number2
        main_window.showtext.setText(str(result))

    elif operator=="/":
        result = number1 / number2
        main_window.showtext.setText(str(result))

    
def AC():
    main_window.showtext.setText("")

main_window.show()

##### Num Button ####
main_window.one_button.clicked.connect(partial(Num,"1"))
main_window.two_button.clicked.connect(partial(Num,"2"))
main_window.three_button.clicked.connect(partial(Num,"3"))
main_window.four_button.clicked.connect(partial(Num,"4"))
main_window.five_button.clicked.connect(partial(Num,"5"))
main_window.six_button.clicked.connect(partial(Num,"6"))
main_window.seven_button.clicked.connect(partial(Num,"7"))
main_window.eight_button.clicked.connect(partial(Num,"8"))
main_window.nine_button.clicked.connect(partial(Num,"9"))
main_window.zero_button.clicked.connect(partial(Num,"0"))

main_window.sum_button.clicked.connect(sum)
main_window.subtraction_button.clicked.connect(sub)
main_window.multiplication_button.clicked.connect(multi)
main_window.division_button.clicked.connect(devision)

main_window.result_button.clicked.connect(find_result)
main_window.AC_button.clicked.connect(AC)




app.exec()