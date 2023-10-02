#!/usr/bin/python3
"""the module of N Quenen

N Queens problem solving 
"""
import sys


def error_exit(message="", code=1):
    """Handles exit.

    Args:
        message (str): the message to print on stdout.
        code (int): exit codee 
    """
    print(message)
    exit(code)


def test_pos(board, y):
    """ testing if queen can be placed on current position.

    Args:
        board (list): a chessboard.
        y (int): high parameter.
    """
    for i in range(y):
        if board[y][1] is board[i][1]:
            return False
        if abs(board[y][1] - board[i][1]) == y - i:
            return False
    return True


def rec_backtrack(board, y):
    """Backtrack the options.

    Args:
        board (list): a chessboard
        y (int): high parametre 
    """
    if y is N:
        print(board)
    else:
        for x in range(N):
            board[y][1] = x
            if test_pos(board, y):
                rec_backtrack(board, y + 1)


if len(sys.argv) is not 2:
    error_exit("Usage: nqueens N")

try:
    N = int(sys.argv[1])
except:
    error_exit("N must be a number")

if N < 4:
    error_exit("N must be at least 4")

board = [[y, 0] for y in range(N)]
rec_backtrack(board, 0)
