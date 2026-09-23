"""
Lab 6.1: Simple Calculator Functions
Functions: add, subtract, multiply, divide, power (challenge)
"""


def add(a, b):
    """Return the sum of a and b."""
    return a + b


def subtract(a, b):
    """Return the result of a minus b."""
    return a - b


def multiply(a, b):
    """Return the product of a and b."""
    return a * b


def divide(a, b):
    """Return a divided by b. Returns an error message if b is 0."""
    if b == 0:
        return "Error: Division by zero"
    return a / b


def power(base, exponent=2):
    """Return base raised to exponent. Defaults to squaring the base."""
    return base ** exponent


def main():
    while True:
        print("\n--- Simple Calculator ---")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power (base^exponent, default exponent = 2)")
        print("6. Exit")

        choice = input("Choose an operation (1-6): ")

        if choice == "6":
            print("Goodbye!")
            break

        if choice not in ("1", "2", "3", "4", "5"):
            print("Invalid choice, please try again.")
            continue

        num1 = float(input("Enter the first number: "))

        if choice == "5":
            has_exponent = input("Enter exponent (leave blank for default = 2): ")
            if has_exponent.strip() == "":
                result = power(num1)
            else:
                result = power(num1, float(has_exponent))
            print(f"Result: {result}")
            continue

        num2 = float(input("Enter the second number: "))

        if choice == "1":
            result = add(num1, num2)
        elif choice == "2":
            result = subtract(num1, num2)
        elif choice == "3":
            result = multiply(num1, num2)
        elif choice == "4":
            result = divide(num1, num2)

        print(f"Result: {result}")


if __name__ == "__main__":
    main()