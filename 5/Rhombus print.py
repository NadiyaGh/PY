i = j = 0
n = int(input("Enter n: "))
for i in range(n):
    for j in range(1,(n-i)):
        print(" ",end="")
    for j in range(0,((2*i)+1)):
        print("*",end="")
    print("")
i = (n-2)
while i>=0:
    for j in range(1,(n-i)):
        print(" ",end="")
    for j in range(0,((2*i)+1)):
        print("*",end="")
    i -= 1
    print("")
