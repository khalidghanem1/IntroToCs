import datetime
#vars
date = datetime.datetime.now()
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
    if month >= date.month:
        yearBorn = date.year-age-1
    else:
        yearBorn = date.year-age
#Name
print("Hello,", name)
#Height
heightFtInt = int(heightCm / 30.48)
heightIn = round((heightCm % 30.48)/2.54)
print("Your height is ", heightFtInt, "'", heightIn, sep="")
#Gender
if gender in genders:
    if gender == "m":
        gender = "M"
    elif gender == "f":
        gender = "F"

    print("You are " + gender)
else:
    print("Invalid gender!")
#Age
print(age)
print("You were born in ", yearBorn)
