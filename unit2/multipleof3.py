num = 1
while num != 0:
    num = int(input("Enter a number or 0 to exit: "))
    if num != 0:
        if num % 3 == 0:
            print(num, "is a multiple of 3",  "("+str(num)+"/3 =", str(num/3)+")")
        else:
            print(num, "is not a multiple of 3", "("+str(num)+"/3 =", str(f"{(num/3):.2f}")+")")
    else:
        print("Goodbye!")
