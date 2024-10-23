
import random
import string

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []

        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:
        """Return True if and only if the word is valid, given the Game's grid"""
        pass # TODO


# Example implementation
# game = Game()
# print(game.grid) # --> OQUWRBAZE
# my_word = "BAROQUE"
# game.is_valid(my_word) # --> True
