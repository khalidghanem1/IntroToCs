# inputs
numberOfEggs = int(input("Number of eggs: "))
pricePerDozen = float(input("How much does one dozen cost: "))
pricePerEgg = float(input("How much does one egg cost: "))
# math
totalNumberOfDozens = (numberOfEggs // 12)
remainderEggs = numberOfEggs % 12
totalPrice = f"{(pricePerEgg * remainderEggs) + (pricePerDozen * totalNumberOfDozens):.2f}"
# prints
print()
print("-" * 50)
print()
print("Total number of dozens: ", totalNumberOfDozens)
print("Total price: ", "$" + totalPrice)