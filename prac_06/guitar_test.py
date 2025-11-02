"""
CP1404 prac
Tests for Guitar.get_age() and Guitar.is_vintage()
Guitar class to store name, year and cost, age/vintage

Estimated time: 35 minutes
Actual time: idk
"""

from prac_06.guitar import Guitar, CURRENT_YEAR


def main():
    """Test get_age() and is_vintage() with sample guitars."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 0)

    expected_gibson_age = CURRENT_YEAR - 1922  # 100 for CURRENT_YEAR = 2022
    expected_another_age = CURRENT_YEAR - 2013  # 9 for CURRENT_YEAR = 2022

    print(f"{gibson.name} get_age() - Expected {expected_gibson_age}. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected {expected_another_age}. Got {another.get_age()}")

    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")


main()
