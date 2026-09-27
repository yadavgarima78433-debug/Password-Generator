"""
Password Generator
Author: First-Year Student
Course: Python Essentials
Description: A simple command-line program that generates random passwords
based on user-specified length and character preferences.
"""

import random
import string


def get_password_length():
    """
    Prompt the user for password length and validate it.
    Ensures the input is a positive integer of at least 4 characters.
    """
    while True:
        length_input = input("Enter password length: ").strip()

        # Check if the input consists of digits only
        if length_input.isdigit():
            length = int(length_input)

            # Check minimum and maximum boundaries
            if length < 4:
                print("Error: Password length must be at least 4. Please try again.\n")
            elif length > 100:
                print("Error: Password length cannot exceed 100. Please try again.\n")
            else:
                return length
        else:
            print("Error: Invalid input! Please enter a positive whole number.\n")
