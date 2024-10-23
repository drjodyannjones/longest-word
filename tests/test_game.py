# tests/test_game.py
from longest_word.game import Game
import string

class TestGame:
    def test_game_initialization(self):
        # setup
        new_game = Game()

        # exercise
        grid = new_game.grid

        # verify
        assert len(grid) == 9
        assert isinstance(grid, list)
        for letter in grid:
            assert letter in string.ascii_uppercase

        # teardown

    def test_empty_word_is_invalid(word: str) -> bool:

        # setup
        new_game = Game()


        # exercise


        # verify
        assert new_game.is_valid('') is False

        # teardown




    def test_is_valid(word: str) -> bool:

        # setup
        new_game = Game()
        test_grid = 'FDRETNALI'
        test_word = 'INFLATED'

        # exercise
        new_game.grid = list(test_grid)

        # verify
        assert new_game.is_valid(test_word) is True

        # teardown
        assert new_game.grid == list(test_grid)

    def test_is_invalid(word: str) -> bool:

        # setup
        new_game = Game()
        test_grid = 'FDRETNALI'
        test_word = 'INFLATION'

        # exercise
        new_game.grid = list(test_grid)

        # verify
        assert new_game.is_valid(test_word) is False

        # teardown
        assert new_game.grid == list(test_grid)
