"""
CP1404/CP5632 - Practical
Test SilverServiceTaxi class
"""

from silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi fare calculation."""
    taxi = SilverServiceTaxi("Fancy Taxi", 100, 2)
    taxi.drive(18)
    fare = taxi.get_fare()

    print(taxi)
    print(f"Fare for 18 km trip: ${fare:.2f}")

    #checking to confirm code functions correctly here
    assert fare == 48.78, f"Expected fare 48.78, got {fare}"


if __name__ == "__main__":
    main()
