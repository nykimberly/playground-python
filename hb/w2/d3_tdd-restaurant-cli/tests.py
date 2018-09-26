import unittest
import ratings as r

class HandleOneRestaurantRating(unittest.TestCase):
    """Create, update, and compare restaurant rating objects"""
    def setUp(self):
        self.restaurant = 'El Gordo'
        self.rating = 10
        self.rr_tuple = (self.restaurant, self.rating)
        self.rr_obj = r.RestaurantRating(self.restaurant, self.rating)
        self.rr_obj_tuple = (self.rr_obj.name, self.rr_obj.rating)

    def test_rating_init(self):
        # Check that object is created and initialized properly
        self.assertEqual(self.rr_tuple, self.rr_obj_tuple)

    def test_rating_update(self):
        # Check that object updates as expected
        updated_rating = 5
        self.rr_obj.update_rating(updated_rating)
        self.assertEqual(5, self.rr_obj.rating)

    def test_rating_comparison_by_rating_eq(self):
        # Check that we can compare by rating
        other = r.RestaurantRating('Other', 10)
        self.assertEqual(other, self.rr_obj)

    def test_rating_comparison_by_rating_lt(self):
        other = r.RestaurantRating('Other', 9)
        self.assertTrue(other < self.rr_obj)


class HandleListRestaurantRating(unittest.TestCase):
    """Create, add, remove, sort, etc. with list of rr objects"""
    def setUp(self):
        pass

    def test_rrlist_init(self):
        pass

    def test_rrlist_add_rating(self):
        pass

    def test_rrlist_remove_rating_by_index(self):
        pass

    def test_rrlist_remove_rating_by_index(self):
        pass

    def test_rrlist_remove_rating_by_index(self):
        pass

    def test_rrlist_get_random_rating(self):
        pass

    def test_rrlist_get_rating_by_name(self):
        pass


if __name__ == '__main__':
    unittest.main()
