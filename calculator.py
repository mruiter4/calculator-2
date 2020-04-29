"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# Replace this with your code
def validate_numeric_input(number):
    try:
        number = float(number)
        return number

    except ValueError:
        print("Make sure you enter numbers for your equation.")
        calculate()

def calculate():
    while True:
        equation = input("Enter your equation or 'q' to quit: ")
        equation_tokens = equation.split(" ")

        if equation.upper() == 'Q':
            print("Goodbye!")
            break

        operator = equation_tokens[0]
        num1 = validate_numeric_input(equation_tokens[1])
        if len(equation_tokens) > 2:
            num2 = validate_numeric_input(equation_tokens[2])


calculate()
