name = input("Enter name of student: ")
print("Enter the scores and after completing them, enter 'exit' ")
sum = 0
i = 0
while 1:
    a = input()
    if a=="exit":
        break
    a = int(a)
    sum += a
    i += 1

print("average = ",(sum/i))