"""
CP1404/CP5632 - Practical
Wimbledon
Estimate: 45 minutes
Actual:  55  minutes
"""

import csv


def main():
    """Load Wimbledon records from the CSV file, count wins and countries, print results."""
    filename = "wimbledon.csv"
    records = load_wimbledon_data(filename)
    champion_to_wins = count_champions(records)
    countries = get_winning_countries(records)
    display_results(champion_to_wins, countries)


def load_wimbledon_data(filename):
    """Return a list of (year, champion, country) from the CSV."""
    records = []
    with open(filename, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)  # skips the header to get right to the data
        for year, champ_country, champion, runner_country, runner_up, score in reader:
            records.append((int(year), champion, champ_country))
    return records


def count_champions(records):
    """Return champion name to number of titles."""
    champion_to_wins = {}
    for _, champion, _ in records:
        wins = champion_to_wins.get(champion, 0)
        champion_to_wins[champion] = wins + 1
    return champion_to_wins



def get_winning_countries(records):
    """Return a set of unique countries that have a champion."""
    countries = set()
    for _, _, country in records:
        countries.add(country)
    return countries


def display_results(champion_to_wins, countries):
    """Print champions with win counts and list the countries that have won."""
    print("Wimbledon Champions:")
    for champion in sorted(champion_to_wins):
        print(f"{champion} {champion_to_wins[champion]}")
    print(f"\nThese {len(countries)} countries have won Wimbledon:")
    print(", ".join(sorted(countries)))


main()
