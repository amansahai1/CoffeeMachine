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

machine_on = True
money = 0



def show_report():
    water = resources["water"]
    print(f"Water : {water}ml")
    milk = resources["milk"]
    print(f"Milk : {milk}ml")
    coffee = resources["coffee"]
    print(f"Coffee : {coffee}g")
    print(f"Money : ${money}")


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


def check_resources(user_choice):
    if user_choice == "espresso":
        if resources["water"] >= MENU["espresso"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["espresso"]["ingredients"]["coffee"]:
            return True
        else:
            return False
    elif user_choice == "latte":
        if resources["water"] >= MENU["latte"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["latte"]["ingredients"]["coffee"] and resources["milk"] >= MENU["latte"]["ingredients"]["milk"]:
            return True
        else:
            return False
    elif user_choice == "cappuccino":
        if resources["water"] >= MENU["cappuccino"]["ingredients"]["water"] and resources["coffee"] >= \
                MENU["cappuccino"]["ingredients"]["coffee"] and resources["milk"] >= \
                MENU["cappuccino"]["ingredients"]["milk"]:
            return True
        else:
            return False


def process_coins():
    print("Please insert coins")
    quarters = int(input("Number of Quarters ?"))
    dimes = int(input("Number of Dimes ?"))
    nickles = int(input("Number of Nickles ?"))
    pennies = int(input("Number of Pennies ?"))
    total_Coin_value = (quarters * .25) + (dimes * .10) + (nickles * .05) + (pennies * .01)
    if MENU[user_selection]["cost"] <= total_Coin_value:
        global money
        money = MENU[user_selection]["cost"] + money
        change = total_Coin_value - MENU[user_selection]["cost"]
        print(f"Your Change is ${change}")
        print("\n")
        print(f"Enjoy your {user_selection} \n")

        return True
    else:
        print("Sorry that's not enough money")
        return False


def deplete_resources(user_choice):
    if user_choice == "espresso":
        resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]
    else:
        resources["water"] = resources["water"] - MENU[user_choice]["ingredients"]["water"]
        resources["milk"] = resources["milk"] - MENU[user_choice]["ingredients"]["milk"]
        resources["coffee"] = resources["coffee"] - MENU[user_choice]["ingredients"]["coffee"]


while machine_on:
    user_selection = input("What would you like? (espresso - $1.5 /latte - $2.5 /cappuccino - $3.0):").lower()
    # TODO : In case user enters other var than dont execute
    if user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
        print(get_cost(user_selection))
        if not (check_resources(user_selection)):
            # TODO : Name the resource which is missing
            print("Sorry there is not enough resources. ")
        else:
            if process_coins():
                deplete_resources(user_selection)

    elif user_selection == "report":
        show_report()
    elif user_selection == "off":
        machine_on = "False"
