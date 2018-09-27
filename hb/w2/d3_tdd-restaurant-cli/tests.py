import unittest
import unittest.mock
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


class HandleRestaurantRating(unittest.TestCase):
    """Create, add, remove, sort, etc. with list of rr objects"""
    # @unittest.mock.patch('ratings.RestaurantRatings')
    # def setUp(self, mock_list):

    def setUp(self):
        first=r.RestaurantRating("Florean Fortescue's Ice Cream Parlour", 4)
        second=r.RestaurantRating("Jellied Eel Shop", 3)
        self.rrlist = r.RestaurantRatings([first, second])

        # r.RestaurantRatings = mock_list()
        # r.RestaurantRatings.ratings.return_value = [first, second]
        # print(r.RestaurantRatings.ratings().name)
        # print(len(r.RestaurantRatings.ratings()))
        # print("\n\n")
        # import pdb; pdb.set_trace()

        # with open('ratings.txt') as f:
        # for line in f:
            # name, rating = line.strip().split(':')
            # ratings.append(r.RestaurantRating(name, int(rating)))
        # self.rrlist = r.RestaurantRatings.ratings
        # print(self.rrlist)

    def test_rrlist_init(self):
        name = self.rrlist.ratings[0].name
        rating = self.rrlist.ratings[0].rating
        first_rating = (name, rating)
        self.assertEqual(first_rating, 
                    ("Florean Fortescue's Ice Cream Parlour", 4))

    def test_rrlist_add_rating_len(self):
        curr_len = len(self.rrlist.ratings)
        new_name, new_rating = 'Kimberly', 10
        self.rrlist.add_rating(new_name, new_rating)
        new_len = len(self.rrlist.ratings)
        self.assertTrue(new_len == curr_len + 1)

    def test_rrlist_add_rating_name_rating(self):
        curr_len = len(self.rrlist.ratings)
        new_name, new_rating = 'Kimberly', 10
        self.rrlist.add_rating(new_name, new_rating)
        latest_obj = self.rrlist.ratings[curr_len]
        name, rating = latest_obj.name, latest_obj.rating
        self.assertTrue((name, rating) == (new_name, new_rating))

    def test_rrlist_remove_rating_by_index(self):
        old_len = len(self.rrlist.ratings)
        old_first = self.rrlist.ratings[0]
        old_second = self.rrlist.ratings[1]
        self.rrlist.remove_rating_by_index(0)
        new_len = len(self.rrlist.ratings)
        new_first = self.rrlist.ratings[0]
        condition1 = new_len == old_len - 1
        condition2 = new_first != old_first
        condition3 = new_first == old_second
        self.assertTrue(condition1 and condition2 and condition3)

    # def test_rrlist_get_random_rating(self):
    #     pass

    # def test_rrlist_get_rating_by_name(self):
    #     pass


if __name__ == '__main__':
    unittest.main()
