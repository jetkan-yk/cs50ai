"""
Unit tests for functions in generate.py

These tests will only work if your own version of generate.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import random as rd

from crossword import Crossword
from generate import CrosswordCreator


def test_enforce_node_consistency():
    crossword = generate_random_crossword()
    creator = CrosswordCreator(crossword)

    creator.enforce_node_consistency()

    for var, values in creator.domains.items():
        for value in values:
            assert len(value) == var.length


# helper function


def generate_random_crossword():
    structure = f"data/structure{rd.randint(0, 2)}.txt"
    words = f"data/words{rd.randint(0, 2)}.txt"

    return Crossword(structure, words)
