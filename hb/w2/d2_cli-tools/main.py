import sys

HELP_TEXT = """usage: restaurantcli.py [-h] [-f RATINGS_FILENAME] [-c CONFIG_FILENAME] [-v] [-r] [-s]
                 action [restaurant_name] [restaurant_rating]

Your Friendly CLI Tool for Restaurant Ratings

positional arguments:
  action                Action to run: add, remove, update, view, viewrandom
  restaurant_name       Name of restaurant to add, update, view or delete.
  restaurant_rating     Rating of restaurant to add

optional arguments:
  -h, --help            show this help message and exit
  -f RATINGS_FILENAME, --ratings-filename RATINGS_FILENAME
                        File containing ratings
  -c CONFIG_FILENAME, --config CONFIG_FILENAME
                        Config file to use
  -v, --verbose         Be increasingly verbose (up to three times).
  -r, --reverse         Sort results in reverse order.
  -s, --sortbyrating    Sort results by rating rather than name."""

HELP_TEXT_SHORT = """usage: restaurantcli.py [-h] [-f RATINGS_FILENAME] [-c CONFIG_FILENAME] [-v] [-r] [-s]
                 action [restaurant_name] [restaurant_rating]"""


def process_arguments(argv):
    if len(sys.argv) == 1:
        # print("Please provide flag and argument")
        print(HELP_TEXT_SHORT)
        sys.exit(1)
    elif sys.argv[1] == '-h':
        print(HELP_TEXT)
        sys.exit(0)
    elif sys.argv[1] == 'T
