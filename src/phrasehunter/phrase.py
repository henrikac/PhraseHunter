from typing import Generator, List

from .character import Character


class Phrase:
    """Responsible for the state of the Phrase"""

    def __init__(self, phrase: List[Character]) -> None:
        if len(phrase) < 1:
            raise ValueError('A phrase must contain at least 1 character')

        self.phrase = phrase

    def __str__(self) -> str:
        return ''.join([str(char) for char in self.phrase])

    def __iter__(self) -> Generator:
        yield from self.phrase

    def get_phrase(self) -> str:
        """Gets the phrase"""
        return ''.join([char.character for char in self.phrase])

    def display_phrase(self) -> None:
        """Displays the phrase"""
        for char in self.phrase:
            char.display_char()

    def been_guessed(self) -> bool:
        """Checks if the phrase has been guessed"""
        chars = ''.join([char.character for char in self.phrase])
        return '_' not in chars

    def reset_phrase(self) -> None:
        """Resets a phrase back to all _"""
        for char in self.phrase:
            char.reset()

