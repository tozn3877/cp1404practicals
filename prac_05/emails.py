"""
CP1404/CP5632 - Practical
Emails
Estimate: 15 minutes
Actual:    minutes
"""


def get_name_from_email(email):
    """Return capitalised name guessed from given email address."""
    username = email.split("@")[0]
    username = username.replace(".", " ")
    return " ".join(word.capitalize() for word in username.split())


def main():
    """Prompt for one email and display name, ask if right"""
    email = input("Email: ")
    name = get_name_from_email(email)
    confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
    if confirmation not in ("", "y", "yes"):
        name = input("Name: ").strip()
    print(f"{name} ({email})")

main()
