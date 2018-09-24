# Method Resolution Order (MRO)
# Super() similar to parent class but sometimes with multiple inheritances it
# might not be

class A:
    def m(self):
        print("A")

class B(A):
    def m(self):
        print("B")
        super().m()

class C(A):
    def m(self):
        print("C")
        super().m()

class D(B, C):
    def m(self):
        print("D")

letter = D()
letter.m()
# D
# B
# C
# A

# Instead of DBA, 
letter.mro() # to show method resolution order

# Interaction between class and instance attributes
class Animal:
    # class attribute
    hunger = 50
    
    def __init__(self, name):
        self.name = name
        self.info()

    def info(self):
        print(self.name, "has hunger of", self.hunger)

dog = Animal("fido")

# Inheritance between superclasses and subclasses
class Animal:
    hunger = 50

class Cat(Animal):
    hunger = 70 # this value returns when we call cat=Cat().hunger

# super initialization

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def greet(self):
        msg = "Hi there. My name is " + self.name + "."
        return msg

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'cat')

astrid = Cat('astrid')
print(astrid.species)

# leveraging super()'s methods
class FriendlyCat(Cat):
    def greet(self):
        msg = super().greet()
        return msg + " You seem awesome."

kimberly = FriendlyCat('kimberly')
print(kimberly.greet())

# polymorphism
class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species
    def speak(self, greet="Hey"):
        print(f"{greet}, I'm {self.name} the {self.species}")

class Cat(Animal):
    def __init__(self, name):
        super().__init__(name, 'cat')
    def speak(self):
        super().speak('Meow')

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name, 'dog')
    def speak(self):
        super().speak('Ruff')

animals = []
acat = Cat('Astrid')
animals.append(acat)
adog = Dog('Kiki')
animals.append(adog)

for animal in animals:
    print(animal.speak())

