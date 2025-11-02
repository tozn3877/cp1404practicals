"""
CP1404 Practical
class for programming language

Estimated time: 10 minutes
Actual time: 8
"""


class ProgrammingLanguage:
    """Represent a programming language with typing, reflection and first-appeared year."""

    def __init__(self, name, typing, reflection, year):
        """Initialise a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the language uses dynamic typing, False otherwise."""
        return self.typing.lower() == "dynamic"

    def __str__(self):
        """Return a nicely formatted string for the language."""
        return (f"{self.name}, {self.typing} Typing, "
                f"Reflection={self.reflection}, First appeared in {self.year}")
