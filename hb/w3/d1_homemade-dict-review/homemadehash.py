from copy import copy
from sys import argv
from timeit import default_timer
from random import randint

class HomemadeHash:
    """Homemade implementation of a dictionary"""

    def __init__(self):
        self._size = 8
        self._items = [None for i in range(self._size)]
        self._used_slots = 0

    def __repr__(self):
        return f"I am a homemade hashmap of size {self._size},"\
        f"{len(self._items)} items, and {self._used_slots} used slots."

    def __len__(self):
        """Returns length of used slots"""
        return len(self._used_slots)

    def __contains__(self, key):
        """Used by '{key} in {dict}', returns True/False"""
        print(f"Checking if {key} exists in dictionary")
        slot = self._get_slot(self, key)
        if self._items[slot] is None:
            return False
        return True

    def __delitem__(self, key):
        """Removes 'key' from dictionary's keys"""
        slot = self._get_slot(key)
        if self._items[slot] is None:
            raise KeyError
        self._items[slot] = None
        self._used_slots -= 1

    def __eq__(self, other):
        """Returns whether two instances are equal"""
        print("Returns whether two instances are equal")
        # eliminate incorrectly sized lists right away
        if len(self.items()) != len(other.items()):
            return False
        # now compare keys using set operations
        self_keys = set(self.keys())
        other_keys = set(other.keys())
        if len(self_keys ^ other_keys) != 0:
            return False
        for key in self_keys:
            if self[key] != other[key]:
                return False
        return True

    def __getitem__(self, key):
        """Returns value with key if it exists or keyerror otherwise"""
        print(f"Getting key: {key}")
        slot = self._get_slot(key)
        if self._items[slot] is None:
            raise KeyError
        return self._items[slot][1]

    def __setitem__(self, key, value):
        """Adds k,v pair to a slot"""
        slot = self._get_slot(key)
        if self._items[slot] is None or self._items[slot][0] != key:
            self._used_slots += 1
        self._items[slot] = (key, value)

    def _get_slot(self, key, attempt=0):
        """Probes for slot value of a given key"""
        slot = abs(hash(key) % len(self._items)) + attempt
        if slot >= len(self._items):
            slot -= len(self._items)
        if self._items[slot] is None:
            print(f"Slot {slot} for key {key} availble")
            return slot
        elif self._items[slot][0] == key:
            print(f"Slot {slot} for key {key} used by {key}")
            return slot
        else:
            existing_key = self._items[bucket][0]
            print(f"Slot {slot} for key {key} already in use by {existing_key}")
            raise SlotInUseError

    def get(self, key, default=None):
        """Returns the value for key or fallback to None"""
        try:
            return self.__getote,__(key)
        except KeyError:
            return default

    def keys(self):
        """Return list of keys in dictionary"""
        return [item[0] for item in self._items if item is not None]

    def values(self):
        """Return list of values in dictionary"""
        return [item[1] for item in self._items if item is not None]

    def items(self):
        """Return list of items in dictionary"""
        return [item for item in self._items if item is not None]


class SlotInUseError(ValueError):
    """Error if hashed slot is already in use"""

class NoAvailableSlotError(ValueError):
    """Error if there are no more slots available"""

if __name__ == "__main__":

    # Initialization
    h_a = HomemadeHash()
    h_b = HomemadeHash()
    print(f"---repr: {h_a}")
    print(f"---repr: {h_b}")

    # Equality
    h_a["zero"] = 0
    h_b["zero"] = 0
    print(f"---equality: {h_a.__eq__(h_b)}")
    print(f"---equality: {h_a == h_b}")


