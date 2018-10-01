from homemadedict import HomeMadeDict, NoAvailableBucketError, ThatsTooBadError
from unittest import TestCase
from unittest.mock import patch, call

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
        self.assertTrue('a' in self.hmd)

    def test_contains_non_existing(self):
        self.assertFalse('z' in self.hmd)

    def test_del_existing(self):
        self.assertTrue('e' in self.hmd)
        del self.hmd["e"]
        self.assertFalse('e' in self.hmd)
        
    def test_del_non_existing(self):
        self.assertTrue('z' not in self.hmd)
        with self.assertRaises(KeyError):
            del self.hmd['z'] 
        
    def test_equality(self):
        d1 = HomeMadeDict()
        d1["abc"] = "abc"
        d1[2] = "two"
        d1["banana"] = 2
    
        d2 = HomeMadeDict()
        d2[2] = "two"
        d2["banana"] = 2
        d2["abc"] = "abc"

        self.assertEqual(d1, d2)
    
        d3 = HomeMadeDict()
        d3[2] = "two"
        d3["potato"] = 2
        d3["abc"] = "abc"

        self.assertNotEqual(d1, d3)
    
        d4 = HomeMadeDict()
        d4["abc"] = "cba"
        d4[2] = "two"
        d4["banana"] = 2

        self.assertNotEqual(d1, d4)
    
        d5 = HomeMadeDict()
        d5["abc"] = "cba"
        d5[2] = "two"
        d5["banana"] = 2

        self.assertNotEqual(d1, d5)
    
        d6 = HomeMadeDict()
        d6["abc"] = "abc"
        d6[2] = "two"

        self.assertNotEqual(d1, d6)

    def test_get_existing(self):
        self.assertEqual(self.hmd.get("f"), "fig")

    def test_get_nonexisting_no_default(self):
        self.assertEqual(self.hmd.get("z"), None)

    def test_get_nonexisting_with_default(self):
        self.assertEqual(self.hmd.get("z", "somedefault"), "somedefault")

    def test_items(self):
        self.assertEqual(sorted(self.hmd.items()), [("a", "apple"), ("b", "berry"), ("c", "cherry"), ("d", "durian"), ("e", "elderberry"), ('f', 'fig')])

    def test_self_items_size_initial(self):
        test_dict = HomeMadeDict()
        test_dict["a"] = "apple"
        test_dict["b"] = "berry"
        test_dict["c"] = "cherry"
        test_dict["d"] = "durian"
        test_dict["e"] = "elderberry"

        self.assertEqual(len(test_dict._items), 8)

    def test_self_items_size_after_first_rehash(self):
        test_dict = HomeMadeDict()
        test_dict["a"] = "apple"
        test_dict["b"] = "berry"
        test_dict["c"] = "cherry"
        test_dict["d"] = "durian"
        test_dict["e"] = "elderberry"

        self.assertEqual(len(test_dict._items), 8)
        test_dict["f"] = "fig"
        self.assertEqual(len(test_dict._items), 16)

    def test_iteration(self):
        keys = []
        values = []
        for k in self.hmd:
           keys.append(k)
           values.append(self.hmd[k]) 

        self.assertEqual(sorted(keys), ["a", "b", "c", "d", "e", "f"])
        self.assertEqual(sorted(values), ["apple", "berry", "cherry", "durian", "elderberry", "fig"])

    def test_keys(self):
        self.assertEqual(sorted(self.hmd.keys()), ["a", "b", "c", "d", "e", "f"])

    def test_length(self):
        self.assertEqual(len(self.hmd), 6)

    def test_length_property(self):
        self.assertEqual(self.hmd.length, 6)

    @patch("homemadedict.randint", side_effect=[4, 74, 22, 63])
    def test_random_succeed_fail(self, mocked_randint):
        hmd = HomeMadeDict()
        with self.assertRaises(ThatsTooBadError):
            hmd.random_succeed()
        self.assertEqual(mocked_randint.call_count, 4)
        mocked_randint.has_calls([
            call(1, 100),
            call(1, 100),
            call(1, 100),
            call(1, 100),
        ])

    @patch("homemadedict.randint", side_effect=[75])
    def test_random_succeed_first_try(self, mocked_randint):
        hmd = HomeMadeDict()
        self.assertEqual(hmd.random_succeed(), "Success!")
        mocked_randint.assert_called_once_with(1, 100)

    @patch("homemadedict.randint", side_effect=[4, 74, 80])
    def test_random_succeed_third_try(self, mocked_randint):
        hmd = HomeMadeDict()
        self.assertEqual(hmd.random_succeed(), "Success!")
        self.assertEqual(mocked_randint.call_count, 3)
        mocked_randint.has_calls([
            call(1, 100),
            call(1, 100),
            call(1, 100),
        ])

    @patch("homemadedict.HomeMadeDict._rehash")
    def test_rehashing(self, rehash_mock):
        test_dict = HomeMadeDict()
        
        test_dict["a"] = "apple"
        test_dict["b"] = "berry"
        test_dict["c"] = "cherry"
        test_dict["d"] = "durian"
        test_dict["e"] = "elderberry"
        rehash_mock.assert_not_called()
        test_dict["f"] = "fig"
        rehash_mock.assert_called_once()
        test_dict["g"] = "grape"
        test_dict["h"] = "honeydew"
        with self.assertRaises(NoAvailableBucketError):
            test_dict["i"] = "indian prune"


    def test_repr(self):
        self.assertEqual(
            self.hmd.__repr__(),
            "{'a': 'apple', 'b': 'berry', 'c': 'cherry', 'd': 'durian', 'e':"\
            " 'elderberry', 'f': 'fig'}"
        )

    def test_subscripting(self):
        self.assertEqual(self.hmd["a"], "apple")
        self.assertEqual(self.hmd["b"], "berry")
        self.assertEqual(self.hmd["c"], "cherry")
        self.assertEqual(self.hmd["d"], "durian")
        self.assertEqual(self.hmd["e"], "elderberry")
        self.assertEqual(self.hmd["f"], "fig")

    def test_subscripting_non_existent(self):
        with self.assertRaises(KeyError):
            self.assertEqual(self.hmd["z"], "doesn't matter, shoukd raise")

    def test_updating_key(self):
        self.assertEqual(self.hmd["b"], "berry")
        self.hmd["b"] = "banana"
        self.assertEqual(self.hmd["b"], "banana")

    def test_values(self):
        self.assertEqual(sorted(self.hmd.values()), ["apple", "berry", "cherry", "durian", "elderberry", "fig"])


if __name__ == "__main__":
    from unittest import main
    main()

