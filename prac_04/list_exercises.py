"""
CP1404/CP5632 - Practical
list exercises: basic list operations and simple username check
"""

usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']


def main():
    numbers = get_five_numbers()
    print_provided_number_info(numbers)



def get_five_numbers():
    """Prompt for 5 numbers and return them as a list."""
    numbers = []
    for _ in range(5):
        number = float(input("Number: "))
        numbers.append(number)
    return numbers

def print_provided_number_info(numbers):
    """Display first, last, smallest, largest and average number"""
    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[-1]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    average = sum(numbers) / len(numbers)
    print(f"The average of the numbers is {average:.1f}")



main()
