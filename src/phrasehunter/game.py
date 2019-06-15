from random import randint
from typing import List

from phrase import Phrase


class Game:
    """Responsible for the state of the Game"""

    def __init__(self, phrases: List[Phrase]) -> None:
        if len(phrases) < 1:
            raise ValueError('At least 1 phrase is required')

        self.phrases = phrases
        self.active_phrase = self.__get_random_phrase()

    def __get_random_phrase(self) -> Phrase:
        """Gets a random phrase"""
        idx = randint(0, len(self.phrases) - 1)
        return self.phrases[idx]

