import sys
def gradeLimit(grade):
    if grade > 8 or grade < 0:
        print()
        print("Invalid grade!")
        sys.exit("six sevennn")
#devTest
overrideGrade = (input("Press enter if not developer. "))
#collect inputs
if overrideGrade == "":
    gradeA = int(input("Enter your grade for Criterion A: "))
    gradeLimit(gradeA)
    gradeB = int(input("Enter your grade for Criterion B: "))
    gradeLimit(gradeB)
    gradeC = int(input("Enter your grade for Criterion C: "))
    gradeLimit(gradeC)
    gradeD = int(input("Enter your grade for Criterion D: "))
    gradeLimit(gradeD)
    grades = [gradeA, gradeB, gradeC, gradeD]
    totalGrade = sum(grades)
else:
    grades = int(overrideGrade)
    totalGrade = int(overrideGrade)
#calculate myp
myp = round(totalGrade/4)
if myp == 8:
    myp = 7
if myp > 8:
    print("hi kg")
#print
if myp >= 6:
    congrats = "Good job! Baba and Mama will be proud!"
else:
    congrats = "Might need to study a bit more..."
print("-" * 50)
print("You got", totalGrade, "points.")
print("Your MYP final grade is:", myp)
print("Your lowest grade is", min(grades))
print(congrats)