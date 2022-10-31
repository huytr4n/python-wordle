import random
from typing import (
    List,
)


def get_random_word(number_of_character: int = 5) -> str:
    words: List[str] = []

    with open("words.txt", "r") as f:
        all_words: List[str] = f.readlines()

        for word in all_words:
            if len(word) == number_of_character + 1:
                words.append(word)

        return random.choice(words).strip()
