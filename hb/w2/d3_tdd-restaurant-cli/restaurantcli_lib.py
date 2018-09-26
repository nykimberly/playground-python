"""Functions used by the ratings cli"""
from ratings import RestaurantRatings

def get_ratings(filename):
    """Return a RestaurantRatings containing ratings from all the filenames"""

    return RestaurantRatings.get_ratings_from_file(filename)


def print_rating(rating):
    """Print a single restaurant and rating."""

    print(f"{rating.name} is rated at {rating.rating}.")

def print_sorted_ratings(restaurant_ratings, by_rating=False, reverse=False):
    """Print restaurants and ratings, sorted."""

    if by_rating:
        def key_f(x): return x.rating
    else:
        def key_f(x): return x.name

    for rating in sorted(restaurant_ratings.ratings, key=key_f, reverse=reverse):
        print_rating(rating)

