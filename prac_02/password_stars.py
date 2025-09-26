"""
CP1404/CP5632 - Practical
Password checker program: ask user for a password, enforce minimum length,
then display asterisks as long as the password.
"""

MIN_PASSWORD_LENGTH = 8


def main():
    """Get a valid password and print asterisks as long as the password."""
    password = input("Enter password: ")
    while len(password) < MIN_PASSWORD_LENGTH:
        print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
        password = input("Enter password: ")
    print('*' * len(password))


main()
