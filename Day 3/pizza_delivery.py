print("welcome to python pizza delivery service")
size = input("What size pizza do you want? S, M, or L: ")
add_pepperoni = input("Do you want pepperoni? Y or N: ")
cheese = input("Do you want extra cheese? Y or N: ")
total_bill = 0
user_name = input("Enter your name: ")
if size.upper() == "S":
    total_bill += 15
    if add_pepperoni.upper() == "Y":
        total_bill += 2
    if cheese.upper() == "Y":
        total_bill += 1
elif size.upper() == "M":
    total_bill += 20
    if add_pepperoni.upper() == "Y":
        total_bill += 3
    if cheese.upper() == "Y":
        total_bill += 1
elif size.upper() == "L":
    total_bill += 25
    if add_pepperoni.upper() == "Y":
        total_bill += 3
    if cheese.upper() == "Y":
        total_bill += 1
print(f"Your total bill is ${total_bill}.")
print(f"Thank you for ordering from python pizza delivery service, {user_name}!")
