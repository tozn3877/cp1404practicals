"""
CP1404/CP5632 - Practical
Program for temperature conversion
"""
# Define the menu as a constant string
MENU = """C - Convert Celsius to Fahrenheit
F - Convert Fahrenheit to Celsius
Q - Quit"""
# Display the menu to the user
print(MENU)
# Get the user's first choice and convert to uppercase
get_choice = input(">>> ").upper()
# Loop until the user chooses to quit
while get_choice != "Q":
    if get_choice == "C":
        # Convert Celsius to Fahrenheit
        celsius = float(input("Celsius: "))
        fahrenheit = celsius * 9.0 / 5 + 32
        print(f"Result: {fahrenheit:.2f} F")
    elif get_choice == "F":
        # Convert Fahrenheit to Celsius
        fahrenheit = float(input("Fahrenheit: "))
        celsius = 5 / 9 * (fahrenheit - 32)
        print(f"Result: {celsius:.2f} C")
    else:
        # Handle invalid input
        print("Invalid option")
    # Show the menu again and ask for another choice
    print(MENU)
    get_choice = input(">>> ").upper()
# Exit message once loop ends
print("Thank you.")
