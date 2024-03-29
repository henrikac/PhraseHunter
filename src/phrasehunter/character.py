class Character:
    """Responsible for holding the state of a given character"""

    def __init__(self, char: str) -> None:
        if not self.__valid_char(char):
            raise ValueError('Please enter a character')

        self.char = char
        self.was_guessed = True if char == ' ' else False

    def __str__(self) -> str:
        return self.char

    def __valid_char(self, char: str) -> bool:
        """Checks if valid character"""
        if char.isdigit():
            raise ValueError('Characters can\'t be numbers')

        return char.isalpha() or char.isspace()

    @property
    def character(self) -> str:
        """Get self.char if has been guessed, _ otherwise"""
        return self.char if self.was_guessed else '_'

    def guess(self, char: str) -> bool:
        """Checks if char is equal to self.char"""
        equal_char = self.char.lower() == char.lower()

        if equal_char and self.was_guessed:
            raise ValueError(f'{char} har already been guessed')

        if equal_char:
            self.was_guessed = True
            return True

        return False

    def display_char(self) -> None:
        """Prints self.char if has been guessed, _ otherwise"""
        print(self.char if self.was_guessed else '_', end=' ')

    def reset(self) -> None:
        """Sets a Character back to 'not guessed'"""
        self.was_guessed = False

