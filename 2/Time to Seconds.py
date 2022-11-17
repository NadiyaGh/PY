while 1:
    Hour = int(input("Enter hours: "))
    if Hour > 24:
        print("Hours should be under 24! try again...")
    else:
        break
while 1:
    Minute = int(input("Enter minute: "))
    if(Minute > 60):
        print("Minute should be under 60! try again...")
    else:
        break
while 1:
    Seconds = int(input("Enter seconde: "))
    if(Seconds > 60):
        print("Seconde should be under 60! try again...")
    else:
        break

print("your entry time is -> ")
if Hour < 10:
    print("0",Hour,":", end = ' ')
else: print(Hour,":", end = ' ')

if Minute < 10:
    print("0",Minute,":", end = ' ')
else: print(Minute,":", end = ' ')

if Seconds < 10:
    print("0",Seconds)
else: print(Seconds)



Seconds = ((Hour*3600)+(Minute*60)+Seconds)
print("it means ",Seconds," seconde")