import random

print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# Define the characters and events
characters = ["hero", "heroine", "villain"]
events = ["You found a hidden path!", "A wild animal appears!", "You discover a mysterious artifact!", "You hear strange whispers in the wind."]

# Introduce the hero
print("You are the hero on a quest to find the hidden treasure on Treasure Island.")

# Define Villain's Door Preference
villain_door = random.choice(["Red", "Blue", "Yellow"])

# Get initial user choice
choice1 = input("You're at a crossroad. Do you want to go left or right? Type 'L' for left or 'R' for right: ").upper()

if choice1 == "L":
    # Hero meets the heroine
    print("You have met the heroine who warns you about the villain.")
    choice2 = input("You arrive at a river. Do you want to swim across or wait for a boat? Type 'S' to swim or 'W' to wait: ").upper()

    if choice2 == "W":
        # Hero and heroine find the doors
        print("You and the heroine wait patiently and find a boat. You arrive safely across the river.")
        print(random.choice(events))
        choice3 = input("You find three doors: Red, Blue, and Yellow. Which door do you choose? Type 'R', 'B', or 'Y': ").upper()

        if choice3 == villain_door[0].upper():
            print(f"The villain was hiding behind the {villain_door} door. Game over!")
        elif choice3 == "Y":
            print("You find the treasure and win!")
        else:
            print("You chose a wrong door. Game over!")
    else:
        print("You get attacked by a sea monster. Game over!")

elif choice1 == "R":
    # Hero encounters the villain
    print(f"You encounter the villain and he traps you behind the {villain_door} door. Game over!")
else:
    print("Invalid choice. Game over.")