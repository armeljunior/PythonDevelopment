# Hangman
import random

Answer = False

loop = 10

wordchoices = ["word", "big", "fat", "marmaduke", "giraffe", "camel", "baboon"]

WordPicked = random.choice(wordchoices)
display = list("")
for letters in range(len(WordPicked)):
    display += "_"

print(display)


print("Word picked was: "+ WordPicked)
while loop > 1:

    Userinput = input("Guess a letter\n").lower()
    if Userinput in WordPicked:
        for i in range(len(WordPicked)):
            if Userinput == WordPicked[i]:
                print(f'The letter {Userinput} was correct')
                display[i] = Userinput
        print(''.join(display))
    else:
        print("This is wrong try again\n")