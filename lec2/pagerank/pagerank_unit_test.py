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

from pagerank import DAMPING, has_changes, links_to, normalize, transition_model
from pagerank_test import checksum, generate_random_data


def test_transition_model_random():
    corpus, page = generate_random_data()

    print("\nRandom corpus:\n")
    pp.pp(corpus)
    print("\nRandom page:", page)

    probability = transition_model(corpus, page, damping_factor=rd.random())

    print("\nTransition model:\n")
    pp.pp(probability)

    return checksum(probability)


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
        assert round(probability[page], 4) == expected[page]


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
        assert round(probability[page], 4) == expected[page]


def test_normalize():
    corpus, _ = generate_random_data()

    probability = {page: rd.random() for page in corpus.keys()}

    print("\nBefore normalizing...\n")
    pp.pp(probability)

    normalize(probability)

    print("\nAfter normalizing...\n")
    pp.pp(probability)

    return checksum(probability)


def test_has_changes():
    assert has_changes(0, 1.5)
    assert has_changes(0, 1)
    assert has_changes(0, 1e-1)
    assert has_changes(0, 1e-2)
    assert not has_changes(0, 1e-3)
    assert not has_changes(0, 1e-4)
    assert not has_changes(0, 0)


def test_links_to():
    corpus, page = generate_random_data()
    links = links_to(corpus, page)

    for link in links:
        if corpus[link]:
            assert page in corpus[link]
