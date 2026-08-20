import random
random_number = random.randint(1,2)
if random_number == 1:
    c = "head"
else:
    c="tail"
user_input=input("enter head or tail")
if user_input=="head" and c == "head":
    print("you won")
elif user_input=="tail" and c =="head":
    print("you lost!")
elif user_input =="head" and c=="tail":
    print("you lost")
elif user_input=="tail" and c =="tail":
    print("you won!")
else :
    print("invalid input")