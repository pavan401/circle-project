# calculator.py

def add(a, b):
    """Return the sum of two numbers."""
    return a + b


def subtract(a, b):
    """Return the difference between two numbers."""
    return a - b


def multiply(a, b):
    """Return the product of two numbers."""
    return a * b


def divide(a, b):
    """Return the division of two numbers."""
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


if __name__ == "__main__":
    print("Simple Calculator")
    print("Select operation: add, subtract, multiply, divide:")

try:
 operation = input("Enter operation: ").strip().lower()
except EOFError:
    print("Input stream closed. Please provide input next time.")
    exit(1)

    if operation == "add":
        print("Result:", add(a, b))
    elif operation == "subtract":
        print("Result:", subtract(a, b))
    elif operation == "multiply":
        print("Result:", multiply(a, b))
    elif operation == "divide":
        print("Result:", divide(a, b))
    else:
        print("Invalid operation")
