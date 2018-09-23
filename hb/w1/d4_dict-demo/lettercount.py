"""Count letters in phrase.

    >>> counts = get_letter_counts('delicious knishes')
    >>> print(get_count_for_letter(counts, 's'))
    3
"""


def get_letter_counts(phrase):
    """Count letter occurrences. Return dict of {ltr:count}."""

    letter_counts = {}

    for letter in phrase:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1

    return letter_counts


def get_count_for_letter(letter_counts, letter):
    """Get count for a letter (0 if none)."""

    return letter_counts.get(letter, 0)


counts = get_letter_counts('delicious knishes')
print(get_count_for_letter(counts, 's'))
