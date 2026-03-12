password = "6767"
tries = 0
while tries < 3:
    inpass = input("Enter password: ")
    if inpass == password:
        print("Welcome!")
        tries = 3
    elif tries < 3:
        print("Incorrect password! You have " + str(2-tries) + " tries left.")
        tries = tries + 1
    else:
        tries = tries + 1
        print("Incorrect password! You have no more attempts.")
