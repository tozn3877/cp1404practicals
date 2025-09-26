"""
CP1404/CP5632 - Practical
Score menu program (basic menu structure only)
"""

MENU = """(G)et a valid score
(P)rint result
(S)how stars
(Q)uit"""


def main():
    """Display menu and process user choice"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "G":
            print("You chose to get a valid score")
        elif choice == "P":
            print("You chose to print result")
        elif choice == "S":
            print("You chose to show stars")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()
    print("Goodbye")




main()
