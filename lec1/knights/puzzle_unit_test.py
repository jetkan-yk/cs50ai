"""
Unit tests for functions in puzzle.py

These tests will only work if your own version of puzzle.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from puzzle import *


def test_Xor():
    P = Symbol("P")
    Q = Symbol("Q")
    assert model_check(Xor(P, Q), Or(P, Q)) == True
    assert model_check(Xor(P, Q), And(P, Q)) == False
