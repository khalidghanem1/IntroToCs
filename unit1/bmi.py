weight = int(input("Enter your weight in kg: "))
height = int(input("Enter your height in cm: "))
bmi = round((weight / (height/100) ** 2), 2)
print("Your BMI is ", bmi, "kg/m^2")