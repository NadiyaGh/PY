n = int(input("Enter n: "))
m = int(input("Enter m: "))
for i in range(n):
    if i%2 == 0:
        for j in range(m):
            if j%2 == 0:
                print("#",end="")
            else:
                print("*",end="")        
            
    else :
        for j in range(m): 
            if j%2 == 0:
                print("*",end="")
            else:
                print("#",end="") 
    print("")
