"""
Lab 6.2 - Part 2: Using the Custom Module and Standard Modules
main_program.py
"""

import my_utils
import math
import random

print("--- Using my_utils module ---")
my_utils.greet("Alice")

test_numbers = [7, 10, 13, 15, 1, 2]
for n in test_numbers:
    print(f"Is {n} prime? {my_utils.is_prime(n)}")

print("\n--- Using math module ---")
number = 49
print(f"Square root of {number}: {math.sqrt(number)}")

print("\n--- Using random module ---")
random_num = random.randint(1, 100)
print(f"Random number between 1 and 100: {random_num}")