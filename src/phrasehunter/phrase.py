from typing import Generator, List

from .character import Character


class Phrase:
    """Responsible for the state of the Phrase"""

    def __init__(self, phrase: List[Character]) -> None:
        self.phrase = phrase
        self.phrase_guessed = False

    def __str__(self) -> str:
        chars = [str(char) for char in self.phrase]
        return ''.join(chars)

    def __iter__(self) -> Generator:
        yield from self.phrase

    def display_phrase(self):
        """Displays the phrase"""
        for char in self.phrase:
            char.display_char()

    def get_phrase(self):
        return ''.join([char.get_char() for char in self.phrase])

