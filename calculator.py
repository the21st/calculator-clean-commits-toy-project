import argparse


def parse_args():
    """Parses command-line arguments for the calculator."""
    parser = argparse.ArgumentParser(
        description="A simple calculator.",
        epilog="Example usage: python calculator.py add 5 3",
    )

    parser.add_argument(
        "operation",
        type=str,
        choices=["add", "subtract", "multiply", "divide", "power"],
        help="The operation to perform.",
    )
    parser.add_argument("a", type=float, help="The first number.")
    parser.add_argument("b", type=float, help="The second number.")

    return parser.parse_args()


def add(a, b):
    """
    This function takes two numbers and returns their sum.
    """
    return a + b


def subtract(a, b):
    """
    This function takes two numbers and returns their difference.
    """
    return a - b


def multiply(a, b):
    """
    This function takes two numbers and returns their product.
    """
    return a * b


def divide(a, b):
    """
    This function takes two numbers and returns their division.
    It also handles division by zero.
    """
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def power(a, b):
    """
    This function takes two numbers and returns the first to the power of the second.
    """
    return a ** b


def main():
    """Main function to run the calculator."""
    args = parse_args()

    result = None
    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "subtract":
        result = subtract(args.a, args.b)
    elif args.operation == "multiply":
        result = multiply(args.a, args.b)
    elif args.operation == "divide":
        result = divide(args.a, args.b)
    elif args.operation == "power":
        result = power(args.a, args.b)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
