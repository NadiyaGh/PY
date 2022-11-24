num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 < num2:
    temp = num2
    num2 = num1
    num1 = temp

i = num1
while i <= (num1*num2):
    if i % num1 == 0 and i % num2 == 0:
        print("LCM = ",i)
        break
    i += 1

