#Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given n scores. Store them in a list and find the score of the runner-up.

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


def heapify(lst, root, end):
    largest = root
    left = 2*root + 1
    right = 2*root + 2
    if left < end and lst[largest] < lst[left]:
        largest = left
    if right < end and lst[largest] < lst[right]:
        largest = right
    if largest != root:
        lst[root], lst[largest] = lst[largest], lst[root]
        heapify(lst, largest, end)


def heapSort(lst):
    end = len(lst)
    for i in range(end-1, -1, -1):
        heapify(lst, i, end)
    for curr in range(end-1, -1, -1):
        lst[0], lst[curr] = lst[curr], lst[0]
        heapify(lst, 0, curr)
    first_place = lst.pop()
    second_place = lst.pop()
    print("first_place", "second_place")
    print(first_place, second_place)
    return second_place


nums = list(set(arr))
heapSort(nums)
