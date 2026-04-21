#funcsss
import sys

sys.set_int_max_str_digits(0)
import time
totalWaste = 0
totalUse = 0
wasteSource = []
def wait(t):
    time.sleep(t)
def shower(t):
    waterW = int(0)
    waterW1 = int(t*16000)
    waterS = int(0)
    WaterW2 = int(waterW1 - waterS)
    print("You get into the shower... you start the water, it's hot.")
    wait(1)
    print("You start with body wash, do you keep the water running while you apply the soap?")
    a = input("Yes/No ").strip().capitalize()
    if a == "Yes":
        waterW = waterW + 6000
        wasteSource.append("leaving water on while applying body wash")
    if a == "No":
        waterS = waterS + 6000
    print("Smelling good! Next up is shampoo and conditioner, do you keep the water running while you apply the soap?")
    b = input("Yes/No ").strip().capitalize()
    if b == "Yes":
        waterW = waterW + 6000
        wasteSource.append("leaving water on while washing hair")
    if b == "No":
        waterS = waterS + 6000
    global totalUse
    global totalWaste
    totalWaste = totalWaste + waterW
    totalUse = totalUse + (waterW1 - waterS)




#welcome
print("Welcome new employee! Please create your UserID to start the UN EcoFriendly Training:")
userId = input("New UserID: ")
print("Welcome, " + userId + "! We will now begin the training regimen with a simulation.")
#start game
print("- "*50)
print("Good morning, " + userId + "! It is 7:45AM.")
wait(1)
print("You need to be at your new job at 8:30. Let's start the day! You showered last night, what do you do first?")
aa1 = int(input("Shower again [1] or brush teeth [2]? (Enter number): "))
if aa1 == 1:
    print("You walk towards the bathroom and open the shower")
    leng = int(input("How long would you like to shower? (Minutes): "))
    shower(leng)
print("You used", totalUse, "Ml of water.", totalWaste, "Ml of which could have ben saved.")
