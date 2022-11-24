n = int(input("Enter n: "))
for i in range(0,n):
    if i%2 == 0:
        print("*",end=' ')
    else:
        print("#",end=' ')