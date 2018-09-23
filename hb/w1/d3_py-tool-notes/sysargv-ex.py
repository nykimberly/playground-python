import sys

filename = sys.argv[1]   # first real argument
for melon_data in open(filename):
    print(melon_data)
