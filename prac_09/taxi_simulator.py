"""
CP1404/CP5632 - Practical
Taxi simulator program
"""

from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

MENU = "q)uit"


def main():
    """Start the taxi simulator."""
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        print("Invalid choice")
        print(MENU)
        choice = input(">>> ").lower()
    print("Goodbye")


if __name__ == "__main__":
    main()
