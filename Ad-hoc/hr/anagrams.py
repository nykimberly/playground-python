#!/bin/python3


# Complete the makeAnagram function below.
def makeAnagram(a, b):

    a = sorted(list(a.lower()))
    b = sorted(list(b.lower()))

    a_i = 0
    b_i = 0
    deleteCount = 0

    while a_i < len(a) and b_i < len(b):
        if a[a_i] < b[b_i]:
            deleteCount += 1
            del(a[a_i])
        elif a[a_i] > b[b_i]:
            deleteCount += 1
            del(b[b_i])
        else:
            a_i += 1
            b_i += 1

    while a_i < len(a):
        deleteCount += 1
        del(a[a_i])

    while b_i < len(b):
        deleteCount += 1
        del(b[b_i])

    return deleteCount


res = makeAnagram("fcrxzwscanmligyxyvym", "jxwtrhvujlmrpdoqbisbwhmgpmeoke")

#a = input()
#b = input()
#res = makeAnagram(a, b)
