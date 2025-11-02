"""
CP1404 prac
Program to collect guitars then display them formatted with vintage tagging.

Estimated time: 35 minutes
Actual time: 52
"""

from prac_06.guitar import Guitar


def main():
    """Prompt for guitars, store them, then display a formatted summary."""
    print("My guitars!")
    guitars = []

    name = input("Name: ")
    while name:
        year = get_positive_int("Year: ")
        cost = get_non_negative_float("Cost: $")
        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")
        name = input("Name: ")

    # Display
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = " (vintage)" if guitar.is_vintage() else ""
            print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


def get_positive_int(prompt):
    """Get a positive integer from the user. used to prevent non valid year entries"""
    value = None
    while value is None:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Number must be > 0")
                value = None
        except ValueError:
            print("Invalid input; enter a valid number")
    return value


def get_non_negative_float(prompt):
    """Get a non-negative float from the user to ensure no negative cost."""
    value = None
    while value is None:
        try:
            value = float(input(prompt))
            if value < 0:
                print("Number must be >= 0")
                value = None
        except ValueError:
            print("Invalid input; enter a valid number")
    return value


main()
