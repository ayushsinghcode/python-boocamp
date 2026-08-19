total_bill = float(input("Enter the total bill amount: "))
tip_percentage = float(input("Enter the tip percentage (e.g., 15 for 15%): "))
total_peoples = int(input("Enter the number of people to split the bill: "))
each_person_tip = total_bill * (tip_percentage / 100) / total_peoples
print(f"Each person should contribute: ${each_person_tip:.2f} as tip.")
print(f"total bill ammount is: ${total_bill:.2f} and tip percentage is {tip_percentage}% and total peoples are {total_peoples} and each person should contribute: ${each_person_tip:.2f} as tip. and total amount to be paid by each person is: ${total_bill / total_peoples + each_person_tip:.2f}")