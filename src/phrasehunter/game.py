import os
from random import randint
from typing import List

from .phrase import Phrase


class Game:
    """Responsible for the state of the Game"""

    def __init__(self, phrases: List[Phrase]) -> None:
        if len(phrases) < 1:
            raise ValueError('At least 1 phrase is required')

        self.phrases = phrases
        self.active_phrase = self.__get_random_phrase()
        self.remaining_tries = 5

    def __get_random_phrase(self) -> Phrase:
        """Gets a random phrase"""
        idx = randint(0, len(self.phrases) - 1)
        return self.phrases[idx]

    def __clear_screen(self) -> None:
        """Clears the screen"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def __prompt_player(self) -> str:
        """Prompts the player for a character"""
        while True:
            guess = input('Enter a character: ')

            if len(guess) != 1 or not guess.isalpha():
                print('Please enter a single character')
            else:
                return guess

    def play(self) -> None:
        """Starts the game"""
        self.__clear_screen()
        print('=' * 12)
        print('PHRASEHUNTER')
        print('=' * 12, end='\n\n')

        phrase = self.active_phrase.get_phrase()
        while '_' in phrase and self.remaining_tries:

            self.active_phrase.display_phrase()
            print(f'\n\nYou have {self.remaining_tries} {"life" if self.remaining_tries < 2 else "lives"} left\n')

            user_input = self.__prompt_player()
            print()

            correct_guess = False
            for char in self.active_phrase:
                try:
                    guess = char.guess(user_input)
                except ValueError as err:
                    print(f'{err}')
                    correct_guess = True
                    break
                else:
                    if guess:
                        correct_guess = True

            if not correct_guess:
                self.remaining_tries -= 1

            phrase = self.active_phrase.get_phrase()

