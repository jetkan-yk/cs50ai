"""
Unit tests for functions in parser.py

These tests will only work if your own version of parser.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import pytest
import os

from my_parser import parser, preprocess


def test_preprocess():
    sentence = "AB, cd's, 12, ..., 1z b213?0K"
    expected = ["ab", "cd", "'s", "1z", "b213", "0k"]

    result = preprocess(sentence)

    print(result)
    assert result == expected


@pytest.mark.parametrize("execution", range(1, 11))
def test_parser(execution):
    with open(os.path.join("sentences", f"{execution}.txt")) as f:
        s = f.read()
    s = preprocess(s)
    try:
        trees = list(parser.parse(s))
        print()
        for tree in trees:
            tree.pretty_print()
    except ValueError as e:
        assert False, e
    if not trees:
        assert False, "Could not parse sentence."
