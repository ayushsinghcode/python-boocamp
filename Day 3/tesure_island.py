print("""
**********************************************************************
*                                                                    *
*                         TREASURE ISLAND                            *
*                                                                    *
*                 ______________________________________             *
*                /                                     \\            *
*               /                                       \\           *
*              /          _____________                  \\          *
*             /          /             \\                 \\         *
*            /          /   TREASURE    \\                 \\        *
*           /          /_______________\\                   \\       *
*          /                                                 \\      *
*         /              ~ ~ ~ ~ ~ ~ ~ ~ ~                    \\     *
*        /          ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~                  \\    *
*       /        ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~ ~                  \\   *
*      /_________________________________________________________\\  *
*                                                                    *
**********************************************************************
""")
import random
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_choice1 = input("You are at a cross road. Where do you want to go? Type 'left' or 'right': ").lower()
if user_choice1 == "right":
    print("You fell into a hole. Game Over.")
else:
    print("You have come to a lake. There is an island in the middle of the lake.")
    user_choice2 = input("Type 'wait' to wait for a boat. Type 'swim' to swim across: ").lower()
    if user_choice2 == "swim":
        print("You get attacked by an angry trout. Game Over.")
    else:
        print("You arrive at the island unharmed. There is a house with 3 doors.")
        user_choice3 = input("One red, one yellow and one blue. Which colour do you choose? ").lower()
        if user_choice3 == "red":
            print("It's a room full of fire. Game Over.")
        elif user_choice3 == "blue":
            print("You enter a room of beasts. Game Over.")
        elif user_choice3 == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("You chose a door that doesn't exist. Game Over.")