"""
CP1404/CP5632 - Practical
Read and display guitars, then sort by year and display again
"""

from guitar import Guitar


def main():
    """Load guitars from CSV, display them, sort by year, then display again."""
    filename = "guitars.csv"
    guitars = load_guitars(filename)

    print("These are my guitars:")
    display_guitars(guitars)

    guitars.sort()
    print("\nThese are my guitars (sorted by year):")
    display_guitars(guitars)


    print("\nAdd new guitars (blank name to finish):")
    guitars.extend(prompt_new_guitars())

    save_guitars(filename, guitars)



def load_guitars(filename):
    """Load guitars from a CSV file with lines. Name,Year,Cost ."""
    guitars = []
    with open(filename, "r", encoding="utf-8") as in_file:
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            name, year_text, cost_text = line.split(",")
            guitars.append(Guitar(name, int(year_text), float(cost_text)))
    return guitars


def display_guitars(guitars):
    """Display each guitar on its own line"""
    for guitar in guitars:
        print(guitar)



def prompt_new_guitars():
    """Prompt user to enter new guitars then return a list of new guitar objects."""
    new_guitars = []
    name = input("Name: ")
    while name:
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitars.append(Guitar(name, year, cost))
        print(f"{name} ({year}) : ${cost:,.2f} added.\n")
        name = input("Name: ")
    return new_guitars


def save_guitars(filename, guitars):
    """Write all guitars to the CSV as lines Name,Year,Cost"""
    with open(filename, "w", encoding="utf-8") as out_file:
        for guitar in guitars:
            print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)





main()
