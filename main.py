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

total_money = 0

# TODO 2. Turn Off Coffee Machine
is_running = True


# TODO 3. Print Report
def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${total_money}")


# TODO 4. Check Resources Sufficient?
def is_resources_sufficient(choice, MENU, resources):
    for x in MENU[choice]["ingredients"]:
        if resources[x] < MENU[choice]["ingredients"][x]:
            print(f"Sorry there is not enough {x}.")
            return False
        else:
            return True


# TODO 5. Process Coin
def process_coin():
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.10
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01

    return total


# TODO 6. Check Transaction Successfull
def check_transaction_success(money, drink_cost):
    global total_money
    if money >= drink_cost:
        change = round(money - drink_cost, 2)
        print(f"Here is ${change} dollars in change.")
        total_money += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


# TODO 7. Make Coffee
def make_coffee():
    for item in MENU[choice]["ingredients"]:
        resources[item] -= MENU[choice]["ingredients"][item]
    print(f"Here is your {choice} ☕. Enjoy!")


while is_running:
    # TODO: 1. Prompt User
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choice == "report":
        print_report()
    elif choice == "off":
        is_running = False
    else:
        resources_check = is_resources_sufficient(choice=choice, MENU=MENU, resources=resources)
        if resources_check:
            user_money = process_coin()
            if check_transaction_success(money=user_money, drink_cost=MENU[choice]["cost"]):
                make_coffee()
