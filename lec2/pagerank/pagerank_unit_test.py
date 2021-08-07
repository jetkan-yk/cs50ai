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

from pagerank import DAMPING, is_significant, links_to, normalize, transition_model
from pagerank_test import generate_random_data

PRECISION = 4


def test_transition_model_random():
    corpus, page = generate_random_data()

    print("\nRandom corpus:\n")
    pp.pp(corpus)
    print("\nRandom page:", page)

    probability = transition_model(corpus, page, damping_factor=rd.random())

    print("\nTransition model:\n")
    pp.pp(probability)

    assert round(sum(probability.values()), PRECISION) == 1


def test_transition_model_custom():
    corpus = {
        "1.html": {"2.html", "3.html"},
        "2.html": {"3.html"},
        "3.html": {"2.html"},
    }
    page = "1.html"
    expected = {"1.html": 0.05, "2.html": 0.475, "3.html": 0.475}

    probability = transition_model(corpus, page, damping_factor=DAMPING)

    for page in expected:
        assert round(probability[page], PRECISION) == expected[page]


def test_transition_model_no_link():
    corpus = {
        "1.html": {},
        "2.html": {},
        "3.html": {},
    }
    page = rd.choice(list(corpus.keys()))
    expected = {"1.html": 0.3333, "2.html": 0.3333, "3.html": 0.3333}

    probability = transition_model(corpus, page, damping_factor=DAMPING)

    for page in expected:
        assert round(probability[page], PRECISION) == expected[page]


def test_normalize():
    corpus, _ = generate_random_data()

    probability = {page: rd.random() for page in corpus.keys()}

    print("\nBefore normalizing...\n")
    pp.pp(probability)

    normalize(probability)

    print("\nAfter normalizing...\n")
    pp.pp(probability)

    assert round(sum(probability.values()), PRECISION) == 1


def test_is_significant():
    assert is_significant(0, 1.5, 1, 4)
    assert is_significant(0, 1, 1, 4)
    assert is_significant(0, 1e-1, 1, 4)
    assert is_significant(0, 1e-2, 1, 4)
    assert is_significant(0, 1e-3, 1, 4)
    assert is_significant(0, 1e-4, 1, 4)
    assert is_significant(0, 5e-5, 1, 4)
    assert not is_significant(0, 4e-5, 1, 4)
    assert not is_significant(0, 1e-6, 1, 4)
    assert not is_significant(0, 0, 1, 4)


def test_links_to():
    corpus, page = generate_random_data()
    links = links_to(corpus, page)

    for link in links:
        assert page in corpus[link]
