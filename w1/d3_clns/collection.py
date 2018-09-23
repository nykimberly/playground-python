#!/home/vagrant/miniconda3/bin/python3
words = ["awesome", "alex", "orange", "ant", "deadly"]
print(words)
a_words = [word for word in words if word.startswith("a")]
print(a_words)


# lambda, like js anonymous functions
print(map(str.upper, ['a', 'b', 'c']))
newlist = map(str.upper, ['a', 'b', 'c'])
print(newlist)
anotherlist = map(lambda x: x + '2', ['a', 'b', 'c'])
print(anotherlist)
