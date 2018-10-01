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

class SlotInUseError(ValueError):
    """Error if hashed slot is already in use"""

if __name__ == "__main__":
    hh = HomemadeHash()
