def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def validate_input(value):
    try:
        val = float(value)
        return val
    except ValueError:
        raise ValueError("Invalid input, please enter a number.")

if __name__ == '__main__':
    # Sample usage
    try:
        num1 = validate_input(input('Enter first number: '))
        num2 = validate_input(input('Enter second number: '))
        print(f'Addition: {add(num1, num2)}')
        print(f'Subtraction: {subtract(num1, num2)}')
        print(f'Multiplication: {multiply(num1, num2)}')
        print(f'Division: {divide(num1, num2)}')
    except ValueError as e:
        print(e)