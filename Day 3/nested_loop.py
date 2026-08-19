print("welcome to premium rollercoaster ride")
user_height = int(input("Enter your height in cm: "))
user_age = int(input("Enter your age: "))
print("basic fare for the ride is $12.")
total_bill = 0
if user_height >= 120:
    print("You are eligible to ride the rollercoaster!")
    if user_age < 12:
        print("you have to pay $5 for the ride.")
        total_bill += 5
    elif 12 < user_age <= 18:
        print("you have to pay $7 for the ride.")
        total_bill += 7
    elif user_age > 18:
        print("you have to pay $12 for the ride.")
        total_bill += 12
    else:
        print("invalid age input.")
    selfie = input("Do you want a selfie? (yes/no): ")
    if selfie.lower() == "yes":
        print("You have opted for a selfie.")
        print("You have to pay an additional $3 for the selfie.")
        total_bill += 3
    else:
        print("You have opted out of the selfie.")

    
else:
    print("Sorry, you need to be at least 120 cm tall to ride the rollercoaster.")
print("Thank you for visiting the premium rollercoaster ride!")

print(f"the total bill amount for the ride is ${total_bill}.")