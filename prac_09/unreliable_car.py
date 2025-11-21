"""
CP1404/CP5632 Practical
Unreliable Car class
"""
import random
from prac_09.car import Car

class UnreliableCar(Car):
    """Represent a Car that has a chance to not drive when asked."""

    def __init__(self, name, fuel, reliability):
        """Initialise UnreliableCar instance. reliability is float between 0 and 100"""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Attempt to drive the given distance based on reliability."""
        random_number = random.uniform(0, 100)
        if random_number < self.reliability:
            distance_driven = super().drive(distance)
        else:
            distance_driven = 0
        return distance_driven