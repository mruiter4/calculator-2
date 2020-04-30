"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, add_mult, add_cubes)


# Replace this with your code
def validate_numeric_input(num_tokens):
    nums = []
    try:
        for num in num_tokens:
            nums.append(float(num))
        return nums

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

        operator, *num_tokens = equation_tokens
        nums = validate_numeric_input(num_tokens)
        if (operator not in ['cube', 'square'] and len(num_tokens) < 2) or \
            (operator == 'x+' and len(num_tokens) <3):
            print("You didn't enter enough operands for this equation. Try again")
            continue

        if equation_tokens[0] == '+':
            result = add(nums[0], nums[1])
           
        elif equation_tokens[0] == '-':
            result = subtract(nums[0], nums[1])
            
        elif equation_tokens[0] == '*':
            result = multiply(nums[0], nums[1])

        elif equation_tokens[0] == '/':
            result = divide(nums[0], nums[1])

        elif equation_tokens[0] == 'square':
            result = square(nums[0])

        elif equation_tokens[0] == 'cube':
            result = cube(nums[0])

        elif equation_tokens[0] == 'pow':
            result = power(nums[0], nums[1])

        elif equation_tokens[0] == 'mod':
            result = mod(nums[0], nums[1])

        elif equation_tokens[0] == 'x+':
            result = add_mult(nums[0], nums[1], nums[2])

        elif equation_tokens[0] == 'cubes+':
            result = add_cubes(nums[0], nums[1])
             
        else:
            print('Please enter a valid operator')
            continue
            
        print(result)

calculate()
