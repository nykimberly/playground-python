from copy import copy
from sys import argv
from timeit import default_timer
from random import randint

def print_timing(func):
    def wrapper(*args, **kwargs):
        if len(argv) == 2:
            start_time = default_timer()
            result = func(*args, **kwargs)
            delta = "{:.2f}".format((default_timer() - start_time) * 1000000)
            dprint(f"Timing: {func.__name__}() took {delta} us")
            return result
        else:
            return func(*args, **kwargs)
    return wrapper

class HomeMadeDict:
    """A homemade implementation of a dictionary."""

    @print_timing
    def __init__(self):
        self._size = 3
        self._items = [None for i in range(2 ** self._size)]
        self._used_slots = 0
        self._print_timing = print_timing

    @print_timing
    def __contains__(self, key):
        """Used by "key in dictionary", returns True/False"""
        dprint(f"Checking if key: {key} is present")
        bucket = self._getbucket(key)
        if self._items[bucket] is None:
            return False
        return True

    @print_timing
    def __delitem__(self, key):
        """Removes "key" from dictionary's keys"""
        bucket = self._getbucket(key)
        if self._items[bucket] is None:
            raise KeyError 
        self._items[self._getbucket(key)] = None
        self._used_slots -= 1

    @print_timing
    def __eq__(self, other):
        """Returns True/False based on whether two instances are equal"""
        if len(self) != len(other):
            return False
        
        self_keys = set(self.keys())
        other_keys = set(other.keys())

        if len(self_keys ^ other_keys) != 0:
            return False

        for key in self_keys:
            if self[key] != other[key]:
                return False

        return True

    @print_timing
    def __getitem__(self, key):
        """Returns value for with "key" if it exists, or a KeyError"""
        dprint(f"Getting key: {key}")
        bucket = self._getbucket(key)
        if self._items[bucket] is None:
            raise KeyError
        return self._items[self._getbucket(key)][1]
        
    @print_timing
    def __iter__(self):
        """Returns an iterator of keys"""
        return self.iterkeys()

    @print_timing
    def __len__(self):
        """Returns the number of items in the dictionary"""
        return self._used_slots

    @print_timing
    def __repr__(self):
        """Returns a string representation of the dictionary"""
        return '{' + ', '.join([f"{k.__repr__()}: {v.__repr__()}" for k, v in sorted(self.items())]) + '}'

    @print_timing
    def __setitem__(self, key, value):
        """Sets the value for key in dictionary, growing if 2/3 full"""
        dprint(f"Setting key: {key}, value: {value}")
        bucket = self._getbucket(key)
        if self._items[bucket] is None or self._items[bucket][0] != key:
            self._used_slots += 1
        self._items[bucket] = (key, value)

        dprint(f"Checking rehash - usage: {self._used_slots} , length: {len(self._items)} = {self._used_slots / len(self._items)}")
        if (self._used_slots / len(self._items)) > 0.66:
            dprint("SHOULD REHASH")
            self._rehash()

    @print_timing
    def _rebucket(func):
        """Decorator around _getbucket to retry"""
        # We know that this will wrap self._getbucket() so we can safely make
        # assumptions about the args passed to this function:
        def wrapper(self, key):
            # If our probing method is correct, this is ok
            for attempt in range(len(self._items)):
                try:
                    return func(self, key, attempt)
                except BucketInUseError:
                    pass
            raise NoAvailableBucketError
        return wrapper

    @print_timing
    @_rebucket
    def _getbucket(self, key, attempt):
        """Probes for a bucket number for a given key"""
        # For simplicity:
        # If bucket is taken, next attempt will look one item to the right:
        # If that would cause an index error, subtract the length of the list
        # to get to zero:
        bucket = (abs(hash(key)) % len(self._items)) + attempt
        if bucket >= len(self._items):
            bucket -= len(self._items)
        if self._items[bucket] is None:
            dprint(f"bucket {bucket} for key {key} available")
            return bucket
        elif self._items[bucket][0] == key:
            dprint(f"bucket {bucket} for key {key} already used by {key}")
            return bucket
        else:
            existing_key = self._items[bucket][0]
            dprint(f"Bucket {bucket} for {key} - already in use by {existing_key}")
            raise BucketInUseError

    @print_timing
    def _rehash(self):
        """Resizes the dictionary to the next size (in powers of two)"""

        self._size += 1 
        new_size = 2 ** self._size

        dprint(f"Rehashing - used_slots: {self._used_slots} len: {len(self._items)}, new_size: {new_size}")

        old_items = self.items()

        self._items = [None for i in range(new_size)]
        self._used_slots = 0
        
        for key, value in old_items:
            self.__setitem__(key, value)

    @print_timing
    def get(self, key, default=None):
        """Returns the value for key, or None, or default if provided"""
        try:
            return self.__getitem__(key)
        except KeyError:
            return default

    @print_timing
    def items(self):
        """Returns a list of tuples of all key/value pairs in dictionary"""
        return [item for item in self._items if item is not None]

    @print_timing
    def iterkeys(self):
        """Returns an iterator of keys in the dictionary"""
        return iter(self.keys())

    @print_timing
    def keys(self):
        """Returns a list of keys in the dictionary"""
        return [item[0] for item in self._items if item is not None]

    @property
    @print_timing
    def length(self):
        """Returns the length of the dictionary as a property"""
        return self._used_slots

    @print_timing
    def retry_three_times(func):
        def wrapper(*args, **kwargs):
            for i in range(4):
                try:
                    return func(*args, **kwargs)
                except ThatsTooBadError:
                    dprint(f"{func.__name__} attempt {i+1} failed.")
                    if i > 2:
                        raise ThatsTooBadError
        return wrapper

    @print_timing
    @retry_three_times
    def random_succeed(self):
        roll = randint(1, 100)
        if roll >= 75:
            return "Success!"
        else:
            raise ThatsTooBadError

    @print_timing
    def values(self):
        """Returns a list of values for all keys in dictionary"""
        return [item[1] for item in self._items if item is not None]


class BucketInUseError(ValueError):
    """Internally used by _getbucket() if a particular bucket is in use"""


class NoAvailableBucketError(ValueError):
    """Error if, for some reason, there are no more buckets available"""

class ThatsTooBadError(Exception):
    """Man, that's just too bad..."""

def dprint(msg):
    if len(argv) == 2:
        print(msg)

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

    print("Trying random_succeed three times:")
    for i in range(3):
        try:
            print(hd.random_succeed())
        except ThatsTooBadError:
            print("Caught ThatsTooBadError")

