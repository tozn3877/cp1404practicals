"""
CP1404/CP5632 - Practical
Test Unreliable Car class
"""

from unreliable_car import UnreliableCar


def main():
    """Test UnreliableCar behaviour."""
    unreliable_car = UnreliableCar("Unreliable Car", 100, 30)

    print("Testing UnreliableCar:")
    for attempt in range(1, 11):
        distance = unreliable_car.drive(10)
        print(f"Attempt {attempt}: {unreliable_car.name} drove {distance}km, "
              f"fuel = {unreliable_car.fuel}")


if __name__ == "__main__":
    main()
