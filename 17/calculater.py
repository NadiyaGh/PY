import math
from PySide6.QtWidgets import QApplication
from PySide6.QtUiTools import QUiLoader
from functools import partial
app = QApplication([])
loader = QUiLoader()
main_window = loader.load("main.ui")

####################
def auditor():
    main_window.showtext.setText(main_window.showtext.text()+'.')

def change_sign():
    number = float(main_window.showtext.text()) 
    number *= (-1)
    main_window.showtext.setText("")
    main_window.showtext.setText(str(number))

def Percent():
    number = float(main_window.showtext.text())
    number /= (100)
    main_window.showtext.setText("")
    main_window.showtext.setText(str(number))

def backspace():
    text = [] 
    text = (main_window.showtext.text())
    text = text[:-1]
    main_window.showtext.setText("")
    main_window.showtext.setText(text)

####################
def sum():
    global number1
    global operator
    operator = "+"
    number1 = float(main_window.showtext.text())    
    main_window.showtext.setText("")
    
def sub():
    global number1
    global operator
    operator = "-"
    number1 = float(main_window.showtext.text())    
    main_window.showtext.setText("")

def multi():
    global number1
    global operator
    operator = "*"
    number1 = float(main_window.showtext.text())    
    main_window.showtext.setText("")

def devision():
    global number1
    global operator
    operator = "/"
    number1 = float(main_window.showtext.text())    
    main_window.showtext.setText("")

def power():
    global number1
    global operator
    operator = "^"
    number1 = float(main_window.showtext.text())    
    main_window.showtext.setText("")

####################
def Sin():
    number = float(main_window.showtext.text())  
    number = ((number * math.pi)/180)  
    result = math.sin(number)
    main_window.showtext.setText("")
    result = format(result, '.2f')
    main_window.showtext.setText(str(result))

def Cos():
    number = float(main_window.showtext.text())  
    number = ((number * math.pi)/180)  
    result = math.cos(number)
    main_window.showtext.setText("")
    result = format(result, '.2f')
    main_window.showtext.setText(str(result))

def Tan():
    number = float(main_window.showtext.text())  
    if (number==90 or number==270):
        result = "∞"
        main_window.showtext.setText(str(result))
    else:
        number = ((number * math.pi)/180) 
        result = math.tan(number)
        main_window.showtext.setText("")
        result = format(result, '.2f')
        main_window.showtext.setText(str(result))

def Cot():
    number = float(main_window.showtext.text())  
    if (number == 0 or number == 180 or number == 360):
        result = "∞"
        main_window.showtext.setText(str(result))
    else:
        number = ((number * math.pi)/180)  
        result = math.tan(number)
        result = (1/result)
        main_window.showtext.setText("")
        result = format(result, '.2f')
        main_window.showtext.setText(str(result))

def Log():
    number = float(main_window.showtext.text())
    result = math.log(number,10)
    main_window.showtext.setText("")
    result = format(result, '.2f')
    main_window.showtext.setText(str(result))

def Sqrt():
    number = float(main_window.showtext.text())
    if (number < 0):
        result = "Error!"
    else:
        result = math. sqrt(number)
        main_window.showtext.setText("")
        result = format(result, '.2f')
        main_window.showtext.setText(str(result))
    
####################
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
    
####################
def find_result():
    number2 = float(main_window.showtext.text())
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
        if (number2 == 0):
            result = "Error!"
            main_window.showtext.setText(str(result))
        else:
            result = number1 / number2
            result = format(result, '.2f')
            main_window.showtext.setText(str(result))

    elif operator=="^":
        result = math.pow(number1 , number2)
        main_window.showtext.setText(str(result))

####################
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
####################
main_window.sum_button.clicked.connect(sum)
main_window.subtraction_button.clicked.connect(sub)
main_window.multiplication_button.clicked.connect(multi)
main_window.division_button.clicked.connect(devision)
main_window.power_button.clicked.connect(power)
####################
main_window.result_button.clicked.connect(find_result)
main_window.AC_button.clicked.connect(AC)
main_window.auditor_button.clicked.connect(auditor)
####################
main_window.sin_button.clicked.connect(Sin)
main_window.cos_button.clicked.connect(Cos)
main_window.tan_button.clicked.connect(Tan)
main_window.cot_button.clicked.connect(Cot)
####################
main_window.sqrt_button.clicked.connect(Sqrt)
main_window.log_button.clicked.connect(Log)
main_window.Percent_button.clicked.connect(Percent)
main_window.change_sign_button.clicked.connect(change_sign)
main_window.backspace_button.clicked.connect(backspace)

app.exec()