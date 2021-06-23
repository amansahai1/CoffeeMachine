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


#DONE Prompt user by asking "What would you like? (espresso/latte/cappuccino):”
def make_coffee(selection):
    pass


def show_report():
    water = resources["water"]
    print(f"Water : {water}ml")
    milk = resources["milk"]
    print(f"Milk : {milk}ml")
    coffee = resources["coffee"]
    print(f"Water : {coffee}g")
    print(f"Money : ${money}")


def turn_machine_off():
    pass


def get_cost(user_choice):
    if user_choice == "espresso":
        return_cost = MENU["espresso"]["cost"]
        return return_cost
    elif user_choice == "latte":
        return_cost = MENU["latte"]["cost"]
        return return_cost
    elif user_choice == "cappuccino":
        return_cost = MENU["cappuccino"]["cost"]
        return return_cost


machine_on = True
money = 10
while machine_on == True:
    user_selection = input("What would you like? (espresso - $1.5 /latte - $2.5 /cappuccino - $3.0):").lower()
    # TODO : In case user enters other var than dont execute
    if user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino" :
        print(get_cost(user_selection))
    elif user_selection == "report":
        show_report()
    elif user_selection == "off":
        machine_on = "False"


