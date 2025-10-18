"""
CP1404/CP5632 - Practical
Word occurrences
Estimate: 15 minutes
Actual:   27 minutes
"""

def main():
    """Count and display word occurrences from user-entered text."""
    text = input("Text: ")
    word_to_count = {}

    for word in text.split():
        count = word_to_count.get(word, 0)
        word_to_count[word] = count + 1

    longest = max((len(word) for word in word_to_count), default=0)
    for word in sorted(word_to_count):
        print(f"{word:{longest}} : {word_to_count[word]}")

main()