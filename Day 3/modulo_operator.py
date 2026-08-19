user_input = int(input("Enter a number: "))
if user_input % 2 == 0:
    print(f"{user_input} is an even number.")
else:
    print(f"{user_input} is an odd number.")
print("Thank you for using the even-odd checker!")

#basically modulo operator is divided by the number and gives the remainder. if the remainder is 0 then it is an even number otherwise it is an odd number.
