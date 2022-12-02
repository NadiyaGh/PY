n = int(input("Entre the number of numbers you want to enter: "))
list_f = []

for i in range (n):
    check_duplicat = True
    num = int(input())
    for j in range(len(list_f)):
        if num == list_f[j]:
           check_duplicat = False
           break

    if check_duplicat == True:
        list_f.append(num)

print("Imported list without duplicate elements -> " , list_f)