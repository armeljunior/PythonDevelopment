alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message\n")
shift = int(input("Type the shift number:\n"))
newposition = ''
newletters = ''


def encoder(typedtext=text, shiftedamnt=shift, type=direction):
    cyphershift = ''

    if direction == 'encode':

        for eachletter in text:
            position = alphabet.index(eachletter)
            newposition = position + shift
            newletters = alphabet[newposition]
            cyphershift += newletters

        print(cyphershift)
    elif direction == 'decode':

        for eachletter in text:
            position = alphabet.index(eachletter)
            newposition = position - shift
            newletters = alphabet[newposition]
            cyphershift += newletters

        print(cyphershift)
    # goes from h > m -> h i(1) j(2) k(3) l(4) m(5)
    return


"""
#version 1  
def encrypt(typedtext=text, shiftedamnt=shift):
    cyphershift = ''
    for eachletter in text:
        position = alphabet.index(eachletter)
        newposition = position + shift
        newletters = alphabet[newposition]
        cyphershift += newletters

    print(cyphershift)
    # goes from h > m -> h i(1) j(2) k(3) l(4) m(5)
    return


def decrypt(typedtext=text, shiftedamnt=shift):
    cyphershift = ''

    for eachletter in text:
        position = alphabet.index(eachletter)
        newposition = position - shift
        newletters = alphabet[newposition]
        cyphershift += newletters

    print(cyphershift)
    # goes from h > m -> h i(1) j(2) k(3) l(4) m(5)
    return


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)
else:
    print("Wrong Input, Please run the code again armel")
 """
