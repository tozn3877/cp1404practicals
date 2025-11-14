"""
CP1404/CP5632 - Practical
project management program

estimate:1.5h
actual:4.5h
"""

from datetime import datetime
from project import Project

DEFAULT_FILENAME = "projects.txt"
DATE_FORMAT = "%d/%m/%Y"


def main():
    """Load projects from the default file, shows the menu"""
    projects = load_projects(DEFAULT_FILENAME)
    print("Welcome to Pythonic Project Management")
    print(f"Loaded {len(projects)} projects from {DEFAULT_FILENAME}")

    print_menu()
    choice = input(">>> ").strip().lower()
    while choice != "q":
        if choice == "l":
            filename = input("Filename to load from: ").strip()
            projects = load_projects(filename)
            print(f"Loaded {len(projects)} projects from {filename}")
        elif choice == "s":
            filename = input("Filename to save to: ").strip()
            save_projects(filename, projects)
            print(f"Saved {len(projects)} projects to {filename}")
        elif choice == "d":
            display_projects(projects)
        elif choice == "f":
            date_string = prompt_valid_date_string("Show projects that start after date (dd/mm/yyyy): ")
            filter_projects_by_date(projects, date_string)
        elif choice == "a":
            add_new_project(projects)
        elif choice == "u":
            update_project(projects)
        else:
            print("Invalid choice")
        print_menu()
        choice = input(">>> ").strip().lower()

    save_choice = input(f"Would you like to save to {DEFAULT_FILENAME}? ").strip().lower()
    if save_choice in ("y", "yes"):
        save_projects(DEFAULT_FILENAME, projects)
    print("Thank you for using custom-built project management software.")


def print_menu():
    """Display the menu options."""
    print("- (L)oad projects")
    print("- (S)ave projects")
    print("- (D)isplay projects")
    print("- (F)ilter projects by date")
    print("- (A)dd new project")
    print("- (U)pdate project")
    print("- (Q)uit")


def load_projects(filename):
    """Load projects from a tab-delimited file. skip header and return a list of Project objects."""
    projects = []
    try:
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
    except FileNotFoundError:
        print("File not found; loading empty list.")
        projects = []
    return projects


def save_projects(filename, projects):
    """Save projects to a tab-delimited file with header; print a message if saving fails."""
    try:
        with open(filename, "w", encoding="utf-8") as out_file:
            print("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage", file=out_file)
            for p in projects:
                start_text = p.start_date.strftime(DATE_FORMAT)
                print(f"{p.name}\t{start_text}\t{p.priority}\t{p.cost_estimate}\t{p.completion}", file=out_file)
    except OSError:
        print("Could not save file.")


def get_priority(project):
    """Return a project's priority"""
    return project.priority


def display_projects(projects):
    """Display incomplete and completed projects, each sorted by priority."""
    incomplete = [p for p in projects if not p.is_complete()]
    completed = [p for p in projects if p.is_complete()]

    incomplete.sort(key=get_priority)
    completed.sort(key=get_priority)

    print("Incomplete projects:")
    for project in incomplete:
        print(f"  {project}")
    print("Completed projects:")
    for project in completed:
        print(f"  {project}")


def get_start_date(project):
    """Return a project's start date (for sorting without lambdas)."""
    return project.start_date


def filter_projects_by_date(projects, date_string):
    """Display only projects that start after the given date (sorted by date)."""
    filter_date = datetime.strptime(date_string, DATE_FORMAT).date()
    filtered = [p for p in projects if p.start_date > filter_date]
    filtered.sort(key=get_start_date)
    for project in filtered:
        print(project)


def add_new_project(projects):
    """Ask the user for inputs and add a new project to memory (with basic validation)."""
    print("Let's add a new project")
    name = prompt_non_empty("Name: ")
    start_text = prompt_valid_date_string("Start date (dd/mm/yyyy): ")
    priority = prompt_valid_int("Priority: ")
    cost_estimate = prompt_valid_float("Cost estimate: $", minimum=0.0)
    completion = prompt_valid_int_in_range("Percent complete: ", 0, 100)

    start_date = datetime.strptime(start_text, DATE_FORMAT).date()
    projects.append(Project(name, start_date, priority, cost_estimate, completion))


def update_project(projects):
    """Choose a project, then modify completion and/or priority; blank retains existing values."""
    for i, project in enumerate(projects):
        print(f"{i} {project}")
    index = prompt_valid_index("Project choice: ", len(projects))
    project = projects[index]
    print(project)

    new_completion_text = input("New Percentage: ").strip()
    if new_completion_text != "":
        try:
            project.completion = prompt_valid_int_in_range_value(new_completion_text, 0, 100)
        except ValueError:
            print("Invalid percentage; keeping existing value.")

    new_priority_text = input("New Priority: ").strip()
    if new_priority_text != "":
        try:
            project.priority = prompt_valid_int_value(new_priority_text)
        except ValueError:
            print("Invalid priority; keeping existing value.")


def prompt_non_empty(prompt):
    """Prompt for a non-empty string."""
    text = input(prompt).strip()
    while text == "":
        print("Input cannot be blank")
        text = input(prompt).strip()
    return text


def prompt_valid_date_string(prompt):
    """Prompt for a date string in dd/mm/yyyy format."""
    text = input(prompt).strip()
    while not is_valid_date(text):
        print("Invalid date format")
        text = input(prompt).strip()
    return text


def is_valid_date(text):
    """Return True if text matches DATE_FORMAT."""
    try:
        datetime.strptime(text, DATE_FORMAT)
        return True
    except ValueError:
        return False


def prompt_valid_int(prompt):
    """Prompt until a valid int is entered; return the int."""
    while True:
        text = input(prompt).strip()
        try:
            return int(text)
        except ValueError:
            print("Invalid integer")


def prompt_valid_int_value(text):
    """Validate an existing text as int; used in update when user already entered something."""
    try:
        return int(text)
    except ValueError:
        raise


def prompt_valid_int_in_range(prompt, low, high):
    """Prompt until an int in [low, high] is entered; return the int."""
    while True:
        text = input(prompt).strip()
        try:
            value = int(text)
            if low <= value <= high:
                return value
            print(f"Value must be between {low} and {high}")
        except ValueError:
            print("Invalid integer")


def prompt_valid_int_in_range_value(text, low, high):
    """Validate an existing text as int in [low, high]; raise if invalid so caller can keep existing."""
    try:
        value = int(text)
        if low <= value <= high:
            return value
        raise ValueError
    except ValueError:
        raise


def prompt_valid_float(prompt, minimum=0.0):
    """Prompt until a valid float >= minimum is entered; return the float."""
    while True:
        text = input(prompt).strip()
        try:
            value = float(text)
            if value >= minimum:
                return value
            print(f"Value must be >= {minimum}")
        except ValueError:
            print("Invalid number")


def prompt_valid_index(prompt, length):
    """Prompt until a valid index in range is entered; return the index."""
    while True:
        text = input(prompt).strip()
        try:
            index = int(text)
            if 0 <= index < length:
                return index
            print("Invalid project number")
        except ValueError:
            print("Invalid integer")


main()