from pprint import pp
from random import randint, random

from helper import compare, predict_family
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
            assert round(sum(variable.values())) == 1


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


def test_has_parent():
    people = load_data("data/family0.csv")

    expected = {"Harry": True, "James": False, "Lily": False}

    for person in people:
        assert has_parent(person, people) == expected[person]


def test_ways():
    expected = {0: [(0, 0)], 1: [(0, 1), (1, 0)], 2: [(0, 2), (1, 1), (2, 0)]}

    for gene in range(3):
        assert [
            (f, m) for f in range(3) for m in range(3) if f + m == gene
        ] == expected[gene]


def test_get_gene():
    people = load_data("data/family0.csv")

    expected = {"Harry": 0, "James": 1, "Lily": 2}

    for person in people:
        assert get_gene(person, {"James"}, {"Lily"}) == expected[person]


def test_family0():
    expected = {
        "Harry": {
            "gene": {2: 0.0092, 1: 0.4557, 0: 0.5351},
            "trait": {True: 0.2665, False: 0.7335},
        },
        "James": {
            "gene": {2: 0.1976, 1: 0.5106, 0: 0.2918},
            "trait": {True: 1.0000, False: 0.0000},
        },
        "Lily": {
            "gene": {2: 0.0036, 1: 0.0136, 0: 0.9827},
            "trait": {True: 0.0000, False: 1.0000},
        },
    }

    predicted = predict_family(0)

    compare(predicted, expected)


def test_family1():
    expected = {
        "Arthur": {
            "gene": {2: 0.0329, 1: 0.1035, 0: 0.8636},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Charlie": {
            "gene": {2: 0.0018, 1: 0.1331, 0: 0.8651},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Fred": {
            "gene": {2: 0.0065, 1: 0.6486, 0: 0.3449},
            "trait": {True: 1.0000, False: 0.0000},
        },
        "Ginny": {
            "gene": {2: 0.0027, 1: 0.1805, 0: 0.8168},
            "trait": {True: 0.1110, False: 0.8890},
        },
        "Molly": {
            "gene": {2: 0.0329, 1: 0.1035, 0: 0.8636},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Ron": {
            "gene": {2: 0.0027, 1: 0.1805, 0: 0.8168},
            "trait": {True: 0.1110, False: 0.8890},
        },
    }

    predicted = predict_family(1)

    compare(predicted, expected)


def test_family2():
    expected = {
        "Arthur": {
            "gene": {2: 0.0147, 1: 0.0344, 0: 0.9509},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Hermione": {
            "gene": {2: 0.0608, 1: 0.1203, 0: 0.8189},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Molly": {
            "gene": {2: 0.0404, 1: 0.0744, 0: 0.8852},
            "trait": {True: 0.0768, False: 0.9232},
        },
        "Ron": {
            "gene": {2: 0.0043, 1: 0.2149, 0: 0.7808},
            "trait": {True: 0.0000, False: 1.0000},
        },
        "Rose": {
            "gene": {2: 0.0088, 1: 0.7022, 0: 0.2890},
            "trait": {True: 1.0000, False: 0.0000},
        },
    }

    predicted = predict_family(2)

    compare(predicted, expected)
