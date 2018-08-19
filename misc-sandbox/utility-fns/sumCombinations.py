# -*- coding: utf-8 -*-

# a + b = c + d, 0 <= a,b,c,d <= 10

a = []
b = []
c = []
d = []
d = {}
res = []

for a in range(0, 10):
    for b in range(0, 10):
        lhs = a + b
        if lhs in d:
            res.append(d[lhs] + [a, b])
        else:
            d[lhs] = [a,b]

for k in d:
    print(str(k) + " can be made of " + str(d[k]))

print(res)

for result in res:
    # print(str(sum(result[0:2])) + " is equal to " + str(sum(result[2:4])))
    if sum(result[0:2]) == sum(result[2:4]):
        print("True")
    else:
        print("False")