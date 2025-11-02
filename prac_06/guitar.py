"""
CP1404 prac
Guitar class to store name, year and cost, age/vintage

Estimated time: 35 minutes
Actual time: 52
"""

CURRENT_YEAR = 2022  # used 2022 as the ages in readme are based off this year


class Guitar:
    """Represent a Guitar with a name, year first made, and cost."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance with defaults."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string like: Gibson L-5 CES (1922) : $16,035.40"""
        return f"{self.name} ({self.year}) : ${self.cost:,.2f}"

    def get_age(self):
        """Return how old the guitar is in years using CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the guitar is 50 or more years old, False otherwise."""
        return self.get_age() >= 50
