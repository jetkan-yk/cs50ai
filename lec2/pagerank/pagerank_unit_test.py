"""
Unit tests for functions in pagerank.py
"""
import pprint as pp
import random as rd

import pytest as pt

from pagerank import DAMPING, transition_model

PRECISION = 1e-4


def test_transition_model_random():
    links = [f"{i}.html" for i in range(rd.randint(1, 10))]
    corpus = {
        link: set(rd.choices(links, k=rd.randint(0, len(links)))) - set([link])
        for link in links
    }
    page = rd.choice(list(corpus.keys()))

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
