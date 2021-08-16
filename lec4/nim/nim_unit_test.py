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


@pytest.mark.parametrize("execution", range(10))
def test_update_q_value(execution):
    ai = NimAI()
    state, action = generate_random_state_action()
    reward = rd.randint(1, 10)
    future_rewards = rd.randint(1, 10)

    old_q = ai.get_q_value(state, action)
    assert old_q == 0

    ai.update_q_value(state, action, old_q, reward, future_rewards)

    new_q = ai.get_q_value(state, action)
    assert new_q == ai.alpha * ((reward + future_rewards) - old_q)

    ai.update_q_value(state, action, new_q, reward, future_rewards)

    new_new_q = ai.get_q_value(state, action)
    assert new_new_q == new_q + ai.alpha * ((reward + future_rewards) - new_q)


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
