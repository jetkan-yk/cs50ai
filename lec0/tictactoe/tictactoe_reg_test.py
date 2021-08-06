"""
Regression tests for tictactoe.py

Make sure that you placed this file in the same directory as tictactoe.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import tictactoe as ttt

# Let the AI play against itself for 10 times. If the minimax function
# is implemented correctly, every round should resolve in a tie.


def test_0():
    play_ai_vs_ai()


def test_1():
    play_ai_vs_ai()


def test_2():
    play_ai_vs_ai()


def test_3():
    play_ai_vs_ai()


def test_4():
    play_ai_vs_ai()


def test_5():
    play_ai_vs_ai()


def test_6():
    play_ai_vs_ai()


def test_7():
    play_ai_vs_ai()


def test_8():
    play_ai_vs_ai()


def test_9():
    play_ai_vs_ai()


# Helper function


def play_ai_vs_ai():
    board = ttt.initial_state()
    game_over = False

    while not game_over:
        move = ttt.minimax(board)
        board = ttt.result(board, move)
        game_over = ttt.terminal(board)

    assert ttt.winner(board) is None
