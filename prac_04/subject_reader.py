"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load records from file and print the nested list."""
    file_data = load_file_data(FILENAME)
    display_subject_details(file_data)

def load_file_data(filename=FILENAME):
    """Return  records as a nested list: [['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]"""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            code, lecturer, students = line.strip().split(',')
            subjects.append([code, lecturer, int(students)])
    return subjects

def display_subject_details(file_data):
    """Display each subject in the format: CP1401 is taught by Ada Lovelace and has 192 students."""
    for code, lecturer, students in file_data:
        print(f"{code} is taught by {lecturer} and has {students} students")


main()