"""
CP1404/CP5632 - Practical
SilverServiceTaxi class
"""

from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """Represent specialised Taxi with fanciness and flagfall."""
    flagfall = 4.50

    def __init__(self, name, fuel, fanciness):
        """Initialise a SilverServiceTaxi instance. with fanciness, float to scale price per km."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        # Scale the base class price_per_km for this instance
        self.price_per_km = Taxi.price_per_km * fanciness

    def __str__(self):
        """Return a string representation with price per km and flagfall"""
        return (f"{super().__str__()}, "
                f"${self.price_per_km:.2f}/km plus flagfall of ${self.flagfall:.2f}")

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        fare = super().get_fare() + self.flagfall
        return round(fare, 2)
