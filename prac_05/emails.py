"""
CP1404/CP5632 - Practical
Emails
Estimate: 15 minutes
Actual:   25 minutes
"""


def get_name_from_email(email):
    """Return capitalised name guessed from given email address."""
    username = email.split("@")[0]
    username = username.replace(".", " ")
    return " ".join(word.capitalize() for word in username.split())


def main():
    """Prompt for one email and display name"""
    email = input("Email: ")
    name = get_name_from_email(email)
    print(name)


main()
