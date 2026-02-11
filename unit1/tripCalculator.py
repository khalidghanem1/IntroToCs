#trip calc
print("Trip Calculator")
print("-" * 50)
#inputs
dest = str(input("Destination: "))
nights = int(input("Number of nights: "))
hotelCost = float(input("Hotel cost: "))
flightCost = float(input("Flight cost: "))
mealsCost = float(input("Meals cost per day: "))
transCost = float(input("Transport cost per day: "))
noPeople = int(input("How many people to split the trip: "))
#calcs
subTotalHotel = nights*hotelCost*noPeople
subTotalFlight = flightCost*noPeople
subTotalMeals = mealsCost*noPeople*nights
subTotalTransCost = transCost*noPeople*nights
#
subTotal = [subTotalMeals, subTotalHotel, subTotalFlight, subTotalTransCost]

expenses = {
    "Hotel": subTotalHotel,
    "Flight": subTotalFlight,
    "Meals": subTotalMeals,
    "Transport": subTotalTransCost
}

total = sum(expenses.values())

#prints
print("-" * 100)
print("Total budget for", dest.capitalize())
print("- " * 50)
print("Subtotals:")

for category, amount in expenses.items():
    percentage = (amount/total)*100
    print (f"{category}: ${amount:.2f},", f"{percentage:.2f}% of total")

print("- " * 50)
print(f"Total:", f"${total:.2f}")
print("Per person:", f"${(total/noPeople):.2f}")


