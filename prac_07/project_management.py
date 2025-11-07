"""
CP1404/CP5632 - Practical
project management program

estimate:1.5h
actual:
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"


def main():
    """Load projects from the default file, shows the menu quit, will add other options later."""
    projects = load_projects(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")
    #add more inputs here
    print("- (Q)uit")
    choice = input(">>> ").strip().lower()
    while choice != "q":
        print("Invalid choice")
        print("- (Q)uit")
        choice = input(">>> ").strip().lower()
    print("Thank you for using custom-built project management software.")


def load_projects(filename):
    """Load projects from a tab-delimited file. skip header and return a list of Project objects."""
    projects = []
    with open(filename, "r", encoding="utf-8") as in_file:
        header = in_file.readline()  # discard header line
        for line in in_file:
            line = line.strip()
            if not line:
                continue
            # File format in txt file:
            # Name    Start Date    Priority    Cost Estimate    Completion Percentage
            name, start_text, priority_text, cost_text, completion_text = line.split("\t")
            start_date = datetime.strptime(start_text, "%d/%m/%Y").date()
            priority = int(priority_text)
            cost_estimate = float(cost_text)
            completion = int(completion_text)
            projects.append(Project(name, start_date, priority, cost_estimate, completion))
    return projects


main()
