n = int(input("Enter n: "))
a = 0
b = 1
print(a,",",b,end=' ')
for i in range(2,n):
    c = a+b
    print(",",c,end=' ')
    temp = b
    b = c
    a = temp