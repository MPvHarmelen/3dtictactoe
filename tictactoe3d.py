# Checklist of what we need to write:
#   - GUI
#       Simple Pygame crap? How is the 3D viewing going to
#       work? Any pretty animations involved?
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
        ''' Should happen every time it's this guy's turn. '''
        # TODO: Make it check every possible move and find
        # the one that suits its needs.
        pass

class Board(object):
    def __init__(self, size, amount_players):
        self.board = {}
        self.size = size

    def getCoord(self, coords):
        return self.board[coords]

    def setCoord(self, coords, value):
        for x in coords:
            if x > self.size-1:
                return False
        self.board[coords] = value
        return True

    def checkIfWon(self):
        # TODO: Think of a good way to check if someone has
        # won without any kind of limit to the board size.
        # Just using lines would be quite hard, since there's
        # multiple diagonals when you have a larger board.
        pass

if __name__ == '__main__':
    Done = False
    while not Done:
        pass

