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


def test_get_q_value():
    ai = NimAI()
    state, action = generate_random_state_action()
    # test default value
    assert ai.get_q_value(state, action) == 0


@pytest.mark.parametrize("execution", range(10))
def test_update_q_value(execution):
    ai = NimAI()
    state, action = generate_random_state_action()
    reward, future_rewards = generate_random_reward_future_rewards()

    old_q = ai.get_q_value(state, action)
    assert old_q == 0

    ai.update_q_value(state, action, old_q, reward, future_rewards)

    new_q = ai.get_q_value(state, action)
    assert new_q == ai.alpha * ((reward + future_rewards) - old_q)

    ai.update_q_value(state, action, new_q, reward, future_rewards)

    new_q2 = ai.get_q_value(state, action)
    assert new_q2 == new_q + ai.alpha * ((reward + future_rewards) - new_q)


@pytest.mark.parametrize("execution", range(10))
def test_best_future_reward(execution):
    ai = NimAI()
    state, action = generate_random_state_action()
    while True:
        _, action2 = generate_random_state_action()
        if action != action2:
            break
    reward, future_rewards = generate_random_reward_future_rewards()
    reward2, future_rewards2 = generate_random_reward_future_rewards()

    # No q-value, return 0
    assert ai.best_future_reward(state) == 0

    # 1 q-value, return result
    old_q = ai.get_q_value(state, action)
    ai.update_q_value(state, action, old_q, reward, future_rewards)
    new_q = ai.get_q_value(state, action)
    assert ai.best_future_reward(state) == new_q

    # 2 q-values, return max result
    ai.update_q_value(state, action2, old_q, reward2, future_rewards2)
    new_q2 = ai.get_q_value(state, action2)
    assert ai.best_future_reward(state) == max(new_q, new_q2)


@pytest.mark.parametrize("execution", range(10))
def deprecated_test_choose_action(execution):
    # test epsilon=False, 100%
    ai, state, expected = choose_action_helper(1)
    # skip cases where result can be 50:50
    if len(set(v for k, v in ai.q.items() if k[0] == tuple(state))) > 1:
        assert ai.choose_action(state, epsilon=False) == expected

    # test epsilon=True, 0%
    ai, state, expected = choose_action_helper(0)
    # skip cases where result can be 50:50
    if len(set(v for k, v in ai.q.items() if k[0] == tuple(state))) > 1:
        assert ai.choose_action(state) == expected


# helper function


def choose_action_helper(eps):
    ai = NimAI(epsilon=eps)
    state, action = generate_random_state_action()
    while True:
        _, action2 = generate_random_state_action()
        if action != action2:
            break
    reward, future_rewards = generate_random_reward_future_rewards()
    reward2, future_rewards2 = generate_random_reward_future_rewards()

    old_q = ai.get_q_value(state, action)

    ai.update_q_value(state, action, old_q, reward, future_rewards)
    new_q = ai.get_q_value(state, action)

    ai.update_q_value(state, action2, old_q, reward2, future_rewards2)
    new_q2 = ai.get_q_value(state, action2)

    expected = action if new_q > new_q2 else action2

    return ai, state, expected


def generate_random_initial():
    return [rd.randint(1, 10) for _ in range(rd.randint(1, 5))]


random_initial = generate_random_initial()
print("\nInitial:", random_initial)


def generate_random_state_action():
    state = [rd.randint(0, i) for i in random_initial]
    pile = rd.randint(0, len(random_initial) - 1)
    action = (pile, rd.randint(1, random_initial[pile]))

    return state, action


def generate_random_reward_future_rewards():
    return rd.randint(1, 10), rd.randint(1, 10)
