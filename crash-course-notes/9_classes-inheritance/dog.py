import sys
sys.path.insert(0, '/home/nykimberly/code/Python/crash-course-notes/')
from kim_tools import animated_print

class Dog():
    """A simple attempt to model a dog."""
    
    def __init__(self, name, age=0):
        """Initialize name and age attributes"""
        self.name = name
        try:
            int(age)
            self.age = int(age)
        except ValueError:
            print("Age provided was not an integer. Defaulting to 0.")
            self.age = 0
        message = "\nWelcome " + self.name.title() + "!\n"
        animated_print(message)
     
    def sit(self):
        """Simulate a dog sitting in response to a command."""
        action = "\n" + self.name.title() + " is now sitting.\n"
        animated_print(action)

    def roll_over(self):
        """Simulate a dog sitting in response to a command."""
        action = "\n" + self.name.title() + " is rolling over!\n"
        animated_print(action)
    
    def celebrate_birthday(self):
        """Simulate a birthday celebration for dog."""
        self.age += 1
        action = "\nHappy Birthday " + self.name.title() + \
                "! You are now " + str(self.age) + " years old.\n"
        animated_print(action)

class CuteDog(Dog):
    """A simple attempt to model a cute dog."""

    def __init__(self, name, cuteness_level, age=0):
        """Initialize attributes of parent class."""
        super().__init__(name, age)
        self.cuteness_level = cuteness_level
        message = "\nYour cuteness level is " + str(self.cuteness_level) + "!\n"
        message += "\nAnd you are only " + str(self.age) + " years old!\n"
        animated_print(message)
    
    def cute_up(self, increment):
        self.cuteness_level += increment
        message = "\n" + self.name.title() + " has gotten cuter!!" +\
                " Cuteness level now " + str(self.cuteness_level) + "!\n"
        animated_print(message)

    def sit(self):
        """Simulate a cute dog sitting"""
        action = "\n" + self.name.title() + " is now sitting cutely.\n"
        animated_print(action)
