# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt

ourpath = 'data/search-results.txt'

with open(ourpath, 'r') as f:

    head = f.readline().split("|")
    head_ar = list(title.strip() for title in head)
    print(head, head_ar)

    sep = f.readline()
    print(sep)

    body_ar = list([] for title in head)
    row_ar = list([] for title in head)
    print(row_ar, body_ar)

    arr = []

    for i, line in enumerate(f):
        row_ar = list(float(val.strip()) for val in line.split("|"))
        for i, title in enumerate(head):
            body_ar[i].append(row_ar[i])

plt.scatter(body_ar[1], body_ar[3])