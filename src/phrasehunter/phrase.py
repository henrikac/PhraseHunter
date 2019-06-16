from typing import List

from .character import Character


class Phrase:
    """Responsible for the state of the Phrase"""

    def __init__(self, phrase: List[Character]) -> None:
        self.phrase = phrase
        self.phrase_guessed = False

    def __str__(self) -> str:
        chars = [str(char) for char in self.phrase]
        return ''.join(chars)

    def __iter__(self) -> Character:
        yield from self.phrase

    def display_phrase(self):
        """Displays the phrase"""
        return ''.join([char.display_char() for char in self.phrase])

