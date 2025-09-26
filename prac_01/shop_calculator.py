"""
CP1404/CP5632 - Practical
program to calculate shop totals
"""

# Initialise total price to 0
price_of_item = 0
# Ask user how many items they want to calculate
number_of_items = int(input("Number of items to calculate: "))
# Ensure the number of items is positive
while number_of_items <= 0:
    print("Invalid number of items!")
    number_of_items = int(input("Number of items to calculate: "))
# Loop through each item to get its price and accumulate the total
for i in range(1, number_of_items + 1):
    price_of_item = price_of_item + int(input(f"Price of item {i} : "))
    # Apply a 10% discount if the total is $100 or more
if price_of_item >= 100:
    price_of_item = price_of_item * 0.9
    # Display the total cost with 2 decimal places
print(f"Total price for {i} items is ${price_of_item:.2f}")