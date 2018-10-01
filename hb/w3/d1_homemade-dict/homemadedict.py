# Notes
## Store key-valye pairs as tuples in a list
## Double size of dictionary every time it gets more than 2/3s its full length
## Start with size 8, then 16, 32, etc.


from copy import copy
import sys

class HomeMadeDict:
    """A homemade implementation of a dictionary."""

    def __init__(self, print_timing=False):
        """Constructor -- ignore print_timing for now"""

    def __contains__(self, key):
        """Used by "key in dictionary", returns True/False"""

    def __delitem__(self, key):
        """Removes "key" from dictionary's keys"""

    def __eq__(self, other):
        """Returns True/False based on whether two instances are equal"""

    def __getitem__(self, key):
        """Returns value for with "key" if it exists, or a KeyError"""
        
    def __iter__(self):
        """Returns an iterator of keys"""

    def __len__(self):
        """Returns the number of items in the dictionary"""

    def __repr__(self):
        """Returns a string representation of the dictionary"""

    def __setitem__(self, key, value):
        """Sets the value for key in dictionary, growing if 2/3 full"""

    def get(self, key, default=None):
        """Returns the value for key, or None, or default if provided"""

    def items(self):
        """Returns a list of tuples of all key/value pairs in dictionary"""

    def iterkeys(self):
        """Returns an iterator of keys in the dictionary"""

    def keys(self):
        """Returns a list of keys in the dictionary"""

    def values(self):
        """Returns a list of values for all keys in dictionary"""


class BucketInUseError(ValueError):
    """Internally used by _getbucket() if a particular bucket is in use"""


class NoAvailableBucketError(ValueError):
    """Error if, for some reason, there are no more buckets available"""

if __name__ == "__main__":
    hd = HomeMadeDict()
    hd["a"] = "apple"
    hd["b"] = "berry"
    hd["b"] = "banana"
    hd["c"] = "cherry"
    hd["d"] = "durian"
    hd["e"] = "elderberry"
    hd["f"] = "fig"

    d1 = HomeMadeDict()
    d1["abc"] = "abc"
    d1[2] = "two"
    d1["banana"] = 2

    d2 = HomeMadeDict()
    d2[2] = "two"
    d2["banana"] = 2
    d2["abc"] = "abc"

    d3 = HomeMadeDict()
    d3[2] = "two"
    d3["potato"] = 2
    d3["abc"] = "abc"

    d4 = HomeMadeDict()
    d4["abc"] = "cba"
    d4[2] = "two"
    d4["banana"] = 2

    d5 = HomeMadeDict()
    d5["abc"] = "cba"
    d5[2] = "two"
    d5["banana"] = 2

    d6 = HomeMadeDict()
    d6["abc"] = "abc"
    d6[2] = "two"

    print(f"Testing repr, hd: {hd}")

    print(f"Checking length of hd: {len(hd)}")
    print(f"Checking property length of hd: {hd.length}")
    print(f"Checking length of hd._items: {len(hd._items)}")


    print(f"Checking hd['a']: {hd['a']}")
    print(f"Checking hd['b']: {hd['b']}")
    print(f"Checking hd['c']: {hd['c']}")
    print(f"Checking hd['d']: {hd['d']}")
    print(f"Checking hd['e']: {hd['e']}")
    print(f"Checking hd['f']: {hd['f']}")
    print(f"Checking hd['z'] for KeyError: ", end='')
    try:
        print(hd['z'])
    except KeyError:
        print("caught KeyError, 'z' is not in hd")

    print("Iterating over hd:")
    for k in hd:
        print(f"- key: {k}, value: {hd[k]}")

    print(f"Checking if 'a' in hd: {'a' in hd}")
    print(f"Checking if 'z' in hd: {'z' in hd}")
    
    print(f"Checking hd keys: {hd.keys()}")
    print(f"Checking hd values: {hd.values()}")
    print(f"Checking hd items: {hd.items()}")

    print(f"Testing equality: d1 == d2 {d1 == d2}")
    print(f"Testing equality: d1 == d3 {d1 == d3}")
    print(f"Testing equality: d1 == d4 {d1 == d4}")
    print(f"Testing equality: d1 == d5 {d1 == d5}")
    print(f"Testing equality: d1 == d6 {d1 == d6}")


    print(f"Checking get(a): {hd.get('a')}")
    print(f"Checking get(z): {hd.get('z')}")
    print(f"Checking get(z): {hd.get('z', 'datdeftho')}")
