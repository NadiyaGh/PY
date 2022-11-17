weight = float(input("Enter your weight(kg): "))
height = float(input("Enter your height(cm): "))

height /= 100
BMI = float(weight / (height ** 2))
BMI = round(BMI,1)

if BMI >= 35 and BMI <= 39.9:
    print("Your BMI is ",BMI,"indicating your weight is in the «Extreme Obesity» category for adults of your height!!!")
elif BMI >= 30 and BMI <= 34.9:
    print("Your BMI is ",BMI,"indicating your weight is in the «Obesity» category for adults of your height!!")
elif BMI >= 25 and BMI <= 29.9:
    print("Your BMI is ",BMI,"indicating your weight is in the «Overweight» category for adults of your height!")
elif BMI >= 18.5 and BMI <= 24.9:
    print("Your BMI is ",BMI,"indicating your weight is in the «Normal Weight» category for adults of your height :)")
else:
    print("Your BMI is ",BMI,"indicating your weight is in the «Underweight!» category for adults of your height!")