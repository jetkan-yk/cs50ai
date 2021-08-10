"""
Unit tests for functions in generate.py

These tests will only work if your own version of generate.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import collections
import random

import pytest

from crossword import Crossword
from generate import CrosswordCreator

invalid_crossword = [(1, 0), (2, 0)]  # These 2 combinations will not work


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
    if (i, j) in invalid_crossword:
        assert not creator.ac3()
    else:
        assert creator.ac3()


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


@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test_consistent(i, j):
    if (i, j) in invalid_crossword:
        return
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)

    empty_assignment = dict()
    assert creator.consistent(empty_assignment) is True

    nostring_assignment = {var: "" for var in creator.domains}
    assert creator.consistent(nostring_assignment) is False

    # Ensure correct length
    creator.enforce_node_consistency()
    consistent_assignment = {
        var: random.choice(list(values)) for var, values in creator.domains.items()
    }
    counter = collections.Counter(consistent_assignment.values())
    to_remove = set()
    # Ensure distinct
    for var, word in consistent_assignment.items():
        if counter[word] > 1:
            to_remove.add(var)
            assert creator.consistent(consistent_assignment) is False
    # Ensure no conflict
    for x, vX in consistent_assignment.items():
        for y, vY in consistent_assignment.items():
            if y in crossword.neighbors(x) and creator.conflict(x, y, vX, vY):
                to_remove.add(x)
                assert creator.consistent(consistent_assignment) is False
    for var in to_remove:
        consistent_assignment.pop(var)
    assert creator.consistent(consistent_assignment) is True


@pytest.mark.parametrize("i", range(3))
@pytest.mark.parametrize("j", range(3))
def test_order_domain_values(i, j):
    crossword = generate_crossword(i, j)
    creator = CrosswordCreator(crossword)

    var = random.choice(list(crossword.variables))
    word = random.choice(list(creator.domains[var]))
    domain = creator.domains[var]

    otherVar = random.choice(list(crossword.variables - {var}))
    otherDomain = creator.domains[otherVar]

    assert domain == otherDomain
    assert word in creator.order_domain_values(otherVar, dict())
    assert word not in creator.order_domain_values(otherVar, dict(var=word))


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
