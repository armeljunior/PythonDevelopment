#Password Generator
import random
letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',
           'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
numbers = ['0','1','2','3','4','5','6','7','8','9']
symbols = ['!','#','$','%','&','(',')','*','+']

print("Welcome to the password generator")

num_letters = int(input("How many letters would you like?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))
print("\n")

lettersSelected = ""
symbolsSelected = ""
numbersSelected = ""
randomPasswordNoOrder = ""
for i in range (num_letters):
    lettersSelected += (letters[random.randint(0,len(letters)-1)])
    #print("letters selected:"+lettersSelected)

for i in range (num_symbols):
    symbolsSelected += (symbols[random.randint(0,len(symbols)-1)])
    #print("symbols selected:"+symbolsSelected)

for i in range (num_numbers):
    numbersSelected += (numbers[random.randint(0,len(numbers)-1)])
    #print("numbers selected:"+numbersSelected)

FinalSelection = lettersSelected + symbolsSelected + numbersSelected

for i in range(0,len(FinalSelection)):
    randomPasswordNoOrder += (random.choice(FinalSelection))


passwordlist = list(FinalSelection)
random.shuffle(passwordlist)
ShuffledPassword = ''.join(passwordlist)

print(ShuffledPassword)
print(FinalSelection)
#print(ShuffledPassword) 