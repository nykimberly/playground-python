#It's New Year's Day and everyone's in line for the Wonderland rollercoaster ride! There are a number of people queued up, and each person wears a sticker indicating their initial position in the queue. Initial positions increment by 1 from 1 at the front of the line to n at the back.

#Any person in the queue can bribe the person directly in front of them to swap positions. If two people swap positions, they still wear the same sticker denoting their original places in line. One person can bribe at most two others. For example, if n=8 and Person 5 bribes Person 4, the queue will look like this: 1, 2, 3, 5, 4, 6, 7, 8.

#Fascinated by this chaotic queue, you decide you must know the minimum number of bribes that took place to get the queue into its current state!


def minimumBribes(q):
    p = [x for x in range(1, len(q) + 1)]
    bribe = 0
    for n in range(len(q)):
        if q[n] > n+1:
            span = q[n] - (n+1)
            if span > 2:
                print("Too chaotic")
                return
            bribe += span
            for i in range(span, 0, -1):
                p[n+i], p[n+i-1] = p[n+i-1], p[n+i]
        if p[n] != q[n]:
            bribe += 1
            p[n+1], p[n] = p[n], p[n+1]
    print(bribe)
    return


#if __name__ == '__main__':
    #t = int(input())
    #for t_itr in range(t):
        #n = int(input())
        #q = list(map(int, input().rstrip().split()))
        #minimumBribes(q)


q = [2, 1, 5, 3, 4]
r = [1, 2, 5, 3, 7, 8, 6, 4]
s = [5, 1, 2, 3, 7, 8, 6, 4]

minimumBribes(q)
minimumBribes(s)
minimumBribes(r)
