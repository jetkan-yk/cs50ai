"""
Unit tests for functions in heredity.py

These tests will only work if your own version of heredity.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pprint as pp
import random as rd

from heredity import get_gene, has_parent, load_data, normalize, update


def test_get_gene():
    people = load_data("data/family0.csv")

    expected = {"Harry": 0, "James": 1, "Lily": 2}

    for person in people:
        assert get_gene(person, {"James"}, {"Lily"}) == expected[person]


def test_has_parent():
    people = load_data("data/family0.csv")

    expected = {"Harry": True, "James": False, "Lily": False}

    for person in people:
        assert has_parent(person, people) == expected[person]


def test_normalize():
    people = [f"Person{n}" for n in range(rd.randint(0, 10))]

    probabilities = {
        person: {
            "gene": {2: rd.random(), 1: rd.random(), 0: rd.random()},
            "trait": {True: rd.random(), False: rd.random()},
        }
        for person in people
    }

    print("\nBefore normalize:")
    pp.pp(probabilities)

    normalize(probabilities)

    print("\nAfter normalize:")
    pp.pp(probabilities)

    for person in probabilities.values():
        for variable in person.values():
            assert round(sum(variable.values())) == 1


def test_update():
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
            "p": rd.randint(1, 100),
        },
        {
            "one_gene": set(people[:3]),
            "two_gene": set(people[3:6]),
            "have_trait": set(people[5:]),
            "p": rd.randint(1, 100),
        },
        {
            "one_gene": set(people[6:]),
            "two_gene": set(people[:3]),
            "have_trait": set(people),
            "p": rd.randint(1, 100),
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

    pp.pp(probabilities)

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


def test_ways():
    expected = {0: [(0, 0)], 1: [(0, 1), (1, 0)]}

    for g in range(2):
        assert [(f, m) for f in [0, 1] for m in [0, 1] if f + m == g] == expected[g]
