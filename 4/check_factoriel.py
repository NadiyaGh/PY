num = int(input("Enter num: "))

fact = 1
i = 1
while 1<2:
    fact = (fact * i)
    
    if fact == num:
        print("yes!")
        break
    elif fact > num:
        print("No!")
        break

    i+=1