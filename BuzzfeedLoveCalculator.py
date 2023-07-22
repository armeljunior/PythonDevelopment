print("Welcome to the love Calculator!")

name1 = input("What is the first persons name? \n")

name2 = input("What is the second persons name? \n")

#lower() takes a string and changes it all to lowercase "Angelia".lower()
#count() will give you the number o times a letter occurs in a string "Angela".count("A") outputs 1 because its only got 1 capital 

combineNames = name1 + name2

combineNames = combineNames.lower()

TotalT_combineNames = combineNames.count("t")
TotalR_combineNames = combineNames.count("r")
TotalU_combineNames = combineNames.count("u")
TotalE_combineNames = combineNames.count("e")

TotalL_combineNames = combineNames.count("l")
TotalO_combineNames = combineNames.count("o")
TotalV_combineNames = combineNames.count("v")
TotalE_combineNames = combineNames.count("e")

print("T occurs " + str(TotalT_combineNames) + " Times" )
print("R occurs " + str(TotalR_combineNames) + " Times" )
print("U occurs " + str(TotalU_combineNames) + " Times" )
print("E occurs " + str(TotalE_combineNames) + " Times" )

print("L occurs " + str(TotalL_combineNames) + " Times" )
print("O occurs " + str(TotalO_combineNames) + " Times" )
print("V occurs " + str(TotalV_combineNames) + " Times" )
print("E occurs " + str(TotalE_combineNames) + " Times" )

trueScore = TotalT_combineNames + TotalR_combineNames + TotalU_combineNames +TotalE_combineNames
loveScore = TotalL_combineNames+TotalO_combineNames+TotalV_combineNames+TotalE_combineNames

truelovescore = str(trueScore) + str(loveScore)

print("Your true love score is: " + truelovescore)


if (int(truelovescore) < 10) or (int(truelovescore) > 90):
    print(f"Your true love score is {truelovescore}, you go like eggs and sardines in an omelette")
elif (int(truelovescore) >= 40) or (int(truelovescore) <= 50):
    print(f"Your true love score is {truelovescore}, ya'll aight nothing special")
    