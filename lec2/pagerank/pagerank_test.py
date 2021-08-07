"""
Regression tests for pagerank.py

Make sure that this file is in the same directory as pagerank.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""

import random as rd

import pytest as pt

from pagerank import DAMPING, SAMPLES, iterate_pagerank, sample_pagerank

PRECISION = 1e-4


@pt.mark.parametrize("execution_number", range(10))
def test(execution_number):
    run_compare()


# helper function


def run_compare():
    corpus, _ = generate_random_data()

    assert sample_pagerank(corpus, damping_factor=DAMPING, n=SAMPLES) == pt.approx(
        iterate_pagerank(corpus, damping_factor=DAMPING), abs=PRECISION
    )


def generate_random_data():
    links = [f"{i}.html" for i in range(rd.randint(1, 10))]
    page = rd.choice(links)
    corpus = {
        link: set(rd.choices(links, k=rd.randint(0, len(links)))) - set([link])
        for link in links
    }
    return corpus, page
