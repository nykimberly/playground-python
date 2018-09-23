# Why use classes?
    # 1. Abstraction (hiding implementation details)
    # 2. Encapsulation (keeping everything together)
    # 3. Polymorphism (interchangeability)

class Animal:
    greeting = "Hey!"

    def __init__(self, name, species):
        self.name = name
        self.species = species

    def speak(self):
        print(f"{self.greeting}, I'm {self.name} the {self.species}")

class Cat(Animal):
    greeting = "Meow!"

    def __init__(self, name):
        super().__init__(name, species='cat')

class Dog(Animal):
    greeting = "Woof!"

    def __init__(self, name, species='dog'):
        super().__init__(name, species)

# ╭─  …/d1_classes-i-ii-iii                                                                     2350  16:32:22 
# ╰─ python3 -i classes-iii.py
    # >>> acat = Cat('astrid')
    # >>> adog = Dog('astroid')
    # >>> acat.speak()
    # Meow!, I'm astrid the cat
    # >>> adog.speak()
    # Woof!, I'm astroid the dog


# If we want, we can make our Animal class abstract
# Typically, we would name it BaseAnimal or AbstractAnimal
# The class itself would be useless and can't be used
# But it provides useful structure for subclasses

class AbstractAnimal:

    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.greet}, I'm {self.name} the {self.species}")


class Cat(AbstractAnimal):
    greet = "Meow"
    species = "cat"


class Dog(AbstractAnimal):
    greet = "Woof"
    species = "dog"
    
# ╭─  …/d1_classes-i-ii-iii                                                                     2351  16:35:31 
# ╰─ python3 -i classes-iii.py
    # >>> cat = Cat('astrid')
    # >>> cat.name
    # 'astrid'
    # >>> cat.species
    # 'cat'
    # >>> cat.speak()
    # Meow, I'm astrid the cat


# Mixin classes
class ChaseLaserPointersMixin:
    """Can chase laser pointers."""

    def chase_laser(self):
          print("Wheee!")


class CoverYouInFurMixin:
     """Can cover you in fur."""

     def enfur(self):
          print("(fur, fur, fur)")

# We'd simply call them in our subclass
class Cat(ChaseLaserPointerMixin, CoverYouInFurMixin, Animal):
    """A cat."""

    # ...


class Dog(CoverYouInFurMixin, Animal):
    """A dog."""

    # ...


class HairlessRobot(ChaseLaserPointerMixin, Animal):
    """A robot."""

    # ...


