repeat = "yes"
import math
while repeat.lower() == "yes":
    print("===============================")
    print("         CALCULATOR            ")
    print("===============================")

    sign = input("Enter your choice (% ,+ ,- , * ,/ ,** ,// ,sr(Square Root) ,max (Maximum of Two numbers) ,min (Minimum of Two numbers) ,odd , even: ").lower()

    if sign.lower() == "sr":
        number = float(input("Enter the number: "))
    elif sign == "even":
        number = int(input("Enter the number: "))
    elif sign == "odd":
        number = int(input("Enter the number: "))
    elif sign in ("max", "min", "%", "**", "/", "+", "-", "*", "//"):
        number1 = int(input("Enter the first number: "))
        number2 = int(input("Enter the second number: "))
    else:
        print("ERROR")
        sign = input("Enter your choice (% ,+ ,- , * ,/ ,** ,// ,sr(Square Root) ,max (Maximum of Two numbers) ,min (Minimum of Two numbers) ,odd , even: ").lower()
        
    if sign == "%":
        print(f"Modulo of {number1} % {number2} is: {number1 % number2}")
    elif sign == "+":
        print(f"Addition of {number1} + {number2} is: {number1 + number2}")
    elif sign == "-":
        print(f"Subtraction of {number1} - {number2} is: {number1 - number2}")
    elif sign == "/":
        if number2 == 0:
            print("Division by zero is not allowed")
        else:
            print(f"Division of {number1} / {number2} is: {number1 / number2}")
    elif sign == "*":
        print(f"Multiplication of {number1} * {number2} is: {number1 * number2}")
    elif sign == "**":
        print(f"Power of {number1} ** {number2} is: {number1 ** number2}")
    elif sign == "//":
        print(f"Sub Division of {number1} // {number2} is: {number1 // number2}")
    elif sign.lower() == "sr":
        print(f"Square root of {number} is: {math.sqrt(number)}")
    elif sign.lower() == "max":
        if number1 > number2:
            print(f"Maximum of {number1} and {number2} is: {number1}")
        elif number2 > number1:
            print(f"Maximum of {number1} and {number2} is: {number2}")
        else:
            print(f"Both numbers are same {number1} and {number2}")
    elif sign.lower() == "min":
        if number1 < number2:
            print(f"Minimum of {number1} and {number2} is: {number1}")
        elif number2 < number1:
            print(f"Minimum of {number1} and {number2} is: {number2}")
        else:
            print(f"Both numbers are same {number1} and {number2}")
    elif sign.lower() == "even":
        if number % 2 == 0:
            print(f"The number {number} is even")
        else:
            print(f"The number {number} is odd")
    elif sign.lower() == "odd":
        if number % 2 != 0:
            print(f"The number {number} is odd")
        else:
            print(f"The number {number} is even")

    else:
        print("--> Please enter from this only (% ,+ ,- , * ,/ ,** ,//) <--")

    repeat = input("Do you want to do another calculation? (yes or no): ").lower()
    if repeat.lower() == "no":
        print("\n--->Thank you for using the calc<---")
    else:
        print("Error")