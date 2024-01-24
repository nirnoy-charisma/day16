from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

my_moneymachine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()


is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"What would you like? {options} ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        my_moneymachine.report()
    else:
        drink = menu.find_drink(choice)
        resource=coffee_maker.is_resource_sufficient(drink)
        transaction = my_moneymachine.make_payment(drink.cost)
        if resource and transaction:
            coffee_maker.make_coffee(drink)


