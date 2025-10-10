"""
CP1404/CP5632 - Practical
list exercises: basic list operations and simple username check
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = get_five_numbers()



def get_five_numbers():
    """Prompt for 5 numbers and return them as a list."""
    numbers = []
    for _ in range(5):
        number = float(input("Number: "))
        numbers.append(number)
    return numbers





main()
