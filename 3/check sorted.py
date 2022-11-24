array = []
check = True
print("Enter array numbers, When you are done entering your array numbers enter \"end\" -> ")
while 1:
    arr = (input("Enter your number: "))
    if arr == "end":
        break
    arr = int(arr)
    array.append(arr)

for i in range(0,len(array)-1):
    if array[i]>array[i+1]:
        check = False
        break

if check == False:
    print("Array isn't sort!")
else:
    print("Array is sort!")
