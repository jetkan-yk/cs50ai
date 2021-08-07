"""
Unit tests for functions in pagerank.py

These tests will only work if your own version of pagerank.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pprint as pp
import random as rd

import pytest as pt

from pagerank import DAMPING, transition_model
from pagerank_test import generate_random_data

PRECISION = 1e-4


def test_transition_model_random():
    corpus, page = generate_random_data()

    print("\nRandom corpus:\n")
    pp.pp(corpus)
    print("\nRandom page:", page)

    probability = transition_model(corpus, page, rd.random())

    print("\nProbability:\n")
    pp.pp(probability)

    assert sum(probability.values()) == pt.approx(1, abs=PRECISION)


def test_transition_model_custom():
    corpus = {
        "1.html": {"2.html", "3.html"},
        "2.html": {"3.html"},
        "3.html": {"2.html"},
    }
    page = "1.html"
    expected = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}

    probability = transition_model(corpus, page, DAMPING)

    assert probability == pt.approx(expected, abs=PRECISION)


def test_transition_model_no_link():
    corpus = {
        "1.html": {},
        "2.html": {},
        "3.html": {},
    }
    page = rd.choice(list(corpus.keys()))
    expected = {"1.html": 0.3333, "2.html": 0.3333, "3.html": 0.3333}

    probability = transition_model(corpus, page, DAMPING)

    assert probability == pt.approx(expected, abs=PRECISION)
