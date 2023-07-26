import random
# from repil clear
KeepPlaying = True


def calculatecardpoints(card):
    if card == "A":
        return 1
    else:
        return int(card)


def Blackjack():
    global KeepPlaying
    if (KeepPlaying == True):
        print("Welcome to blackjack")

        cards = ["A", "2", "3", "4", "5", "6",
                 "7", "8", "9", "10", "J", "Q", "K"]
        p1cardspicked = []
        computercardspicked = []
        totalpointsp1 = 0
        totalpointscomputer = 0

        for i in range(4):
            randomcardpicker = random.randint(0, len(cards)-1)
            calculatepoints = calculatecardpoints(randomcardpicker)

            if i < 2:
                totalpointsp1 += calculatepoints + 1
                p1cardspicked.append(cards[randomcardpicker])
            else:
                totalpointscomputer += calculatepoints + 1
                computercardspicked.append(cards[randomcardpicker])

        print("Your Cards are: " + str(p1cardspicked))
        print(f"The Total amount is: {totalpointsp1}")

        print("Computer cards are: " + str(computercardspicked))
        print(f"The Total amount is: {totalpointscomputer}")

    while KeepPlaying:
        if totalpointscomputer == 21 and totalpointsp1 != 21:
            print("Computer hit 21. You lose.")
            KeepPlaying = False
            break
        elif totalpointsp1 == 21:
             print(" You hit 21. You win.")
             KeepPlaying = False
             break
        
        decision = input("Would you like another chance to get a card?")
        print("\nHere is your new card")
        randomcardpicker = random.randint(0, len(cards)-1)
        calculatepoints = calculatecardpoints(randomcardpicker)

        totalpointsp1 += calculatepoints + 1
        p1cardspicked.append(cards[randomcardpicker])

        print("Your Cards are: " + str(p1cardspicked))
        print(f"Your New Total amount is: {totalpointsp1}")


        if totalpointsp1 > 21:
            print("You lose Try again")
            KeepPlaying = False
            break
        elif input("Would you like to add another card? Type 'y' to continue or 'n' to reset") == 'y':
            KeepPlaying = True
        elif totalpointsp1 == 21:
            print("You Won !")
            KeepPlaying = False
            break


Blackjack()
