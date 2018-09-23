"""Restaurant rating lister."""

def store_to_dict(filename, separator):

    with open(filename) as f:
        lines = f.readlines()

    restaurant_ratings = {}
    for line in lines:
        restaurant_rating = line.rstrip().split(separator)
        restaurant_ratings[restaurant_rating[0]] = restaurant_rating[1]

    return restaurant_ratings


def add_restaurant_rating(restaurant_ratings):
    restaurant_name = input("Restaurant: ")
    rating = input("Rating: ")
    restaurant_ratings[restaurant_name] = rating

    return restaurant_ratings


def print_sorted(restaurant_ratings):
    restaurant_ratings_sorted_list = sorted(restaurant_ratings, key=lambda s: s.casefold())

    for restaurant in restaurant_ratings_sorted_list:
        rating = restaurant_ratings[restaurant]
        print(restaurant, ":", rating)

    return

restaurant_ratings = store_to_dict('scores.txt', ':')
add_restaurant_rating(restaurant_ratings)
print_sorted(restaurant_ratings)
