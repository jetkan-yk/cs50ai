from pprint import pp
from random import randint, random

from pytest import approx

from heredity import *


def test_normalize():
    print("\n\n======================== Testing normalize() ========================\n")

    people = [f"Person{n}" for n in range(randint(0, 10))]

    probabilities = {
        person: {
            "gene": {2: random(), 1: random(), 0: random()},
            "trait": {True: random(), False: random()},
        }
        for person in people
    }

    print("Before normalize:")
    pp(probabilities)

    normalize(probabilities)

    print("\nAfter normalize:")
    pp(probabilities)

    for person in probabilities.values():
        for variable in person.values():
            assert sum(variable.values()) == approx(1)


def test_update():
    print("\n\n======================== Testing update() ========================\n")

    people = [f"Person{n}" for n in range(9)]

    probabilities = {
        person: {
            "gene": {2: 0, 1: 0, 0: 0},
            "trait": {True: 0, False: 0},
        }
        for person in people
    }

    testcases = [
        {
            "one_gene": set(people[3:6]),
            "two_gene": set(people[6:]),
            "have_trait": set(people[:5]),
            "p": randint(1, 100),
        },
        {
            "one_gene": set(people[:3]),
            "two_gene": set(people[3:6]),
            "have_trait": set(people[5:]),
            "p": randint(1, 100),
        },
        {
            "one_gene": set(people[6:]),
            "two_gene": set(people[:3]),
            "have_trait": set(people),
            "p": randint(1, 100),
        },
    ]

    for dist in testcases:
        update(
            probabilities,
            dist["one_gene"],
            dist["two_gene"],
            dist["have_trait"],
            dist["p"],
        )

    pp(probabilities)

    group1 = [probabilities[people[i]]["gene"] for i in range(3)]
    group2 = [probabilities[people[i]]["gene"] for i in range(3, 6)]
    group3 = [probabilities[people[i]]["gene"] for i in range(6, 9)]
    group4 = [probabilities[people[i]]["trait"] for i in range(5)]
    group5 = [probabilities[people[i]]["trait"] for i in range(5, 9)]

    assert all(item == group1[0] for item in group1)
    assert all(item == group2[0] for item in group2)
    assert all(item == group3[0] for item in group3)
    assert all(item == group4[0] for item in group4)
    assert all(item == group5[0] for item in group5)
