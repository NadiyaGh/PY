Sec_in = int(input("Enter seconds: "))
Hour = int(Sec_in/3600)
Sec_in -= (Hour * 3600)
Minute = int(Sec_in/60)
Sec_in -= (Minute * 60)
Seconds = Sec_in

print("Time is -> ")
if Hour < 10:
    print("0",Hour,":", end = ' ')
else: print(Hour,":", end = ' ')

if Minute < 10:
    print("0",Minute,":", end = ' ')
else: print(Minute,":", end = ' ')

if Seconds < 10:
    print("0",Seconds)
else: print(Seconds)