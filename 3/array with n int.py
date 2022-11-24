n = int(input("Enter n: "))

arr = []
i = 0
while i<n:
    num = int(input())
    if num not in arr:
        arr.append(num)
        i+=1
    else:
        print("The entered number is duplicate! ")


print(arr)