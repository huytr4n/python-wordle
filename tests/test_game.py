from unittest import TestCase

from engine import Wordle


class WordleEngineTestSuite(TestCase):
    """
    Test the Wordle game engine.
    """

    def setUp(self) -> None:

        pass

    def test_wordle_default_configuration(self) -> None:

        wordle = Wordle()

        self.assertEqual(wordle.word_length, 5)
        self.assertEqual(wordle.maximum_guesses, 6)
        self.assertEqual(wordle.number_of_guesses, 1)
        self.assertEqual(wordle.display_text, "")
        self.assertEqual(len(wordle.the_word), 5)
        self.assertEqual(len(wordle.factorial_word), 5)

    def test_wordle_with_given_keyword(self) -> None:
        wordle = Wordle(the_word="apple")

        self.assertEqual(wordle.the_word, "apple")
        self.assertEqual(wordle.factorial_word, ["a", "p", "p", "l", "e"])

    def test_function_check_word(self) -> None:
        wordle = Wordle(the_word="apple")
        correct_results = [
            {
                "position": index,
                "letter": letter,
                "is_in_the_word": True,
                "is_in_the_right_place": True,
            }
            for index, letter in enumerate(list("apple"))
        ]
        incorrect_results = [
            {
                "position": index,
                "letter": letter,
                "is_in_the_word": False,
                "is_in_the_right_place": False,
            }
            for index, letter in enumerate(list("mommy"))
        ]
        mixed_results = [
            {
                "position": 0,
                "letter": "t",
                "is_in_the_word": False,
                "is_in_the_right_place": False,
            },
            {
                "position": 1,
                "letter": "a",
                "is_in_the_word": True,
                "is_in_the_right_place": False,
            },
            {
                "position": 2,
                "letter": "b",
                "is_in_the_word": False,
                "is_in_the_right_place": False,
            },
            {
                "position": 3,
                "letter": "l",
                "is_in_the_word": True,
                "is_in_the_right_place": True,
            },
            {
                "position": 4,
                "letter": "e",
                "is_in_the_word": True,
                "is_in_the_right_place": True,
            },
        ]

        self.assertEqual(wordle.check("apple"), correct_results)
        self.assertEqual(wordle.check("mommy"), incorrect_results)
        self.assertEqual(wordle.check("table"), mixed_results)

    def test_is_won(self) -> None:
        wordle = Wordle(the_word="apple")

        self.assertTrue(wordle.is_won("apple"))
        self.assertFalse(wordle.is_won("table"))
