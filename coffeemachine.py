MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 150,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 250,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 300,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "CashInside": 0
}

def Calculatemoney():
    pennyinput = int(input("How many 1p coins?: ")) 
    teninput = int(input("How many 10p coins?: ")) * 10
    fiftyinput = int(input("How many 50p coins?: ")) * 50
    poundinput = int(input("How many £1 pense coins?: ")) * 100

    totalmoney = pennyinput + teninput + fiftyinput + poundinput

    return totalmoney






def CoffeeMachine():
    MachineOn = True
    while MachineOn:
    
        UserInput1 = input("\nWhat would you like? (espresso/latte/cappuccino): ").lower()

        #if UserInput1 == "espresso":
        if UserInput1 == "report":
            print(resources)
        elif UserInput1 in ["espresso","latte","cappuccino"]: 
            
            resources - (MENU[UserInput1]["ingredients"])



            CashIn = Calculatemoney()
            resources["CashInside"] += CashIn
            drinkcost = float(MENU[UserInput1]["cost"])
            poundchange = CashIn - drinkcost/100
            if CashIn < drinkcost:
                print("YOU BROKE, SIR KINDLY GET YOUR MONEY UP ")
            else:
                print(f"\nHere is your {UserInput1} Hope you enjoy it")
                print(f"Here is your change £{poundchange}0p")


CoffeeMachine()