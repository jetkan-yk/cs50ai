"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None
SIZE = 3  # board size, e.g. 3 x 3 grid


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

    for i in range(SIZE):
        for j in range(SIZE):
            if board[i][j] == EMPTY:
                result.add((i, j))

    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    i, j = action

    if i not in range(SIZE):
        raise ValueError(f"i must be [0, {SIZE})")
    elif j not in range(SIZE):
        raise ValueError(f"j must be [0, {SIZE})")
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
    # check horizontally
    for row in board:
        if row.count(X) == SIZE:
            return X
        elif row.count(O) == SIZE:
            return O

    # check vertically
    for col in zip(*board):
        if col.count(X) == SIZE:
            return X
        elif col.count(O) == SIZE:
            return O

    # check diagonally
    center = board[SIZE // 2][SIZE // 2]

    if center == EMPTY:
        return None

    # left diagonal
    left_win = True
    for i in range(SIZE):
        if board[i][i] != center:
            left_win = False

    # right diagonal
    right_win = True
    for i in range(SIZE):
        if board[i][-(i + 1)] != center:
            right_win = False

    if left_win or right_win:
        return center
    else:
        return None


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
