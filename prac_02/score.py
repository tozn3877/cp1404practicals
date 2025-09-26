"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

def main():
    """Get a score from user and display result, then show a random score result."""
    score = float(input("Enter score: "))
    calculate_score_result(score)
    print(calculate_score_result(score))

    random_score = random.randint(0, 100)
    print(f"Ramdom score: {calculate_score_result(random_score)}")

def calculate_score_result(score: float):
    """Determine the status string for a given score."""
    if score < 0 or score > 100:
        return("Invalid score")
    elif score >= 90:
        return("Excellent")
    elif score >= 50:
        return("Passable")
    else:
        return("Bad")


main()