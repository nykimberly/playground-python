"""Disable ability to make orders of over 100 melons"""

class TooManyMelonsError(ValueError):

    def __init__(self, message):
        self.message = message

