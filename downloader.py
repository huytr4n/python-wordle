import os
import requests


WORD_SITE_URL = "https://www.mit.edu/~ecprice/wordlist.10000"


def download_word_site() -> None:
    """
    Download the word list from the MIT site.
    """
    if not os.path.exists("words.txt"):
        response = requests.get(WORD_SITE_URL)
        with open("words.txt", "wb") as f:
            f.write(response.content)


if __name__ == "__main__":
    download_word_site()
