"""
Unit tests for functions in shopping.py

These tests will only work if your own version of shopping.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from shopping import load_data

expected0 = [0, 0.0, 0, 0.0, 1, 0.0, 0.2, 0.2, 0.0, 0.0, 1, 1, 1, 1, 1, 1, 0]


def test_load_data():
    evidence, labels = load_data("./shopping.csv")
    assert len(evidence) == len(labels)
    assert evidence.iloc[0].values.tolist() == expected0
    assert labels.iloc[0].values == 0
