while True:
    n = int(input("Enter n :"))
    if(n%2==0):
        print("Enter odd number : ")
    else:
        break

for i in range(n):
    for j in range(n+1):
        if j%10==1:
            print("❤",end=" ")
        elif j%10==2:
            print("🧡",end=" ")
        elif j%10==3:
            print("💛",end=" ")
        elif j%10==4:
            print("💚",end=" ")
        elif j%10==5:
            print("💙",end=" ")
        elif j%10==6:
            print("💜",end=" ")
        elif j%10==7:
            print("🤎",end=" ")
        elif j%10==8:
            print("🖤",end=" ")
        elif j%10==9:
            print("🤍",end=" ")
    print()
        