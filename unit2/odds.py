a = int(input("Enter a minimum: "))
b = int(input("Enter a maximum: "))
print("Odd numbers from", a, "to", b, "are")
for i in range(a,b):
    if i % 2 != 0:
        print(i)