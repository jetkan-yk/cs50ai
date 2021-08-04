from puzzle import *


def test_Xor():
    P = Symbol("P")
    Q = Symbol("Q")
    assert model_check(Xor(P, Q), Or(P, Q)) == True
    assert model_check(Xor(P, Q), And(P, Q)) == False


def test_puzzle0():
    assert model_check(knowledge0, AKnight) == False
    assert model_check(knowledge0, AKnave) == True
    assert model_check(knowledge0, BKnight) == False
    assert model_check(knowledge0, BKnave) == False
    assert model_check(knowledge0, CKnight) == False
    assert model_check(knowledge0, CKnave) == False


def test_puzzle1():
    assert model_check(knowledge1, AKnight) == False
    assert model_check(knowledge1, AKnave) == True
    assert model_check(knowledge1, BKnight) == True
    assert model_check(knowledge1, BKnave) == False
    assert model_check(knowledge1, CKnight) == False
    assert model_check(knowledge1, CKnave) == False


def test_puzzle2():
    assert model_check(knowledge2, AKnight) == False
    assert model_check(knowledge2, AKnave) == True
    assert model_check(knowledge2, BKnight) == True
    assert model_check(knowledge2, BKnave) == False
    assert model_check(knowledge2, CKnight) == False
    assert model_check(knowledge2, CKnave) == False


def test_puzzle3():
    assert model_check(knowledge3, AKnight) == True
    assert model_check(knowledge3, AKnave) == False
    assert model_check(knowledge3, BKnight) == False
    assert model_check(knowledge3, BKnave) == True
    assert model_check(knowledge3, CKnight) == True
    assert model_check(knowledge3, CKnave) == False
