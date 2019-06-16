from typing import List

from phrasehunter.character import Character
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase


def create_phrases() -> List[Phrase]:
    """Creates a list of phrases"""
    phrases: List[Phrase] = []
    str_phrases = [
        'hello',
        'cowboy',
        'christmas',
        'tomato',
        'univers'
    ]

    for phrase in str_phrases:
        chars = [Character(char) for char in phrase]
        phrases.append(Phrase(chars))

    return phrases


if __name__ == '__main__':
    phrases = create_phrases()
    game = Game(phrases)
    game.play()

# Inside Dunder Main:
## Create an instance of your Game class
## Start your game by calling the instance method that starts the game loop
