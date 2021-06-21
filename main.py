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


# TODO Prompt user by asking "What would you like? (espresso/latte/cappuccino):”
def make_coffee(selection):
    pass


def show_report():
    pass


def turn_machine_off():
    pass


user_selection = input("What would you like? (espresso/latte/cappuccino):").lower()

print(user_selection)
if user_selection == "latte" or user_selection == "espresso" or user_selection == "cappiccino":
    make_coffee(user_selection)
elif user_selection == "report":
    show_report()
elif user_selection == "off":
    turn_machine_off
