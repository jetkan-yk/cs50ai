from random import random
from pytest import approx
from heredity import *


def test_normalize():
    people = ["Person1", "Person2", "Person3"]

    probabilities = {
        person: {
            "gene": {2: random(), 1: random(), 0: random()},
            "trait": {True: random(), False: random()},
        }
        for person in people
    }

    normalize(probabilities)

    for person in probabilities.values():
        for variable in person.values():
            assert sum(variable.values()) == approx(1)