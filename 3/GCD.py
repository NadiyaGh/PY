num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

if num1 > num2:
    temp = num2
    num2 = num1
    num1 = temp

i = num1
while i>0:
    if num1%i==0 and num2%i==0:
        print("GCD = ",i)
        break
    i -= 1

