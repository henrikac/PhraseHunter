class Character:
    """Responsible for holding the state of a given character"""

    def __init__(self, char: str) -> None:
        self.char = char
        self.was_guessed = True if char == ' ' else False

    def guess(self, char: str) -> bool:
        """Checks if char is equal to self.char"""
        if self.char == char and self.was_guessed:
            raise ValueError(f'{char} har already been guessed')

        if self.char == char:
            self.was_guessed = True
            return True

        return False

    def display_char(self) -> None:
        """Prints self.char if has been guessed, _ otherwise"""
        print(self.char if self.was_guessed else '_', end=' ')

    def get_char(self) -> str:
        """Get self.char if has been guessed, _ otherwise"""
        return self.char if self.was_guessed else '_'

    def __str__(self) -> str:
        return self.char

