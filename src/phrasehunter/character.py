class Character:
    """Responsible for holding the state of a given character"""

    def __init__(self, char: str) -> None:
        self.char = char
        self.was_guessed = False

    def guess(self, char: str) -> bool:
        """Checks if char is equal to self.char"""
        if self.char == char:
            self.was_guessed = True

        return self.was_guessed

    def get_char(self) -> str:
        """Gets self.char if has been guessed, _ otherwise"""
        return self.char if self.was_guessed else '_'

    def __str__(self) -> str:
        return self.char

