
import random
import string
import requests

class Game:
    def __init__(self) -> list:
        """Attribute a random grid to size 9"""
        self.grid = []

        for _ in range(9):
            self.grid.append(random.choice(string.ascii_uppercase))


    def is_valid(self, word: str) -> bool:

        """Return True if and only if the word is valid, given the Game's grid"""

        if not word:
            return False

        # Create a copy of grid
        letters = self.grid.copy() # create a duplicate of self.grid


        letters = list(letters)


        for letter in word:
            if letter in letters:
                letters.remove(letter)
            else:
                return False
        else:
            return self.__check_dictionary(word)


    @staticmethod
    def __check_dictionary(word):
        response = requests.get(f"https://dictionary.lewagon.com/{word}")
        json_response = response.json()
        return json_response['found']








# Example implementation
# game = Game()
# print(game.grid) # --> OQUWRBAZE
# my_word = "BAROQUE"
# game.is_valid(my_word) # --> True
