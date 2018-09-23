# Filename extensions
# 	cupcakes.py: Python source code
# 	cupcakes.pyc: Compiled Python source code
# 	cupcakes.pyo: Optimized compiled Python source code
# 	cupcakes.pyd: Compiled C importable by Python


# Namespaces
    # Namespace is all the identifiers available for use
    # For example:
        # cupcake_flavor = 'chocolate'
        # adds a variable named cupcake_flavor to your namespace
    # and
        # def decorate_cupcake(cupcake):
        #   """Add icing, sprinkles and candies."""
        # adds a function named decorate_cupcake to your namespace


# Ways to import modules

## import the module and use module name in method calls
import random
print(random.randint(1,10))

## import specific method, allowing us to call with just method name
from random import choice
print(choice([1, 2, 3]))

## from random import * is generally a bad idea due to ambiguity

## to avoid namespace overwrites or to shorten long names, use 'as'
from server import session as server_session
from db import session as db_session
import sqlalchemy as sqla

## importing entire module or running module file will run all lines of code
## If you want something not to run on import:
if __name__ == '__main__':
    # code goes here
    # executes when file is run directly
    # does NOT execute when imported as a module


# Packages
    # A directory importable by Python
    # Useful for organizing code
    # Example
    # projectroot/
    #   server.py
    #   db/
    #     model.py
    #     seed.py
    #     foo.csv
    #     bar.csv
    #   tests/
    #     test_ratings.py
    # from db import model          # model.User
    # or:
    # from db.model import User     # User
    # or:
    # import db.model                # db.model.User

# The Dot(s)
    # Only works inside packages:
    # from .model import User
    # Explicitly says “import from current directory”
    # from ..model import User
    # Import from the model module in the parent directory

# Good to break up code
#     pacman/
#       game.py        # the player, and how we move around
#       score.py       # functions dealing with the score
#       ghosts.py      # logic around how ghosts move
#       maze.py        # the mazes and levels
