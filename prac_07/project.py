"""
CP1404/CP5632 - Practical
project class to store project details
"""

from datetime import date


class Project:
    """Represent a project with name, start date, priority, cost estimate, completion percentage."""

    def __init__(self, name: str, start_date: date, priority: int, cost_estimate: float, completion: int):
        """Initialise a Project."""
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion = completion

    def __str__(self) -> str:
        """Return a user-friendly string for this project."""
        start = self.start_date.strftime("%d/%m/%Y")
        return (f"{self.name}, start: {start}, priority {self.priority}, "
                f"estimate: ${self.cost_estimate:.2f}, completion: {self.completion}%")

    def is_complete(self) -> bool:
        """Return True if the project is complete (100%)."""
        return self.completion == 100
