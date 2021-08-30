"""
Unit tests for functions in questions.py

These tests will only work if your own version of questions.py
also happen to have implemented the same functions as mine!
Feel free to replace the unit test functions with your version.

'Why do we fall sir? So that we can learn to pick ourselves up.'
                                        - Batman Begins (2005)
"""
import os

from questions import load_files

DIRECTORY = "corpus"


def test_load_files():
    files = load_files(DIRECTORY)

    expected = len([file for file in os.listdir(DIRECTORY) if file.endswith(".txt")])

    assert len(files) == expected
