"""
Regression tests for generate.py

Make sure that this file is in the same directory as generate.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest

from generate import CrosswordCreator
from generate_unit_test import generate_crossword, invalid_crossword


@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test(i, j):
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)
    assignment = creator.solve()
    generate_output(creator, assignment, f"data/output{i}-{j}.png")

    if (i, j) in invalid_crossword:
        assert assignment is None
    else:
        assert len(assignment) == len(crossword.variables)


# helper function
def generate_output(creator, assignment, file):
    if assignment is None:
        print("No solution")
    else:
        creator.print(assignment)
        creator.save(assignment, file)
