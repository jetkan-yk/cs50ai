"""
Unit tests for functions in generate.py

These tests will only work if your own version of generate.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import copy
import random

from crossword import Crossword
from generate import CrosswordCreator


def test_enforce_node_consistency():
    crossword = generate_random_crossword()
    creator = CrosswordCreator(crossword)

    creator.enforce_node_consistency()

    for var, values in creator.domains.items():
        for value in values:
            assert len(value) == var.length


def test_revise_and_conflict():
    crossword = generate_crossword(0, 0)
    creator = CrosswordCreator(crossword)

    creator.enforce_node_consistency()

    for x in crossword.variables:
        for y in crossword.variables:
            if x == y:
                continue
            oldDomain = copy.deepcopy(creator.domains[x])
            if creator.revise(x, y):
                removed = oldDomain - creator.domains[x]
                for valueX in removed:
                    for valueY in creator.domains[y]:
                        overlap = crossword.overlaps[x, y]
                        assert_conflict(overlap, valueX, valueY)
            else:
                assert oldDomain == creator.domains[x]


# helper function


def assert_conflict(overlap, valueX, valueY):
    assert overlap is not None
    (i, j) = overlap
    print(valueX[i], "!=", valueY[j])
    assert valueX[i] != valueY[j]


def generate_crossword(i, j):
    structure = f"data/structure{i}.txt"
    words = f"data/words{j}.txt"
    print(f"\nTesting structure{i} words{j}")
    return Crossword(structure, words)


def generate_random_crossword():
    i = random.randint(0, 2)
    j = random.randint(0, 2)
    return generate_crossword(i, j)
