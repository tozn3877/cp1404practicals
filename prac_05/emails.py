"""
CP1404/CP5632 - Practical
Emails
Estimate: 15 minutes
Actual:   47 minutes
"""


def get_name_from_email(email):
    """Return capitalised name from given email address."""
    username = email.split("@")[0]
    username = username.replace(".", " ")
    return " ".join(word.capitalize() for word in username.split())


def main():
    """Prompt for emails until blank; confirm/correct names; then display all."""
    emails_to_names = {}
    email = input("Email: ").strip()
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").strip().lower()
        if confirmation not in ("", "y"):
            name = input("Name: ").strip()
        emails_to_names[email] = name
        email = input("Email: ").strip()

    for email, name in emails_to_names.items():
           print(f"{name} ({email})")
main()
