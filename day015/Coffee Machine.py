# 100 Days of Code
# DAY 015
# Created by eduardorabe
# Coffee Machine

from menu import MENU, resources


def report(water, milk, coffee, profit):
    """Show report about machine resources ans money"""
    print(f"Water : {water}ml")
    print(f"Milk : {milk}ml")
    print(f"Coffee : {coffee}g")
    print(f"Money : ${profit:.2f}")


def is_resources_sufficient(order_ingredients):
    """Returns True when order can be made, False if there is not enough ingredients"""
    for item in order_ingredients:
        if order_ingredients.get(item) >= resources.get(item):
            print(f"Sorry, there is not enough {item}")
            return False
    return True


def process_coins():
    """Returns total from coins inserted"""
    print("Please insert coins. ")
    total = int(input("How many quarters? ")) * .25
    total += int(input("How many dimes? ")) * .10
    total += int(input("How many nickles? ")) * .05
    total += int(input("How many pennies? ")) * .01
    return total


def is_transaction_succesful(money_received, drink_cost):
    """Return True when payment is accepted, False if money is insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money Refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")


is_on = True
profit = 0

while is_on:
    choice = str(input("What would you like? (espresso/latte/cappuccino): ")).lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        report(resources.get("water"), resources.get("milk"), resources.get("coffee"), profit)
    else:
        drink_ingredients = MENU.get(choice).get("ingredients")
        if is_resources_sufficient(drink_ingredients):
            payment = process_coins()
            if is_transaction_succesful(payment, MENU.get(choice).get("cost")):
                make_coffee(choice, drink_ingredients)
