"""
Lab 6.2 - Part 1: Custom Module
my_utils.py
"""


def greet(name):
    """Print a greeting message to the given name."""
    print(f"Hello, {name}!")


def is_prime(number):
    """Return True if number is a prime number, False otherwise."""
    if number < 2:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True