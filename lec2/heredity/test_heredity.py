from pprint import pp
from random import randint, random

from pytest import approx

from heredity import *


def test_normalize():
    print("\nTesting normalize()...")

    people = [f"Person{n}" for n in range(randint(0, 10))]

    probabilities = {
        person: {
            "gene": {2: random(), 1: random(), 0: random()},
            "trait": {True: random(), False: random()},
        }
        for person in people
    }

    print("\nBefore normalize:")
    pp(probabilities)

    normalize(probabilities)

    print("\nAfter normalize:")
    pp(probabilities)

    for person in probabilities.values():
        for variable in person.values():
            assert sum(variable.values()) == approx(1)
