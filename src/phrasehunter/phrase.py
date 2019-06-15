from typing import List

from character import Character


class Phrase:
    """Responsible for the state of the Phrase"""

    def __init__(self, phrase: List[Character]) -> None:
        self.phrase = phrase
        self.phrase_guessed = False

