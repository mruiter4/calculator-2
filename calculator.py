"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


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
        if len(equation_tokens) >3:
            num3 = validate_numeric_input(equation_tokens[3])

        if equation_tokens[0] == '+':
            result = add(num1, num2)
           
        elif equation_tokens[0] == '-':
            result = subtract(num1, num2)
            
        elif equation_tokens[0] == '*':
            result = multiply(num1, num2)

        elif equation_tokens[0] == '/':
            result = divide(num1, num2)

        elif equation_tokens[0] == 'square':
            result = square(num1)

        elif equation_tokens[0] == 'cube':
            result = cube(num1)

        elif equation_tokens[0] == 'pow':
            result = power(num1, num2)

        elif equation_tokens[0] == 'mod':
            result = mod(num1, num2)

        elif equation_tokens[0] == 'x+':
            result = add_mult(num1, num2, num3)

        elif equation_tokens[0] == 'cube+':
            result = add_cubes(num1, num2)
             
        else:
            print('Please enter a valid operator')
            continue

        print(result)

calculate()
