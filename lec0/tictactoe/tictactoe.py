"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY], [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    X_count = sum(row.count(X) for row in board)
    O_count = sum(row.count(O) for row in board)

    return X if X_count == O_count else O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    result = set()

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == EMPTY:
                result.add((i, j))

    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i not in range(0, len(board)):
        raise ValueError(f"i must be [0, {len(board)})")
    elif j not in range(0, len(board[0])):
        raise ValueError(f"j must be [0, {len(board[0])})")
    elif board[i][j] != EMPTY:
        raise ValueError(f"({i}, {j}) has been taken by player {board[i][j]}")
    else:
        new_board = deepcopy(board)
        new_board[i][j] = player(board)
        return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
