import os
import sys
from typing import List, Any, Optional
from utils import get_random_word

from termcolor import colored


# Debug mode.
DEBUG = os.getenv("DEBUG", False) == "True"


class Wordle:

    the_word: str  # This is the word to guess.
    factorial_word: List[str]
    word_length: int
    maximum_guesses: int = 6
    number_of_guesses: int = 1
    display_text: str = ""

    def __init__(self, the_word: Optional[str] = None) -> None:
        self.initialize(the_word=the_word)

    def initialize(self, the_word: Optional[str] = None) -> None:
        if the_word:
            # Set the world for testing purposes.
            self.the_word = the_word
        else:
            self.the_word = get_random_word()

        self.factorial_word = list(self.the_word)
        self.word_length = len(self.the_word)
        self.number_of_guesses = 1
        self.display_text = ""

        if DEBUG:
            print("DEBUG -- The word is: " + self.the_word)

    def start(self) -> None:
        print("Welcome to the game of Wordle!")
        print(
            f"You have {self.maximum_guesses} chances to guess a {self.word_length} letter word."
        )

        while self.number_of_guesses <= self.maximum_guesses:
            word: str = self.enter_word()

            if len(word) != self.word_length:
                print(f"Word must be {self.word_length} characters long")
            else:
                self.number_of_guesses += 1

                results = self.check(word)
                self.display_results(results)

                if self.is_won(word):
                    print("You won!")
                    self.play_again()

        print("You lost!")
        self.play_again()

    def play_again(self) -> None:
        if self.is_play_again():
            self.restart()
        else:
            self.end()

    def restart(self) -> None:
        self.initialize()
        self.start()

    def is_play_again(self) -> bool:
        answer: str = input("Do you want to play again? (y/n): ")
        if answer == "y":
            return True
        return False

    def end(self) -> None:
        sys.exit(0)

    def is_won(self, word: str) -> bool:
        if word == self.the_word:
            return True
        return False

    def enter_word(self) -> str:
        return input(f"Guess number {self.number_of_guesses}: ")

    def display_results(self, results: List[Any]) -> None:
        line: str = ""

        for result in results:
            letter: str = result["letter"].upper()
            if result["is_in_the_right_place"]:
                line += colored(letter, "green", attrs=["reverse"]) + " "
            elif result["is_in_the_word"]:
                line += colored(letter, "yellow") + " "
            else:
                line += colored(letter, "grey") + " "

        self.display_text += line + "\n"
        print(self.display_text)

    def check(self, word: str) -> List[dict[str, Any]]:
        factorial_word = list(word)
        results: List[dict[str, Any]] = []

        for index in range(0, len(factorial_word)):
            letter = factorial_word[index]
            meta = {
                "position": index,
                "letter": letter,
                "is_in_the_word": False,
                "is_in_the_right_place": False,
            }

            if letter in self.factorial_word:
                meta["is_in_the_word"] = True
                if letter == self.factorial_word[index]:
                    meta["is_in_the_right_place"] = True

            results.append(meta)

        return results
