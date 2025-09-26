"""
Program to calculate and display a user's bonus based on sales.
If sales are under $1,000, the user gets a 10% bonus.
If sales are $1,000 or over, the bonus is 15%.
"""
# Ask user for initial sales value
get_sales = float(input("Enter sales: $"))
# Continue looping while sales is non-negative
while get_sales >= 0:
    if get_sales >= 1000:
        # Apply 15% bonus if sales are $1000 or more
        get_sales = get_sales * 0.15
    else:
        # Apply 10% bonus if sales are under $1000
        get_sales = get_sales * 0.10
    # Display calculated bonus
    print(f"Bonus: {get_sales:.2f} ")
    # Ask for sales again (loop continues if >= 0)
    get_sales = float(input("Enter sales: $"))
# End program when negative input entered
print("Program exited due to negative input")