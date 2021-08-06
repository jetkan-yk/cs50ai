"""
Unit tests for functions in puzzle.py
"""
from puzzle import *


def test_Xor():
    P = Symbol("P")
    Q = Symbol("Q")
    assert model_check(Xor(P, Q), Or(P, Q)) == True
    assert model_check(Xor(P, Q), And(P, Q)) == False
