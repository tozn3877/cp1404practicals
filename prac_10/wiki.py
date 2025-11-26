"""
CP1404 - Practical
Wikipedia API search program
"""

import wikipedia


def main():
    """Prompt for a page title/search phrase and show Wikipedia details."""
    page_title = input("Enter page title: ")
    while page_title != "":
        handle_search(page_title)
        page_title = input("Enter page title: ")


def handle_search(page_title):
    """Get and display Wikipedia page info for the given title."""
    try:
        # autosuggest=False so we only get exactly what was asked for
        page = wikipedia.page(page_title, auto_suggest=False)
    except wikipedia.DisambiguationError as disambiguation:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(disambiguation.options)
    except wikipedia.PageError:
        print(f'Page id "{page_title}" does not match any pages. Try another id!')
    except wikipedia.WikipediaException as exception:
        # Generic catch-all for other Wikipedia-related errors
        print(f"An error occurred accessing Wikipedia: {exception}")
    else:
        print(page.title)
        # Default summary, it will truncate itself
        print(wikipedia.summary(page.title))
        print(page.url)


if __name__ == "__main__":
    main()
