class Complex:
    def __init__(self,a,b):
        self.A = a
        self.B = b
        pass
    def Show_com(self):
        print(self.A,end=" ")
        if self.B>0:
            print(" + ",end=" ")
        print(self.B,"j")
    def sum_com(self,Com2):
        sumA = (self.A+Com2.A)
        sumB = (self.B+Com2.B)
        return (Complex(sumA,sumB))
    def Subtraction_com(self,Com2):
        subA = (self.A-Com2.A)
        subB = (self.B-Com2.B)
        return (Complex(subA,subB))
    def multiplication_com(self,Com2):
        mulA = (self.A*Com2.A)-(self.B*Com2.B)
        mulB = (self.A*Com2.B)+(self.B*Com2.A)
        return (Complex(mulA,mulB))

A1 = int(input('Enter «a» of first complex number: '))
B1 = int(input('Enter «b» of first complex number: '))
A2 = int(input('Enter «a» of second complex number: '))
B2 = int(input('Enter «b» of second complex number: '))
print("*******************")
print("Sum of two complex -> ")
C = Complex(A1,B1)
C2 = Complex(A2,B2)
C_A = C.sum_com(C2)
C_A.Show_com()
print("*******************")
print("Subtraction of two complex -> ")
C = Complex(A1,B1)
C2 = Complex(A2,B2)
C_A = C.Subtraction_com(C2)
C_A.Show_com()
print("*******************")
print("multiplication of two complex -> ")
C = Complex(A1,B1)
C2 = Complex(A2,B2)
C_A = C.multiplication_com(C2)
C_A.Show_com()
