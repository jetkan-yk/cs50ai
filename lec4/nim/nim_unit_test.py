"""
Unit tests for functions in nim.py

These tests will only work if your own version of nim.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import random as rd

import pytest

from nim import NimAI


@pytest.mark.parametrize("execution", range(10))
def test_get_q_value(execution):
    ai = NimAI()
    state, action = generate_random_state_action()
    assert ai.get_q_value(state, action) == 0


# helper function


def generate_random_initial():
    return [rd.randint(1, 10) for _ in range(rd.randint(1, 5))]


random_initial = generate_random_initial()
print("\nInitial:", random_initial)


def generate_random_state_action():
    state = [rd.randint(0, i) for i in random_initial]
    pile = rd.randint(0, len(random_initial) - 1)
    action = (pile, rd.randint(1, random_initial[pile]))

    return state, action
