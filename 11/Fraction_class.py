import math
class Fraction:
    def __init__(self,numerator,denominator):
        self.Numerator = numerator
        self.Denominator = denominator
        pass
####################
    def Show(self):
        if self.Denominator == 0:
            print("Fraction is undefined! ")
        else:
            print(int(self.Numerator),"/",int(self.Denominator))
####################
    def F_Sum(self,self2):
        self.Den = math.lcm(self.Denominator,self2.Denominator)
        self.Coefficient1 = self.Den / self.Denominator
        self.Coefficient2 = self.Den / self2.Denominator
        self.Numerator *= self.Coefficient1
        self2.Numerator *= self.Coefficient2
        return Fraction((self.Numerator+self2.Numerator),self.Den)
####################
    def F_Sub(self,self2):
        self.Den = math.lcm(self.Denominator,self2.Denominator)
        self.Coefficient1 = self.Den / self.Denominator
        self.Coefficient2 = self.Den / self2.Denominator
        self.Numerator *= self.Coefficient1
        self2.Numerator *= self.Coefficient2
        return Fraction((self.Numerator-self2.Numerator),self.Den)
####################
    def F_Multi(self,self2):
        return Fraction((self.Numerator*self2.Numerator),(self.Denominator*self2.Denominator))
####################
    def F_div(self,self2):
        return Fraction((self.Numerator*self2.Denominator),(self.Denominator*self2.Numerator))
####################
    def Convert_to_decimal_num(self):
        return (self.Numerator/self.Denominator)
####################
    def Simplification(self):
        Counter = math.gcd(self.Numerator,self.Denominator)
        self.Numerator/=Counter
        self.Denominator/=Counter
        return Fraction((self.Numerator),(self.Denominator))
####################    
Numerator1 = int(input("Enter Numerator of first fraction: "))
Denominator1 = int(input("Enter Denominator of first fraction: "))
Numerator2 = int(input("Enter Numerator of second fraction: "))
Denominator2 = int(input("Enter Denominator of second fraction: "))

print("Sum = ",end="")
F = Fraction(Numerator1,Denominator1)
F2 = Fraction(Numerator2,Denominator2)
F_A = Fraction(1,1)
F_A = F.F_Sum(F2)
F_A.Show()
########## 
F = Fraction(Numerator1,Denominator1)
F2 = Fraction(Numerator2,Denominator2)
print("subtraction = ",end="")
F_A = F.F_Sub(F2)
F_A.Show()
########## 
F = Fraction(Numerator1,Denominator1)
F2 = Fraction(Numerator2,Denominator2)
print("multiplication = ",end="")
F_A = F.F_Multi(F2)
F_A.Show()
########## 
F = Fraction(Numerator1,Denominator1)
F2 = Fraction(Numerator2,Denominator2)
print("Division = ",end="")
F_A = F.F_div(F2)
F_A.Show()
########## 
F = Fraction(Numerator1,Denominator1)
print("Decimal number of first Franction = ",end="")
output_decimal = F.Convert_to_decimal_num()
print(output_decimal)
########## 
F2 = Fraction(Numerator2,Denominator2)
print("Decimal number of second Franction = ",end="")
output_decimal = F2.Convert_to_decimal_num()
print(output_decimal)
########## 
F = Fraction(Numerator1,Denominator1)
print("Simplified of first Franction = ",end="")
F.Simplification()
F.Show()
########## 
F2 = Fraction(Numerator2,Denominator2)
print("Simplified of second Franction = ",end="")
F2.Simplification()
F2.Show()