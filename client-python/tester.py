import re

import chess

def main():
    #board = chess.Board()

    user_input = ''
    while(user_input != 'q' and user_input != 'quit'):
        print("Waiting for command...")
        user_input = raw_input().lower()

        if user_input == 's' or user_input == 'set':
            set_board()
        elif user_input == 'p' or user_input == 'print':
            print_board()
        elif user_input == 'r' or user_input == 'reset':
            reset_board()
        elif user_input == 'u' or user_input == 'undo':
            undo_move()
        elif user_input == 'us' or user_input == 'undos':
            undo_moves()
        elif user_input == 'm' or user_input == 'move':
            move()
        elif user_input == 'ms' or user_input == 'moves':
            moves()
        elif user_input == 'h' or user_input == 'help':
            print_help()

def set_board():
    chess.chess_reset()
    board_str = ''
    print "Enter depth (23): "
    depth = raw_input()
    try:
        depth = int(depth)
        if not depth < 41:
            raise Exception
    except:
        print "not a valid number"
        return False
    board_str += str(depth) + ' '

    print "Enter player color (w/b): "
    color = raw_input().lower()
    if color != 'w' and color != 'b':
        print "Not a valid player color"
        return False
    board_str += color.upper() + "\n"

    print "Enter row 1 (PPPPP): "
    row = raw_input()
    if len(row) < 5:
        print "Invalid row (Too few characters)"
        return False
    elif len(row) > 5:
        print "Invalid row (Too many characters)"
        return False
    if not re.match('[.pPkKqQbBnNrR]', row):
        print "Not a valid row"
        return False
    board_str += row + "\n"

    print "Enter row 2 (PPPPP): "
    row = raw_input()
    if len(row) < 5:
        print "Invalid row (Too few characters)"
        return False
    elif len(row) > 5:
        print "Invalid row (Too many characters)"
        return False
    if not re.match('[.pPkKqQbBnNrR]', row):
        print "Not a valid row"
        return False
    board_str += row + "\n"

    print "Enter row 3 (PPPPP): "
    row = raw_input()
    if len(row) < 5:
        print "Invalid row (Too few characters)"
        return False
    elif len(row) > 5:
        print "Invalid row (Too many characters)"
        return False
    if not re.match('[.pPkKqQbBnNrR]', row):
        print "Not a valid row"
        return False
    board_str += row + "\n"

    print "Enter row 4 (PPPPP): "
    row = raw_input()
    if len(row) < 5:
        print "Invalid row (Too few characters)"
        return False
    elif len(row) > 5:
        print "Invalid row (Too many characters)"
        return False
    if not re.match('[.pPkKqQbBnNrR]', row):
        print "Not a valid row"
        return False
    board_str += row + "\n"

    print "Enter row 5 (PPPPP): "
    row = raw_input()
    if len(row) < 5:
        print "Invalid row (Too few characters)"
        return False
    elif len(row) > 5:
        print "Invalid row (Too many characters)"
        return False
    if not re.match('[.pPkKqQbBnNrR]', row):
        print "Not a valid row"
        return False
    board_str += row + "\n"

    print "Enter row 6 (PPPPP): "
    row = raw_input()
    if len(row) < 5:
        print "Invalid row (Too few characters)"
        return False
    elif len(row) > 5:
        print "Invalid row (Too many characters)"
        return False
    if not re.match('[.pPkKqQbBnNrR]', row):
        print "Not a valid row"
        return False
    board_str += row + "\n"

    chess.chess_boardSet(board_str)

def print_board():
    print chess.chess_boardGet()
    #print "print board"

def reset_board():
    chess.chess_reset()
    print "Board reset"

def undo_move():
    chess.chess_undo()
    print "Undid move"

def undo_moves():
    print "Enter the number of moves you want to undo: "
    num_of_moves = raw_input()
    if not re.match('[0-9]+',num_of_moves):
        print "Not a valid number"
        return False
    else:
        num_of_moves = int(num_of_moves)
        for i in range(1, num_of_moves):
            chess.chess_undo()

def move():
    print "Enter move: "
    move = raw_input()
    if len(move) < 7:
        print "Invalid move (Too few characters)"
        return False
    elif len(move) > 7:
        print "Invalid move (Too many characters)"
        return False
    if re.match('[a-e][1-6]-[a-e][1-6]\\\\n', move):
        chess.chess_move(move)
        return True
    else:
        print "Invalid move (Wrong format)"
        return False

def moves():
    print "Enter moves: "
    move = raw_input()
    if (len(move)%7) > 0:
        print "Invalid move (Wrong number of characters)"
        return False
    moves = re.split('([a-e][1-6]-[a-e][1-6]\\\\n)', move)

    for mv in moves:
        if not re.match('[a-e][1-6]-[a-e][1-6]\\\\n', mv):
            if not mv:
                moves.remove(mv)
            else:
                print "Invalid moves (Wrong format)"
                return False
    #print moves
    for mv in moves:
        chess.chess_move(mv)
    return True

def print_help():
    print "Type 'h' or 'help' to get this dialog."
    print "Type 'q' or 'quit' to exit the application."
    print "Type 's' or 'set' to set the board."
    print "Type 'p' or 'print' to print the current board state."
    print "Type 'r' or 'reset' to reset the board to a start state."
    print "Type 'u' or 'undo' to undo a move"
    print "Type 'us' or 'undos' to undo a specified number of moves"
    print "Type 'm' or 'move' to move a piece."
    print "Type 'ms' or 'moves' to input a series of moves."

if __name__ == "__main__":
    main()