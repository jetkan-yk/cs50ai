"""
Unit tests for functions in parser.py

These tests will only work if your own version of parser.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import re

import nltk


def preprocess(sentence):
    """
    Convert `sentence` to a list of its words.
    Pre-process sentence by converting all characters to lowercase
    and removing any word that does not contain at least one alphabetic
    character.
    """
    tokens = nltk.word_tokenize(sentence.lower())
    return list(filter(lambda t: re.search("[a-z]", t), tokens))


def test_preprocess():
    sentence = "AB, cd's, 12, ..., 1z b213?0K"
    expected = ["ab", "cd", "'s", "1z", "b213", "0k"]

    result = preprocess(sentence)

    print(result)
    assert result == expected
