# -*- coding: utf-8 -*-

# [1, 5, 3, 9]
# [23, 6, 5, 4]

def common_elements(ar1, ar2):

    res = []
    ar1_elements = { element: 0 for element in ar1 }

    for element in ar2:
        if element in ar1_elements:
            res.append(element)

    return list(set(res))

common_elements([1, 5, 3, 9], [23, 6, 5, 4]) == [5]
common_elements([1, 5, 5, 3, 9, -1, 'a'], ['a', 23, 6, 5, 5, 5, 4])