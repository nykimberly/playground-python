"""
Consider a list (list = []). You can perform the following commands:
insert i e: Insert integer e at position i.
print: Print the list.
remove e: Delete the first occurrence of integer e.
append e: Insert integer e at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.

Initialize your list and read in the value of n followed by n lines of commands where each command will be of the types listed above.
Iterate through each command in order and perform the corresponding operation on your list.

Input Format
The first line contains an integer, n, denoting the number of commands.
Each line i of the n subsequent lines contains one of the commands described above.

Constraints
The elements added to the list must be integers.

Output Format
For each command of type print, print the list on a new line.
"""
def operations_(arr, action, arg):
    operations = {
            "insert": insert_,
            "print": print_,
            "remove": remove_,
            "append": append_,
            "sort": sort_,
            "pop": pop_,
            "reverse": reverse_
            }
    func = operations[action]
    return func(arr, arg)


def insert_(arr, arg):
    index = arg[0]
    integer = arg[1]
    if index >= len(arr):
        arr.append(integer)
    else:
        arr.insert(index, integer)
    return


def print_(arr, arg):
    print(arr)
    return


def remove_(arr, arg):
    arr.remove(arg[0])
    return


def append_(arr, arg):
    arr.append(arg[0])
    return


def sort_(arr, arg):
    arr.sort()
    return


def pop_(arr, arg):
    arr.pop()
    return


def reverse_(arr, arg):
    arr.reverse()
    return arr


if __name__ == '__main__':
    lst = []

    N = int(input())
    instructions = []

    for _ in range(N):
        instruction = input()
        instructions.append(instruction)

    for instruction in instructions:
        inst_lst = instruction.split()
        action = inst_lst.pop(0)
        args = list(int(val) for val in inst_lst)
        operations_(lst, action, args)
