#Higher or lower Guessing game
import random


def compareguess(guess, pickednumber,lives):
    if guess > pickednumber:
        print("Your guess is too high, try again")
        return lives - 1
    elif guess < pickednumber:
        print("Your guess is too low, try again")
        return lives - 1
    else:
        print(f"You guessed correctly the number was {pickednumber}")    
        return 0 

easy = 10
hard = 5

pickednumber = random.randint(1,100)

print("Welcome to the number guessing game!\n I'm thinking of a number between 1 and 100.")
lives = input("Choose a difficulty. Type 'easy' or 'hard': ")

if lives == "easy":
    lives = easy
elif lives == "hard":
    lives = hard
else:
    print("Invalid choice, please try again")

print(f"You have {lives} attempts remaining to guess the number.")
guess = input("Make a guess: ")
        

while lives != 0 :
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a guess: ")) 
    lives = compareguess(guess,pickednumber,lives)  
else:
    print(f"Game Over, You lose {lives} lives left. The answer was : {pickednumber}")
