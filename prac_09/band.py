"""
CP1404/CP5632 - Practical
Band class
"""


class Band:
    """Band class to manage a collection of musicians."""

    def __init__(self, name=""):
        """Construct a Band with a name and empty musician collection."""
        self.name = name
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        musician_strings = ", ".join(str(musician) for musician in self.musicians)
        return f"{self.name} ({musician_strings})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing"""
        parts = []
        for musician in self.musicians:
            parts.append(musician.play())
        return "\n".join(parts)
