n = int(input("Entre the number of numbers you want to enter: "))
list_f = []
list_p = []
for i in range (n):
    num = int(input())
    list_f.append(num)

i = (n-1)
while i>=0:
    list_p.append(list_f[i])
    i -= 1

print("Reverse list -> ", list_p)