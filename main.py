from menu import MENU, resources
quarter = 0.25
dime = 0.10
nickel = 0.05
penny = 0.01

water_vol = resources['water']
milk_vol = resources['milk']
coffee_vol = resources['coffee']
resources['money'] = 0
money = float(resources['money'])
MENU['espresso']['ingredients']['milk'] = 0
current_resource = f"Water : {water_vol}ml \nMilk: {milk_vol}g \nCoffee: {coffee_vol}g\nMoney : ${money}"



def check_resources(choice):
    if MENU[choice]['ingredients']['water'] > water_vol:
        print('insufficient water')
    elif MENU[choice]['ingredients']['coffee'] > coffee_vol:
        print('Insufficient Coffee.')
    elif MENU[choice]['ingredients']['milk'] > milk_vol:
        print('Insufficient milk')
    else:
        #Take coins
        print("Please insert coins: ")

def calculate_payment():
    quarters = num_quarter * quarter
    dimes = num_dime * dime
    nickels = num_nickel * nickel
    pennies = num_pennies * penny
    total = quarters + dimes + nickels + pennies
    return total

def check_payment():
    balance = item_cost - payment
    if item_cost > payment:
        print(f"Insufficient funds. you are ${"%.2f" % balance} short.")
    else:
        print("Please wait while we make your coffee.")


#Prompt user by asking “ What would you like? (espresso/latte/cappuccino): ”
user_choice = input("What would you like? (espresso / latte / cappuccino): \n").lower()

#Turn off the Coffee Machine by entering “ off ” to the prompt.
if user_choice == "off":
#Turn off the machine
    print("Switching off...")

#Print report.
elif user_choice == "report":
    print(current_resource)

#Check resources sufficient?
check_resources(user_choice)

# Take Payment
num_quarter = int(input('How many quarters'))
num_dime = int(input('How many dimes'))
num_nickel = int(input('How many nickels'))
num_pennies = int(input('How many pennies'))

item_cost = MENU[user_choice]['cost']
payment = calculate_payment()

check_payment()





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
