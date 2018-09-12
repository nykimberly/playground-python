import time
import sys
import random

def animated_print(phrase):
    for char in phrase:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(random.randrange(0,2)/10)
