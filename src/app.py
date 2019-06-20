from typing import List

from phrasehunter.character import Character
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase


def create_phrases() -> List[Phrase]:
    """Creates a list of phrases"""
    phrases: List[Phrase] = []
    str_phrases = [
        'H3llo',
        'Cowboy',
        'Christmas',
        'Santa Claus',
        'Univers'
    ]

    for phrase in str_phrases:
        try:
            chars = [Character(char) for char in phrase]
        except ValueError as err:
            print(f'\nError: {err}\n')
        else:
            phrases.append(Phrase(chars))

    return phrases


if __name__ == '__main__':
    phrases = create_phrases()
    game = Game(phrases)
    game.play()

