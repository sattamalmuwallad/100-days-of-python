from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

order = True


while order:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice.lower() == "off":
        order = False
    elif choice.lower() == "report":
        coffeemaker.report()
        money.report()
    else:
        drink = menu.find_drink(choice)
        if coffeemaker.is_resource_sufficient(drink):
            if money.make_payment(drink.cost):
                coffeemaker.make_coffee(drink)
