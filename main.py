from menu import MENU, resources
power_off = False
#Get and set the value of resources
water_in_machine = resources["water"]
milk_in_machine = resources["milk"]
coffee_in_machine = resources["coffee"]
sales = 0
MENU["espresso"]["ingredients"]["milk"] = 0

#Define Currency values
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def take_payment():
    """
    This function receives payment and returns the total amount paid.
    """
    num_quarter = int(input("How many quarters? \n"))
    num_dime = int(input("How many dimes? \n"))
    num_nickel = int(input("How many nickels? \n"))
    num_pennies = int(input("How many pennies? \n"))

    quarters = num_quarter * quarter
    dimes = num_dime * dime
    nickels = num_nickel * nickel
    pennies = num_pennies * penny
    total = quarters + dimes + pennies + nickels
    return  total

def check_payment():
    """This function checks if the payment made is sufficient to purchase the required item."""
    balance = payment - cost
    if payment > cost :
        print(f"Here's your $ {'% .2f' % balance} change. Enjoy your {user_choice} ")
        return True
    elif payment < cost :
        balance *= -1
        print(f"Insufficient balance. You are ${'% .2f' % balance} short. Your money has been refunded.")
    else:
        print(f"Processing your {user_choice}...")
        return True


    #report = f" Water : {water_in_machine}\n Milk : {milk_in_machine} \n Coffee : {coffee_in_machine}\n Money : {sales}"
    return milk_in_machine, water_in_machine, coffee_in_machine, sales

while not power_off:
    report = f" Water : {water_in_machine}\n Milk : {milk_in_machine} \n Coffee : {coffee_in_machine}\n Money : {sales}"


    #Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    user_choice = input("What would you like? (espresso / latte / cappuccino): \n").lower()

    #Check the user’s input to decide what to do next.
    #Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice == "off":
        print("Power Off.")
        power_off = True

    #When the user enters “report” to the prompt, a report should be generated that shows
    #the current resource values.
    elif user_choice == "report":
        print(report)
    else:
        req_water = MENU[user_choice]["ingredients"]["water"]
        req_coffee = MENU[user_choice]["ingredients"]["coffee"]
        req_milk = MENU[user_choice]["ingredients"]["milk"]
        cost = MENU[user_choice]["cost"]

    #Check resources
        if milk_in_machine < req_milk:
            print("Insufficient milk")

        elif coffee_in_machine < req_coffee:
            print("Insufficient Coffee.")

        elif water_in_machine < req_water:
            print("Insufficient water.")

        else:
            # Take Payment
            payment = take_payment()

        #process Payment
            is_transaction_successful = check_payment()

            if is_transaction_successful:
                milk_in_machine -= req_milk

                coffee_in_machine -= req_coffee

                water_in_machine -= req_water

                sales += cost




#TODO 1:  Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
"""
a. Check the user’s input to decide what to do next.
#b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
"""

#TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
"""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
"""

#TODO 3: Print report.
"""
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""

#TODO 4:  Check resources sufficient?
"""
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""

#TODO 5: Process coins.
"""
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
"""

#TODO 6: Check transaction successful?
"""
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
"""

