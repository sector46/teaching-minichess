import re

import time

import chess

def main():
    #board = chess.Board()
    chess.chess_reset()

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
        elif user_input == 'rm' or user_input == 'random_move':
            random_move()
        elif user_input == 'tm' or user_input == 'tournament_move':
            tournament_move()
        elif user_input == 'am' or user_input == 'alphabeta_move':
            alphabeta_move()
        elif user_input == 'gh' or user_input == 'get_history':
            get_history()
        elif user_input == 'pa' or user_input == 'play_alphabeta':
            play_alphabeta()
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

def random_move():
    move = chess.chess_moveRandom()
    print "Move: {}".format(move)
    print_board()
    return True

def alphabeta_move():
    print "Enter time restriction: "
    input_time = raw_input()
    if not input_time.isdigit():
        print "Invalid time: not a number"
        return False
    input_time = int(input_time)
    if input_time < 0:
        print "Invalid time: less than 0"
        return False
    move = chess.chess_moveAlphabeta(6, input_time)
    print "Move: {}".format(move)
    print_board()
    return True

def tournament_move():
    print "Enter time restriction: "
    input_time = raw_input()
    if not input_time.isdigit():
        print "Invalid time: not a number"
        return False
    input_time = int(input_time)
    if input_time < 0:
        print "Invalid time: less than 0"
        return False
    move = chess.chess_moveAlphabeta(-1, input_time)
    print "Move: {}".format(move)
    print_board()
    return True

def get_history():
    history = chess.getHistory()
    history_len = len(history)
    if history_len == 0:
        print "There are no entries in the history list."
        return True
    print "Enter the number of entries to see (max is {}: ".format(history_len)
    entry_num = raw_input()
    if not entry_num.isdigit():
        print "Invalid input: not a number"
        return False
    entry_num = int(entry_num)
    if entry_num < 0:
        print "Invalid input: less than 0"
        return False
    if history_len < entry_num:
        print "Invalid input: greater than number of entries available"
        return False
    start_point = history_len - entry_num
    for i in range(start_point, history_len):
        print "{0}) {1}".format(i, history[i])
    return True

def play_alphabeta():
    print "Total starting time per side: 300000"
    white_time = 300000
    black_time = 300000
    player = ''

    while True:
        check_winner = chess.chess_winner()
        if check_winner == 'B':
            print "Black wins!"
            break
        elif check_winner == 'W':
            print "White wins!"
            break
        elif check_winner == '=':
            print "Draw!"
            break
        else:
            board = chess.chess_boardGet()
            print board
            if board[1] == ' ':
                player = board[2]
            else:
                player = board[3]
            move = ''
            if player == 'B':
                print "PERFORMING BLACK MOVE..."
                print "Black time left: {}".format(black_time)
                start_time = time.time()
                move = chess.chess_moveAlphabeta(-1, black_time)
                end_time = time.time()
                black_time = black_time - (end_time - start_time)
            else:
                print "PERFORMING WHITE MOVE..."
                print "White time left: {}".format(white_time)
                start_time = time.time()
                move = chess.chess_moveAlphabeta(-1, white_time)
                end_time = time.time()
                white_time = white_time - (end_time - start_time)
            print "Move: {}".format(move)
    return True

def print_help():
    print "Type 'h' or 'help' to get this dialog."
    print "Type 'q' or 'quit' to exit the application."
    print "Type 's' or 'set' to set the board."
    print "Type 'p' or 'print' to print the current board state."
    print "Type 'r' or 'reset' to reset the board to a start state."
    print "Type 'u' or 'undo' to undo a move."
    print "Type 'us' or 'undos' to undo a specified number of moves."
    print "Type 'm' or 'move' to move a piece."
    print "Type 'ms' or 'moves' to input a series of moves."
    print "Type 'rm' or 'random_move' to input a random move"
    print "Type 'tm' or 'tournament_move' to input a tournament move."
    print "Type 'am' or 'alphabeta_move' to input a normal alphabeta move."
    print "Type 'gh' or 'get_history' to obtain the history of moves."
    print "Type 'pa' or 'play_alphabeta' to play a simulated game using alphabeta."

if __name__ == "__main__":
    main()