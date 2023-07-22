for Number in range(1,101):
    if(Number % 3 == 0):
        print("Fizz")
    elif(Number % 5 == 0):
        print("Buzz")
    elif(Number % 3 and Number % 5 == 0 ):
        print("FizzBuzz")
    else:
        print(Number)