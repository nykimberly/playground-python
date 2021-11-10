"""Given an array of integers, where all elements but one occur twice, find the unique element.

lonelyinteger has the following parameter(s):
int a[n]: an array of integers

Returns
int: the element that occurs only once

Approach: Frequency map and return the one with count of 1
"""

def lonelyinteger(a):
    counter = {}
    for item in a:
        counter.setdefault(item, 0)
        counter[item] += 1
    for item, count in counter.items():
        if count == 1:
            return item


def lonelyinteger2(a):
    arr = collections.Counter(a)
    for k, v in arr.items():
        if v == 1:
            return k

        
if __name__ == '__main__':
    a = [4, 9, 95, 93, 57, 4, 57, 93, 9]
    result = lonelyinteger(a)
    print(result)
