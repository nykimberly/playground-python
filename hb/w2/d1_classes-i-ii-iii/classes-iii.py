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

# Mixins should come first in MRO as opposed to parent class

# static method to add methods required for a class but not directly related

class Cat:

    # Methods that operate on class, not an instance
    @classmethod
    def get_from_db(cls, name):
        """Get cat with given name from database."""

        # # raise Exception("No such cat: {}".format(name))
        # try:
        #     cursor = db.session.execute(cls._SELECT, {'name': name})
        #     cat_db_row = cursor.fetchone()
        #     hunger = cat_db_row[1]   # row is (name, hunger)
        # except LookupError:
        #     print("I couldn't get your cat.")

        cursor = db.session.execute(cls._SELECT, {'name': name})
        cat_db_row = cursor.fetchone()
        hunger = cat_db_row[1]   # row is (name, hunger)

        # Better yet, extend exception class with our exception
        if cat_db_row:
            return cls(name, hunger)
        else:
            raise NoSuchCatError("No such cat: {}".format(name))

    @staticmethod
    def kibble_to_calories(kibble):
        return kibble * 0.3456

Cat.kibble_to_calories(10)

# Look up 'decorators'

class NoSuchCatError(Exception):
    """Couldn't find this cat in database."""

# Something using your Cat class, v4
try:
    snowball_ii = Cat.get_from_db("Snowball II")

except NoSuchCatError:
    print("I couldn't get your cat.")


# Animal class with static factory method
# This is because Animal is hard coded into the static method. A class method does the right thing.

class Animal:
    """Animal."""

    @classmethod
    def make_one(cls):
        """Make an instance."""
        return cls()

class Cat:
    """Cat."""

>>> Animal.make_one()
    <__main__.Animal object at 0x10ba3e110>

>>> Cat.make_one()
    <__main__.Cat object at 0x10ba63d50>


# define a repr to show more useful object info

Special methods
__repr__
<__main__.Cat object at 0x10ba63d50> sucks. How useless is this?

class Cat:
     def __repr__(self):
         return f"<Cat: name={self.name}, hunger={self.hunger}>"

>>> auden = Cat('Auden')
>>> print(auden)
<Cat: name=Auden, hunger=50>
Other special methods:
__lt__, __le__, __gt__, __ge__, __eq__
__bool__
__hash__

