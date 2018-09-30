from unittest import TestCase, mock
import restaurantcli as rcli
import restaurantratings as rr


class CLITestCase(TestCase):
    """Tests for our Restaurant CLI"""

    def setUp(self):
        self.ratings = rr.RestaurantRatings([
            rr.RestaurantRating("The Tavern", 10),
            rr.RestaurantRating("Gastropub", 7)
        ])

    def test_get_ratings(self):
        # Create mock method that returns ratings attr

        def mock_get_ratings_from_file(filename):
            return self.ratings

        with mock.patch(
                "restaurantratings.RestaurantRatings.get_ratings_from_file",
                mock_get_ratings_from_file) as m:

            ratings = rr.RestaurantRatings.get_ratings_from_file("mockfile")

        self.assertEqual(len(ratings.ratings), 2)
        self.assertEqual(ratings.ratings[0].name, "The Tavern")
        self.assertEqual(ratings.ratings[0].rating, 10)
        self.assertEqual(ratings.ratings[1].name, "Gastropub")
        self.assertEqual(ratings.ratings[1].rating, 7)


class RestaurantRatingTests(TestCase):
    """Tests for individual restaurant rating objects"""

    def test_init(self):
        rating = rr.RestaurantRating("The Tavern", 10)
        self.assertEqual(rating.name, "The Tavern")
        self.assertEqual(rating.rating, 10)

    def test_update_rating(self):
        rating = rr.RestaurantRating("The Tavern", 10)
        rating.update_rating(2)
        self.assertEqual(rating.rating, 2)

    def test_eq_true(self):
        rating_1 = rr.RestaurantRating("The Tavern", 10)
        rating_2 = rr.RestaurantRating("Gastropub", 10)
        self.assertEqual(rating_1, rating_2)

    def test_eq_false(self):
        rating_1 = rr.RestaurantRating("The Tavern", 10)
        rating_2 = rr.RestaurantRating("Gastropub", 9)
        self.assertNotEqual(rating_1, rating_2)

    def test_lt_true(self):
        rating_1 = rr.RestaurantRating("The Tavern", 9)
        rating_2 = rr.RestaurantRating("Gastropub", 10)
        self.assertLess(rating_1, rating_2)

    def test_lt_false(self):
        rating_1 = rr.RestaurantRating("The Tavern", 10)
        rating_2 = rr.RestaurantRating("Gastropub", 9)
        self.assertFalse(rating_1 < rating_2)


class RestaurantRatingsTests(TestCase):
    """Tests for the RestaurantRatingsTests umbrella objects"""

    def setUp(self):
        """Set up sub-objects for RestaurantRatings tests"""
        self.rrobj = rr.RestaurantRatings([
            rr.RestaurantRating("The Tavern", 10),
            rr.RestaurantRating("Gastropub", 9),
            rr.RestaurantRating("Snack Shack", 5)
        ])

    def test_init(self):
        rrobj = rr.RestaurantRatings()
        self.assertEqual(len(rrobj.ratings), 0)
        self.assertEqual(rrobj.ratings, [])

    def test_init_with_source(self):
        rrobj = rr.RestaurantRatings([rr.RestaurantRating("The Tavern", 10)])
        self.assertEqual(len(rrobj.ratings), 1)
        self.assertEqual(rrobj.ratings[0].name, "The Tavern")
        self.assertEqual(rrobj.ratings[0].rating, 10)

    def test_add_rating(self):
        self.rrobj.add_rating("Kimberly's", 5)
        self.assertEqual(len(self.rrobj.ratings), 4)
        self.assertEqual(self.rrobj.ratings[3].name, "Kimberly's")
        self.assertEqual(self.rrobj.ratings[3].rating, 5)

    def test_get_rating_by_name(self):
        restaurant_rating = self.rrobj.get_rating_by_name("The Tavern")
        self.assertEqual(restaurant_rating.name, "The Tavern")
        self.assertEqual(restaurant_rating.rating, 10)

    def test_remove_rating_by_name(self):
        self.rrobj.remove_rating_by_name("The Tavern")
        self.assertEqual(len(self.rrobj.ratings), 2)
        self.assertEqual(self.rrobj.ratings[0].name, "Gastropub")
        self.assertEqual(self.rrobj.ratings[1].name, "Snack Shack")

    def test_remove_rating_by_index(self):
        self.rrobj.remove_rating_by_index(1)
        self.assertEqual(len(self.rrobj.ratings), 2)
        self.assertEqual(self.rrobj.ratings[1].name, "Snack Shack")
        self.assertEqual(self.rrobj.ratings[1].rating, 5)

    def get_rating_by_name_error(self):
        with self.assertRaises(NoSuchRestaurantError):
            self.rrobj.get_rating_by_name("Not a Restaurant")


if __name__ == "__main__":

    import unittest

    unittest.main()
