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

profits = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def resources_report():
    """Prints a report of the current available resources and money earned."""
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profits}")
    

def is_resource_sufficient(drink_ingredients):
    """Returns True if order can be made, False if ingredients are not enough"""
    for ingredient in drink_ingredients:
        if drink_ingredients[ingredient] >= resources[ingredient]:
            print(f"Sorry, there is no enough {ingredient}")
            return False
    return True


def process_coins():
    """Returns the total calculated from the inserted coins."""
    print("Please, insert coins: ")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.1
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


def is_transaction_successful(received_money, drink_cost):
    """Returns True if the payment is accepted, or False if money is insufficient."""
    if received_money >= drink_cost:
        change = round(received_money - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profits
        profits += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Deduct the required ingredients from the resources"""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_name}!")

is_on = True

while is_on:
    user_choice = input(
        "What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == 'off':
        is_on = False
    elif user_choice == 'report':
        resources_report()
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(user_choice, drink['ingredients'])
                