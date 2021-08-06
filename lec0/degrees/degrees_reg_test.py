"""
Regression tests for degrees.py

Make sure that you placed this file in the same directory as degrees.py!

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from degrees import load_data, person_id_for_name, shortest_path

load_data("large")


def test_zero_degree():
    source = person_id_for_name("Tim Zinnemann")
    target = person_id_for_name("Lahcen Zinoun")
    assert shortest_path(source, target) == None


def test_one_degree():
    source = person_id_for_name("Tom Cruise")
    target = person_id_for_name("Lea Thompson")
    assert len(shortest_path(source, target)) == 1


def test_two_degree():
    source = person_id_for_name("Tom Cruise")
    target = person_id_for_name("Tom Hanks")
    assert len(shortest_path(source, target)) == 2


def test_three_degree():
    source = person_id_for_name("Emma Watson")
    target = person_id_for_name("Jennifer Lawrence")
    assert len(shortest_path(source, target)) == 3


def test_four_degree():
    source = person_id_for_name("Fred Astaire")
    target = person_id_for_name("Mohamed Zinet")
    assert len(shortest_path(source, target)) == 4


def test_eight_degree():
    source = person_id_for_name("Juliane Banse")
    target = person_id_for_name("Julian Acosta")
    assert len(shortest_path(source, target)) == 8
