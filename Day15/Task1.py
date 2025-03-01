###Coffee Machine Program
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

def money():
    print("Please insert coins.")
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickles = int(input("How many nickles: "))
    pennies = int(input("How many pennies: "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return total

def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

earnings = 0
def transaction_Successful(money_received,cost_drink):
    if money_received >= cost_drink:
        change = round(money_received - cost_drink,2)
        print(f"Here is ${change} in change.")
        global earnings
        earnings += cost_drink
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False
    
def make_coffee(drink_name,order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


order = True
while order:
    print("Welcome to the Coffee Machine")
    Coffee = input("​What would you like? (espresso/latte/cappuccino): ")
    if Coffee.lower == "off":
        order = False
    elif Coffee.lower == "espresso" or Coffee.lower == "latte" or Coffee.lower == "cappuccino":
        drink = MENU[Coffee]
        if check_resources(drink["ingredients"]):
            trasaction = money()
        if transaction_Successful(trasaction,drink["cost"]):
            make_coffee(Coffee,drink["ingredients"])
    elif Coffee.lower == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${earnings}")
    else:
        print("Invalid Input")
        order = False
        
