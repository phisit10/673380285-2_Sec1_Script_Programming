"""
Activity 6.1: Refactoring a Previous Lab Assignment
Refactored from Week 2 - Number Classifier
Repetitive/logical blocks pulled out into functions.
"""


def is_positive_negative_zero(num):
    """Return a message describing whether num is positive, negative, or zero."""
    if num > 0:
        return "your number is positive number "
    elif num < 0:
        return "your number is negative number "
    elif num == 0:
        return "your number is ZERO"
    else:
        return "invalid number"


def is_even_odd(num):
    """Return a message describing whether num is even or odd."""
    evodd = num % 2
    if evodd == 1:
        return "your number is odd number"
    elif evodd == 0:
        return "your number is even number"
    else:
        return ""


def classify_sign_and_parity(num):
    """Return a combined message describing sign (positive/negative/zero) and parity (even/odd)."""
    evodd = num % 2

    if num > 0 and evodd == 0:
        return "your number is positive and even umber"
    elif num > 0 and evodd == 1:
        return "your number is positive and odd umber"
    elif num < 0 and evodd == 0:
        return "your number is negative and even umber"
    elif num < 0 and evodd == 1:
        return "your number is negative and odd umber"
    elif num == 0 and evodd == 0:
        return "your number is zero and even umber"
    else:
        return ""


def main():
    num = float(input("What your number : "))

    print(is_positive_negative_zero(num))
    print(is_even_odd(num))

    print("CHALENGE")
    print(classify_sign_and_parity(num))


if __name__ == "__main__":
    main()