import math
print("\n--  Calculator  --")

print("   +   -   *  /   ")
print(" sin cos  tan cot ")
print(" factorial   sqrt ")
print(" log    **    x^2 ")
print("------------------")

ins = input("Enter the desired operator: ")

if ins=="sin" or ins=="cos" or ins=="tan" or ins=="cot" or ins=="factorial" or ins=="sqrt" or ins=="log" or ins=="x^2":
    A = int(input("Enter the desired number: "))

elif ins=="+" or ins=="-" or ins=="*" or ins=="/"  or ins=="**" :
    A = float(input("Enter the first number: "))
    B = float(input("Enter the second number: "))


if ins=="sin":
    A = ((A * math.pi)/180)
    ans = math.sin(A)
elif ins=="cos":
    A = ((A * math.pi)/180)
    ans = math.cos(A)
elif ins=="tan":
    A = ((A * math.pi)/180)
    ans = math.tan(A)
elif ins=="cot":
    A = ((A * math.pi)/180)
    ans = (1 / (math.tan(A)))
elif ins=="factorial":
    ans = math.factorial(A)
elif ins=="sqrt":
    ans = math.sqrt(A)
elif ins=="log":
    ans = math.log(A,10)
elif ins=="x^2":
    ans = (A**2)
elif ins == "+":
    ans = (A+B)
elif ins == "-":
    ans = (A-B)
elif ins == "*":
    ans = (A*B)
elif ins == "/":
    if B==0:
        ans = "This value is undefined, you cannot divide a number by zero! "
    else:
        ans = (A/B)
elif ins == "**":
    ans = (A**B)

print("Answer = ",ans)
