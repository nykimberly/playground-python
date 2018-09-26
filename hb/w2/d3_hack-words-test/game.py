import random
from sys import argv

def get_guess():
    """Get a guess from the user.
    
    Use of built-in is factored out of code here for
    testability.
    """

    return input("Guess a letter > ")

def get_file(filename):
    """Get file contents.

    Use of built-in is factored out of code here for
    testability.
    """

    f = open(filename)
    return f

def get_words(filename):
    """Either process words in a file, or return some default words."""

    try: 
      f = get_file(filename)
      return [ word.strip() for word in f ]

    except FileNotFoundError:
      return [ 'foobar', 'skunkworks', 'arpanet', 'unix' ]

def handle_guess(guess, guessed, answer):
    """Handle guess by user."""

    # Keep track of the fact that they made this guess
    guessed[guess] = 1
    if guess in answer:
        return "Right!"
    else:
        return "Wrong!"


def show_word(answer, guessed):
    """Show board with correct letters filled in."""

    result = ""

    for letter in answer:
        if letter in guessed:
            result = result + letter
        else:
            result = result + "-"

    return result


def has_won(answer, guessed):
    """Has user won game? (True or False)"""

    for letter in answer:
        if not (letter in guessed):
            return False

    return True


def main_loop(answer):
    """Game loop."""

    print(show_welcome())

    guessed = {}

    while not has_won(answer, guessed):
        
        guess = get_guess()

        print(handle_guess(guess, guessed, answer))

        print(show_word(answer, guessed))
        

def play_game(word_file):
    """Main game loop."""

    words = get_words(word_file)
    answer = random.choice(words)

    main_loop(answer)
    print("You won!")

def show_welcome():
    """Show fun banner before playing game."""

    return """
     ____________________________
    !\\_________________________/!\\
    !!                         !! \\
    !!                         !!  \\
    !!    Welcome to           !!  !
    !!                         !!  !
    !!                         !!  !
    !!     Hack Words!  :)     !!  !
    !!                         !!  !
    !!                         !!  /
    !!_________________________!! /
    !/_________________________\\!/
       __\\_________________/__/!_
      !_______________________!/
    ________________________
   /oooo  oooo  oooo  oooo /!
  /ooooooooooooooooooooooo/ /
 /ooooooooooooooooooooooo/ /
/C=_____________________/_/

    """

if __name__ == "__main__":

    if len(argv) > 1:
      word_file = argv[1]
    else:
      word_file = ""

    play_game(word_file)
