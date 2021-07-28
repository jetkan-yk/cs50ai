"""
Tic Tac Toe Player
"""

from copy import deepcopy
import math

X = "X"
O = "O"
EMPTY = None
BOARD_SIZE = 3  # board size, e.g. 3 x 3 grid
INF = 2  # utility is either -1, 0, 1


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

    for i in range(BOARD_SIZE):
        for j in range(BOARD_SIZE):
            if board[i][j] == EMPTY:
                result.add((i, j))

    return result


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action is None:
        return board
    (i, j) = action

    if i not in range(BOARD_SIZE):
        raise ValueError(f"i must be [0, {BOARD_SIZE})")
    elif j not in range(BOARD_SIZE):
        raise ValueError(f"j must be [0, {BOARD_SIZE})")
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
        if row.count(X) == BOARD_SIZE:
            return X
        elif row.count(O) == BOARD_SIZE:
            return O

    # check vertically
    for col in zip(*board):
        if col.count(X) == BOARD_SIZE:
            return X
        elif col.count(O) == BOARD_SIZE:
            return O

    # check diagonally
    center = board[BOARD_SIZE // 2][BOARD_SIZE // 2]

    if center == EMPTY:
        return None

    # left diagonal
    left_win = True
    for i in range(BOARD_SIZE):
        if board[i][i] != center:
            left_win = False

    # right diagonal
    right_win = True
    for i in range(BOARD_SIZE):
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
    # someone has won the game
    if winner(board):
        return True

    for row in board:
        for cell in row:
            if cell == EMPTY:
                # there is at least 1 empty cell
                return False
    # no empty cell
    return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    player = winner(board)

    if player == X:
        return 1
    elif player == O:
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_action = None

    # max player chooses move that maximizes the min values in next step
    if player(board) == X:
        best_value = -INF
        for action in actions(board):
            value = min_value(result(board, action))
            # found killer move, return immediately
            if value == 1:
                return action
            elif best_value < value:
                best_value, best_action = value, action

    # min player chooses move that minimizes the max values in next step
    else:
        best_value = INF
        for action in actions(board):
            value = max_value(result(board, action))
            # found killer move, return immediately
            if value == -1:
                return action
            elif best_value > value:
                best_value, best_action = value, action

    return best_action


def max_value(board):
    """
    Returns the highest value for the current player.
    """
    if terminal(board):
        return utility(board)
    v = -INF
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        # found killer move, prune other actions
        if v == 1:
            break
    return v


def min_value(board):
    """
    Returns the smallest value for the current player.
    """
    if terminal(board):
        return utility(board)
    v = INF
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        # found killer move, prune other actions
        if v == -1:
            break
    return v
