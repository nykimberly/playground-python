"""Search"""


def find_index(elements, value):
    left, right = 0, len(elements) - 1
    while left <= right:
        middle = (left + right) // 2
        if elements[middle] == value:
            return middle
        if elements[middle] < value:
            left = middle + 1
        elif elements[middle] > value:
            right = middle - 1
    return -1


if __name__ == "__main__":
    result = find_index([1, 2, 3, 4, 5, 10, 11, 13], 3)
    print(result)