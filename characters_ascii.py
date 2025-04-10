#!/usr/bin/env python3
# Created by: Reid MacLean
# Created on: March 2025
# This program checks if a character is uppercase, lowercase, or not a letter
# Function to check if the character is uppercase, lowercase, or not a letter
def check_case(user_character):
    try:
        # Check if the input is a single character
        if len(user_character) != 1:
            print("Error: Invalid input.")  # Invalid if it's not a single character
        else:
            # Get the ASCII value of the character
            ascii_value = ord(user_character)

            # Check if the character is uppercase
            if 65 <= ascii_value <= 90:
                print(f"{user_character} is an uppercase letter.")
            # Check if the character is lowercase
            elif 97 <= ascii_value <= 122:
                print(f"{user_character} is a lowercase letter.")
            else:
                # If the character is neither uppercase nor lowercase
                print(f"{user_character} is not a letter.")
    except Exception:
        # If an unexpected error occurs
        print("Error: Invalid input.")


# Main program execution
try:
    # Greeting message
    print("Hello, thank you for using the character guesser.")

    # Get user input (character)
    user_character = input("Enter a character: ")

    # Call the function to check the character
    check_case(user_character)

# Catch any unexpected errors
except Exception:
    print("Error: Invalid input.")
