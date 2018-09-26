import unittest
import game

class HandleGuessTestCase(unittest.TestCase):
    """Test for displaying the current state of progress towards answer."""
    def setUp(self):
        self.answer = 'foobar'
        self.guessed = {}

    def test_handle_guess_initial_wrong(self):
        # guess nothing and guess is wrong
        guess = 'd'
        output = game.handle_guess(guess, self.guessed, self.answer)
        self.assertNotIn(guess, self.answer)

    def test_handle_guess_initial_right(self):
        # guess nothing and guess is wrong
        guess = 'a'
        output = game.handle_guess(guess, self.guessed, self.answer)
        self.assertIn(guess, self.answer)

    def test_handle_guess_ultimate_right(self):
        # guess entire word except one character and guess is correct
        for letter in 'fooba':
            self.guessed[letter] = 1
        guess = 'r'
        output = game.handle_guess(guess, self.guessed, self.answer)
        # self.assertIn(guess, self.answer)

    def test_handle_guess_wrong_after_1(self):
        self.guessed['r'] = 1
        guess = 'd'
        output = game.handle_guess(guess, self.guessed, self.answer)
        self.assertEqual(output, 'Wrong!')

    def test_handle_guess_right_after_2(self):
        self.guessed['o'] = 1
        guess = 'r'
        output = game.handle_guess(guess, self.guessed, self.answer)
        self.assertEqual(output, 'Right!')

class ShowWordTestCase(unittest.TestCase):
    """Test for displaying the current state of progress towards answer."""
    def setUp(self):
        self.guessed = {}

    def test_show_word_after_correct_double(self):
        self.answer = 'mississippi'
        self.guessed['i'] = 1
        self.guessed['p'] = 1
        output = game.show_word(self.answer, self.guessed)
        self.assertEqual(output, '_i__i__ippi')

    def test_show_word_after_incorrect_guesses(self):
        self.answer = 'hi'
        incorrect_guesses = 'qzx'
        for letter in incorrect_guesses:
            self.guessed[letter] = 1
        output = game.show_word(self.answer, self.guessed)
        self.assertEqual(output, '--')

    def test_show_word_after_correct_double(self):
        self.answer = 'mississippi'
        guesses = 'misp'
        for guess in guesses:
            self.guessed[guess] = 1
        output = game.show_word(self.answer, self.guessed)
        self.assertEqual(output, 'mississippi')

class UserWinTestCase(unittest.TestCase):

    """Test for win outcome."""
    def setUp(self):
        self.guessed = {}
        self.answer = 'mississippi'

    def test_has_won_ultimate(self):
        guesses = 'misp'
        for guess in guesses:
            self.guessed[guess] = 1
        output = game.has_won(self.answer, self.guessed)
        self.assertTrue(output)

    def test_has_not_won_initial(self):
        output = game.has_won(self.answer, self.guessed)
        self.assertFalse(output)

    def test_show_welcome_simple_call(self):
        output = game.show_welcome()
        self.assertIsNotNone(output)

    def test_show_welcome_str_return(self):
        output = game.show_welcome()
        self.assertIsInstance(output, str)

if __name__ == '__main__':
    unittest.main()
