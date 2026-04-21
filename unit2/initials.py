def initials(first, last):
    h = first[0].capitalize()
    j = last[0].capitalize()
    initials_str = f"{h},{j}"
    return initials_str

first_name = input("Enter first name: ")
last_name = input("Enter last name: ")

result = initials(first_name, last_name)

print(result)
