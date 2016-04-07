import random

##########################################################

class Board:
    def __init__(self):
        self.depth = 1
        self.playerColor = 'W'
        self.board = []

        self.board.append('kqbnr')
        self.board.append('ppppp')
        self.board.append('.....')
        self.board.append('.....')
        self.board.append('PPPPP')
        self.board.append('RNBQK')

    def setDepth(self, depth):
        self.depth = int(depth)
    def getDepth(self):
        return self.depth
    def getDepthStr(self):
        return str(self.depth)

    def setPlayerColor(self, playerColor):
        self.playerColor = playerColor
    def getPlayerColor(self):
        return self.playerColor

    def setBoard(self, board):
        self.board = board
    def getBoard(self):
        return self.board
    def getBoardRow(self, rowNum):
        return self.board[rowNum]

##########################################################
#                 V A R I A B L E S                      #
##########################################################

board = Board()

##########################################################
#              E N D   V A R I A B L E S                 #
##########################################################

def chess_reset():
    # reset the state of the game / your internal variables - note that this function is highly dependent on your implementation
    board.setDepth(1)
    board.setPlayerColor('W')
    resetBoard = []
    resetBoard.append('kqbnr')
    resetBoard.append('ppppp')
    resetBoard.append('.....')
    resetBoard.append('.....')
    resetBoard.append('PPPPP')
    resetBoard.append('RNBQK')

    board.setBoard(resetBoard)
    #print 'Board has been reset!'
    return

def chess_boardGet():
    # return the state of the game - one example is given below - note that the state has exactly 40 or 41 characters
    '''
    strOut += '1 W\n'
    strOut += 'kqbnr\n'
    strOut += 'ppppp\n'
    strOut += '.....\n'
    strOut += '.....\n'
    strOut += 'PPPPP\n'
    strOut += 'RNBQK\n'
    '''
    strOut = ''

    strOut += board.getDepthStr() + ' ' + board.getPlayerColor() + '\n'
    strOut += board.getBoardRow(0) + '\n'
    strOut += board.getBoardRow(1) + '\n'
    strOut += board.getBoardRow(2) + '\n'
    strOut += board.getBoardRow(3) + '\n'
    strOut += board.getBoardRow(4) + '\n'
    strOut += board.getBoardRow(5) + '\n'

    # debug statement
    #print strOut
    return strOut


def chess_boardSet(strIn):
    # read the state of the game from the provided argument and set your internal variables accordingly - note that the state has exactly 40 or 41 characters
    #print strIn
    strIn = strIn.splitlines()
    initialInfo = strIn[0]
    initialInfo = initialInfo.split()
    #print 'initialInfo = {0}'.format(initialInfo)
    #print 'initialInfo[0] = {0}'.format(initialInfo[0])
    board.setDepth(initialInfo[0])
    board.setPlayerColor(initialInfo[1])
    newBoard = []
    newBoard.append(strIn[1])
    newBoard.append(strIn[2])
    newBoard.append(strIn[3])
    newBoard.append(strIn[4])
    newBoard.append(strIn[5])
    newBoard.append(strIn[6])
    board.setBoard(newBoard)
    return


def chess_winner():
    # determine the winner of the current state of the game and return '?' or '=' or 'W' or 'B' - note that we are returning a character and not a string

    currBoard = board.getBoard()
    bKingAlive = False
    wKingAlive = False
    for row in currBoard:
        if 'K' in row:
            wKingAlive = True
        if 'k' in row:
            bKingAlive = True

    #print board.getDepth()

    if not wKingAlive:
        #print 'Black Wins!'
        return 'B'
    elif not bKingAlive:
        #print 'White Wins!'
        return 'W'
    if 40 < board.getDepth():
        # print 'Draw!'
        return '='
    else:
        #print 'Game not over'
        return '?'


def chess_isValid(intX, intY):
    if intX < 0:
        return False
        
    elif intX > 4:
        return False
    
    if intY < 0:
        return False
        
    elif intY > 5:
        return False
    
    return True


def chess_isEnemy(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side not on move - note that we could but should not use the other is() functions in here but probably
    #print strPiece
    if strPiece == '.':
        return False
    elif strPiece.isupper():
        if board.getPlayerColor() == 'W':
            return False
        else:
            return True
    elif strPiece.islower():
        if board.getPlayerColor() == 'W':
            return True
        else:
            return False
    else:
        return False


def chess_isOwn(strPiece):
    # with reference to the state of the game, return whether the provided argument is a piece from the side on move - note that we could but should not use the other is() functions in here but probably
    #print strPiece
    if strPiece == '.':
        return False
    elif strPiece.isupper():
        if board.getPlayerColor() == 'W':
            return True
        else:
            return False
    elif strPiece.islower():
        if board.getPlayerColor() == 'W':
            return False
        else:
            return True
    else:
        return False


def chess_isNothing(strPiece):
    # return whether the provided argument is not a piece / is an empty field - note that we could but should not use the other is() functions in here but probably
    #print strPiece
    if strPiece == '.':
        return True
    else:
        return False


def chess_eval():
    # with reference to the state of the game, return the the evaluation score of the side on move - note that positive means an advantage while negative means a disadvantage
    
    return 0


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
    
    strOut = []
    
    strOut.append('a5-a4\n')
    strOut.append('b5-b4\n')
    strOut.append('c5-c4\n')
    strOut.append('d5-d4\n')
    strOut.append('e5-e4\n')
    strOut.append('b6-a4\n')
    strOut.append('b6-c4\n')
    
    return strOut


def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
    
    return []


def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_moves() function in here
    
    return []


def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move
    
    pass


def chess_moveRandom():
    # perform a random move and return it - one example output is given below - note that you can call the chess_movesShuffled() function as well as the chess_move() function in here
    
    return 'c5-c4\n'


def chess_moveGreedy():
    # perform a greedy move and return it - one example output is given below - note that you can call the chess_movesEvaluated() function as well as the chess_move() function in here
    
    return 'c5-c4\n'


def chess_moveNegamax(intDepth, intDuration):
    # perform a negamax move and return it - one example output is given below - note that you can call the the other functions in here
    
    return 'c5-c4\n'


def chess_moveAlphabeta(intDepth, intDuration):
    # perform a alphabeta move and return it - one example output is given below - note that you can call the the other functions in here
    
    return 'c5-c4\n'


def chess_undo():
    # undo the last move and update the state of the game / your internal variables accordingly - note that you need to maintain an internal variable that keeps track of the previous history for this
    
    pass
