"""
Unit tests for functions in generate.py

These tests will only work if your own version of generate.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest
import random

from crossword import Crossword
from generate import CrosswordCreator


@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test_enforce_node_consistency(i, j):
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)

    creator.enforce_node_consistency()

    for var, values in creator.domains.items():
        for value in values:
            assert len(value) == var.length


@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test_revise_and_conflict(i, j):
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)

    creator.enforce_node_consistency()

    for x in crossword.variables:
        for y in crossword.variables:
            if x == y:
                continue
            oldDomain = creator.domains[x].copy()
            if creator.revise(x, y):
                removed = oldDomain - creator.domains[x]
                for valueX in removed:
                    for valueY in creator.domains[y]:
                        overlap = crossword.overlaps[x, y]
                        assert_conflict(overlap, valueX, valueY)
            else:
                assert oldDomain == creator.domains[x]


@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test_ac3(i, j):
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)

    creator.enforce_node_consistency()
    if (i, j) not in [(1, 0), (2, 0)]:
        assert creator.ac3()
    else:
        assert not creator.ac3()


def test_assignment_complete():
    crossword = generate_random_crossword()
    creator = CrosswordCreator(crossword)

    empty_assignment = dict()
    assert creator.assignment_complete(empty_assignment) is False

    complete_assignment = {
        var: random.choice(list(crossword.words)) for var in crossword.variables
    }
    assert creator.assignment_complete(complete_assignment) is True

    random_var = random.choice(list(complete_assignment.keys()))
    incomplete_assignment = complete_assignment.copy()
    incomplete_assignment[random_var] = None
    assert creator.assignment_complete(incomplete_assignment) is False


# helper function


def assert_conflict(overlap, valueX, valueY):
    assert overlap is not None
    (i, j) = overlap
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
