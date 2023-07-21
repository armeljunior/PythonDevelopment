two_digit_number = input("Please type a two digit number \n")

firstDigit = two_digit_number[0]
print(firstDigit)

secondDigit = two_digit_number[1]
print(secondDigit)

AdditionofTwoNumbers = int(firstDigit) + int(secondDigit)
firstDigitStr = str(firstDigit)
secondDigitStr = str(secondDigit)
AdditionofTwoNumbersStr = str(AdditionofTwoNumbers)

print(two_digit_number[0] + " + " +two_digit_number[1] + " = " + AdditionofTwoNumbersStr)