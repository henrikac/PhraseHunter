class Character:
    """Responsible for holding the state of a given character"""

    def __init__(self, char: str) -> None:
        self.check_if_valid_char(char)
        self.char = char
        self.was_guessed = False

    def check_if_valid_char(self, char: str) -> None:
        """Checks if char is a character"""
        if len(char) != 1:
            raise ValueError('Invalid input: Please enter a single character')
        elif not char.isalpha():
            raise ValueError('Invalid input: Please enter a character')

    def guess(self, char: str) -> None:
        """Checks if char is equal to self.char"""
        self.check_if_valid_char(char)

        if self.char == char:
            self.was_guessed = True

    def display_char(self) -> str:
        """Displays self.char if has been guessed, _ otherwise"""
        return self.char if self.was_guessed else '_'

    def __str__(self) -> str:
        return self.char

