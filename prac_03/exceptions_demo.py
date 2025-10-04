"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    when you enter something that isn't a number, such as a letter
2. When will a ZeroDivisionError occur?
    when you enter a 0 to try devide by 0
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    yes by checking if the user entered a 0 and if so ask again for new denominator.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero.")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")
