"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

while True:

    input_string = input("> ")
    tokens = input_string.split(" ")
    print(tokens)

    if "q" in tokens:
        print("Exiting program")
        break

    elif len(tokens) < 2:
        print("Please supply an operator and required number(s)\n\
                i.e. '+ 2 3'")
    else:
        print("calculating!")
        
        # not_valid = True
        # while not_valid:
        #     try:
        #         num1 = float(tokens[1])
        #         break
        #     except ValueError:
        #         print("Please supply an operator and required number(s)")
        #         input_string = input("> ")
        #         continue

        operator = tokens[0]
        num1 = float(tokens[1])

        if operator == "+":
            num2 = float(tokens[2])
            print(add(num1, num2))

        elif operator == "-":
            num2 = float(tokens[2])
            print(subtract(num1, num2))

        elif operator == "*":
            num2 = float(tokens[2])
            print(multiply(num1, num2))

        elif operator == "/":
            num2 = float(tokens[2])
            print(divide(num1, num2))

        elif operator == "square":
            print(square(num1))

        elif operator == "cube":
            print(cube(num1))

        elif operator == "pow":
            num2 = float(tokens[2])
            print(power(num1, num2))

        elif operator == "mod":
            num2 = float(tokens[2])
            print(mod(num1, num2))
