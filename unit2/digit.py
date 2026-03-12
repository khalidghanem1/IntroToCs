num = str(input("Enter a number: "))

print("Digits are")
for i in num:
    if i.isdigit():
        print(i)
    else:
        print("Not a digit")