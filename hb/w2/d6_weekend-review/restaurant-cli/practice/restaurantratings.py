import os

class RestaurantRating:
    """A single restaurant object containing name and rating"""

    # initialize object with name and rating
    def __init__(self, name, rating):
        self.name = name
        self.rating = rating

    # compare based on rating attr of our object
    def __eq__(self, other):
        return self.rating == other.rating

    def __lt__(self, other):
        return self.rating < other.rating

    def __gt__(self, other):
        return self.rating > other.rating

    # print class info
    def __repr__(self):
        return f"<{self.__class__.__name__}: name={self.name},
        rating={self.rating}>"


class RestaurantRatings:
    """Umbrella object containing list of restaurant objects"""

    # if no ratings list provided, set ratings attr to empty list
    def __init__(self, ratings=None):
        if ratings:
            self.ratings = ratings
        else:
            self.ratings = []

    def add_rating(self, name, rating):
        """Create new restaurant rating object and append to our list"""
        self.ratings.append(RestaurantRating(name, rating))

    def remove_rating_by_index(self, index):
        """Remove rating from list by index"""
        del self.ratings(index)

    def remove_rating_by_name(self, restaurant_name):
        """Look up rating obj by name and remove it"""
        for i, rating in enumerate(self, ratings):
            if rating.name == restaurant_name:
                self.remove_rating_by_index(i)
                # exit program once found
                return
        # if program hasn't exited, presume item not found
        raise NoSuchRestaurantError(f"No rating for {restaurant_name}")

    def get_rating_by_name(self, restaurant_name):
        """Return a rating based on a given name"""
        for rating in self.ratings:
            if rating.name == restaurant_name:
                return rating
        # if program hasn't exited, presume item not found
        raise NoSuchRestaurantError(f"No rating for {restaurant_name}")

    @classmethod
    def get_ratings_from_file(cls, filename):
        """Return RestaurantRatings object from ratings in file"""
        ratings = []
        with open(filename) as f:
            for line in f:
                name, rating = line.strip().split(":")
                ratings.append(RestaurantRating(name, int(rating)))
        return cls(ratings)

    def save_to_file(self, filename, overwrite=False):
        """Save existing ratings to a file, overwriting if specified"""
        # check if file exists:
        if os.path.exists(filename) and overwrite is False:
            raise RatingsFileExistsError(f"{filename} exists! Set overwrite to
            overwrite")
        with open(filename, "w") as f:
            for rating in self.ratings:
                print(rating.name, rating.rating, file=f, sep=":")

class RatingsFileExistsError(FileExistsError):
    """Error when trying to overwrite file"""

class NoSuchRatingsFileError(LookupError):
    """Error when trying to look up ratings file"""

class NoSuchRestaurantError(LookupError):
    """Error when the restaurant being searched for does not exist"""
