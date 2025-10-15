"""
CP1404/CP5632 - Practical
Hex colours lookup
"""

HEX_COLOURS = {
    "absolute zero": "#0048ba",
    "acid green": "#b0bf1a",
    "aliceblue": "#f0f8ff",
    "alizarin crimson": "#e32636",
    "amaranth": "#e52b50",
    "amber": "#ffbf00",
    "amethyst": "#9966cc",
    "antiquewhite": "#faebd7",
    "antiquewhite1": "#ffefdb",
    "antiquewhite2": "#eedfcc",
}

colour_name = input("Enter colour name: ").strip().lower()
while colour_name != "":
    try:
        print(f"{colour_name} is {HEX_COLOURS[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").strip().lower()