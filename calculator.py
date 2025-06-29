import argparse


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


def main():
    """Main function to run the calculator."""
    parser = argparse.ArgumentParser(
        description="A simple calculator.",
        epilog="Example usage: python calculator.py add 5 3",
    )

    parser.add_argument(
        "operation",
        type=str,
        choices=["add", "subtract"],
        help="The operation to perform.",
    )
    parser.add_argument("a", type=float, help="The first number.")
    parser.add_argument("b", type=float, help="The second number.")

    args = parser.parse_args()

    result = None
    if args.operation == "add":
        result = add(args.a, args.b)
    elif args.operation == "subtract":
        result = subtract(args.a, args.b)

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
