"""A CLI tool for recording restaurant ratings. """

import argparse
import os
import json
import sys

from restaurantcli_lib import get_ratings, print_rating, print_sorted_ratings
from ratings import NoSuchRestaurantError

parser = argparse.ArgumentParser(
    description="Your Friendly CLI Tool for Restaurant Ratings"
)
parser.add_argument(
    "-f",
    "--ratings-filename",
    dest="ratings_filename",
    type=str,
    action="store",
    help="File containing ratings",
)
parser.add_argument(
    "-c",
    "--config",
    dest="config_filename",
    type=str,
    action="store",
    help="Config file to use",
    default="config.json",
)
parser.add_argument(
    "-v",
    "--verbose",
    dest="verbose",
    action="count",
    help="Be increasingly verbose (up to three times).",
    default=0,
)
parser.add_argument(
    "-r",
    "--reverse",
    dest="reverse",
    action="store_true",
    help="Sort results in reverse order.",
    default=False,
)
parser.add_argument(
    "-s",
    "--sortbyrating",
    dest="sortbyrating",
    action="store_true",
    help="Sort results by rating rather than name.",
    default=False,
)

parser.add_argument(
    'action',
    action='store',
    type=str,
    help="Action to run: add, remove, update, view, viewrandom",
)
parser.add_argument(
    'restaurant_name',
    action='store',
    nargs="?",
    type=str,
    help="Name of restaurant to add, update, view or delete.",    
    default=None,
)
parser.add_argument(
    'restaurant_rating',
    action='store',
    nargs="?",
    type=int,
    help="Rating of restaurant to add",    
    default=None,
    choices=range(1, 6),
)


def set_ratings_filename(args):
    # Get filename either from cli, environ, or config (in that order):
    if args.ratings_filename:
        if args.verbose:
            print(f"Using ratings file {args.ratings_filename} from CLI.")
    elif "RATINGS_FILE" in os.environ:
        args.ratings_filename = os.environ["RATINGS_FILE"]
        if args.verbose:
            print(f"Using ratings file {args.ratings_filename} from env.")
    else:
        config = json.load(open(args.config_filename))
        args.ratings_filename = config["ratings_file"]
        if args.verbose:
            print(f"Using ratings file {args.ratings_filename} from config.")


if __name__ == "__main__":
    args = parser.parse_args()
    if args.verbose > 2:
        print("Being extra verbose.")
    elif args.verbose > 1:
        print("Be very verbose")
    elif args.verbose:
        print("Be verbose")

    # Set the ratings filename
    set_ratings_filename(args)

    # Figure out which command we're running:
    if args.action in ["add", "update"]:
        if args.restaurant_name is None or args.restaurant_rating is None:
            print(f"Must provide a name and rating when adding or updating.")
            parser.print_usage()
            sys.exit(1)
        try:
            ratings = get_ratings(args.ratings_filename)
        except NoSuchRestaurantError:
            print("No restaurant by that name.")
            sys.exit(2)

        if args.action == 'add':
            ratings.add_rating(args.restaurant_name, args.restaurant_rating)

            if args.verbose:
                print("Adding {}, rated {} to {}.".format(
                    args.restaurant_name, args.restaurant_rating,
                    args.ratings_filename))
        elif args.action == 'update':
            try:
                rating = ratings.get_rating_by_name(args.restaurant_name)
            except NoSuchRestaurantError:
                print(f"No restaurant named {args.restaurant_name}.")
                sys.exit(2)
            rating.update_rating(args.restaurant_rating)

            if args.verbose:
                print("Updating {} to rating {} in {}.".format(
                    args.restaurant_name, args.restaurant_rating,
                    args.ratings_filename))

        ratings.save_to_file(args.ratings_filename, overwrite=True)
        
    elif args.action == "remove":
        if args.restaurant_name is None or args.restaurant_rating is not None:
            print(f"Must provide only a name and no rating when removing.")
            parser.print_usage()
            sys.exit(1)
        ratings = get_ratings(args.ratings_filename)
        try:
            ratings.remove_rating_by_name(args.restaurant_name)
        except NoSuchRestaurantError:
            print(f"No restaurant named {args.restaurant_name}.")
            sys.exit(2)

        if args.verbose:
            print("Removing {} from {}.".format(
                args.restaurant_name, args.ratings_filename))

        ratings.save_to_file(args.ratings_filename, overwrite=True)

    elif args.action == "view":
        ratings = get_ratings(args.ratings_filename)
        if args.restaurant_name is None:
            if args.verbose:
                print(f"Printing ratings from {args.ratings_filename}")
            print_sorted_ratings(ratings, by_rating=args.sortbyrating, reverse=args.reverse)
        elif args.restaurant_rating is None:
            try:
                rating = ratings.get_rating_by_name(args.restaurant_name)
            except NoSuchRestaurantError:
                print(f"No restaurant named {args.restaurant_name}.")
                sys.exit(2)
            if args.verbose:
                print(f"Printing restaurant from {args.ratings_filename}")
            print_rating(rating)
        else:
            print("Cannot specify a rating when viewing a restaurant.")
            parser.print_usage()
            sys.exit(1)

    elif args.action == "viewrandom":
        ratings = get_ratings(args.ratings_filename)
        rating = ratings.get_random_rating()
        if args.verbose:
            print(f"Printing one random rating from {args.ratings_filename}")
        print_rating(rating)

    else:
        print(f"Unknown action: {args.action}")
        parser.print_usage()
        sys.exit(1)

