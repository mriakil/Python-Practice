import math
import random

class Player:
    def __init__(self,letter):
        # letter is x or o
        self.letter = letter

    # we want all players to get their next move given a game
    def get_move(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self,game):
        square = random.choice(game.available_move())
        return square

class HumanPlayer(Player):
    def __init__(self,letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-9):')
            # we are going to check that this is a correct value by trying to cast
            # if to an integer , and if it's not,then we say it's invalid
            # if that spot is not availableon the board, we also say its invalid
        try:
            val = input(square)
            if val not in game.available_move():
                raise ValueError
            valid_square = True # if these  are successful, then yay
        except ValueError:
            print("Invalid square. Try again.")

        return val