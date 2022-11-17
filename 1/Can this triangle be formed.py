a = float(input("Enter the size of the first side: "))
b = float (input("Enter the size of the second side: "))
c = float (input("Enter the size of the third side: "))

if a+b>c and a+c>b and c+b>a:
    print("You can draw a triangle with these sides :) ")
else:
    print("You can't draw a triangle with these sides :( ")