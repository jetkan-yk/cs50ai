"""
Unit tests for functions in my_parser.py

These tests will only work if your own version of my_parser.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
from my_parser import preprocess


def test_preprocess():
    sentence = "AB, cd's, 12, ..., 1z b213?0K"
    expected = ["ab", "cd", "'s", "1z", "b213", "0k"]

    result = preprocess(sentence)

    print(result)
    assert result == expected
