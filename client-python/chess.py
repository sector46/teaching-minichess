import random

##########################################################
"""
 ***** DATA REPRESENTATION *****
 Data Object:       Actual:
    01234            abcde

  0 kqbnr          6 kqbnr
  1 ppppp          5 ppppp
  2 .....          4 .....
  3 .....          3 .....
  4 PPPPP          2 PPPPP
  5 RNBQK          1 RNBQK
"""
##########################################################
class Board:
    def __init__(self):
        self.depth = 0
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

    def setPiece(self, row, col, piece):
        listRow = list(self.board[row])
        #self.board[row][col] = ()piece
#        print("Piece: {0}".format(piece))
#        print("ListRow before: {0}".format(listRow))
        listRow[col] = piece
#        print("ListRow after : {0}".format(listRow))
        self.board[row] = "".join(listRow)
        #self.board
    def movePiece(self, start_row, start_col, end_row, end_col):
        #start_row = abs(start_row - 6) #-=  1 #abs(start_row - 6)
        #start_col = start_col - 1 #-= 1 #start_col - 1
        #end_row = abs(end_row - 6) #-= 1 #abs(end_row - 6)
        #end_col = end_col - 1 #-= 1 #end_col - 1
#        print("{0}{1} {2}{3}").format(start_row, start_col, end_row, end_col)
#        print("row: {0}".format(self.board[start_row]))
        piece = self.board[start_row][start_col]
#        print piece
        if piece == "P" and end_row == 0:
            piece = "Q"
        elif piece == "p" and end_row == 5:
            piece = "q"
        self.setPiece(start_row, start_col, '.')
        self.setPiece(end_row, end_col, piece)
        if self.playerColor == "W":
            self.playerColor = "B"
        else: # self.playerColor == "B":
            self.playerColor = "W"
            self.depth += 1

class Piece_State:
    def __init__(self, piece, row, column):
        self.piece = piece
        self.row = row
        self.column = column
        self.moves = []

    def setPiece(self, piece):
        self.piece = piece
    def getPiece(self):
        return self.piece

    def getRowVal(self):
        return self.row

    def getColVal(self):
        return self.column

    def setMoves(self, moves):
        self.moves = moves
    def getMoves(self):
        return self.moves

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
    board_state = board.getBoard()
    score = 0
    KING_VAL   = 100
    QUEEN_VAL  = 25
    BISHOP_VAL = 15
    KNIGHT_VAL = 4
    ROOK_VAL   = 10
    PAWN_VAL   = 7

    for row in board_state:
        for piece in row:
            piece_val = score
            if piece.upper() == "K":
                if chess_isOwn(piece):
                    score += KING_VAL
                else:
                    score -= KING_VAL
            elif piece.upper() == "Q":
                if chess_isOwn(piece):
                    score += QUEEN_VAL
                else:
                    score -= QUEEN_VAL
            elif piece.upper() == "B":
                if chess_isOwn(piece):
                    score += BISHOP_VAL
                else:
                    score -= BISHOP_VAL
            elif piece.upper() == "N":
                if chess_isOwn(piece):
                    score += KNIGHT_VAL
                else:
                    score -= KNIGHT_VAL
            elif piece.upper() == "R":
                if chess_isOwn(piece):
                    score += ROOK_VAL
                else:
                    score -= ROOK_VAL
            elif piece.upper() == "P":
                if chess_isOwn(piece):
                    score += PAWN_VAL
                else:
                    score -= PAWN_VAL

#            piece_val = score - piece_val
#            print("{0}: {1}".format(piece, piece_val))
#        print("row: {0}".format(row))
#    print("total score: {0}".format(score))
    return score


def chess_moves():
    # with reference to the state of the game and return the possible moves - one example is given below - note that a move has exactly 6 characters
    
    strOut = []

    piece_states = []
    rowCnt = 0
    columnCnt = 0
    #"""
    curr_board = board.getBoard()
    print "Start!"
    for row in curr_board:
        columnCnt = 0
        print "row: {0}".format(row)
        for piece in row:
            print "piece: {0}".format(piece)
            if chess_isOwn(piece):
                piece_state = Piece_State(piece, rowCnt, columnCnt)
                piece_states.append(piece_state)
                print "grabbing piece: {0}".format(piece)
            columnCnt += 1
        rowCnt += 1
    end_moves = []

    for piece_state in piece_states:
        print "piece in piece states: {0}".format(piece_state.getPiece())
        print "starting position: [{0},{1}]".format(piece_state.getRowVal(),piece_state.getColVal())

    for piece_state in piece_states:
        #print "piece in piece states: {0}".format(piece_state.getPiece())
        new_piece_state = calculate_moves(piece_state)

        if new_piece_state is not None:
            #print "new piece state: piece = {0}, row,col = [{1},{2}]".format(new_piece_state.getPiece(),
            #                                                                 new_piece_state.getRowVal(),
            #                                                                 new_piece_state.getColVal())
            end_moves.append(new_piece_state)


    for state in end_moves:
        print state.getPiece()
        print "Start position: [{0},{1}]".format(state.getRowVal(), state.getColVal())
        print "Possible moves: {0}".format(state.getMoves())
    #print("End moves: {0}".format(end_moves))
    #"""
    # WRITE CONVERSION FROM ROW NUMBER TO ROW ALPHA CHARACTER
    
    strOut.append('a5-a4\n')
    strOut.append('b5-b4\n')
    strOut.append('c5-c4\n')
    strOut.append('d5-d4\n')
    strOut.append('e5-e4\n')
    strOut.append('b6-a4\n')
    strOut.append('b6-c4\n')



    print strOut
    return strOut


def chess_movesShuffled():
    # with reference to the state of the game, determine the possible moves and shuffle them before returning them- note that you can call the chess_moves() function in here
    
    return []


