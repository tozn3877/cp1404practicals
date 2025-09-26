"""
CP1404/CP5632 - Practical
loops program to show different loop uses
"""
# Print odd numbers from 1 to 20
for i in range(1, 21, 2):
    print(i, end=' ')
print()

# Print multiples of 10 from 0 to 100
for i in range(0, 110, 10):
    print(i, end=' ')
print()

# Print numbers from 20 down to 1
for i in range(20, 0, -1):
    print(i, end=' ')
print()

# Ask user how many stars to display (all on one line, separated by spaces)
number_of_stars = int(input("Enter number of stars: "))
for i in range(number_of_stars):
    print("*", end=' ')
print()

# Ask user how many lines of stars to display in increasing pattern
number_of_lines = int(input("Enter number of lines: "))
for i in range(1, number_of_lines +1):
    print("*" * i)