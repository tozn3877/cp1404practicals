"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    """Load records from file and print the nested list."""
    data = load_data(FILENAME)
    print(data)


def load_data(filename=FILENAME):
    """Return  records as a nested list: [['CP1401', 'Ada Lovelace', 192],['CP1404', 'Alan Turing', 98]]"""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            code, lecturer, students = line.strip().split(',')
            subjects.append([code, lecturer, int(students)])
    return subjects

main()
