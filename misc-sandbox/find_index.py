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


def first_a(bac: str) -> int:
    end = len(bac) - 1
    l, r = 0, end
    while l <= r:
        m = (l + r) // 2
        if bac[m] == "b":
            l = m + 1
        elif bac[m] == "c":
            r = m - 1
        else:
            if (m == 0) or (m > 0 and bac[m-1] == "b"):
                return m
            else:
                r = m - 1
    return -1

def last_a(bac: str) -> int:
    end = len(bac) - 1
    l, r = 0, end
    while l <= r:
        m = (l + r) // 2
        if bac[m] == "b":
            l = m + 1
        elif bac[m] == "c":
            r = m - 1
        else:
            if (m == end) or (m < end and bac[m+1] == "c"):
                return m
            else:
                l = m + 1
    return -1

def count_as(bac: str) -> int:
    return last_a(bac) - (first_a(bac) - 1)


if __name__ == "__main__":
    print(count_as("baaaaaac")) # 6
    print(count_as("aaaa")) # 4
    print(count_as("aaaaac")) # 5
    print(count_as("baa")) # 2