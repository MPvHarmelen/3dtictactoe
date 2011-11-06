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

# Data functions
def change_value(coordinates,value,game_space):
    game_space = None
    return game_space

def return_value(coordinates):
    value = None
    return value

def Main():
    Done = False
    while not Done:
        pass
