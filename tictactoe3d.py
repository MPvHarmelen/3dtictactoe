# Checklist of what we need to write:
#   - GUI
#       Simple Pygame crap? How is the 3D viewing going to
#       work? Any pretty animations involved?
#           No idea, I think the easiest we can do is the way we play
#           3dtictactoe on paper. I would like nice animations, but have
#           no idea of how we could make them...
#
#   - Data structure
#
#   - Smartass computer
#       Simple idea:
#         Computer calculates all possible moves, chooses
#         the one with the highest chance of winning.
#         Maybe multiple difficulties, with lower difficulties
#         picking the ones with lower chance of winning (or
#         even choosing at random).
#           This is not a simple idea, because you need to calculate
#           the winning chance of all possible moves.
#       Mayby not simple but still effective idea:
#         1: Check if computer can win, and do so if possible
#         2: Check if computer will lose, and prevent so if possible
#         3: Count how many squares of own are in each row, colum,
#            diagonal and other stuff (we need to think of names for
#            different things) and count how many squares of opponents
#            are in each blabla, and then play in the bla with the least
#            of opponent, but most of own.
#   - Rens' idea:
#       Track scores, like nr of wins/losses/draws
#         

# Coordinates will be tuples of (x,y,z)

# Board will be size*size*size
size = 3

class Computer(object):
    ''' An AI object with different difficulty levels. Creates a real challenge. '''
    def __init__(self, board, difficulty):
        self.board = board
        self.difficulty = difficulty

    def turn(self):
        ''' Should happen every time it's this cpu's turn. '''
        # TODO: Make it check every possible move and find
        # the one that suits its needs.
        #  Use function I described in the comment under CheckIfWon
        pass

from Board import Board


if __name__ == '__main__':
##    Done = False
##    while not Done:
        pass
