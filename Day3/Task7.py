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
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
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

choice= input('Please enter either left or right to continue? ')
if choice.lower()=="left":
    print("You've come to a lake. There is an island in the middle of the lake.")
    left_choice = input('Please enter either wait or swim to continue? ')
    if left_choice.lower()=="wait":
        door_choice = input("Which door? Red, Blue or Yellow: ")
        if door_choice.lower() == "red":
            print("Burned by fire. Game Over.")
            exit()
        elif door_choice.lower() == "blue":
            print("You got eaten by Beasts! Game Over.")
            exit()
        elif door_choice.lower() == "yellow":
            print("You found the treasure! Congratulations!")
            exit()
        else:
            print("Invalid door choice. Game Over.")
            exit()
    else:
        print("Attacked by Trout. Game Over.")
        exit()
else:
    print("Fall into a hole. Game Over.")
    exit()