#TODO 7: Make Coffee.
"""
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""from menu import MENU, resources
power_off = False
#Get and set the value of resources
water_in_machine = resources["water"]
milk_in_machine = resources["milk"]
coffee_in_machine = resources["coffee"]
sales = 0
MENU["espresso"]["ingredients"]["milk"] = 0

#Define Currency values
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

def take_payment():
    """
    This function receives payment and returns the total amount paid.
    """
    num_quarter = int(input("How many quarters? \n"))
    num_dime = int(input("How many dimes? \n"))
    num_nickel = int(input("How many nickels? \n"))
    num_pennies = int(input("How many pennies? \n"))

    quarters = num_quarter * quarter
    dimes = num_dime * dime
    nickels = num_nickel * nickel
    pennies = num_pennies * penny
    total = quarters + dimes + pennies + nickels
    return  total

def check_payment():
    """This function checks if the payment made is sufficient to purchase the required item."""
    balance = payment - cost
    if payment > cost :
        print(f"Here's your $ {'% .2f' % balance} change. Enjoy your {user_choice} ")
        return True
    elif payment < cost :
        balance *= -1
        print(f"Insufficient balance. You are ${'% .2f' % balance} short. Your money has been refunded.")
    else:
        print(f"Processing your {user_choice}...")
        return True


    return milk_in_machine, water_in_machine, coffee_in_machine, sales

while not power_off:
    report = f" Water : {water_in_machine}\n Milk : {milk_in_machine} \n Coffee : {coffee_in_machine}\n Money : {sales}"


    #Prompt user by asking “ What would you like? (espresso/latte/cappuccino):
    user_choice = input("What would you like? (espresso / latte / cappuccino): \n").lower()

    #Check the user’s input to decide what to do next.
    #Turn off the Coffee Machine by entering “ off ” to the prompt.
    if user_choice == "off":
        print("Power Off.")
        power_off = True

    #When the user enters “report” to the prompt, a report should be generated that shows
    #the current resource values.
    elif user_choice == "report":
        print(report)
    else:
        req_water = MENU[user_choice]["ingredients"]["water"]
        req_coffee = MENU[user_choice]["ingredients"]["coffee"]
        req_milk = MENU[user_choice]["ingredients"]["milk"]
        cost = MENU[user_choice]["cost"]

    #Check resources
        if milk_in_machine < req_milk:
            print("Insufficient milk")

        elif coffee_in_machine < req_coffee:
            print("Insufficient Coffee.")

        elif water_in_machine < req_water:
            print("Insufficient water.")

        else:
            # Take Payment
            payment = take_payment()

        #process Payment
            is_transaction_successful = check_payment()

            if is_transaction_successful:
                milk_in_machine -= req_milk

                coffee_in_machine -= req_coffee

                water_in_machine -= req_water

                sales += cost




#TODO 1:  Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
"""
a. Check the user’s input to decide what to do next.
#b. The prompt should show every time action has completed, e.g. once the drink is
dispensed. The prompt should show again to serve the next customer.
"""

#TODO 2: Turn off the Coffee Machine by entering “ off ” to the prompt.
"""
a. For maintainers of the coffee machine, they can use “off” as the secret word to turn off
the machine. Your code should end execution when this happens.
"""

#TODO 3: Print report.
"""
a. When the user enters “report” to the prompt, a report should be generated that shows
the current resource values. e.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
"""

#TODO 4:  Check resources sufficient?
"""
a. When the user chooses a drink, the program should check if there are enough
resources to make that drink.
b. E.g. if Latte requires 200ml water but there is only 100ml left in the machine. It should
not continue to make the drink but print: “ Sorry there is not enough water. ”
c. The same should happen if another resource is depleted, e.g. milk or coffee.
"""

#TODO 5: Process coins.
"""
a. If there are sufficient resources to make the drink selected, then the program should
prompt the user to insert coins.
b. Remember that quarters = $0.25, dimes = $0.10, nickles = $0.05, pennies = $0.01
c. Calculate the monetary value of the coins inserted. E.g. 1 quarter, 2 dimes, 1 nickel, 2
pennies = 0.25 + 0.1 x 2 + 0.05 + 0.01 x 2 = $0.52
"""

#TODO 6: Check transaction successful?
"""
a. Check that the user has inserted enough money to purchase the drink they selected.
E.g Latte cost $2.50, but they only inserted $0.52 then after counting the coins the
program should say “ Sorry that's not enough money. Money refunded. ”.
b. But if the user has inserted enough money, then the cost of the drink gets added to the
machine as the profit and this will be reflected the next time “report” is triggered. E.g.
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
c. If the user has inserted too much money, the machine should offer change.
E.g. “Here is $2.45 dollars in change.” The change should be rounded to 2 decimal
places.
"""

#TODO 7: Make Coffee.
"""
a. If the transaction is successful and there are enough resources to make the drink the
user selected, then the ingredients to make the drink should be deducted from the
coffee machine resources.
E.g. report before purchasing latte:
Water: 300ml
Milk: 200ml
Coffee: 100g
Money: $0
Report after purchasing latte:
Water: 100ml
Milk: 50ml
Coffee: 76g
Money: $2.5
b. Once all resources have been deducted, tell the user “Here is your latte. Enjoy!”. If
latte was their choice of drink.
"""