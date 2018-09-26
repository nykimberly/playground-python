from random import choice
from os import path

class RestaurantRating:
    """A rating about one restaurant"""

    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    def update_rating(self, new_rating):
        self.rating = new_rating

    def __eq__(self, other):
        return self.rating == other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __repr__(self):
        return f"<{self.__class__.__name__}: name={self.name}, rating={self.rating}>"


class RestaurantRatings:
    """A list of ratings"""

    def __init__(self, ratings=None):
        if ratings:
            self.ratings = ratings
        else:
            self.ratings = []

    def add_rating(self, name, rating):
        """Create a new Rating object and append it to the list"""

        self.ratings.append(RestaurantRating(name, rating))

    def remove_rating_by_index(self, rating_idx):
        """Remove a rating from the list by index"""

        del self.ratings[rating_idx]

    def remove_rating_by_name(self, restaurant_name):
        """Remove a rating from the list by its name"""

        for idx, rating in enumerate(self.ratings):
            if rating.name == restaurant_name:
                self.remove_rating_by_index(idx)
                return

        raise NoSuchRestaurantError(f"No rating for restaurant {restaurant_name}")
        

    def get_random_rating(self):
        """Return a random rating from the list"""

        return choice(self.ratings)

    def get_rating_by_name(self, restaurant_name):
        """Return a rating based on a given name"""

        for rating in self.ratings:
            if rating.name == restaurant_name:
                return rating

        raise NoSuchRestaurantError(f"No rating for restaurant {restaurant_name}")
        
    @classmethod
    def get_ratings_from_file(cls, filename):
        """Return a RestaurantRatings object containing raitings from file"""

        ratings = []
        with open(filename) as f:
            for line in f:
                name, rating = line.strip().split(':')
                ratings.append(RestaurantRating(name, int(rating)))
            
        return cls(ratings)

    def save_to_file(self, filename, overwrite=False):
        """Save existing ratings to a file, overwriing if specified"""

        # Check if file exists:
        if path.exists(filename) and overwrite is False:
            raise RatingsFileExistsError

        with open(filename, 'w') as f:
            for rating in self.ratings:
                print(rating.name, rating.rating, file=f, sep=':')

    def __repr__(self):
        return f"<{self.__class__.__name__}: num_ratings={len(self.ratings)}>"


class RatingsFileExistsError(FileExistsError):
    """Error when trying to overwrite file"""

class NoSuchRestaurantError(LookupError):
    """Error when the restaurant being searched for does not exist"""
