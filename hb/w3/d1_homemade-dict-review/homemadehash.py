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

    def _get_slot(self, key):
        """Probes for slot value of a given key"""

        slot = abs(hash(key) % len(self._items)) + attempt

        if slot >= len(self._items):
            slot -= len(self._items)

        if self._items[slot] is None:
            dprint(f"Slot {slot} for key {key} availble")
            return slot

        elif self._items[slot][0] == key:
            dprint(f"Slot {slot} for key {key} already used by {key}")
            return slot

        else:
            existing_key = self._items[bucket][0]
            dprint(f"Slot {slot} for key {key} already in use by {existing_key}")
            raise SlotInUseError

    def __contains__(self, key):
        """Used by '{key} in {dict}', returns True/False"""
        dprint(f"Checking if {key} exists in dictionary")
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
        """Returns value with key if it exists or keyerror otherwise"""
        # eliminate incorrectly sized lists right away
        if len(self) != len(other):
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

    def keys(self):
        """Return list of keys in dictionary"""
        return [item[0] for item in self._items if item is not None]


class SlotInUseError(ValueError):
    """Error if hashed slot is already in use"""

if __name__ == "__main__":
    hh = HomemadeHash()
