print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
bill = 0 

# todo: work out how much they need to pay based on their size choice.
if size.lower() == "s":
    bill += 15
elif size.lower() == "m":
    bill += 20
elif size.lower() == "l":
    bill += 25
else:
    print("Invalid size. Please choose S, M or L.")
    
# todo: work out how much to add to their bill based on their pepperoni choice.

if pepperoni.lower() == "y":
    if size.lower() == "s":
        bill += 2
    else:
        bill += 3


# todo: work out their final amount based on whether if they want extra cheese.
if extra_cheese.lower() == "y":
    bill += 1

print(f"Your final bill is ${bill:.2f}.")