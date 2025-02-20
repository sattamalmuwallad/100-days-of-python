from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

moneymachine = MoneyMachine()
coffeemaker = CoffeeMaker()
menu = Menu()

order = True

print(menu.get_items())
## choice = input(print(f"What would you like? {menu.get_items()}"))