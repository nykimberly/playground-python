import string

filename = 'test.txt'
# filename = 'twain.txt'

with open(filename) as f:
    words = f.read().rstrip().replace("\n", " ").split(" ")

word_count = {}
for word in words:
    word =  word.strip(string.punctuation)
    word_count[word] = word_count.get(word, 0) + 1

for word in word_count:
    print(word,"=",word_count[word])
