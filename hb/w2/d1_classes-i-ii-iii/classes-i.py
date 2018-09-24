#!/Users/kimberlyvnguyen/anaconda3/bin/python3

# We should write classes in uppercase but built in classes may be lower case

# We can use type() to figure out what class an instance belongs to

# Don't change class attributes to avoid instance-class attribute ambiguity

# By convention, start variable with underscore if you want it to be 'private'

class Animal:
    """A living creature"""
    name = None
    nicknames = []

# Can assign attributes to instances of class
dog = Animal()
dog.name = 'fido'
print(dog.name)

# Don't give any mutable types to a class attribute due to 'sticky' id

# In the below code, we’re setting nicknames = [] as a class attribute (set directly on the class). 
# This means that all of the instances of Animal will share this list. So, if you made two Animals:
fido = Animal()
snowball = Animal()
fido.nicknames.append("Woofster")
print(fido.nicknames)
print(snowball.nicknames)

# You can prevent this problem by rebinding the nickname for Fido, rather than appending it:
fido = Animal()
snowball = Animal()
fido.nicknames = ['Woofster']
print(fido.nicknames)
print(snowball.nicknames)
# But a better suggestion is to not set mutable attributes as class attributes; always set these in the __init__ method described below. Many developers (including Hackbright staff) follow the even-better principle of setting all initial values in __init__, where possible, and setting nothing as class attributes. This can reduce confusion.

# Another curious thing is making sure we use 'self' to refer to the instance
# and className to refer to 'global' variable adjustments
class CountKeeper:
    count = 0
    def add(self, value):
        CountKeeper.count += value
        # self.count += value here if you only wanted to change for instance
x = CountKeeper()
y = CountKeeper()
x.add(3)
print(x.count) # 3
print(y.count) # 3

# getattr()
# print(fido.tail_length)
    # ---------------------------------------------------------------------------
    # AttributeError                            Traceback (most recent call last)
    # <ipython-input-3-30bc9705613c> in <module>()
    # ----> 1 fido.tail_length
    # AttributeError: 'Animal' object has no attribute 'tail_length'
getattr(fido, 'tail_length', 'unknown')
    # 'unknown'

# Functions Versus Methods
    # Both are code
    # Both have lists of parameters
    # Both get called with ()
    # Methods are defined on a class
    # Methods take self as first argument
    # When you call a method, Python passes instance as self

class Animal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(self.name)

fido = Animal('fido')
Animal.speak(fido)
