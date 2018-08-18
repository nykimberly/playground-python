# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = int(input())
    arr = sorted(list(set(map(int, input().split()))))
    print(arr[-2])