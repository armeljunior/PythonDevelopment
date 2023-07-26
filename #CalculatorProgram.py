# CalculatorProgram
print('''
 _____________________
|  _________________  |
| | ZeArmelCalc   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
''')
# Calculations
# add


def Addition(num1, num2):
    return num1 + num2
# subract


def Subtraction(num1, num2):
    return num1 - num2
# multiply


def Multiply(num1, num2):
    return num1*num2
# divide


def Divide(num1, num2):
    return num1/num2


operations = {
    "+": Addition,
    "-": Subtraction,
    "*": Multiply,
    "/": Divide,
}


def calculator():
    num1 = float(input("What's the first number?: "))

    for i in operations:
        print(i)
    continueloop = True

    while continueloop == True:

        pickoperation = input("Pick an Operation from the list above: ")
        num2 = float(input("What's the second number?: "))
        calculatefunc = operations[pickoperation]
        solution = calculatefunc(num1, num2)
        print(f"{num1} {pickoperation} {num2} = {solution}")

        if input(f"Would you like to continue with {solution} type y, or type n to start a whole new calculation: ") == "y":
            num1 = solution
        else:
            continueloop = False
            calculator()

calculator()