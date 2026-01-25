import datetime
#vars
date = datetime.datetime.now()
born = False
yearBorn = date.year
name = str(input("Enter your name: "))
heightCm = float(input("Enter your height (cm): "))
age = int(input("Enter your age: "))
months = range(1,12)
month = int(input("What month were you born (Number): "))
genders = ["M", "F", "m", "f"]
gender = input("Gender (M/F): ")
###
if month in months:
    if month >= date.month and age >= 0:
        born = True
        yearBorn = date.year-age-1
    elif month < date.month and age >= 0:
        born = True
        yearBorn = date.year-age
    else:
        born = False
        yearBorn = "Stop trying to break me!"
#Name
print("Hello,", name)
#Height
heightFtInt = int(heightCm / 30.48)
heightIn = round((heightCm % 30.48)/2.54)
print("Your height is ", heightFtInt, "'", heightIn, sep="")
#Gender
if gender in genders:
    if gender == "m" or gender == "M":
        gender = "male"
    elif gender == "f" or gender == "F":
        gender = "female"

    print("You are " + gender)
else:
    print("Invalid gender!")
#Age
if age >= 0:
    print("You are", age)
else:
    print("You are not less than 0!")
if born:
    print("You were born in", yearBorn)
else:
    print("Stop trying to break me!")