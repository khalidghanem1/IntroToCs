item1 = 12.99
item2 = 5.49
item3 = 8.75
taxRate = 0.08
totalBfrTax = item1 + item2 + item3
taxAmount = totalBfrTax * taxRate
totalAfterTax = totalBfrTax + taxAmount
#
print("Total cost before tax:", str(totalBfrTax))
print("Tax amount:", str(taxAmount))
print("Total cost after tax:", str(totalAfterTax))

