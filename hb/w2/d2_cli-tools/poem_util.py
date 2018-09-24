import sys

HELP_TEXT = """Name:\n
    poem utility - returns upto 3 haikus

Usage:\n
    python3 poem_utility.py [-n num]

Options and arguments:\n
    -n num : number flag and number of poems to provide
"""

HELP_TEXT_SHORT = "Usage: python3 poem_utility.py [-n num]"

ERROR_MSG = """poem_util.py: illegal option"""

POEMS = [
"""An old silent pond...
A frog jumps into the pond,
splash! Silence again.""",

"""Autumn moonlight—
a worm digs silently
into the chestnut. """,

"""In the twilight rain
these brilliant-hued hibiscus —
A lovely sunset. """ ]

# print(sys.argv[0]) #poem_util.py
# print(sys.argv[1]) #-n
# print(sys.argv[2]) #3
# print(sys.argv) # ['poem_util.py', '-n', '0']


def process_arguments(argv):

    if len(sys.argv) == 1:
        print("Please provide flag and argument")
        print(HELP_TEXT_SHORT)
        sys.exit(1)

    elif sys.argv[1] == '-n':
        try:
            n = int(sys.argv[2])
            if n > 3:
                print("\nWe only have 3 poems.")
            return n
        except:
            print("Please provide an integer upto 3")
            print(HELP_TEXT_SHORT)
            sys.exit(1)

    elif sys.argv[1] == '-h':
        print(HELP_TEXT)
        sys.exit(0)

    else:
        print(ERROR_MSG)
        print(HELP_TEXT_SHORT)
        sys.exit(1)


def display_poems(poems):

    for poem in poems:
        print(f"\n{poem}")

    print("\n")


if __name__ == "__main__":

    n = process_arguments(sys.argv)

    display_poems(POEMS[:n])
