class Board(object):
    '''This is the object that represents the board.'''
    def __init__(self, size, amount_players):
        self.board = {}
        self.size = size
        for x in range(size):
            for y in range(size):
                for z in range(size):
                    self.board[(x,y,z)]=None

    def getCoord(self, coords):
        return self.board[coords]

    def setCoord(self, coords, value):
        for x in coords:
            if x > self.size-1:
                return False
        # We are defining this out of scope, will it work?
        self.board[coords] = value
        return True

    def CheckIfWon(self):
        # TODO: Think of a good way to check if someone has
        # won without any kind of limit to the board size.
        # Just using lines would be quite hard, since there's
        # multiple diagonals when you have a larger board.
        #  I think lines would be okay. We just need to edit the
        #  function below to stand up to (is this correct EN?) our needs
        #  of a 3D game. We also need to think of names for things like
        #  collumns and rows that are in different angles. I think that
        #  last is best to be discussed in real life =).
        pass
    def BoardToLines(self):
            # If we use yield, we can only call it once. I'm not sure if you
            # know about generators, but if you do:
            # yield generates a generator =)
            size = self.size
            # (0,0,line) >> (size,size,line)
            for x in range(size):
                for y in range(size):
                    yield [self.getCoord((x,y,z)) for z in range(size)]

            # (0,line,0) >> (size,line,size)
            for x in range(size):
                for z in range(size):
                    yield [self.getCoord((x,y,z)) for y in range(size)]
                    

##            # (line,0,0) >> (line,size,size)
##            for y in range(size):
##                for z in range(size):
##                    self.lines.append(
            
            
            

##def board_to_lines():
##    lines = []
##
##    # Rows
##    for y_co in range(gridsize):
##        lines.append([])
##        for x_co in range(gridsize):
##            lines[y_co].append(return_cell((x_co,y_co)))
##    
##    # Columns
##    for x_co in range(gridsize):
##        lines.append([])
##        for y_co in range(gridsize):
##            lines[gridsize + x_co].append(return_cell((x_co,y_co)))
##
##    # 1st diagonal
##    lines.append([])
##    for co in range(gridsize):
##        lines[gridsize*2].append(return_cell((co,co)))
##    
##    # 2nd diagonal
##    lines.append([])
##    for co in range(gridsize):
##        lines[gridsize*2 +1].append(return_cell((co,(gridsize-1)-co)))
##
##    return lines

if __name__ == '__main__':
    board = Board(3,3)
    lala = board.BoardToLines()
    for i in lala: print(i)
