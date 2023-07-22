import random

ComputerChoice = random.randint(0,2)

User = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Printing User's choice
print("You chose:")
if User == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
elif User == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''')
elif User == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')
else:
    print("Invalid choice!")
    exit()

# Printing Computer's choice
print("Computer chose:")
if ComputerChoice == 0:
    print('''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
    ''')
elif ComputerChoice == 1:
    print('''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
    ''')
elif ComputerChoice == 2:
    print('''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
    ''')

# Determining the winner
if User == ComputerChoice:
    print("It's a draw!")
elif (User == 0 and ComputerChoice == 2) or (User == 1 and ComputerChoice == 0) or (User == 2 and ComputerChoice == 1):
    print("You win!")
else:
    print("You lose!")
