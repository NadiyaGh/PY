import math
while True:
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    d = float(input("Enter d: "))

    if a != 0:
        break;

if a == 1:
    a = b
    b = c
    c = d

p = int((b - ((a*a)/3)))
q = int((((2*(a*a*a))/27) - ((a*b)/3) + c))
delta = int((((q*q)/4) + ((p*p*p)/27)))
print(delta)
if delta > 0:
    x = int(((((-q/2) + math.sqrt(delta)) ** (1/3)) + (((-q/2) - math.sqrt(delta)) ** (1/3)) - (a/3)))
    print(x)
elif delta == 0:
    x1 = int((-2 * ((q/2)**(1/3)) - (a/3)))
    x2 = int((((q/2)**(1/3)) - (a/3)))
    print("x1 = ",x1,"\nx2 = ",x2)
else:
    x2 = (-2/(math.sqrt(3)))*math.sqrt(-p)*math.sin(((1/3)*(math.sin**(-1)((3*math.sqrt(3)*q))/(2*((math.sqrt(-p)**3))))+math.pi/3)-(a/3))
    x1 = (2/(math.sqrt(3)))*math.sqrt(-p)*math.sin(((1/3)*(math.sin**(-1)((3*math.sqrt(3)*q))/(2*((math.sqrt(-p)**3)))))-(a/3))
    x3 = (2/(math.sqrt(3)))*math.sqrt(-p)*math.cos(((1/3)*(math.sin**(-1)((3*math.sqrt(3)*q))/(2*((math.sqrt(-p)**3))))+math.pi/6)-(a/3))
    print("x1: ",x1)
    print("x2: ",x2)
    print("x3: ",x3)
    