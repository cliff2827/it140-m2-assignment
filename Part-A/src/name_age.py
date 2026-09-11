
# A simple program that asks the user for their name and age,
# then calculates and displays the year they were born.

"""
Input:
    name (str): The user's name.
    age (int): The user's current age.

Process:
    Subtract the user's age from the current year to determine birth year.

Output:
    A formatted message greeting the user and stating their birth year.

Typical usage example:
    What is your name? Bob
    How old are you? 24
    Hello Bob! You were born in 2001.

"""

# === Imports ===
from datetime import date

# === Constants ===
CURRENT_YEAR = date.today().year  # Get current year from system

# === Main Function ===
def main() -> None:
    """Run the name-age program."""

    # Get user input
    user_name = input("What is your name? ")
    user_age = int(input("How old are you? "))

    # Calculate birth year
    birth_year = CURRENT_YEAR - user_age

    # Display result
    print(f"\nHello {user_name}! You were born in {birth_year}.")


# === Dunder Check ===
if __name__ == "__main__":
    main()
