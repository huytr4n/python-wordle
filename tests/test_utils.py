from unittest import TestCase

from utils import get_random_word


class TestRandomWord(TestCase):
    def test_random_word(self):
        self.assertEqual(len(get_random_word()), 5)
