"""CLI tool for recording restaurant ratings"""
# import modules
import os
import json
import sys
import argparse

import restaurantratings as rr

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
        nargs="?", # one or more
        type=str,
        help="name of restaurant",
        default=None,
)

parser.add_argument(
        "restaurant_rating",
        action="store",
        nargs="?", # one or more
        type=int,
        help="rating of restaurant",
        default=None,
        choices=range(1,6),
)

def set_ratings_filename(args):
    # pull ratings from ratings file, environ var, or config file
    if args.ratings_filename:
        if args.verbosity:
            print(f"---Using ratings file {args.ratings_filename}")
    elif "RATINGS_FILE" in os.environ:
        args.ratings_filename = os.environ["RATINGS_FILE"]
        if args.verbosity:
            print(f"---Using ratings file {args.ratings_filename} from env")
    elif args.config_filename:
        config = json.load(open(args.config_filename))
        args.ratings_filename = config["ratings_file"]
        if args.verbosity:
            print(f"---Using ratings file {args.ratings_filename} from config")
    else:
        print("please provide ratings file to read from and write to!")
        sys.exit(2)

if __name__ == "__main__":

    # parse arguments into args
    args = parser.parse_args()

    # announce verbosity level
    if args.verbosity> 2:
        print("---Being as verbose as possible")
    elif args.verbosity> 1:
        print("---Being very verbose")
    elif args.verbosity:
        print("---Being verbose")

    # set ratings filename
    set_ratings_filename(args)

    # create restaurantratings object from ratings file
    try:
        ratings = rr.RestaurantRatings.get_ratings_from_file(args.ratings_filename)
    except rr.NoSuchRatingsFileError:
        print("no ratings information by that file name")
        sys.exit(2)

    # respond to action commands
    if args.action == "add" or args.action == "update":

        # check if necessary files have been provided to cli
        if args.restaurant_name is None or args.restaurant_rating is None:
            print(f"must provide name and rating")
            parser.print_usage()
            sys.exit(1)

        # if action is add, then add the name and rating to ratings
        if args.action == "add":
            ratings.add_rating(args.restaurant_name, args.restaurant_rating)
            
            if args.verbosity:
                print("---Adding {} with a {} rating to {}".format(
                    args.restaurant_name, args.restaurant_rating,
                    args.rating_filename))

        # if action is update,
        # then look up by name, update ratings obj, and save to file
        if args.action == "update":

            # look up by name
            try:
                rating = ratings.get_rating_by_name(args.restaurant_name)
            except rr.NoSuchRestaurantError:
                print(f"no restaurant named {args.restaurant_name}")
                sys.exit(2)

            # update rating
            rating.update_rating(args.restaurant_rating)
            
            # print actions if verbose
            if args.verbosity:
                print("---Updating {} with a {} rating to {}".format(
                    args.restaurant_name, args.restaurant_rating,
                    args.rating_filename))

            # save to file
            ratings.save_to_file(args.rating_filename, overwrite=True)

    # if action is remove,
    # then look up by name, remove from ratings object and save to file
    elif args.action == "remove":

        # check that a restaurant name to be removed is specified
        if args.restaurant_name is None:
            print("please provide restaurant name to delete")
            parser.print_usage()
            sys.exit(1)

        # check that the restaurant name exists in our ratings obj
        try:
            ratings.remove_rating_by_name(args.restaurant_name)
        except rr.NoSuchRestaurantError:
            print(f"no restaurant named {args.restaurant_name}")
            sys.exit(2)

        # print actions if verbose
        if args.verbosity:
            print("---Removing {} from {}".format(args.restaurant_name,
                args.ratings_filename))

        ratings.save_to_file(args.ratings_filename, overwrite=True)

    # if action is to view, 
    # then walk through ratings object and print each name and rating
    elif args.action == "view":

        # if restaurant name is specified, print rating just for that restaurant
        if args.restaurant_name:
            if args.verbosity:
                print(f"---Looking up {args.restaurant_name}...")
            try:
                rating = ratings.get_rating_by_name(args.restaurant_name)
            except rr.NoSuchRestaurantError:
                print(f"no restaurant named {args.restaurant_name}")
                sys.exit(2)
            print(f"{rating.name} is rated a {rating.rating}")

        # if no restaurant name specified, then print all ratings
        else:
            if args.verbosity:
                print(f"---Printing ratings from {args.ratings_filename}")
            
            if args.sort_by_rating:
                def key_f(x): return x.rating
            else:
                def key_f(x): return x.name

            for rating in sorted(ratings.ratings, key=key_f,
                    reverse=args.reverse_sort):
                print(f"{rating.name} is rated a {rating.rating}.")
