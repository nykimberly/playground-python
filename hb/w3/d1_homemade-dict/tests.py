from homemadedict import HomeMadeDict, NoAvailableBucketError
from unittest import TestCase
from unittest.mock import patch

class HomeMadeDictTestCase(TestCase):

    def setUp(self):
        self.hmd = HomeMadeDict()
        self.hmd["a"] = "apple"
        self.hmd["b"] = "berry"
        self.hmd["c"] = "cherry"
        self.hmd["d"] = "durian"
        self.hmd["e"] = "elderberry"
        self.hmd["f"] = "fig"

    def test_contains_existing(self):
		pass

    def test_contains_non_existing(self):
        pass

    def test_del_existing(self):
        pass
        
    def test_del_non_existing(self):
        pass
        
    def test_equality(self):
        pass

    def test_get_existing(self):
        pass

    def test_get_nonexisting_no_default(self):
        pass

    def test_get_nonexisting_with_default(self):
        pass

    def test_items(self):
        pass

    def test_iteration(self):
        pass

    def test_keys(self):
        pass

    def test_length(self):
        pass

    def test_length_property(self):
        pass

    def test_repr(self):
        pass

    def test_subscripting(self):
        pass

    def test_subscripting_non_existent(self):
        pass

    def test_updating_key(self):
        pass

    def test_values(self):
        pass


if __name__ == "__main__":
    from unittest import main
    main()

