"""
CP1404 Practical
Client program to use the ProgrammingLanguage class.

Estimated time: 10 minutes
Actual time: 8
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Create provided list of programming languages. Then print python and the list task"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    # Shows that __str__ works
    print(python)

    # Put them in a list
    languages = [python, ruby, visual_basic]

    # Print only the dynamically typed languages using the is_dynamic method
    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)


main()