def chess_movesEvaluated():
    # with reference to the state of the game, determine the possible moves and sort them in order of an increasing evaluation score before returning them - note that you can call the chess_movesShuffled() function in here
    
    return []


def chess_move(strIn):
    # perform the supplied move (for example 'a5-a4\n') and update the state of the game / your internal variables accordingly - note that it advised to do a sanity check of the supplied move
    print("Before:")
    print strIn
    print chess_boardGet()
    start_col = strIn[0]
    start_col = change_str_to_num(start_col)
    print("start_col: {0}".format(start_col))
#    print start_col
    start_row = strIn[1]
    start_row = change_str_to_num(start_row)
    print("start_row: {0}".format(start_row))
    end_col = strIn[3]
#    print end_col
    end_col = change_str_to_num(end_col)
    print("end_col: {0}".format(end_col))
#    print end_col
    end_row = strIn[4]
    end_row = change_str_to_num(end_row)
    print("end_row: {0}".format(end_row))

    board.movePiece(start_row, start_col, end_row, end_col)
    print("After:")
    print chess_boardGet()
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

def change_str_to_num(str):
    # return a number that indicates the
    str = str.lower()
    if(str == 'a'):
        return 0
    elif(str == 'b'):
        return 1
    elif(str == 'c'):
        return 2
    elif(str == 'd'):
        return 3
    elif(str == 'e'):
        return 4
    elif(str == '1'):
        return 5
    elif(str == '2'):
        return 4
    elif(str == '3'):
        return 3
    elif(str == '4'):
        return 2
    elif(str == '5'):
        return 1
    elif(str == '6'):
        return 0
    return None

def change_num_to_str(num, toAlpha):
    if toAlpha:
        if num == 0:
            return 'f'
        elif num == 1:
            return 'e'
        elif num == 2:
            return 'd'
        elif num == 3:
            return 'c'
        elif num == 4:
            return 'b'
        elif num == 5:
            return 'a'
    else:
        if num == 0:
            return '1'
        elif num == 1:
            return '2'
        elif num == 2:
            return '3'
        elif num == 3:
            return '4'
        elif num == 4:
            return '5'
    return None

def calculate_moves(piece_state):
    # Constants contain the eigen vectors for each possible move
    KING_AND_QUEEN_MOVES  = [[1,0],[1,1],[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1]]
    BISHOP_MOVES          = [[1,1],[-1,1],[-1,-1],[1,-1]]
    KNIGHT_MOVES          = [[2,1],[1,2],[-1,2],[-2,1],[-2,-1],[-1,-2],[1,-2],[2,-1]]
    ROOK_MOVES            = [[1,0],[0,1],[-1,0],[0,-1]]
    PAWN_MOVES            = [[-1,0],[1,0]]

    moves = []
    piece = piece_state.getPiece()
    piece = piece.upper()
    startRow = piece_state.getRowVal()
    startCol = piece_state.getColVal()
    if piece == 'K':
        for poss_move in KING_AND_QUEEN_MOVES:
            endRow = startRow + poss_move[0]
            endCol = startCol + poss_move[1]
            if chess_isValid(endCol, endRow):
                #print "Valid"
                moves.append([endRow, endCol])
    elif piece == 'Q':
        for poss_move in KING_AND_QUEEN_MOVES:
            for i in range(1,6):
                endRow = startRow + (poss_move[0] * i)
                endCol = startCol + (poss_move[1] * i)
                if chess_isValid(endCol, endRow):
                    #print "Valid"
                    moves.append([endRow, endCol])
                else:
                    # Doesn't check further moves in this direction
                    break
    elif piece == 'B':
        for poss_move in BISHOP_MOVES:
            for i in range(1, 6):
                endRow = startRow + (poss_move[0] * i)
                endCol = startCol + (poss_move[1] * i)
                if chess_isValid(endCol, endRow):
                    #print "Valid"
                    moves.append([endRow, endCol])
                else:
                    # Doesn't check further moves in this direction
                    break
    elif piece == 'N':
        for poss_move in KNIGHT_MOVES:
            endRow = startRow + poss_move[0]
            endCol = startCol + poss_move[1]
            if chess_isValid(endCol, endRow):
                #print "Valid"
                moves.append([endRow, endCol])
    elif piece == 'R':
        for poss_move in ROOK_MOVES:
            print "rook poss_move: {0}".format(poss_move)
            for i in range(1, 6):
                endRow = startRow + (poss_move[0] * i)
                endCol = startCol + (poss_move[1] * i)
                print "rook end: [{0},{1}]".format(endRow, endCol)
                if chess_isValid(endCol, endRow):
                    #print "Valid"
                    moves.append([endRow, endCol])
                else:
                    # Doesn't check further moves in this direction
                    break
    elif piece == 'P':
        # If White: pawn moves upward
        if piece_state.getPiece().isupper():
            print "White pawn move: [{0},{1}]".format(PAWN_MOVES[0][0], PAWN_MOVES[0][1])
            endRow = startRow + PAWN_MOVES[0][0]
            endCol = startCol + PAWN_MOVES[0][1]
            if chess_isValid(endCol,endRow):
                #print "Valid"
                moves.append([endRow, endCol])
        # If Black: pawn moves downward
        else:
            print "Black pawn move: [{0},{1}]".format(PAWN_MOVES[1][0], PAWN_MOVES[1][1])
            endRow = startRow + PAWN_MOVES[1][0]
            endCol = startCol + PAWN_MOVES[1][1]
            if chess_isValid(endCol, endRow):
                #print "Valid"
                moves.append([endRow, endCol])
    if len(moves) == 0:
        piece_state.setMoves(None)
    else:
        piece_state.setMoves(moves)
        return piece_state
