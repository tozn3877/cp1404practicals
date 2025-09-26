"""
Password checker program
Ask user for a password, enforce minimum length, then display asterisks.
"""

MIN_PASSWORD_LENGTH = 8

password = input("Enter password: ")
while len(password) < MIN_PASSWORD_LENGTH:
    print(f"Password must be at least {MIN_PASSWORD_LENGTH} characters long.")
    password = input("Enter password: ")

print('*' * len(password))