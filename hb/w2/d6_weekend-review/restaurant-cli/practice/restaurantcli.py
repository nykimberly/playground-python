"""CLI tool for recording restaurant ratings"""
# import modules
import os
import json
import sys
import argparse

# Initialize parser with description
parser = argparse.ArgumentParser(
        description="CLI tool for Restaurant Ratings"
)

# allow user to provide ratings filename
parser.add_argument(
        "-f",
        "--ratings_filename",
        dest="ratings_filename",
        type=str,
        action="store",
        help="file containing ratings"
)

# allow user to alternatively provide a config file that points to ratings
parser.add_argument(
        "-c",
        "--config",
        dest="config_filename",
        type=str,
        action="store",
        help="file containing configuration",
)

# allow user to request verbose output
parser.add_argument(
        "-v",
        "--verbose",
        dest="verbosity",
        action="count",
        help="three verbosity levels of output",
        default=0
)

# allow user to sort by rating
parser.add_argument(
        "-s",
        "--sortbyrating",
        dest="sort_by_rating",
        action="store_true",
        help="sort results by rating rather than name (default)",
        default=False,
)

parser.add_argument(
        "-r",
        "--reversesort",
        dest="reverse_sort",
        action="store_true",
        help="sort results by name in reverse order",
        default=False,
)

parser.add_argument(
        "action",
        action="store",
        type=str,
        help="action to run: view, add remove, update"
)

parser.add_argument(
        "restaurant_name",
        action="store",
        type=int,
        help="name of restaurant",
        default=None,
)

parser.add_argument(
        "restaurant_rating",
        action="store",
        type=int,
        help="rating of restaurant",
        default=None,
)
