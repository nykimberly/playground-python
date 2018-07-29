# Enter your code here. Read input from STDIN. Print output to STDOUT
import sys

a = sys.stdin.read(file.txt)
a, b, c = input().strip().split(' ')

col, thresh, count = int(a), int(b), int(c)
# 3, 12, 2

i = 0
j = 0
table = []
for line in sys.stdin:
    if i > 5:
        if float(line.split()[col]) > thresh:
            j += 1
            if j >= count:
                print(line.split()[0])
        if float(line.split()[col]) < thresh:
            j = 0
    i += 1