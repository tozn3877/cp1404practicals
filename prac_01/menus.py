"""
CP1404/CP5632 - Practical
program that provides the user with a basic menu
"""

# Ask the user for their name
get_name = (input("Enter name: "))
# Show the menu options to the user
print("(H)ello\n(G)oodbye\n(Q)uit")
get_menu_choice = (input(">>>> "))
# Loop until the user chooses to quit
while get_menu_choice != "Q":
    # If user chose "H", greet them, if user chose "G", say goodbye
    if get_menu_choice == "H":
        print(f"Hello {get_name}")
    elif get_menu_choice == "G":
        print(f"Goodbye {get_name}")
    else:
        #Any other input is invalid
        print("Invalid choice")
    #Prints the menu again for next input
    print("(H)ello\n(G)oodbye\n(Q)uit")
    get_menu_choice = (input(">>>> "))
print("Finished")