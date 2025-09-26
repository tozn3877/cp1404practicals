"""
CP1404/CP5632 - Practical
Score menu program
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Display menu and process user choice"""
    score = get_valid_score()
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is None:
                print("You must get a valid score first")
            else:
                print(f"Result is: {calculate_score_result(score)}")
        elif choice == "S":
            if score is None:
                print("You must get a valid score first")
            else:
                print_stars(score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")


def get_valid_score():
    """Prompt the user for a valid score between 0 and 100"""
    score = float(input("Enter score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score

def print_stars(score):
    """Print stars equal to the integer value of the score."""
    print('*' * int(score))

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
