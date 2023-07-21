#Tip_Calculator
print("Welcome to the tip calculator")

UserInput = input("What was the total bill?")

How_much_Tip = input("What percentage tip would you like to give? 10, 20, or 15? ")

TotalPeople = input("How many people to split the bill? ")

tipinfloat = float(How_much_Tip)/100 + 1

EachPersonAmount = (float(UserInput)/float(TotalPeople)) * tipinfloat
EachPersonAmount = str(EachPersonAmount)
print("Each person should pay: " + EachPersonAmount)

