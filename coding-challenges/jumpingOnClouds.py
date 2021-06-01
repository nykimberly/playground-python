#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumpingOnClouds(c):
    steps = 0
    i = 0
    while i+1 < len(c):
        if i+2 < len(c) and c[i+2] == 0:
            i += 2
        else:
            i += 1
        steps += 1
    return steps

if __name__ == '__main__':
    n = int(input().strip())
    c = list(map(int, input().rstrip().split()))
    result = jumpingOnClouds(c)
    print(result)