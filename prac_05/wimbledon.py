"""
CP1404/CP5632 - Practical
Wimbledon
Estimate: 45 minutes
Actual:    minutes
"""

import csv


def main():
    """Load Wimbledon records from the CSV file."""
    filename = "wimbledon.csv"
    records = load_wimbledon_data(filename)
    print(f"Loaded {len(records)} records")


def load_wimbledon_data(filename):
    """Return a list of (year, champion, country) from the CSV."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skips the header to get right to the data
        for year, champ_country, champion, runner_country, runner_up, score in reader:
            records.append((int(year), champion, champ_country))
    return records


main()
