#!/bin/python3


# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    # create hash of words in magazine
    mag = {word: 0 for word in set(magazine)}
    # loop through words in magazine and increment
    for word in magazine:
        mag[word] += 1
    # then loop through words in note and decrement
    for word in note:
        # if words not in hash then return "No"
        if word not in mag.keys():
            print("No")
            return
        mag[word] -= 1
        # if word in hash but decrementer has returned negative, return "No"
        if mag[word] < 0:
            print("No")
            return
    print("Yes")
    return


if __name__ == '__main__':

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    checkMagazine(magazine, note)
