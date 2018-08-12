#!/bin/python3


def minimumBribes(q):

    # let's create an array that starts at 'proper'
    p = [x for x in range(1, len(q) + 1)]

    # track bribes
    bribe = 0

    # let's print our argument for clarity sake
    print("q is currently ", q)

    # iterate through q, with n+1 as the 'proper' queue value at that spot
    for n in range(len(q)):

        # if the value at q is greater than proper value, we assume bribe
        if q[n] > n+1:

            # let's count how many bribes
            span = q[n] - (n+1)

            # if there are more than 2 bribes, it's too chaotic!
            if span > 2:
                print("Too chaotic")
                return

            # print("%d bribed %d times" % (q[n], span))
            bribe += span

            for i in range(span, 0, -1):
                # let's swap this until position matches q
                p[n+i], p[n+i-1] = p[n+i-1], p[n+i]

        # check for any sub-bribes
        if p[n] != q[n]:
            bribe += 1
            p[n+1], p[n] = p[n], p[n+1]

    print(bribe)
    return


q = [2, 1, 5, 3, 4]
r = [1, 2, 5, 3, 7, 8, 6, 4]
s = [5, 1, 2, 3, 7, 8, 6, 4]

minimumBribes(q)
minimumBribes(s)
minimumBribes(r)
