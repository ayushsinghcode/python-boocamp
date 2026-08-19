print("                             Bmi Calculator")
user_name = input("Enter your name: ")
print(f"Hello, {user_name}! Welcome to the BMI Calculator.")
print("Please enter your weight in kilograms and height in meters to calculate your BMI.")
user_weight = float(input("Enter your weight in kg: "))
user_height = float(input("Enter your height in meters: ")) 
if user_height <= 0:
    print("Height must be greater than zero.")
elif user_weight <= 0:
    print("Weight must be greater than zero.")
else:
    bmi = user_weight / (user_height ** 2)
    print(f"{user_name}, your BMI is: {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif 18.5 <= bmi < 24.9:
        print("You have a normal weight.")
    elif 25 <= bmi < 29.9:
        print("You are overweight.")
    else:
        print("You are obese.")
