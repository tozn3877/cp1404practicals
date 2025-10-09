"""
CP1404/CP5632 Practical
Starter code for cumulative total income program
"""


def main():
    """Display income report for incomes over a given number of months."""
    incomes = []  # store each month's income
    number_of_months = int(input("How many months? ")) # Number of months to calculate

    def print_income_report(incomes: list[any], number_of_months: int):
        # prints the income report
        print("\nIncome Report\n-------------")
        total = 0
        # starts from month 1
        for month in range(1, number_of_months + 1):
            income = incomes[month - 1]
            total += income
            print("Month {:2} - Income: ${:10.2f} Total: ${:10.2f}".format(month, income, total))

    #income loop that collects number of months and income for each one
    for month in range(1, number_of_months + 1):
        income = float(input(f"Enter income for month {month}: "))
        incomes.append(income)

    print_income_report(incomes, number_of_months)

main()
