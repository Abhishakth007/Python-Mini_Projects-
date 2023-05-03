MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            'milk' : 100,
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
    "water": 500,
    "milk": 300,
    "coffee": 100,
    "profit" : 0,
}
def report():
    for key,value in resources.items():
        print(key,":",value)
def espresso():
                if MENU["espresso"]["ingredients"]['water'] > resources['water']:
                    print("Insufficient water")
                elif MENU["espresso"]["ingredients"]['milk'] > resources['milk']:
                    print("Insufficient milk")
                elif MENU["espresso"]["ingredients"]['coffee'] > resources['coffee']:
                    print("Insufficient coffee")
                else:
                   return True

def cappuccino():
                if MENU["cappuccino"]["ingredients"]['water'] > resources['water']:
                    print("Insufficient water")

                elif MENU["cappuccino"]["ingredients"]['milk'] > resources['milk']:
                    print("Insufficient milk")

                elif MENU["cappuccino"]["ingredients"]['coffee'] > resources['coffee']:
                    print("Insufficient coffee")

                else:
                    return True

def latte():
                if MENU["latte"]["ingredients"]['water'] > resources['water']:
                    print("Insufficient water")
                elif MENU["latte"]["ingredients"]['milk'] > resources['milk']:
                    print("Insufficient milk")

                elif MENU["latte"]["ingredients"]['coffee'] > resources['coffee']:
                    print("Insufficient coffee")

                else:
                    return True

def amount_calculator(quarters,dimes,nickels,pennies):
    x= quarters * 0.25
    y = dimes * 0.10
    z = nickels * 0.05
    a = pennies * 0.01
    total_amount  = x+y+z+a
    return total_amount


end_of_service = False
while not end_of_service:
    end_of_round = False
    while not end_of_round:
        user_choice = input("What do you want ?(espresso/cappuccino/latte)").lower()
        if user_choice == 'off':
            print("Bye")
            end_of_round = True
            end_of_service = True
        elif user_choice == 'espresso':
            if espresso():
                quarter = int(input("Enter no.of quarters:"))
                dime = int(input("Enter no.of dimes:"))
                nickel = int(input("Enter no.of nickels:"))
                penny = int(input("Enter no.of pennies:"))
                resources['water'] -= MENU["espresso"]["ingredients"]['water']
                resources['milk'] -= MENU["espresso"]["ingredients"]['milk']
                resources['coffee'] -= MENU["espresso"]["ingredients"]['coffee']
                resources['profit'] += MENU["espresso"]['cost']
                paid_amount = amount_calculator(quarters=quarter, dimes=dime, nickels=nickel, pennies=penny)
                print(f'The amount u paid is {paid_amount}')
                if paid_amount < MENU["espresso"]["cost"]:
                    print("Insufficient amount")
                elif paid_amount == MENU["espresso"]["cost"]:
                    print("That is exactly the amount required ...")
                    print("Enjoy your Espresso")
                    end_of_round = True
                elif paid_amount > MENU["espresso"]["cost"]:
                    refund_amount = MENU["espresso"]["cost"] - paid_amount
                    print("Enjoy Your Espresso")
                    print(f'Amount refunded = {refund_amount * -1}$.')
                    end_of_round = True

                else:
                    print("Something went wrong")
                    end_of_round = True


            else:
                end_of_round = True

        elif user_choice == 'cappuccino':
            if cappuccino():
                quarter = int(input("Enter no.of quarters:"))
                dime = int(input("Enter no.of dimes:"))
                nickel = int(input("Enter no.of nickels:"))
                penny = int(input("Enter no.of pennies:"))
                resources['water'] -= MENU["cappuccino"]["ingredients"]['water']
                resources['milk'] -= MENU["cappuccino"]["ingredients"]['milk']
                resources['coffee'] -= MENU["cappuccino"]["ingredients"]['coffee']
                resources['profit'] += MENU["cappuccino"]['cost']
                paid_amount = amount_calculator(quarters=quarter, dimes=dime, nickels=nickel, pennies=penny)
                print(f'The amount u paid is {paid_amount}')
                if paid_amount < MENU["cappuccino"]["cost"]:
                    print("Insufficient amount ...:(")
                    print("Amount refunded.")
                elif paid_amount == MENU["cappuccino"]["cost"]:
                    print("That is exactly the amount required ...")
                    print("Enjoy your cappuccino...:)")
                    end_of_round = True
                elif paid_amount > MENU["cappuccino"]["cost"]:
                    refund_amount = MENU["cappuccino"]["cost"] - paid_amount
                    print("Enjoy your cappuccino...:)")
                    print(f'Amount refunded = {refund_amount * -1}$.')
                    end_of_round = True


            else:
                end_of_round = True

        elif user_choice == 'latte':
            if latte():
                quarter = int(input("Enter no.of quarters:"))
                dime = int(input("Enter no.of dimes:"))
                nickel = int(input("Enter no.of nickels:"))
                penny = int(input("Enter no.of pennies:"))
                resources['water'] -= MENU["latte"]["ingredients"]['water']
                resources['milk'] -= MENU["latte"]["ingredients"]['milk']
                resources['coffee'] -= MENU["latte"]["ingredients"]['coffee']
                resources['profit'] += MENU["latte"]['cost']
                paid_amount = amount_calculator(quarters=quarter, dimes=dime, nickels=nickel, pennies=penny)
                print(f'The amount u paid is {paid_amount}')
                if paid_amount < MENU["latte"]["cost"]:
                    print("Insufficient amount")
                elif paid_amount == MENU["latte"]["cost"]:
                    print("That is exactly the amount required ...")
                    print("Enjoy your latte")
                    end_of_round = True
                elif paid_amount > MENU["latte"]["cost"]:
                    refund_amount = MENU["latte"]["cost"] - paid_amount
                    print("Enjoy your latte ..:)")
                    print(f'Amount refunded = {refund_amount*-1}$.')
                    end_of_round = True


            else:
                end_of_round = True

        elif user_choice == 'report':
            print(report())











