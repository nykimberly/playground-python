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


if __name__ == "__main__":

    unittest.main()
