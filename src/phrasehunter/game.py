import os
from random import randint
from typing import List

from .phrase import Phrase


class Game:
    """Responsible for the state of the Game"""

    def __init__(self, phrases: List[Phrase]) -> None:
        if len(phrases) < 5:
            raise ValueError('At least 5 phrases is required')

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

            if len(guess) != 1:
                print('Please enter a single character')
            elif not guess.isalpha():
                print('Invalid guess: Please enter a character')
            else:
                return guess.lower()

    def __correct_guess(self, char_guess: str) -> bool:
        """Checks if user guess is correct or not"""
        correct_guess = False
        for char in self.active_phrase:
            try:
                guess = char.guess(char_guess)
            except ValueError as err:
                print(f'{err}\n')
                correct_guess = True
                break
            else:
                if guess:
                    correct_guess = True
        return correct_guess

    def __display_victory(self) -> None:
        """Lets the player know that he/she won"""
        self.__clear_screen()
        print('=' * 8)
        print('VICTORY!')
        print('=' * 8, end='\n\n')
        print('You guessed the phrase!')
        print(f'Phrase: {self.active_phrase.get_phrase()}')
        print(f'Lives remaining: {self.remaining_tries}\n')

    def __display_failure(self) -> None:
        """Lets the player know that he/she failed to guess the phrase"""
        self.__clear_screen()
        print('=' * 7)
        print('BUMMER!')
        print('=' * 7, end='\n\n')
        print('You didn\'t manage to guess the phrase!')
        print(f'The phrase was: {str(self.active_phrase)}\n')

    def __play_again(self) -> bool:
        """Prompts the user if he/she wants to play again"""
        user_input = input('Do you want to play again [Y/N]? ')
        return user_input.lower() == 'y'

    def __restart_game(self) -> None:
        """Restarts the game"""
        self.active_phrase.reset_phrase()
        self.active_phrase = self.__get_random_phrase()
        self.remaining_tries = 5

    def play(self) -> None:
        """Starts the game"""
        self.__clear_screen()
        print('=' * 12)
        print('PHRASEHUNTER')
        print('=' * 12, end='\n\n')

        while not self.active_phrase.been_guessed() and self.remaining_tries:

            self.active_phrase.display_phrase()
            print(f'\n\nYou have {self.remaining_tries} {"life" if self.remaining_tries < 2 else "lives"} left\n')

            user_input = self.__prompt_player()
            print()

            if not self.__correct_guess(user_input):
                self.remaining_tries -= 1

            if self.active_phrase.been_guessed():
                self.__display_victory()

                if self.__play_again():
                    self.__restart_game()
            elif self.remaining_tries == 0:
                self.__display_failure()

                if self.__play_again():
                    self.__restart_game()

        print('\nHope to see again soon! :-)\n')

