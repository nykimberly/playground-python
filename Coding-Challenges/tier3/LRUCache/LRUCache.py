class Node:

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity):

        assert capacity < 100,\
            "The max capacity is 100!"
        assert type(capacity) is int, \
            "Capacity must be an integer value."

        self.dict = dict()
        self.capacity = capacity
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key):


        if key in self.dict:
            payload = self.dict[key]
            return payload.value
        return -1

    def put(self, key, value):



        if key in self.dict:
            self._remove(self.dict[key])
        payload = Node(key, value)
        self._add(payload)
        self.dict[key] = payload

        if len(self.dict) > self.capacity:
            payload = self.head.next
            self._remove(payload)
            del self.dict[payload.key]

    def _remove(self, payload):
        p = payload.prev
        n = payload.next
        p.next = n
        n.prev = p

    def _add(self, payload):
        # p = <-self.tail
        p = self.tail.prev
        # p -> payload
        p.next = payload
        # p <- payload
        payload.prev = p
        # payload <-self.tail
        self.tail.prev = payload
        # payload -> self.tail
        payload.next = self.tail
        # p <-> payload <-> self.tail
