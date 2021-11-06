#Given two strings in lowercase, the task is to make them anagram. The only allowed operation is to remove a character from any string. Find minimum number of characters to be deleted to make both the strings anagram?


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
print(res)
